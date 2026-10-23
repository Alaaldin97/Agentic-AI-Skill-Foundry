---
name: python-bug-triage
description: Triage a Python or AI-agent bug report into severity, likely component, missing facts, and the next action. Use when the user shares a traceback, crash, failing test, or "this is broken" report and needs it classified quickly. Does NOT fire on: general repo explanations, onboarding, writing help, code review, or non-bug instructions.
---

# Python Bug Triage

This skill turns a noisy bug report into a clean triage note: severity, likely component, required missing information, and the next action.

## When to use this

Fires when the user asks to:

- triage a Python bug report or traceback
- classify a crash, regression, or failing AI-agent workflow
- identify missing fields in a bug submission
- decide severity and likely component for a broken Python or agent flow

**Does NOT fire on:**

- explaining how a repository works or onboarding a new developer
- writing a brief, summary, or general guidance document
- reviewing pull requests or debugging code without a bug report
- non-bug tasks such as writing a cover letter or general help that is not a report triage

## Steps

1. Read the bug report exactly as given by the user.
2. Read `resources/triage-rules.md` to load the triage rules and required facts.
3. Run `triage_bug.py` with the raw bug report text so the severity and missing-facts logic are deterministic.
4. If the report is missing expected result, actual result, reproduction steps, or version/environment, say so plainly and ask for those facts instead of guessing.
5. Write a brief triage summary with four items: severity, likely component, missing facts, and the next action.
6. Save the finished triage to `triage-agent.md` with `save_output`.

## Rules

- Never invent a traceback, stack trace, or user environment.
- A bug report without reproduction steps is not a complete report.
- If the report is severe, say so only when the evidence matches the rule set.
- Prefer precise missing-information requests over guesses.
- Do not escalate feature requests into bug triage.
- Keep the output tight, factual, and actionable.

## Resources

| File | What it holds | Loaded when |
|---|---|---|
| `resources/triage-rules.md` | Severity rules, required evidence, and the missing-facts workflow | Step 2 |

## Scripts

| Script | What it does |
|---|---|
| `scripts/triage_bug.py` | Determines severity, identifies likely component, and reports missing facts using deterministic checks |
