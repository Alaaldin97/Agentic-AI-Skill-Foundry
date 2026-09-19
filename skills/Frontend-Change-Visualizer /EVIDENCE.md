# Evidence — `Frontend-Change-Visualizer`

**Tested on:** VS Code 1.137 with Copilot SDK · **Date:** 2026-09-15

---

## 1. It fired when it should

**What I typed:**

```
Show me what changed in the frontend after the redesign.
```

**What happened:**

```
The skill inspected the current worktree, checked Git status and the project
file inventory, and found no tracked React/frontend diff after
`neej-frontend-craft`. It generated
`frontend-change-report-current-worktree.html` with an honest empty comparison:
0 changed UI components, 0 changed pages, and 0 responsive changes. The report
explains that the only uncommitted changes are the visualizer skill files and
does not invent a before state.
```

**Did it activate on its own?** No. This run was explicitly invoked by naming
`Frontend-Change-Visualizer`; automatic trigger behavior still needs to be
tested in a fresh natural-language prompt.

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```
Use the UI/UX design skill to redesign my shopping page.
```

**Did it stay dormant?** Yes. The request asks for a UI change, not a
before/after analysis. `neej-frontend-craft` is the appropriate skill.

**Why this one is a real test:** Both prompts concern frontend design work, but
only the first asks for post-change comparison and visualization.

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~42 tokens |
| Body, once it fired | ~1,150 tokens |
| What stayed on disk because it did not fire | ~1,150 tokens |

---

## 4. Anything a reviewer should know

- Known limitation: no reliable "before" state when changes were made outside
  git or history was squashed — the skill reports this gap instead of
  guessing.
- Needs an API key / network: no
- Anything that surprised you: The repository used for the verification run
  contained static HTML learning materials but no React app or package
  manifest, so the correct output was a limitation report rather than a
  component comparison.
