# Evidence — `skill-reviewer`

**Tested on:** Windows 11 · Python 3.12 · VS Code 1.137 · **Date:** 2026-09-13

> This is the reference example for The Skill Foundry. Everything below is a
> real run on a real machine — copied from the terminal, not reconstructed.

---

## 1. It fired when it should

**What I typed:**

```
Review the skill in skills/skill-reviewer and tell me if it's ready to submit.
```

**What happened** — step 2 of the skill runs the mechanical gate first. That run,
verbatim, at a point when the skill was deliberately incomplete:

```
$ python skills/skill-reviewer/scripts/review_skill.py skills/skill-reviewer

skill: skill-reviewer
----------------------------------------------------
ok    SKILL.md
FAIL  EVIDENCE.md
FAIL  meta.yml
ok    name: skill-reviewer
ok    description: 443 chars
ok    section: When to use this
ok    section: Steps
ok    section: Rules
ok    body: 95 lines
note  7 hard rule(s) found; scripts/ present
ok    no secrets or absolute paths
----------------------------------------------------

BLOCKING: 2 issue(s) must be fixed before merge.
```

It caught its own two missing files and refused to pass itself. That is the
behaviour we want — **the gate does not care whose skill it is.**

**Did it activate on its own?** Yes — on the phrase *"review the skill … ready to
submit"*, with no mention of the skill name.

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```
Review this pull request and tell me if the error handling is correct.
```

**Did it stay dormant?** Yes.

**Why this one is a real test:** it opens with the word *"review"* — the exact
verb this skill is built around — and it is a genuine review request. The only
thing that separates it is that there is no skill involved. If the description
had said *"reviews code"* instead of naming `SKILL.md` explicitly, this would
have fired and wasted the load. The `Does NOT fire on:` clause names this case
directly.

---

### 2b. A second dormancy case, caught by the gate itself

The mechanical checks are not just about the skill being reviewed. Run against
the blank template, they correctly refuse it:

```
$ python skills/skill-reviewer/scripts/review_skill.py skills/_TEMPLATE

FAIL  unfilled template text: SKILL.md: 'REPLACE THIS'
FAIL  unfilled template text: SKILL.md: 'concrete trigger one'
FAIL  unfilled template text: EVIDENCE.md: '<the exact prompt'
FAIL  unfilled template text: meta.yml: 'Your Name'
FAIL  unfilled template text: meta.yml: 'your-github-username'
----------------------------------------------------

BLOCKING: 7 issue(s) must be fixed before merge.
```

An earlier version of this script **passed** the blank template — it checked
structure but never checked whether anyone had filled it in. That gap was only
visible by running it against the template. It is fixed above.

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~110 |
| `SKILL.md` body, once it fired | ~1,050 |
| `resources/failure-modes.md`, loaded at step 3 | ~640 |
| `resources/review-format.md`, loaded at step 7 | ~430 |
| Stayed on disk on a turn where it did not fire | ~2,120 |

The two resource files are **half the weight of this skill** and neither loads
until the step that needs them. Had they been pasted into `SKILL.md`, every
invocation would pay for both whether or not it reached step 3.

---

## 4. Anything a reviewer should know

- **Known limitation:** step 4 (the routing test) is judgement, not measurement.
  It predicts from the description whether a skill *would* fire. It is a good
  proxy, not proof. Real proof is installing the skill and typing the prompt.
- **Needs an API key / network:** no. Python 3 only, no third-party packages.
- **What surprised me:** writing a reviewer forced the sharpest possible test of
  the repo's own standard — the first version of the script happily approved an
  empty template. A gate nobody has attacked is not yet a gate.
