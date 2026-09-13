---
name: skill-reviewer
description: >
  Review an agent skill before it is submitted or merged. Use when the user asks
  to review a skill, check a SKILL.md, audit a skill's description, work out why
  a skill is not firing, why a skill fires on the wrong prompts, or whether a
  skill is ready to open a pull request against The Skill Foundry.
  Does NOT fire on: reviewing ordinary source code, reviewing a pull request that
  contains no SKILL.md, or writing a brand-new skill from scratch.
---

# skill-reviewer

Reviews an agent skill the way a maintainer would: does the description earn its
place in the menu, will it fire when it should, will it stay quiet when it
shouldn't, and is anything critical sitting in prose where the model can skip it.

## When to use this

Fires when the user asks to:

- review a skill, or check whether a skill is ready to submit
- audit a `SKILL.md` description
- work out **why a skill is not firing** on the prompt they expected
- work out **why a skill keeps firing** on prompts it should ignore
- check a skill against The Skill Foundry merge bar

**Does NOT fire on:**

- reviewing ordinary application source code — that is a normal code review
- reviewing a pull request that contains no `SKILL.md`
- authoring a new skill from scratch — this reviews what already exists
- fixing a skill that fails to *install* — that is a client configuration problem

## Steps

1. **Locate the skill.** Find its `SKILL.md`. If the user named a folder, use it.
   If they did not, search for `SKILL.md` files and ask which one.

2. **Run the mechanical gate first.** Execute:

   ```
   python scripts/review_skill.py <path-to-skill-folder>
   ```

   This reports hard failures — missing files, malformed frontmatter, a name that
   disagrees with the folder, committed secrets. Do not spend reasoning on
   anything the script can decide. Report its output verbatim.

3. **Judge the description.** This is the part the script cannot do. Read the
   `description:` field alone, with no other context, and answer:
   - Does it name **the symptom a user would type**, or the feature the author built?
   - Does it include a `Does NOT fire on:` clause?
   - Read `resources/failure-modes.md` and check it against every mode listed there.

4. **Test routing on paper.** Write three prompts:
   - one that **must** fire it
   - one near-miss that **must not** fire it
   - one genuinely ambiguous case
   For each, decide from the description alone whether it would load. Show your
   reasoning. If you cannot decide, the description is too vague — say so.

5. **Check determinism.** Scan the body for any rule phrased as "always",
   "never", "must". For each, ask whether it is enforced by a script or merely
   stated. Flag anything critical that only exists as a sentence.

6. **Check the weight.** Note the body length. Anything over ~500 lines that is
   not in `resources/` loads in full every time the skill fires.

7. **Report** using the format in `resources/review-format.md`. End with one of
   exactly three verdicts: **Ready to submit**, **Needs work**, or **Reconsider
   the scope**.

## Rules

- **Never rewrite the skill.** Report findings and suggest edits; the author fixes it.
- **Always run the script before reasoning.** A mechanical failure makes the
  judgement moot, and the script is faster and more reliable than reading.
- Quote the exact line you are criticising. A finding without a quote is noise.
- Give at most **five** findings, ordered by severity. A twenty-item list gets ignored.
- If the description is the problem, say so first — it is the highest-leverage fix.
- Never approve a skill whose `EVIDENCE.md` has no dormancy test.

## Resources

| File | What it holds | Loaded when |
|---|---|---|
| `resources/failure-modes.md` | The seven ways a description goes wrong | Step 3 |
| `resources/review-format.md` | The report structure and the three verdicts | Step 7 |

## Scripts

| Script | What it does |
|---|---|
| `scripts/review_skill.py` | Mechanical checks — structure, frontmatter, secrets, weight |
