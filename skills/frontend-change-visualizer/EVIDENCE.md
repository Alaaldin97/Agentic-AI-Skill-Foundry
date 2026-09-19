# Evidence — `Frontend-Change-Visualizer`

**Tested on:** VS Code 1.137 with Copilot SDK · **Date:** 2026-09-19

---

## 1. It fired when it should (real diff, Step 5 fully executed)

**Setup:** A minimal React shopping app (`AddToCartButton.jsx/css`,
`ProductCard.jsx/css`) was created and committed as the "before" state, then a
real `neej-frontend-craft`-style pass was committed as the "after" state:
button color/padding/border-radius/hover/focus-visible/aria-label, and card
border-radius/shadow/spacing/a mobile breakpoint.

**What I typed:**

```
Show me what changed in the frontend after the redesign.
```

**What happened:**

```
The skill ran `git diff HEAD~1 HEAD`, found 4 changed files, and discarded one
code-only change (a `productName` prop pass-through with no independent visible
effect). It classified the remaining changes into 2 real component-level
changes:
  - Add to Cart Button — 🎨 Visual, 🎯 Interaction, ♿ Accessibility — Medium impact
  - Product Card — 🎨 Visual, 📱 Responsive — Low impact
It then read `resources/report-template.html`, duplicated the
COMPONENT_CARD_START/END block once per component, filled every placeholder
({{COMPONENT_NAME}}, {{PAGE_PATH}}, {{CATEGORY_BADGES}}, {{IMPACT_BADGE}},
{{BEFORE_CONTENT}}, {{AFTER_CONTENT}}, {{WHAT_CHANGED_LIST}}) with real
before/after markup built from the actual before/after CSS values, and filled
the header placeholders with real counts (2 components, 1 page, 1 responsive
change). Output: `frontend-change-report-demo-shopping-app.html`.

Opened in a browser and verified visually: the Before button renders gray,
small padding, sharp corners; the After button renders blue, larger padding,
rounded corners, matching the real diff. Side-by-Side, Slider, and Overlay tabs
all switch correctly and the slider drag updates the clip in real time.
```

**Did it activate on its own?** No. This run was explicitly invoked by naming
`Frontend-Change-Visualizer`; automatic trigger behavior still needs to be
tested in a fresh natural-language prompt.

---

## 1b. It fired when it should (no real diff available — honest empty result)

**What I typed:**

```
Show me what changed in the frontend after the redesign.
```

**What happened:** run against a repository with no tracked React/frontend
diff and no package manifest. The skill correctly reported 0 changed
components, 0 changed pages, 0 responsive changes, stated plainly that no
reliable before-state or observable change existed, and did not invent a
comparison. Output: `frontend-change-report-current-worktree.html`.

> This first run is what originally shipped in the PR. It did not reach Step 5
> (reading `resources/report-template.html`) because it exited early on the
> empty-report path — that gap is why the missing `resources/` folder wasn't
> caught until review. Test 1 above re-runs the skill against a project with a
> real diff so Step 5 actually executes.

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
- Anything that surprised you: The first test run (1b) exited before Step 5
  ever executed, so a missing `resources/report-template.html` would not have
  been caught by that test alone — confirmed by re-running against a project
  with a real diff (Test 1), which does exercise Step 5 end-to-end.
- Fixed for this submission: `resources/report-template.html` is included in
  this PR, and the skill folder is named exactly `Frontend-Change-Visualizer`
  (no trailing space).
