# Evidence — `commit-generator`


**Tested on:** <VS Code  1.135.0> · **Date:** <2026-09-20>

---

## 1. It fired when it should

**What I typed:**

```
python3 skill_runner.py "Write a short commit to push this skill -commit-generator- to github"
```

**What happened:**

```
====================================================================
REQUEST  Write a short commit to push this skill -commit-generator- to github
SKILLS   7 on disk: commit-generator, interview-prep, jhf-brief, lab-grader, recipe-scaler, repo-onboarder, trip-formatter
ROUTED   commit-generator
====================================================================

--------------------------------------------------------------------
ANSWER

feat(commit-generator): initial commit of commit message skill

- Add skill to generate conventional commit messages based on changes
- Supports types like feat, fix, refactor, docs, style, test, chore
- Formats commit messages with scope and short description

--------------------------------------------------------------------
PROGRESSIVE DISCLOSURE — what it actually cost
  skills on disk .............. 7
  menu shown to the router .... ~473 tokens
  if we had loaded ALL of them. ~2,262 tokens
  we actually loaded .......... ~180 tokens (commit-generator)
  SAVED ....................... ~2,082 tokens
--------------------------------------------------------------------
```

**Did it activate on its own?** <yes>

---

## 2. It stayed quiet when it should

The whole point of a narrow description is that the skill does **not** fire on
things that merely sound similar.

**A near-miss I tested:**

```
how do I use git rebase
```

***Did it stay dormant?** yes

**Why this one is a real test:** It involves Git and version control terminology, but it is an instructional/conceptual question rather than a request to generate a commit message.

---

## 3. What it cost

|| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~473 |
| Body, once it fired | ~180 |
| What stayed on disk because it did not fire | ~2,262 |

---

## 4. Anything a reviewer should know

- Known limitation: None.
- Needs an API key / network:  no
- Anything that surprised you: The router efficiently distinguished between formatting a commit and general git usage.