---
name: _TEMPLATE
description: >
  REPLACE THIS. Describe the symptom the user will type, not the feature you
  built. Two to four sentences. Start with the verbs a user would use, name the
  concrete artefacts involved, then add the near-misses.
  Does NOT fire on: list the close-but-wrong cases here.
---

# Skill name

One sentence on what this does and who it is for.

## When to use this

Fires when the user asks to:

- concrete trigger one — the words a user actually types
- concrete trigger two
- concrete trigger three

**Does NOT fire on:**

- the near-miss that would be wrong — and why it is different
- another near-miss

> Be specific here. This section is what stops your skill hijacking unrelated
> conversations once someone has thirty skills installed.

## Steps

1. First action. One thing per step.
2. Second action.
3. Third action.
4. Report back with <what the user gets>.

## Rules

- Hard constraint that must never be violated.
- Another constraint.
- If something must happen *every single time*, do not write it here — put it
  in `scripts/` and call it. A rule in prose is advisory; a script is enforced.

## Resources

<!-- Delete this section if you have none. -->

| File | What it holds | Loaded when |
|---|---|---|
| `resources/example.md` | Reference data the model cannot guess | Step 2 |

## Scripts

<!-- Delete this section if you have none. -->

| Script | What it does |
|---|---|
| `scripts/example.py` | Does the deterministic part |
