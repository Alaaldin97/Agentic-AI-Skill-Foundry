---
name: website-build-requirements-checklist
description: "Use when a user is planning or building a website or web app and asks what requirements, features, controls, or technical components to include. Typical requests ask what is needed to build a website, plan a web app, or include features such as accounts, payments, forms, or dashboards. Does NOT fire on: launch-readiness audits, specific coding bugs, page redesign, copywriting, SEO-only or security-only requests, or requests to build the whole site."
---

# Website Build Requirements Checklist

Produce a tailored planning/build-requirements checklist for a website or web app, scoped to its
type and the features the user describes, so the user knows what requirements, controls, and
supporting components to include while planning or building - before any code is written.

This is a **planning checklist**, not an audit. It never marks items PASS, FAIL, MISSING, or NOT
VERIFIED, because there is nothing built yet to verify.

## When to use this

Fires when the user naturally asks to:

- plan what requirements or features a website or web app should have before building it
- ask what they need to build a specific kind of website (dynamic, e-commerce, portal, etc.)
- ask what to include when their planned site has certain features (user accounts, payments,
  forms, admin dashboard, bookings, etc.)
- get a checklist of technical/feature requirements to scope a build

**Does NOT fire on:**

- “My website is already built and almost ready to go live. What should I check before launch?”
  — this is launch-readiness auditing of an existing site, not planning requirements for a new
  build.
- “Is my website ready to launch?” / “What am I missing before publishing my site?” — same
  reason: already-built, pre-launch review, not planning.
- “Can you fix the CSS on my navigation menu?” — an isolated front-end bug, not planning.
- “Help me redesign my homepage hero section.” — a page redesign request, not a requirements plan.
- “Write some homepage copy for my bakery website.” — a copywriting request.
- “Explain SEO for my website.” — general SEO-only advice, not a build-requirements checklist.
- “Do a security audit of this login page.” — a security-only audit of existing code.
- “Build me the whole website now.” — a direct implementation request; this skill defines
  requirements to plan against, it does not write the site's code.

## Steps

Follow this pipeline in order:

### 1. Determine website type and features

Identify (from what the user already said, or by asking) the website type/category, e.g.:

- informational / brochure website
- content-heavy or dynamic (database-driven) website
- website with contact or application forms
- website with user registration/login
- e-commerce or payment-enabled website
- booking/reservation website
- user portal/admin dashboard
- other

Also determine, **only when relevant**:

- whether it will have user accounts/login
- whether it will accept payments
- whether it will have forms or file uploads
- whether it will have an admin/dashboard area
- whether it will collect personal data
- whether it will have bookings or notifications
- who will maintain the site after launch
- any specific deployment/hosting requirements

Ask one brief clarifying question at a time only when the missing information would materially
change the checklist. Do not ask about features the user has already described, and do not ask
about features that are clearly irrelevant to what they're building.

### 2. Assemble the checklist from two layers

**A. Core requirements** — always include, tailored to what's relevant:
- responsive/mobile support
- navigation and information architecture
- SEO basics
- performance
- error handling
- maintainability

**B. Conditional modules** — include only the modules that match the features the user described:

| Feature detected | Module items |
|---|---|
| User accounts/login | registration, login/logout, secure password storage, password reset, email verification when appropriate, session management, authorization/access control, account deletion/deactivation, protection against brute force and abuse |
| Payments/e-commerce | trusted payment provider, test/live environments, webhook verification, payment success/failure handling, refunds/cancellations, receipts/invoices, correct pricing/currency, fraud/security controls, never storing raw payment-card data unnecessarily |
| Forms | client and server validation, spam protection, confirmation messages, email/notification delivery, error handling, privacy handling, safe file uploads when applicable |
| Contact form requirements  |
| Admin/dashboard | authentication, role-based permissions, audit/logging where appropriate, safe administrative actions, search/filtering where useful, session/security controls, protection of sensitive data |
| Booking | availability, timezone handling, confirmation/cancellation, reminders, conflict prevention, calendar integration if required |
| Dynamic/data-driven sites | database/data model, API/backend needs, validation, caching where appropriate, error handling, backups, migrations | establish a process for handling contact requests and deletion or correction requests, test the form across browsers, mobile devices, and common email providers

Do not include a conditional module for a feature the user did not describe.

### 3. Output format

Output a practical checklist using clear headings and checkbox bullets — do not score or audit
any item. Use this shape:

```
Website/app type: <type/features summary>

### Core website requirements
- [ ] <requirement>
...

### <Conditional module name, e.g. User accounts / authentication>
- [ ] <requirement>
...

### Default security & best-practice baseline
- [ ] Use HTTPS everywhere
- [ ] Handle secrets and environment variables securely
- [ ] Plan dependency updates and vulnerability awareness
- [ ] Validate input server-side where relevant
- [ ] Configure appropriate security headers
- [ ] Apply least-privilege access and role permissions
- [ ] Maintain backups and test restore capability
- [ ] Provide logging and error monitoring
- [ ] Separate development, staging, and production environments
- [ ] Apply privacy and data-minimization basics
- [ ] Include accessibility basics
- [ ] Use secure session and cookie settings where sessions exist
```

Group items by section: Core first, then each applicable conditional module, in the order the
user described the features (or a logical build order if unspecified), and always include
`### Default security & best-practice baseline` as the final section.

Keep explanations short — add a brief clarifying note only when a requirement's meaning might be
unclear, not for every item.

## Rules

- Never mark items PASS, FAIL, MISSING, NOT VERIFIED, or NOT APPLICABLE — this is a planning
  checklist for something not yet built, not an audit of existing work.
- Tailor the checklist to the features the user actually described; do not dump every possible
  website requirement or include modules for features they didn't mention.
- Only ask clarifying questions that would materially change which modules or items appear; skip
  questions whose answers are already given.
- Do not claim legal, privacy, accessibility, security, or compliance certification — frame items
  as things to plan/build for, not guarantees.
- Do not offer to build or write the actual site code as part of this skill's output; it defines
  requirements, it does not implement them.
- If the user is asking about an already-built site's launch readiness, do not use this skill;
  answer outside this skill or let a launch-readiness skill handle it if available.

## Resources

This skill has no external reference resources. The core checklist and conditional modules are
fully defined in this file.

## Scripts

This skill has no scripts. Producing a tailored checklist from user-provided context requires
judgment (determining relevance and framing requirements clearly), not deterministic execution,
so no script is included.