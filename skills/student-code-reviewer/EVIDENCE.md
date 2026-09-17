# Evidence — `student-code-reviewer`

**Tested on:** VS Code 1.137 · **Date:** 2026-09-17

---

## 1. It fired when it should

**What I typed:**

```
Can you look at my C code? I want it to check if x is 5, but it always prints 'x is five' even when x is 3: if (x = 5) { printf('x is five'); }
```

**What happened:**

```text
====================================================================
REQUEST  Can you look at my C code? I want it to check if x is 5, but it always prints 'x is five' even when x is 3: if (x = 5) { printf('x is five'); }
SKILLS   5 on disk: jhf-brief, lab-grader, repo-onboarder, sql-explainer-optimiser, student-code-reviewer
ROUTED   student-code-reviewer
====================================================================
  -> read_resource({'relative_path': 'resources/common-mistakes.md'}...)

--------------------------------------------------------------------
ANSWER

Thanks for sharing your code snippet! One thing you're doing well is using an if statement to check a condition, which is the right approach to decide what to print based on the value of x.

Now, let's look at the issue:

- **Location:** The condition inside the if statement: `if (x = 5)`
- **Observation:** The code uses a single equals sign `=`, which in C means assignment, not comparison. So instead of checking if x is 5, it sets x to 5. Since the assignment expression evaluates to the assigned value (which is 5, a non-zero value), the condition is always true, and the print statement always runs.
- **Think about it:** How do you write a condition in C that checks if two values are equal rather than assigning one value to another? What operator is used for equality comparison?

Also, a small note about your `printf` statement: you used single quotes `'x is five'`, but in C, string literals should be enclosed in double quotes `"x is five"`.

Try changing the condition to use the equality operator and fix the quotes in the print statement, then test your program again. Let me know what happens!
```

**Did it activate on its own?** Yes — the router selected it from five skills on
disk without being named, and the skill then loaded `resources/common-mistakes.md`
before diagnosing.

Note that it diagnosed the assignment-vs-comparison bug and the single-quote
string literal without ever supplying corrected code — the fix is left to the
student as a leading question, which is the whole point of the skill.

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```
Can you write a python script to reverse a string?
```

**Did it stay dormant?** Yes — routed `NO_SKILL — answering directly`.

```text
====================================================================
REQUEST  Can you write a python script to reverse a string?
SKILLS   5 on disk: jhf-brief, lab-grader, repo-onboarder, sql-explainer-optimiser, student-code-reviewer
ROUTED   NO_SKILL — answering directly
====================================================================
```

**Why this one is a real test:** it is a beginner Python request aimed at the
same audience the skill serves, so it sits close to the trigger. The difference
is that there is no student code to review — the user wants new code written.
The description draws exactly that line ("ONLY trigger if the user provides a
code snippet to review"), and the router respected it.

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~359 for the whole 5-skill menu |
| Body, once it fired | SKILL.md + `resources/common-mistakes.md` on demand |
| What stayed on disk because it did not fire | ~3,270 if every skill had been loaded eagerly |

Measured on the dormancy run: five skills on disk, the router saw only the
~359-token menu, nothing was loaded, and ~3,270 tokens were saved versus
loading all five bodies up front.

---

## 4. Anything a reviewer should know

- Known limitation: the review quality depends on the student stating the
  expected behaviour. If they paste code with no description of what it should
  do, the skill asks a clarifying question rather than guessing.
- Needs an API key / network: no
- Anything that surprised you: the resource file is loaded on demand rather
  than sitting in the description, so the routing cost stays small even though
  the checklist itself is long.
