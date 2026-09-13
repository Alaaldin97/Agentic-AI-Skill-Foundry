# Evidence — `find-skills`

**Tested on:** Windows 11 · Python 3.14 · VS Code 1.137 · **Date:** 2026-09-13

---

## 1. It fired when it should

**What I typed:**

```
Is there already a skill for reviewing code, or do I need to build one?
```

**What happened** — step 2 runs the search across all three sources:

```
$ python skills/find-skills/scripts/search_skills.py "code review" --limit 3

searching for: "code review"

  The Skill Foundry    unavailable - HTTP 404
  skillspool.org       unavailable - HTTP 522

  GitHub
  ------
    Auto-claude-code-research-in-sleep  [16,072 stars - UNREVIEWED]
      ARIS (Auto-Research-In-Sleep) - Lightweight Markdown-only skills for
      autonomous ML research: cross-model review loops, idea discovery...
      https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
    gentle-ai  [6,717 stars - UNREVIEWED]
      Gentle-AI configures the AI coding agents you already use: Claude Code,
      Cursor, OpenCode, Codex, Pi, and more...
      https://github.com/Gentleman-Programming/gentle-ai
    delegate-skills  [1,973 stars - UNREVIEWED]
      Delegate a coding task to a separate coding agent CLI, review the diff,
      land the commit yourself - one per implementer.
      https://github.com/amElnagdy/delegate-skills

note: 2 source(s) down - results are partial: The Skill Foundry, skillspool.org
3 result(s). Read the SKILL.md before installing anything.
```

**Did it activate on its own?** Yes — on *"is there already a skill for…"*, with
no mention of the skill name.

A second run, different query, to confirm it was not a one-off:

```
$ python skills/find-skills/scripts/search_skills.py "linkedin post" --limit 2

  GitHub
  ------
    social-media-research-skills  [2,298 stars - UNREVIEWED]
    linkedin-agent-skill          [174 stars - UNREVIEWED]

note: 2 source(s) down - results are partial
2 result(s).
```

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```
Find me a Python package for parsing PDFs.
```

**Did it stay dormant?** Yes.

**Why this one is a real test:** it opens with *"find me a…"* — the exact phrase
this skill is built around — and it is a genuine discovery request. The only
difference is the object: a **package**, not a **skill**. The description names
this case explicitly (`Does NOT fire on: finding a Python package, VS Code
extension, or MCP server`), which is what keeps it quiet.

Without that clause this skill would fire on every "find me a…" in the session
and search three skill directories for something that was never a skill.

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~125 |
| `SKILL.md` body, once it fired | ~980 |
| `resources/trust-signals.md`, loaded at step 4 | ~700 |
| Stayed on disk on a turn where it did not fire | ~1,680 |

The trust-signals file is ~40% of this skill's total weight and only loads once
there is a candidate worth judging. A search that returns nothing never pays for
it.

---

## 4. Two real failures found while building this

Both are in the file now. Both are the kind of thing that only shows up when you
actually run the thing.

### skillspool.org was down — and the first version just crashed

The upstream skill this was adapted from calls the skillspool API directly and
assumes it answers. On the day I built this, it did not:

```
try 1: Response status code does not indicate success: 522.
try 2: Response status code does not indicate success: 522.
try 3: Response status code does not indicate success: 522.
```

`522` is Cloudflare reporting that the origin server never answered. **The skill
was unusable** for anything its single source could not serve.

The fix is the three-source design: each source is tried independently, a failure
degrades the result instead of ending it, and the user is *told* the search was
partial. In every run above, two of three sources were down and the skill still
returned useful answers — and said so honestly.

### It crashed on Windows the first time it found a result

```
UnicodeEncodeError: 'charmap' codec can't encode characters in position 11-12
```

The first GitHub description containing an emoji killed the script, because
Windows consoles default to `cp1252`. Every student on Windows would have hit
this on their first run. Fixed by forcing UTF-8 on stdout with
`errors="replace"`.

> Worth noting how this was caught: not by reading the code, but by running it
> once. Neither bug is visible on inspection.

---

## 5. Anything a reviewer should know

- **Needs network:** yes. No API key for any of the three sources.
- **Rate limits:** unauthenticated GitHub search is 10 requests/minute per IP. A
  whole class searching at once during a lab will hit it. The script reports the
  HTTP 403 as a source failure rather than crashing.
- **The Foundry source returns 404 in these transcripts** because `web/skills.json`
  did not exist at the time of the run. Once the catalog is deployed it resolves,
  and Foundry results — the reviewed ones — will rank first.
- **Known limitation:** it searches titles and descriptions, not skill bodies. A
  skill whose description is poorly written will not be found by this, which is a
  fair punishment for a poorly written description.
