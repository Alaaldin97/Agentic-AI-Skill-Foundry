#!/usr/bin/env python3
"""Search for an agent skill across three sources, nearest first.

    python scripts/search_skills.py "code review"
    python scripts/search_skills.py "linkedin post" --limit 5

Order matters and is deliberate:

  1. The Skill Foundry  - our own catalog. Already reviewed, already has evidence,
                          and a classmate can explain it to you. Always check first.
  2. skillspool.org     - a curated directory with an API.
  3. GitHub search      - the long tail. Noisy, unreviewed, but comprehensive.

Each source can fail independently. A dead source degrades the result; it never
crashes the run. Stdlib only - no pip install required.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

# Windows consoles default to cp1252 and will crash on the first non-ASCII
# character in a third-party description. Force UTF-8 and degrade gracefully.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FOUNDRY_RAW = (
    "https://raw.githubusercontent.com/Alaaldin97/"
    "Agentic-AI-Skill-Foundry/main/web/skills.json"
)
SKILLSPOOL = "https://skillspool.org/api/v1/skills/search"
GITHUB = "https://api.github.com/search/repositories"

UA = {"User-Agent": "skill-foundry-finder", "Accept": "application/json"}
TIMEOUT = 20


def fetch(url: str, headers: dict | None = None) -> tuple[dict | list | None, str]:
    """Return (payload, status). Never raises."""
    req = urllib.request.Request(url, headers={**UA, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return json.loads(r.read().decode("utf-8")), "ok"
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return None, f"unreachable ({e.reason})"
    except (TimeoutError, json.JSONDecodeError) as e:
        return None, f"bad response ({type(e).__name__})"


def search_foundry(q: str, limit: int) -> tuple[list[dict], str]:
    data, status = fetch(FOUNDRY_RAW)
    if data is None:
        return [], status
    terms = q.lower().split()
    hits = []
    for s in data if isinstance(data, list) else data.get("skills", []):
        blob = f"{s.get('name','')} {s.get('description','')} {s.get('category','')}".lower()
        score = sum(1 for t in terms if t in blob)
        if score:
            hits.append((score, s))
    hits.sort(key=lambda x: -x[0])
    return [
        {
            "name": s.get("name", ""),
            "desc": (s.get("trigger") or s.get("description", ""))[:150],
            "by": s.get("author", ""),
            "url": f"https://github.com/Alaaldin97/Agentic-AI-Skill-Foundry/tree/main/skills/{s.get('folder','')}",
            "trust": "reviewed by this cohort",
        }
        for _, s in hits[:limit]
    ], "ok"


def search_skillspool(q: str, limit: int) -> tuple[list[dict], str]:
    url = f"{SKILLSPOOL}?{urllib.parse.urlencode({'q': q, 'limit': limit})}"
    data, status = fetch(url)
    if data is None:
        return [], status
    return [
        {
            "name": d.get("name", ""),
            "desc": (d.get("description") or "")[:150],
            "by": d.get("author", ""),
            "url": f"https://skillspool.org/skills/{d.get('slug','')}",
            "trust": f"{d.get('stars', 0):,} stars",
        }
        for d in data.get("data", [])[:limit]
    ], "ok"


def search_github(q: str, limit: int) -> tuple[list[dict], str]:
    query = f"{q} agent skill"
    url = f"{GITHUB}?{urllib.parse.urlencode({'q': query, 'sort': 'stars', 'per_page': limit})}"
    data, status = fetch(url, {"Accept": "application/vnd.github+json"})
    if data is None:
        return [], status
    return [
        {
            "name": r.get("name", ""),
            "desc": (r.get("description") or "")[:150],
            "by": r.get("full_name", "").split("/")[0],
            "url": r.get("html_url", ""),
            "trust": f"{r.get('stargazers_count', 0):,} stars — UNREVIEWED",
        }
        for r in data.get("items", [])[:limit]
    ], "ok"


SOURCES = [
    ("The Skill Foundry", search_foundry),
    ("skillspool.org", search_skillspool),
    ("GitHub", search_github),
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("query", help="what you need done, in plain words")
    ap.add_argument("--limit", type=int, default=5)
    args = ap.parse_args()

    print(f'searching for: "{args.query}"\n')
    total = 0
    degraded = []

    for label, fn in SOURCES:
        results, status = fn(args.query, args.limit)
        if status != "ok":
            print(f"  {label:<20} unavailable — {status}")
            degraded.append(label)
            continue
        if not results:
            print(f"  {label:<20} no matches")
            continue

        print(f"\n  {label}")
        print(f"  {'-' * len(label)}")
        for r in results:
            print(f"    {r['name']}  [{r['trust']}]")
            if r["desc"]:
                print(f"      {r['desc']}")
            print(f"      {r['url']}")
            total += 1

    print()
    if degraded:
        print(f"note: {len(degraded)} source(s) down — results are partial: {', '.join(degraded)}")
    if total == 0:
        print("nothing found. try broader English keywords, or open a skill request:")
        print("  https://github.com/Alaaldin97/Agentic-AI-Skill-Foundry/issues/new?template=skill-request.yml")
        return 1
    print(f"{total} result(s). Read the SKILL.md before installing anything.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
