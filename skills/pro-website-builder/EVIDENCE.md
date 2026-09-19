# Evidence — `pro-website-builder`

**Author's runs:** VS Code + GitHub Copilot · 2026-09-19
**Reviewer verification:** Alaaldin Ahmed · 2026-09-19 · Module 5B `skill-runner`,
`openai/gpt-4.1-mini` via OpenRouter, 4 skills on disk

> The transcripts in sections 1 and 2 are from the reviewer's verification runs,
> not the author's original session. They were captured because the first
> submission described the behaviour in prose rather than pasting it. The
> author's own observations are kept in section 5 and match what the runs show.

---

## 1. It fired when it should

**What I typed:**

```text
Build a professional bookstore website.
```

**What happened:**

```text
====================================================================
REQUEST  Build a professional bookstore website.
SKILLS   4 on disk: find-skills, pro-website-builder, skill-reviewer, student-code-reviewer
ROUTED   pro-website-builder
====================================================================

--------------------------------------------------------------------
ANSWER

To build a professional bookstore website that meets your needs, I need to gather
some important details to ensure the website is designed and developed appropriately.

1. Target Users & Purpose:
- Who are the main users? (e.g., casual readers, collectors, students)
- What is the main purpose? (e.g., selling books online, showcasing a catalog, book reviews)

2. Pages & Sections:
- What pages do you want? (e.g., Home, Catalog, Book Details, About, Contact)
- Should there be user accounts or profiles?
- Do you want a shopping cart and checkout flow?

3. Features & Functionality:
- Should users be able to search, filter, and sort books?
- Do you want book reviews or ratings?
- Is authentication required for purchases or profiles?
- Payment integration needed?

4. Content & Data:
- Do you have an existing book catalog or data source?
- Should the site use real book data or demo data?
- Will you provide book cover images or should I use public domain or licensed images?

5. Visual Direction:
- Any preferred colors, styles, or branding?
- Should the design be modern, classic, minimalist, or something else?

6. Access & Deployment:
- Where should the website be accessible? Local only, network devices, or public URL?

Please provide as much detail as you can for these points, or let me know if you
want me to choose professional defaults for any of them.
```

**Did it activate on its own?** Yes — the prompt never names the skill, and three
other skills were on disk for the router to choose from.

The answer is the behaviour the skill specifies: it ran the Project Discovery &
User Interview before writing any code, and the six areas it asked about map to
the numbered discovery list in `SKILL.md` §1. It did not start generating a site
from an incomplete brief.

---

## 2. It stayed quiet when it should

### Near-miss A — unrelated programming task

```text
Help me debug a Python function that calculates the average of a list of numbers.
Do not build or modify any website.
```

```text
REQUEST  Help me debug a Python function that calculates the average of a list of numbers. Do not build or modify any website.
SKILLS   4 on disk: find-skills, pro-website-builder, skill-reviewer, student-code-reviewer
ROUTED   NO_SKILL — answering directly
```

**Did it stay dormant?** Yes.

### Near-miss B — web topic, but learning not building

```text
Explain how CSS flexbox works. I am studying for an exam, do not build anything.
```

```text
ROUTED   NO_SKILL — answering directly
```

**Why this one is a real test:** it is squarely a web front-end topic, so a
description keyed on "website" or "CSS" would have fired. The skill's scope is
*building or improving* a site, and the router respected that.

### Near-miss C — existing site, pre-launch review

```text
My website is already built and almost ready to go live. What should I check before launch?
```

```text
ROUTED   NO_SKILL — answering directly
```

**Why this one is a real test:** this is the trigger phrase another Foundry skill
(`website-build-requirements-checklist`) uses as *its* near-miss. It is about
auditing a finished site rather than building one, and `pro-website-builder`
correctly left it alone.

---

## 3. What it cost

Measured by the Module 5B runner on the dormancy run:

```text
PROGRESSIVE DISCLOSURE — what it actually cost
  skills on disk .............. 4
  menu shown to the router .... ~255 tokens
  if we had loaded ALL of them. ~9,726 tokens
  we actually loaded .......... ~0 tokens (nothing)
  SAVED ....................... ~9,726 tokens
```

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~80 (of the ~255-token 4-skill menu) |
| Body, once it fired | ~7,141 |
| What stayed on disk because it did not fire | ~7,141 |

This skill has by far the largest body in the catalog, which makes the dormancy
result the important number: on all three near-misses none of those ~7,141
tokens were loaded.

---

## 4. Anything a reviewer should know

- Known limitation: the body is ~7,141 tokens. That cost is only paid on a match,
  but it is large enough that a trimming pass would be worthwhile — several
  sections read as general web best practice rather than as instructions that
  change what the agent does.
- Needs an API key / network: no (the skill itself; the verification runs used
  OpenRouter because that is how the Module 5B runner works).
- The `## When to use this` and `## Steps` headings were added during review so
  the file matches the Foundry's expected shape. The numbered sections they point
  to are the author's own.

---

## 5. The author's original observations

Kept from the first submission, as a record of what was tried before the
verification runs above:

> **Positive test — Website building request.** User request: Build a professional
> fashion website. Observed behavior: The agent activated the website-building
> workflow and first asked discovery questions about the website purpose, target
> users, pages/sections, features, visual direction, content/data, images,
> languages, and access mode before implementation. Result: Pass.

> **Positive test — Bookstore website.** User request: Build a professional
> bookstore website. Observed behavior: The agent built the website and performed
> implementation verification. The project build completed successfully and
> linting reported no errors. During verification, image requirements were
> identified as an area that needed stronger handling, which led to improving the
> Skill's visual-content requirements. Result: Pass.

> **Near-miss test — Python debugging.** User request: Help me debug a Python
> function that calculates the average of a list of numbers. Do not build or
> modify any website. Observed behavior: The agent treated the request as a normal
> Python debugging task... and did not start the website-building workflow.
> Result: Pass.

The verification runs reproduce the first and third of these. The second — an
end-to-end build with a passing lint — was not re-run during review, because it
needs a real project workspace rather than the routing harness.
