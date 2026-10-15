
# Evidence — python-env-doctor

**Tested on:** Module 05B skill_runner.py, PowerShell,
Python 3.12 environment

**Date:** 2026-10-15

---

## 1. It fired when it should

**What I typed:**

```text
My project requires Python 3.12, but PowerShell is using Python 3.14.3. Help me diagnose and fix the Python environment mismatch.
```

**What happened:**

```text
SKILLS   4 on disk: jhf-brief, lab-grader, python-env-doctor, repo-onboarder
ROUTED   python-env-doctor

ANSWER

To diagnose and fix the Python environment mismatch where your project requires Python 3.12 but PowerShell is using Python 3.14.3, let's start by gathering some information.

Please run the following commands in your PowerShell and share the output:

1. Check the Python version:
python --version

2. Check the Python executable path:
Get-Command python

3. List all installed Python versions using the Python launcher:
py -0p

[...]

PROGRESSIVE DISCLOSURE
skills on disk .............. 4
menu shown to the router .... ~306 tokens
if we had loaded ALL of them. ~1,924 tokens
we actually loaded .......... ~443 tokens (python-env-doctor)
SAVED ....................... ~1,481 tokens
```

**Did it activate on its own?** Yes.

The request did not mention the skill name.
The runner automatically selected python-env-doctor.
The response requested diagnostic information before
recommending environment changes.

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```text
My Python code gives a SyntaxError because I forgot a colon after an if statement. Explain why this happens and show me how to fix the code.
```

**What happened:**

```text
SKILLS   4 on disk: jhf-brief, lab-grader, python-env-doctor, repo-onboarder
ROUTED   NO_SKILL — answering directly

ANSWER

A `SyntaxError` occurs in Python when the code structure does not follow the language's syntax rules.

[...]

Simply add a colon at the end of the `if` statement:

if x > 10:
    print("x is greater than 10")

[...]

PROGRESSIVE DISCLOSURE
skills on disk .............. 4
menu shown to the router .... ~306 tokens
if we had loaded ALL of them. ~1,924 tokens
we actually loaded .......... ~0 tokens (nothing)
SAVED ....................... ~1,924 tokens
```

**Did it stay dormant?** Yes.

**Why this one is a real test:**

Both requests involve Python errors. However, the
negative test concerns Python syntax, not interpreter
or virtual environment configuration. The agent
correctly answered without activating the skill.

---

## 3. What it cost

| Measurement | Tokens (approx.) |
|---|---|
| Menu for all four skills | 306 |
| python-env-doctor body when activated | 443 |
| Other skill bodies not loaded in positive test | 1,481 |
| Skill bodies loaded in negative test | 0 |

The runner reports the combined menu cost rather
than the individual description cost.

---

## 4. Anything a reviewer should know

- Known limitation: The skill provides diagnostic
  instructions but does not automatically execute
  commands on the user's computer.
- Needs an API key / network: The tested runner uses
  an OpenRouter API key and network access.
- The skill itself does not require a separate API key.
- The positive test confirmed correct routing and
  initial diagnosis, not a completed environment repair.
- The negative test confirmed that Python syntax
  questions do not trigger this skill.
