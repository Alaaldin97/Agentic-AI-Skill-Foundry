---
name: find-skills
description: >
  Find an existing agent skill instead of building one from scratch. Use when the
  user asks to find a skill for a task, whether a skill already exists for
  something, or says they are about to build a skill and wants to check first.
  Searches The Skill Foundry, skillspool.org and GitHub.
  Does NOT fire on: writing or editing a skill they already have, reviewing a
  skill's quality, or finding a Python package, VS Code extension or MCP server.
---

# find-skills

Checks whether somebody has already solved the problem before you spend three
hours solving it again. Searches nearest-first, and tells you honestly how much
to trust each result.

## When to use this

Fires when the user asks:

- "find me a skill for <task>"
- "is there already a skill that does <thing>?"
- "where can I get a skill that <does X>?"
- "I'm about to build a skill for <task>" — check first, this is the best moment
- when a task comes up repeatedly and no installed skill covers it

**Does NOT fire on:**

- writing or editing a skill they already have — that is authoring, not discovery
- reviewing a skill's quality — use `skill-reviewer`
- an installed skill failing to load — that is a client configuration problem
- finding a Python package, VS Code extension, or MCP server. Those are not skills

## Steps

1. **Turn the request into English keywords.** The indexes are English-only. If
   the user writes in Arabic or another language, translate the *intent* — do not
   pass the raw string.

2. **Run the search:**

   ```
   python scripts/search_skills.py "<keywords>" --limit 5
   ```

   It queries three sources in this order, and a dead source degrades the result
   rather than ending the run:

   | Order | Source | Why it is in this position |
   |---|---|---|
   | 1 | **The Skill Foundry** | Already reviewed, already has evidence, and a classmate can explain it |
   | 2 | **skillspool.org** | Curated directory with real metadata |
   | 3 | **GitHub** | The long tail — comprehensive but unreviewed |

3. **Read the degradation note.** If the script reports sources down, say so in
   your answer. A partial search that looks complete is worse than one that
   admits its gaps.

4. **Assess safety before recommending.** Apply `resources/trust-signals.md` to
   every candidate. Never present an unreviewed result as if it were vetted.

5. **Recommend at most three.** For each: one line on why it fits, the trust
   signal, and the link. More than three and the user just picks the first anyway.

6. **If nothing fits, say so and offer the alternative:** open a skill request on
   the Foundry, or build it — the request template is at
   `.github/ISSUE_TEMPLATE/skill-request.yml`.

7. **Before they install anything from outside the Foundry**, read its `SKILL.md`
   and check it against the red flags in `resources/trust-signals.md`.

## Rules

- **Never auto-install.** Recommend, link, and let the user decide. Installing a
  skill grants it the same tool access you have.
- **Always check The Skill Foundry first.** A reviewed skill from a classmate
  beats a 40k-star repo nobody here has read.
- Never present a GitHub result without the word **unreviewed** attached.
- Star count is a popularity signal, not a safety signal. A skill can be popular
  and still be wrong for this user.
- If every source is down, say so plainly. Do not answer from memory — skill
  directories change weekly and a remembered answer will be stale.

## Resources

| File | What it holds | Loaded when |
|---|---|---|
| `resources/trust-signals.md` | How to judge a skill you did not write | Steps 4 and 7 |

## Scripts

| Script | What it does |
|---|---|
| `scripts/search_skills.py` | Queries all three sources, degrades gracefully, stdlib only |
