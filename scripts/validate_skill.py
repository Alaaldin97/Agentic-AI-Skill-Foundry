#!/usr/bin/env python3
"""Validate a skill folder before it can be merged into The Skill Foundry.

Run it yourself before you push - it is the same script CI runs:

    python scripts/validate_skill.py skills/my-skill-name
    python scripts/validate_skill.py --all

Everything in CONTRIBUTING.md is advice. This file is the gate.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
REQUIRED = ["SKILL.md", "EVIDENCE.md", "meta.yml"]

PLACEHOLDERS = [
    r"REPLACE THIS",
    # Match the template folder name only as a standalone token - otherwise it
    # also fires on legitimate references to .github/ISSUE_TEMPLATE/.
    r"(?<![A-Za-z])_TEMPLATE(?![A-Za-z])",
    r"Your Name",
    r"your-github-username",
    r"<the exact prompt",
    r"concrete trigger one",
]

# Things that must never be committed.
SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9]{20,}", "OpenAI-style API key"),
    (r"sk-or-v1-[A-Za-z0-9]{20,}", "OpenRouter API key"),
    (r"gh[pousr]_[A-Za-z0-9]{30,}", "GitHub token"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key"),
    (r"C:\\\\Users\\\\[A-Za-z0-9._-]+", "absolute Windows home path"),
    (r"/Users/[A-Za-z0-9._-]+/", "absolute macOS home path"),
]


class Result:
    def __init__(self, name: str):
        self.name = name
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    @property
    def ok(self) -> bool:
        return not self.errors


def strip_code_fences(text: str) -> str:
    """Remove fenced blocks before scanning for placeholders.

    An EVIDENCE.md may legitimately quote template text when it pastes the
    output of a tool that detected that text. Only prose counts as unfilled.
    """
    return re.sub(r"```.*?```", "", text, flags=re.S)


def parse_frontmatter(text: str) -> dict | None:
    """Minimal YAML frontmatter reader - no dependency on PyYAML.

    Handles `key: value` and folded `key: >` blocks, which is all a SKILL.md
    header should ever need.
    """
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip("\n")

    data: dict[str, str] = {}
    key: str | None = None
    buf: list[str] = []

    for raw in block.split("\n"):
        if not raw.strip():
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", raw)
        if m and not raw.startswith((" ", "\t")):
            if key:
                data[key] = " ".join(buf).strip()
            key = m.group(1)
            val = m.group(2).strip()
            buf = [] if val in (">", "|", ">-", "|-") else [val]
        elif key:
            buf.append(raw.strip())

    if key:
        data[key] = " ".join(buf).strip()
    return data


def check_secrets(path: pathlib.Path, res: Result) -> None:
    for f in path.rglob("*"):
        if not f.is_file() or f.suffix in {".png", ".jpg", ".jpeg", ".gif", ".pdf"}:
            continue
        try:
            body = f.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        rel = f.relative_to(path)
        for pattern, label in SECRET_PATTERNS:
            if re.search(pattern, body):
                res.error(f"{rel}: looks like it contains a {label} - remove it")


def validate(path: pathlib.Path) -> Result:
    res = Result(path.name)

    if not path.is_dir():
        res.error("not a directory")
        return res

    # --- folder name -----------------------------------------------------
    if path.name != path.name.lower():
        res.error(f"folder name must be lowercase (got '{path.name}')")
    if "_" in path.name or " " in path.name:
        res.error(f"folder name must use hyphens, not underscores or spaces (got '{path.name}')")

    # --- required files --------------------------------------------------
    for req in REQUIRED:
        if not (path / req).exists():
            res.error(f"missing required file: {req}")
    if res.errors:
        return res

    skill_text = (path / "SKILL.md").read_text(encoding="utf-8")
    evidence_text = (path / "EVIDENCE.md").read_text(encoding="utf-8")
    meta_text = (path / "meta.yml").read_text(encoding="utf-8")

    # --- frontmatter -----------------------------------------------------
    fm = parse_frontmatter(skill_text)
    if fm is None:
        res.error("SKILL.md has no YAML frontmatter (must start with --- and close with ---)")
        return res

    name = fm.get("name", "").strip()
    desc = fm.get("description", "").strip()

    if not name:
        res.error("SKILL.md frontmatter is missing 'name'")
    elif name != path.name:
        res.error(f"frontmatter name '{name}' does not match folder name '{path.name}'")

    if not desc:
        res.error("SKILL.md frontmatter is missing 'description' - this is the public API")
    else:
        if len(desc) < 20:
            res.error(f"description is only {len(desc)} chars - too vague to route on")
        if len(desc) > 500:
            res.warn(f"description is {len(desc)} chars - it loads on every turn, consider trimming")
        if "does not fire" not in desc.lower() and "does NOT fire" not in desc:
            res.warn("description has no 'Does NOT fire on:' clause - dormancy is half the grade")

    # --- placeholders ----------------------------------------------------
    skill_prose = strip_code_fences(skill_text)
    evidence_prose = strip_code_fences(evidence_text)
    meta_prose = strip_code_fences(meta_text)
    for ph in PLACEHOLDERS:
        if re.search(ph, skill_prose):
            res.error(f"SKILL.md still contains template placeholder: '{ph}'")
        if re.search(ph, evidence_prose):
            res.error(f"EVIDENCE.md still contains template placeholder: '{ph}'")
        if re.search(ph, meta_prose):
            res.error(f"meta.yml still contains template placeholder: '{ph}'")

    # --- body sections ---------------------------------------------------
    for section in ("When to use this", "Steps"):
        if section.lower() not in skill_text.lower():
            res.warn(f"SKILL.md has no '## {section}' section")

    # --- evidence --------------------------------------------------------
    if "```" not in evidence_text:
        res.error("EVIDENCE.md has no fenced transcript - paste what you actually typed and got")
    if not re.search(r"dormant|stayed quiet|did not fire|near-miss", evidence_text, re.I):
        res.error("EVIDENCE.md has no dormancy test - show a near-miss it correctly ignored")
    if len(evidence_text.strip()) < 400:
        res.error("EVIDENCE.md is too short to be a real record of a real run")

    # --- meta ------------------------------------------------------------
    meta = parse_frontmatter("---\n" + meta_text + "\n---\n") or {}
    if not meta.get("author"):
        res.error("meta.yml is missing 'author'")
    if not meta.get("category"):
        res.warn("meta.yml is missing 'category' - it will be filed under 'other'")

    check_secrets(path, res)
    return res


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="*", help="skill folders to validate")
    ap.add_argument("--all", action="store_true", help="validate every skill in skills/")
    args = ap.parse_args()

    if args.all or not args.paths:
        targets = sorted(
            p for p in SKILLS.iterdir() if p.is_dir() and not p.name.startswith("_")
        )
        if not targets:
            print("no skills yet - nothing to validate")
            return 0
    else:
        targets = [pathlib.Path(p).resolve() for p in args.paths]

    results = [validate(t) for t in targets]
    failed = 0

    for r in results:
        if r.ok and not r.warnings:
            print(f"  PASS  {r.name}")
        elif r.ok:
            print(f"  PASS  {r.name}")
            for w in r.warnings:
                print(f"        warning: {w}")
        else:
            failed += 1
            print(f"  FAIL  {r.name}")
            for e in r.errors:
                print(f"        error:   {e}")
            for w in r.warnings:
                print(f"        warning: {w}")

    print()
    print(f"{len(results) - failed}/{len(results)} passed")

    if failed:
        print("\nFix the errors above, then run this again. Warnings do not block a merge.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
