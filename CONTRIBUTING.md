# Contributing a skill to The Skill Foundry

Everything here takes about **20 minutes** the first time and **5 minutes** after that.

> **The rule:** a skill gets merged when someone else can install it and it works for them too. That is the only bar. Everything below exists to make that likely.

---

## Before you start

You need a skill that **you have actually run**. Not one you wrote and assumed works — one you watched fire on a real prompt and produce a real output. If you have not run it yet, go do that first; the evidence file will be impossible to write otherwise.

---

## Step 1 — Branch

```bash
git clone https://github.com/Alaaldin97/Agentic-AI-Skill-Foundry.git
cd Agentic-AI-Skill-Foundry
git checkout -b skill/my-skill-name
```

Branch naming: `skill/<kebab-case-name>`. Match your folder name.

---

## Step 2 — Copy the template

```bash
cp -r skills/_TEMPLATE skills/my-skill-name
```

On Windows PowerShell:
```powershell
Copy-Item -Recurse skills\_TEMPLATE skills\my-skill-name
```

Folder name rules — CI enforces all three:
- lowercase
- hyphens, not spaces or underscores
- must match the `name:` in your frontmatter

---

## Step 3 — Write `SKILL.md`

### The frontmatter is the public API

```yaml
---
name: linkedin-marketing
description: >
  Plan, draft, audit and publish LinkedIn posts and comments. Use when the user
  wants to write a viral LinkedIn post, draft a comment or reply on any LinkedIn
  post URL, or audit a draft against current algorithm heuristics.
  Does NOT fire on: general copywriting, other social platforms, or CV writing.
---
```

**This description is the only thing the model sees when deciding whether to load your skill.** The body stays on disk until the description wins. So:

| ❌ Don't write | ✅ Write |
|---|---|
| "A powerful LinkedIn tool" | "when the user wants to write a viral LinkedIn post" |
| "Handles social media" | "draft a comment or reply on any LinkedIn post URL" |
| The feature you built | **The symptom the user will type** |

Add a `Does NOT fire on:` line. It is the single highest-leverage sentence in the file — it is what stops your skill hijacking unrelated conversations.

### The body — three sections, in this order

```markdown
## When to use this
Concrete triggers. Then: **Does NOT fire on** — the near-misses.

## Steps
Numbered. Each step one action. This is the part the model follows.

## Rules
Hard constraints. What must never happen.
```

Keep it under ~500 lines. If it is longer, move the bulk into `resources/` and reference it — that way it loads only when actually needed.

---

## Step 4 — Write `EVIDENCE.md` (the part people skip)

**This is what replaces "submit an issue with a screenshot."** It is the proof your skill works, and it is what reviewers read first.

You need three things:

### 1. A positive case
The exact prompt you typed, and the real output. Paste it. Trim it if it is enormous, but do not paraphrase it.

### 2. A dormancy case
A prompt that is *close to* your trigger but should NOT fire it — and confirmation that it didn't.

> Example: `linkedin-marketing` should stay dormant on *"write me a cover letter."* Close, but wrong. If it fires there, the description is too greedy.

### 3. What it cost
Roughly how much context the skill loaded when it fired. You can read this from your client's token counter.

> **Why dormancy matters more than you think:** with 40 skills installed, a greedy description does not just fire once wrongly — it competes for attention on *every* turn, for everyone. One badly-scoped skill degrades the whole library. This is why we review.

---

## Step 5 — Validate locally

```bash
python scripts/validate_skill.py skills/my-skill-name
```

This is **the same script CI runs.** If it passes locally it will pass on GitHub. It checks:

- frontmatter parses and has `name` + `description`
- `name` matches the folder name
- description is 20–500 chars and is not the template placeholder
- `EVIDENCE.md` exists, has a transcript, and has a dormancy section
- `meta.yml` parses and has an author
- no secrets, API keys or absolute home paths committed

> Notice what just happened: everything in this guide is **advice**, but that script is a **gate**. Advice gets ignored under deadline; gates do not. That is the whole lesson of the module, applied to the repo you are reading.

---

## Step 6 — Open the PR

```bash
git add skills/my-skill-name
git commit -m "Add skill: my-skill-name"
git push origin skill/my-skill-name
```

Then open the PR on GitHub. The template will prompt you for:

- one line on what it does
- the trigger phrase you tested
- the near-miss it correctly ignored
- which client you tested on

---

## Step 7 — Review someone else's

**You are expected to review at least one other PR.** Not optional — it is half of what you get out of this.

What to look for:

| Check | The question to ask |
|---|---|
| **Description scope** | Would this fire on something unrelated to its job? |
| **Dormancy evidence** | Did they actually test a near-miss, or invent one? |
| **Determinism** | Is a must-happen rule sitting in prose where the model can skip it? |
| **Size** | Is the body bloated with things that belong in `resources/`? |
| **Would I install it?** | The only question that really matters. |

Leave one concrete, actionable comment. "Looks good" is not a review.

---

## After the course

This repo does not close in Week 10. If you build something at work that saves you an hour a week, bring it back here. The library is only as good as what stays in it.

---

## Quick reference

```bash
# start
git checkout -b skill/my-skill-name
cp -r skills/_TEMPLATE skills/my-skill-name

# check
python scripts/validate_skill.py skills/my-skill-name

# ship
git add skills/my-skill-name
git commit -m "Add skill: my-skill-name"
git push origin skill/my-skill-name
```
