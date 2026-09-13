#!/usr/bin/env python3
"""Mechanical checks for a skill folder. The part that does not need judgement.

    python scripts/review_skill.py <path-to-skill-folder>

Deliberately dependency-free so it runs anywhere the agent can reach a shell.
"""
from __future__ import annotations

import pathlib
import re
import sys

SECRETS = [
    (r"sk-[A-Za-z0-9]{20,}", "OpenAI-style API key"),
    (r"sk-or-v1-[A-Za-z0-9]{20,}", "OpenRouter API key"),
    (r"gh[pousr]_[A-Za-z0-9]{30,}", "GitHub token"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key"),
    (r"C:\\\\Users\\\\[A-Za-z0-9._-]+", "absolute Windows home path"),
    (r"/Users/[A-Za-z0-9._-]+/", "absolute macOS home path"),
]

VAGUE = ["analyze", "analyse", "help with", "improve", "manage", "handle", "process", "work with"]

PLACEHOLDERS = ["REPLACE THIS", "_TEMPLATE", "Your Name", "your-github-username",
                "concrete trigger one", "<the exact prompt"]


def frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    data, key, buf = {}, None, []
    for raw in text[3:end].strip("\n").split("\n"):
        if not raw.strip():
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", raw)
        if m and not raw.startswith((" ", "\t")):
            if key:
                data[key] = " ".join(buf).strip()
            key = m.group(1)
            v = m.group(2).strip()
            buf = [] if v in (">", "|", ">-", "|-") else [v]
        elif key:
            buf.append(raw.strip())
    if key:
        data[key] = " ".join(buf).strip()
    return data


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: review_skill.py <path-to-skill-folder>")
        return 2

    path = pathlib.Path(sys.argv[1]).resolve()
    fails: list[str] = []
    notes: list[str] = []

    print(f"skill: {path.name}")
    print("-" * 52)

    if not path.is_dir():
        print(f"FAIL  not a directory: {path}")
        return 1

    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        print("FAIL  no SKILL.md")
        return 1

    text = skill_md.read_text(encoding="utf-8")
    fm = frontmatter(text)

    # structure
    for f in ("SKILL.md", "EVIDENCE.md", "meta.yml"):
        print(f"{'ok  ' if (path / f).exists() else 'FAIL'}  {f}")
        if not (path / f).exists():
            fails.append(f"missing {f}")

    # frontmatter
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not fm:
        fails.append("frontmatter missing or malformed")
        print("FAIL  frontmatter did not parse")
    else:
        print(f"{'ok  ' if name else 'FAIL'}  name: {name or '(missing)'}")
        if name and name != path.name:
            fails.append(f"name '{name}' != folder '{path.name}'")
            print(f"FAIL  name does not match folder '{path.name}'")
        if not desc:
            fails.append("no description")
            print("FAIL  description missing - this is the public API")
        else:
            print(f"ok    description: {len(desc)} chars")
            if len(desc) > 500:
                notes.append(f"description is {len(desc)} chars; it loads every turn")
            if len(desc) < 60:
                notes.append("description is very short - may route unpredictably")
            if not re.search(r"does not fire|does NOT fire", desc, re.I):
                notes.append("no 'Does NOT fire on:' clause - dormancy is half the grade")
            hits = [v for v in VAGUE if v in desc.lower()]
            if hits:
                notes.append(f"generic trigger word(s): {', '.join(hits)}")

    # body sections
    for section in ("When to use this", "Steps", "Rules"):
        present = section.lower() in text.lower()
        print(f"{'ok  ' if present else 'warn'}  section: {section}")
        if not present:
            notes.append(f"no '## {section}' section")

    # weight
    lines = len(text.splitlines())
    print(f"{'ok  ' if lines <= 500 else 'warn'}  body: {lines} lines")
    if lines > 500:
        notes.append(f"body is {lines} lines - move bulk into resources/")

    # determinism
    hard = re.findall(r"^.*\b(always|never|must)\b.*$", text, re.I | re.M)
    hard = [h.strip() for h in hard if not h.strip().startswith("#")]
    has_scripts = (path / "scripts").is_dir()
    if hard:
        print(f"note  {len(hard)} hard rule(s) found; scripts/ {'present' if has_scripts else 'ABSENT'}")
        if not has_scripts:
            notes.append(
                f"{len(hard)} rule(s) use always/never/must but nothing is enforced in code"
            )

    # evidence
    ev = path / "EVIDENCE.md"
    if ev.exists():
        e = ev.read_text(encoding="utf-8")
        if "```" not in e:
            fails.append("EVIDENCE.md has no transcript")
            print("FAIL  EVIDENCE.md has no fenced transcript")
        if not re.search(r"dormant|stayed quiet|did not fire|near-miss", e, re.I):
            fails.append("EVIDENCE.md has no dormancy test")
            print("FAIL  EVIDENCE.md has no dormancy test")

    # secrets
    leaked = []
    for f in path.rglob("*"):
        if f.is_file() and f.suffix not in {".png", ".jpg", ".jpeg", ".gif", ".pdf"}:
            body = f.read_text(encoding="utf-8", errors="ignore")
            for pat, label in SECRETS:
                if re.search(pat, body):
                    leaked.append(f"{f.relative_to(path)}: {label}")
    if leaked:
        for item in leaked:
            print(f"FAIL  secret: {item}")
        fails.extend(leaked)
    else:
        print("ok    no secrets or absolute paths")

    # unfilled template
    stale = []
    for f in (path / "SKILL.md", path / "EVIDENCE.md", path / "meta.yml"):
        if not f.exists():
            continue
        # Fenced blocks may legitimately quote template text - e.g. an
        # EVIDENCE.md pasting the output of a tool that detected it.
        body = re.sub(
            r"```.*?```", "", f.read_text(encoding="utf-8", errors="ignore"), flags=re.S
        )
        for ph in PLACEHOLDERS:
            if ph in body:
                stale.append(f"{f.name}: '{ph}'")
    if stale:
        for item in stale:
            print(f"FAIL  unfilled template text: {item}")
        fails.extend(stale)
    else:
        print("ok    no leftover template text")

    print("-" * 52)
    if notes:
        print("\nfor the reviewer to judge:")
        for n in notes:
            print(f"  - {n}")
    if fails:
        print(f"\nBLOCKING: {len(fails)} issue(s) must be fixed before merge.")
        return 1

    print("\nMechanical checks passed. Judgement still required on the description.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
