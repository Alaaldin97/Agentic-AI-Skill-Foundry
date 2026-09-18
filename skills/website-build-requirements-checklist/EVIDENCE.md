# Evidence — `website-build-requirements-checklist`

**Tested on:** VS Code 1.137 · **Date:** 2026-09-18

---

## 1. It fired when it should

**What I typed:**

```text
I want to build a website with user accounts, Stripe payments, contact forms, and an admin dashboard. What requirements should I include?
```

**What happened:**

```text
Read skill `website-build-requirements-checklist`

Website/app type: database-driven website with user accounts, Stripe payments, contact forms, and a role-protected admin dashboard.

### Core website requirements
- [ ] Define the site’s purpose, primary user journeys, and content structure.
- [ ] Design responsive layouts that work well on mobile, tablet, and desktop.
- [ ] Provide clear navigation, search where content volume warrants it, and useful empty/error states.
- [ ] Establish page requirements: homepage, pricing/product pages, account pages, contact page, legal pages, and dashboard.
- [ ] Build SEO foundations: semantic HTML, descriptive metadata, sitemap, robots rules, canonical URLs, and social-sharing metadata.
- [ ] Set performance budgets for images, scripts, loading speed, and Core Web Vitals.
[...]

### User accounts and authentication
- [ ] Support registration, login, logout, and secure password storage using a proven password-hashing algorithm.
- [ ] Specify whether registration requires email verification before access or payment.
- [ ] Provide password reset and account-recovery flows that use short-lived, single-use tokens.
[...]

### Stripe payments
- [ ] Define the payment model: one-time payments, subscriptions, trials, upgrades/downgrades, taxes, and supported currencies.
- [ ] Use Stripe-hosted Checkout or Stripe Elements so raw card data never passes through your servers unnecessarily.
- [ ] Separate Stripe test and live environments, credentials, products, prices, and webhook endpoints.
[...]

### Contact forms
- [ ] Specify required fields, routing destination, service-level expectations, and who owns follow-up.
- [ ] Validate every field on both client and server, with accessible, actionable validation messages.
- [ ] Add spam prevention such as a honeypot, CAPTCHA/Turnstile where appropriate, and rate limiting.
[...]

### Admin dashboard
- [ ] Require separate, strong administrator authentication and enforce role-based access control on every server-side action.
- [ ] Define dashboard capabilities: user management, payment/subscription visibility, contact-message handling, content management, and reporting.
- [ ] Protect sensitive data by showing only the minimum information needed for each role.
[...]

### Data, backend, and operations
- [ ] Design a data model for users, roles, sessions, contact submissions, Stripe customer IDs, orders/subscriptions, entitlements, and audit events.
- [ ] Use database migrations, validation at API boundaries, and transactional updates for critical account/payment state.
- [ ] Define backup frequency, retention, encryption, and a tested restore procedure.
[...]

### Default security & best-practice baseline
- [ ] Use HTTPS everywhere.
- [ ] Handle secrets and environment variables securely; never expose Stripe secret keys or webhook secrets to browsers.
- [ ] Plan dependency updates and vulnerability awareness.
- [ ] Validate input server-side where relevant.
- [ ] Configure appropriate security headers.
- [ ] Apply least-privilege access and role permissions.
- [ ] Maintain backups and test restore capability.
- [ ] Provide logging and error monitoring.
- [ ] Separate development, staging, and production environments.
- [ ] Apply privacy and data-minimization basics, including a privacy notice and clear data-retention rules.
- [ ] Include accessibility basics.
- [ ] Use secure session and cookie settings where sessions exist.
- [ ] Protect against common web attacks, including CSRF, XSS, injection, insecure redirects, and broken access control.
```

**Did it activate on its own?** Yes — I described the website I wanted to build without naming the skill, and VS Code automatically loaded `website-build-requirements-checklist`.

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```text
My website is already built and almost ready to go live. What should I check before launch?
```

**Did it stay dormant?** Yes — `website-build-requirements-checklist` did not load. VS Code instead loaded:

```text
Read skill `website-launch-readiness-checklist`
```

**Why this one is a real test:** It is still a website-related request, but it asks about an already-built site's launch readiness rather than what requirements should be included while planning or building it.

---

## 3. What it cost

|                                             | Tokens (approx.) |
| ------------------------------------------- | ---------------: |
| Description in the menu (always loaded)     |             ~160 |
| Body, once it fired                         |           ~1,900 |
| What stayed on disk because it did not fire |           ~1,900 |

These are rough estimates based on the skill text. VS Code's token counter showed the full agent-session context rather than the skill alone, so I did not use the full-session totals as the skill-specific cost.

---

## 4. Anything a reviewer should know

* Known limitation: the checklist quality depends on the user describing enough about the website or web app. If the request is vague, the skill asks only the minimum clarifying questions needed to determine the relevant modules.
* Needs an API key / network: no
* Anything that surprised you: a very short prompt such as `I want to build a website help me` was enough for the skill to activate, ask relevant clarifying questions, and produce a tailored checklist.
