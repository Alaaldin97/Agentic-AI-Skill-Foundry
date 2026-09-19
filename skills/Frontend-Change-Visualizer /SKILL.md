---
name: Frontend-Change-Visualizer
description: Turn a frontend code change (a diff, a commit, another agent's redesign) into a standalone visual before/after report — only the parts that actually changed, explained in plain language. Use when the user asks to "show what changed", "visualize the redesign", "before and after this update", or after any UI-affecting edit lands and someone wants to see the impact without reading code.
---

# Skill: Frontend Change Visualizer

Point this at a frontend project right after something changed it — a redesign
pass, a refactor, another skill, a teammate's PR. It produces one static HTML
page: what changed, why it matters, and a before/after view of only the
affected pieces. It never re-renders or re-designs the app itself.

## When to use this

Fires on: "show me what changed", "before and after", "visualize this
redesign", "what did that update actually change", "diff report for the UI",
right after a frontend-editing skill/agent/commit finishes.

Does **not** fire on: making the UI change itself (that's `neej-frontend-craft`
or similar), reviewing code quality/security (`code-review`), or requests with
no prior "before" state to compare against — see Step 2's escape hatch.

## The rule that matters

Every "what changed" claim must trace to a real diff, a real previous file, or
a real screenshot — never an assumption about what a redesign "probably" did.
If no reliable before-state exists, say so in the report instead of inventing
a comparison. A believable but fabricated before/after is worse than no report.

## Steps

### 1 — Understand the project (read-only)

Without modifying anything, determine:

- Framework (React, Next.js, Vue, Angular, plain HTML/CSS, etc.) from
  `package.json`, config files, and file extensions.
- Component/page structure and routing.
- Styling system in use (CSS Modules, Tailwind, SCSS, styled-components,
  inline styles).
- Relevant assets (images, icons, fonts).
- Any existing screenshots, visual snapshots, or test fixtures already in the
  repo (e.g. `__snapshots__/`, `screenshots/`, Storybook/Chromatic output).

### 2 — Determine the before state

Look, in priority order, for:

1. `git diff` / `git show` against the previous commit (most reliable).
2. The pre-change version of touched files via `git log -p` or a stash.
3. Existing before-screenshots or visual snapshots checked into the repo.
4. A previous build/deploy artifact if one is available.

**Escape hatch:** if none of these exist (e.g. changes were made outside git,
or history was squashed), do not guess a "before". State plainly in the
report's Technical Details section that no reliable before-state was found,
and show the after-state only, labeled as such.

### 3 — Determine the after state and isolate real changes

Diff the before/after file contents directly (don't rely on commit messages).
For each hunk, decide:

- **Is it visually observable?** A CSS/markup/asset change a user could see
  or a behavior a user could trigger.
- **Is it code-only?** Renamed variables, added comments, internal refactors,
  reordered imports, type annotations — no observable effect.

Discard code-only changes from the visual report (list them once, briefly, in
Technical Details — don't build a card for each). Only carry forward changes
with an observable UI or behavioral effect.

### 4 — Translate each real change into plain language

Never present a raw diff line as the explanation. Map code deltas to what a
non-technical reviewer would notice. Examples:

| Code delta | Plain-language change |
|---|---|
| `padding: 8px 16px` → `10px 20px` | Button spacing increased — larger, easier to tap |
| `border-radius: 4px` → `10px` | Corners are noticeably more rounded |
| new `@media (max-width: 768px)` block | A mobile-specific layout was added |
| `aria-label` added to icon button | Screen readers can now announce this control |
| `transition: none` → `transition: all .2s` | Hover/focus now animates instead of snapping |

Classify every change into one or more categories, and assign one impact
level. Use these exact labels and emoji consistently in the report:

**Categories:** 🎨 Visual · 📐 Layout · 📱 Responsive · ✍️ Typography ·
🎯 Interaction · ♿ Accessibility · ⚡ Animation · 🧩 Component · 🧱 Structure ·
🔧 Functional · 📝 Content · 💻 Code-only

**Impact:**
- **High** — major UI or functional change (e.g. "checkout layout redesigned")
- **Medium** — noticeable component-level improvement (e.g. "product cards
  redesigned")
- **Low** — small visual adjustment (e.g. "border radius 8px → 10px")

### 5 — Build the report, scoped to what changed

Read `resources/report-template.html` — a self-contained, no-build-step HTML
template with a dark developer/design-review theme and three working
comparison widgets (side-by-side, drag slider, opacity overlay) built with
plain CSS/JS, no dependencies.

For each real change identified in Step 4:

1. Duplicate the block between `<!-- COMPONENT_CARD_START -->` and
   `<!-- COMPONENT_CARD_END -->`.
2. Fill the placeholders (`{{COMPONENT_NAME}}`, `{{PAGE_PATH}}`,
   `{{CATEGORY_BADGES}}`, `{{IMPACT_BADGE}}`, `{{BEFORE_CONTENT}}`,
   `{{AFTER_CONTENT}}`, `{{WHAT_CHANGED_LIST}}`).
3. `{{BEFORE_CONTENT}}` / `{{AFTER_CONTENT}}` are inline markup snippets or
   `<img>` tags pointing at real screenshots if available — never full-page
   dumps when only one component changed. Crop to the affected component or
   region only.
4. If a screenshot genuinely isn't obtainable (no browser tool, no existing
   snapshot), fall back to a rendered HTML/CSS mini-mockup of just that
   component using its real before/after markup and styles — still real code,
   not an invented visual.

Fill the header placeholders (`{{PROJECT_NAME}}`, `{{REPORT_DATE}}`,
`{{COMPONENT_COUNT}}`, `{{PAGE_COUNT}}`, `{{RESPONSIVE_COUNT}}`,
`{{CHANGE_SUMMARY}}`) with real counts from Step 4 — never round numbers up
or invent a summary sentence not supported by the actual diff.

List every discarded code-only change under the `{{TECHNICAL_DETAILS}}`
section so the report is auditable, and note explicitly if Step 2 found no
reliable before-state.

### 6 — Save and hand off

Save the filled-in file as `frontend-change-report-<slug>.html` (slug from the
project or change name) in the project root or a `reports/` folder if one
exists. Tell the user where it is and that they can open it directly in a
browser — no server or build step required.

## Guardrails

- Never modify the frontend project's own source files — this skill only
  reads and produces a separate report file.
- Never show the entire page when only one component changed. Crop to the
  affected region.
- Never invent a "before" when none exists — report the gap instead.
- Never classify a code-only change as Visual/Layout/etc. just to pad the
  report.
- If literally nothing observable changed, say so directly rather than
  manufacturing minor-sounding findings.
