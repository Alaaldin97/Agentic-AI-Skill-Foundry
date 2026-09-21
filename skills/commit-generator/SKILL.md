---
name: commit-generator
description: >
  Generate standard conventional commit messages from a list of code changes or diff descriptions.
  Use when the user asks to write a commit message, generate a conventional commit, or summarize changes for a commit.
  Does NOT fire on: questions about git rebase, general version control help, or explaining git commit commands.
---

# Git Commit Message Generator

Generate standard conventional commit messages from a list of code changes or diff descriptions.

## When to use this

Fires when the user asks to:

- write a commit message for these changes
- generate a conventional commit for code changes
- summarize this diff for git

**Does NOT fire on:**

- how do I use git rebase — because it is a conceptual question, not a commit writing request
- explain git commit commands — because it asks for documentation rather than generating a message
- writing a pull request description from a branch's commits — that summarises a branch for
  reviewers, not a single change (see `commit-to-pr-builder`)

## Steps

1. Parse the user's provided list of changes or brief description of what was done.
2. Categorize the change into standard conventional types: feat, fix, refactor, docs, style, test, or chore.
3. Format the output strictly as a conventional commit message: `<type>(<scope>): <short description>`, followed by a short bulleted body if details are provided.
4. Keep the subject line under 50 characters.

## Rules

- Must strictly follow the Conventional Commits specification.
- Subject line must be under 50 characters.