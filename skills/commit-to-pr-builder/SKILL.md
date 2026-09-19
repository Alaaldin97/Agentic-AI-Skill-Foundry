---
name: commit-to-pr-builder
description: "Turn the commits on a branch into a pull request title and description. Use when the user is about to open a PR, asks what to write in the PR body, wants to fill in a PR template, or wants their commits or git log summarised for reviewers. Does NOT fire on: writing a single commit message, reviewing someone else's PR, release notes or changelogs, or status updates written from commits."
---

# Commit-to-PR Builder

Turns the commits on the current branch into a PR title and description that a
reviewer can read in one pass, using the repo's own PR template when it has one.

## When to use this

Fires when the user asks to:

- write the description or body for a pull request they are about to open
- work out what to put in their PR, or fill in the repo's PR template
- turn their commits or `git log` into something a reviewer can read

**Does NOT fire on:**

- writing one commit message for staged changes: that describes a single change, not a branch
- reviewing or commenting on someone else's PR: that judges code, it does not describe it
- release notes or a CHANGELOG: the reader is a user of the software, not a reviewer
- a daily or weekly status update from commits: the reader is the team, and it is not tied to one branch

## Steps

1. **Collect the real commits.** Take the base branch the user names, or `main`
   if they name none. If you can run commands, run
   `git log --oneline <base>..HEAD` and `git diff --stat <base>...HEAD`. If you
   cannot, ask the user to paste the output of those two commands and wait.
   Everything after this step is built from that output, so do not start writing
   before you have it.
2. **Look for a PR template** in `.github/PULL_REQUEST_TEMPLATE.md`,
   `.github/pull_request_template.md`, `docs/` and the repo root. If one exists,
   its headings are the structure of your answer: fill every section in order and
   add none of your own.
3. **Group the commits by intent, not by order:** features, fixes, then
   refactors and chores. Fold `wip`, `fixup` and typo commits into the change they
   belong to, because a reviewer cares about what changed, not how many attempts it took.
4. **Write the title:** imperative mood, under 72 characters, naming the outcome
   ("Add commit-to-pr-builder skill", not "Updates").
5. **Write the body.** With no template, use these four sections:
   - *Summary*: one or two sentences on what the branch does and why
   - *Changes*: the grouped list from step 3
   - *How to test*: concrete steps based on the files the diff touches
   - *Notes for reviewers*: breaking changes, risky spots, follow-ups
6. **Report back** with the title and body in one fenced markdown block the user
   can paste as-is, followed by a short list of the gaps they need to fill themselves.

## Rules

- Describe only what the commits and the diff show. When a commit message is
  vague (`fix`, `update`, `wip`), read that commit's diff with `git show --stat <sha>`;
  if you still cannot tell, list it as a gap instead of guessing. An invented
  change in a PR description misleads the person approving it.
- Leave every checklist box unticked unless the user has told you it is true in
  this conversation. Ticking "tests pass" or "validator passes" on their behalf is
  a claim they have not made.
- Issue numbers, screenshots and test results are gaps unless the user gave them.
- Write in English unless the user or the repo's existing PRs use another language.
