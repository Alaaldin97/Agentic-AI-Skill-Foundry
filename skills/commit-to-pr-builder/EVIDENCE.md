# Evidence — `commit-to-pr-builder`

**Tested on:** Claude Code v2.1.272 (Opus 5), 19 skills installed · **Date:** 2026-09-19

Both runs were in a fresh session, in my fork of this repo, on the branch
`skill/commit-to-pr-builder`. Transcripts are from Claude Code's `/export`; I
only removed the `/export` line itself because it contains my home path.

---

## 1. It fired when it should

**What I typed:**

```
I'm about to open a pull request for this branch. What should I write in the description?
```

**What happened:**

```
 ▐▛███▛█   Claude Code v2.1.272
▝▜██████▀  Opus 5 · Claude Pro
  ▝▝ ▝▝    ~/Agentic-AI-Skill-Foundry


❯ I'm about to open a pull request for this branch. What should I write in the  
  description?                                                                  

● Skill(commit-to-pr-builder)
  ⎿  Successfully loaded skill

  Ran 3 shell commands (ctrl+o to expand)

● The repo has a PR template (.github/PULL_REQUEST_TEMPLATE.md), so this follows
  its sections exactly. Past merges use the skill name as the title (e.g.
  lecture-timeline-mapper (#8)), so I did the same.

  markdown
  commit-to-pr-builder

  ## What does it do?

  Turns the commits on the current branch into a PR title and description a
  reviewer can read in one pass, filling in the repo's own PR template when
  there is one.

  ## The trigger phrase you tested

  I'm about to open a pull request for this branch. What should I write in the
  description?

  ## The near-miss it correctly ignored

  <TODO: e.g. "Write a commit message for my staged changes">

  ## Checklist

  - [ ] I have **actually run this** — `EVIDENCE.md` contains a real transcript,
  not a description
  - [ ] It fired **without me naming it**
  - [ ] I tested a near-miss and it **stayed dormant**
  - [ ] `python scripts/validate_skill.py skills/<my-skill>` passes locally
  - [ ] No API keys, tokens, or absolute paths from my machine
  - [ ] `meta.yml` has my name and the client I tested on

  ## Shape

  - [ ] Instructions only — `SKILL.md` and nothing else
  - [ ] Enforces a method — makes the model follow a process it would otherwise
  skip
  - [ ] Ships scripts — something must happen the same way every time
  - [ ] Ships knowledge — facts the model cannot guess
  - [ ] Ships a runtime — needs a real toolchain

  ## Anything a reviewer should know

  - Adds `skills/commit-to-pr-builder/` with `SKILL.md`, `meta.yml` and
  `EVIDENCE.md` (3 files, +137 lines).
  - Needs `git` on the PATH. If the model can't run commands, the skill asks the
  user to paste `git log` and `git diff --stat` output instead.
  - Scoped to exclude single commit messages, reviewing other people's PRs,
  release notes/changelogs and status updates.
  - Checklist boxes stay unticked unless the user has confirmed them, and
  anything the diff doesn't show is listed as a gap, not guessed.

  ---

  <sub>Reviewers: install it and try to break it. Does it fire on something
  unrelated? Is a must-happen rule sitting in prose where the model can skip it?
  One concrete comment beats "looks good".</sub>

  The branch will fail CI right now. I ran python scripts/validate_skill.py 
  skills/commit-to-pr-builder and it fails: EVIDENCE.md is still the unfilled
  template (it still contains _TEMPLATE). Fix this before you open the PR.

  Things you still need to fill in:
  - EVIDENCE.md: Add a real transcript. This conversation counts for section 1:
    your prompt above loaded the skill without you naming it. You still need to
    test a near-miss and fill in the token costs.
  - Near-miss prompt: You haven't tested one yet. Try one and paste it in once
    you've seen the skill stay quiet.
  - meta.yml: It still says tested_on: TBD. Put your client there (e.g. Claude
    Code).
  - Checklist and Shape: I left every box unticked. meta.yml says shape: method,
    which matches "Enforces a method", so tick that if it's right. Tick the
    checklist items once each one is true. The validator item only applies after
    the fix above.

✻ Brewed for 25s · done 12:53 AM
```

**Did it activate on its own?** Yes. The prompt never names the skill, and
`Skill(commit-to-pr-builder)` loaded before anything else happened.

What the run shows beyond firing: it found and filled the repo's own PR
template instead of inventing sections, left every checkbox unticked, listed
the missing near-miss as a TODO instead of making one up, and the "+137 lines"
matches the real diff (61 + 67 + 9 lines across the three files).

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```
Write a commit message for my staged changes.
```

**What happened** (new session, same repo and branch, with one real staged
change to `meta.yml`):

```
❯ Write a commit message for my staged changes.

  Ran 1 shell command

Here's a commit message for the one staged change, which sets tested_on in skills/commit-to-pr-builder/meta.yml:

Set tested_on for commit-to-pr-builder

It's a single line to match your recent commit subjects. If you want a body too:

Set tested_on for commit-to-pr-builder

Record Claude Code 2.1.272 as the tested version in meta.yml,
replacing the TBD placeholder.

I haven't committed anything. If you commit it through me, I'll add a Co-Authored-By: Claude Opus 5 <noreply@anthropic.com> trailer.

✻ Sautéed for 6s · done 1:03 AM
```

**Did it stay dormant?** Yes. No `Skill(commit-to-pr-builder)` line: it wrote a
plain commit message and did not reach for a PR template.

**Why this one is a real test:** same repo, same branch, same git history, and
the output is also a summary of changes written for other developers. The only
difference is the unit: one staged change for a commit, not a whole branch for
a PR.

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~100 |
| Body, once it fired | ~760 |
| What stayed on disk because it did not fire | ~760 (the whole body, in run 2) |

`/context` in Claude Code reported **2.9k tokens for all 19 installed skill
descriptions together** and does not split that per skill in its default view,
so the per-skill numbers above are estimated from file size at about 4
characters per token (388-character description, about 3,050-character body).

---

## 4. Anything a reviewer should know

- Known limitation: the base branch defaults to `main`. On a repo that uses
  `master` or `develop`, the user has to name the base branch.
- Needs an API key / network: no. Needs `git`.
- Anything that surprised you: in run 1 it went beyond the steps in two ways.
  It picked the title from the repo's past merge titles instead of the
  imperative title in step 4, and it ran the validator on its own to warn that
  CI would fail. Both were useful here, but neither is something the skill asks for.
