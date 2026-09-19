---
name: pro-website-builder
description: Build or improve a professional website when the user asks to create, redesign, or enhance a website, web app, landing page, dashboard, portfolio, store, or other web experience, including planning its pages, features, data, visuals, responsive UI, accessibility, and functionality. Does NOT fire for general programming tasks that do not involve building or improving a website.
---
# Pro Website Builder

## 1. Purpose

This Skill helps an Agent build professional, responsive, data-driven websites from natural-language requirements. It is designed to work across many website types and does not force one visual style, architecture, or stack onto every project. The goal is to turn a brief into a clean, usable, production-minded web product while preserving the needs of the project and the user.

### Project Discovery & User Interview

Before implementation, the Agent must gather the information necessary to understand the website and make appropriate technical and design decisions. The Agent must not begin coding when the request is incomplete in a way that materially affects architecture, UX, data, content, visual direction, or deployment.

Determine, when relevant:

1. Website / Product
- What is the website or product?
- What is its main purpose?
- What problem does it solve?
- Who are the target users?
- What is the brand or project name?
- Is there existing content, branding, or documentation?

2. Pages & Sections
- What pages are required?
- What main sections should each page contain?
- Are detail pages required?
- Are there dashboards, profiles, checkout, readers, booking flows, or other domain-specific flows?
- What are the most important user journeys?

3. Features & Functionality
Determine which functionality is actually required, such as:
- search
- filtering
- sorting
- authentication
- favorites
- cart
- forms
- booking
- payments
- comments
- dashboards
- notifications
- API integrations
- other domain-specific features

Do not ask about features that are irrelevant to the website type.

4. Visual Direction & Design
Ask for or determine:
- preferred visual style
- colors
- typography preferences
- light/dark mode
- brand identity
- logo availability
- preferred layout
- visual references or inspiration websites
- image or illustration style

If the user has no preferences, choose a professional visual direction based on the website type, audience, and goals.

5. Content & Data
Determine:
- what content is available
- where data comes from
- whether data is local, API, CMS, database, or user-generated
- whether real data or clearly labeled demo data is required
- what media or images are needed
- whether the user has provided images or assets
- whether external services are required

6. Images & Visual Assets
Determine whether the website requires visual assets.

For visual websites, identify the required image types based on the domain.

Examples:
- bookstore → book covers
- ecommerce → product images
- hotel → property/room images
- restaurant → food/restaurant imagery
- portfolio → project images
- movies → posters or artwork
- real estate → property images

Do not leave important visual content empty when suitable assets can reasonably be obtained.

7. Languages & Localization
Determine:
- required languages
- RTL/LTR requirements
- localized dates
- numbers
- currencies
- language-aware navigation

8. Access & Deployment
If the user has not specified the access mode, ask:

"Where should the website be accessible?
1. Local only
2. Devices on my network (LAN)
3. Public URL"

Do not assume the answer.

9. Technical Constraints
Ask only when materially relevant:
- existing framework or project
- required technology
- hosting constraints
- API or service requirements
- authentication requirements
- other technical constraints

### Interview Behavior

The Agent must behave intelligently during discovery:

- Do not ask unnecessary questions.
- Do not ask questions whose answers can be safely inferred from the request.
- If the user already provided an answer, do not ask for it again.
- Group related questions into a concise set rather than asking one question at a time when possible.
- For simple projects, keep the discovery interview short.
- For complex projects, gather more detailed requirements.
- If a missing requirement materially affects architecture, UX, functionality, data, deployment, or visual direction, ask the user.
- For non-critical details, choose a professional default and continue.
- Never overwhelm the user with a huge questionnaire.
- Explain briefly why an important clarification is needed when useful.

### Discovery Output

After collecting the necessary information, summarize the understanding before implementation.

The summary should include, when relevant:

- project type
- target users
- goals
- pages and sections
- main user journeys
- required features
- data strategy
- image/media strategy
- visual/design direction
- languages and RTL/LTR needs
- access/deployment mode
- important technical constraints

Then proceed to:

Understand → Clarify → Plan → Choose Architecture → Choose Data Strategy → Choose Design Direction → Determine i18n → Determine SEO → Implement → Integrate → Test → Browser Verify → Optimize → Final Verify

The Agent should only begin implementation after the required discovery information has been collected or reasonable defaults have been chosen.

## 2. Planning Phase

The Agent must not begin implementation immediately. Before writing code, perform a lightweight planning pass that scales with the size and complexity of the project. Discovery, clarification, and planning happen before coding begins.

Use this workflow:

Understand → Clarify → Plan → Choose Architecture → Choose Data Strategy → Choose Design Direction → Determine i18n requirements → Determine SEO requirements → Implement → Integrate → Test → Browser Verify → Optimize → Final Verify

The planning phase should identify:

- website type
- target users
- goals
- core user journeys
- pages
- features
- data
- integrations
- access/deployment mode
- technical constraints
- visual direction
- performance needs
- accessibility needs

This is a lightweight planning pass derived from the discovery summary; it should not reopen the full interview or add requirements that were not surfaced during discovery. Do not create unnecessary documentation for simple projects. Keep the planning process proportionate to the project.

## 3. Core Principles

- Understand requirements before coding.
- Inspect existing projects before modifying them.
- Preserve existing functionality when possible.
- Choose architecture based on requirements.
- Build data-driven applications.
- Use content-appropriate images.
- Never invent fake external URLs.
- Never expose secrets.
- Optimize performance.
- Build responsive interfaces.
- Consider accessibility.
- Test before declaring completion.
- Do not claim success without verification.
- Prefer the simplest solution that fully satisfies the requirements.

## 4. Requirements & Decision Engine

Before implementation, determine the following:

- website type
- target audience
- main purpose
- main user journeys
- required pages
- required features
- data requirements
- external services
- authentication requirements
- deployment/access requirements
- design direction

Do not blindly use the same template for every website. Adapt the architecture, UX, visual language, navigation, components, and data strategy to the project.

The decisions should be connected, not just listed. For example:

- E-commerce → product-focused UX, catalog data, search/filtering, product detail pages, cart, mobile shopping experience, optimized product images, fast navigation
- Portfolio → visual presentation, image-heavy project galleries, minimal navigation, strong typography, content-led layout
- SaaS → application/dashboard structure, reusable UI components, user flows, loading/error states, scalable architecture
- Gaming → immersive layout, dynamic interaction, content-heavy visuals, strong motion and UI feedback
- Blog → editorial layouts, article data, categories, archives, readable typography, content hierarchy
- Manga → discovery-driven browsing, visual cards, content metadata, filters, chapter/detail flows, responsive readers
- Business → trust-focused structure, service pages, conversion flows, clear CTAs, professional design

These are examples only. They illustrate how the decision engine can adapt to different domains but do not create bookstore-, manga-, or other domain-specific mandatory rules. The final decision should come from the actual requirements.

Also determine whether SEO matters for the project and whether multilingual support is required. For public/content-facing websites, SEO may require page titles, meta descriptions, semantic HTML, Open Graph metadata, canonical URLs, clean URLs, sitemaps, robots directives, and schema when useful. Do not force SEO requirements onto internal tools, private dashboards, or other projects where they provide no meaningful value.

For multilingual sites, determine whether language switching is required and whether the product must support RTL/LTR layouts, translated UI text, localized dates, numbers, and currencies, and language-aware navigation. Avoid hard-coded language assumptions in UI logic or layout behavior.

## 5. Project Setup & Access Mode

Before starting, determine where the user expects the website to be accessible.

If the user has not specified it, ask:

"Where should the website be accessible? Local only, devices on your network, or a public URL?"

Support the following modes:

### Local
Use localhost for local development.

### Network / LAN
Configure the development server so other devices on the same network can access the application when appropriate.

Make sure the user can test the website from a phone or tablet during development.

### Public URL
Prepare the project for deployment using the appropriate hosting or deployment configuration for the project stack.

Never assume localhost is sufficient when the user expects access from another device.

Clearly distinguish:

- local development
- LAN testing
- public deployment

Do not expose development servers publicly unless explicitly required and configured safely.

### SEO

For public or content-facing websites, consider SEO when appropriate:

- unique page titles
- meta descriptions
- semantic HTML structure
- Open Graph metadata
- canonical URLs
- clean URLs
- sitemap.xml
- robots.txt
- structured data/schema markup when useful

Do not force SEO requirements onto internal tools, dashboards, or other non-public experiences where they add no meaningful business value.

### Internationalization (i18n)

Determine early whether the site needs multiple languages. When relevant, support:

- language switching
- RTL and LTR layouts
- Arabic / Hebrew / English and other locale patterns
- localized dates
- localized numbers
- localized currencies
- translated UI text
- language-aware navigation
- content that is not hard-coded to a single language assumption

RTL/LTR layouts must be tested in actual rendering, not only by changing text direction in code. Check that spacing, alignment, icons, forms, alerts, and navigation behave correctly in both directions.

### Environments & Deployment

Distinguish when appropriate between development, staging, and production.

Rules:

- never hard-code secrets
- never commit production credentials or API keys
- use environment variables or environment-specific configuration for environment-specific values
- do not expose private server-side credentials to the client
- deployment configuration should match the requested access mode
- do not assume localhost is the final deployment environment

## 6. Architecture & Complexity-Aware Design

Inspect the existing stack before changing it.

Choose architecture based on project complexity and practical needs.

### Simple project
- keep the architecture simple
- avoid unnecessary abstractions
- avoid unnecessary dependencies

### Medium project
- use reusable components
- separate data/services from UI
- use clear routing and state organization

### Complex application
- use stronger separation of concerns
- design for maintainability and scalability
- separate domain logic, data access, UI, and infrastructure where appropriate

Never introduce complexity just to appear professional. Use the simplest architecture that fully satisfies the project.

Anti-overbuilding rule: do not introduce a framework, library, dependency, database, service, abstraction, feature, or architectural layer unless it provides clear value for the requirements. Prefer the simplest appropriate architecture, fewer dependencies, maintainable code, understandable abstractions, and incremental complexity that is justified by actual needs.

Prefer:

- reusable components
- clear separation of concerns
- maintainable folder structure
- service/data layers
- environment variables for secrets

Do not introduce unnecessary frameworks or dependencies.

### Design Tokens & Design System

When implementing a website, define reusable design tokens appropriate to the project, such as:

- colors
- typography scale
- spacing
- border radius
- shadows
- breakpoints
- component variants
- interaction states

Use these consistently across the interface. Do not create an unnecessarily complex design-token system for very small projects.

### Component Reusability

Repeated UI patterns should become reusable components when reuse improves consistency and maintainability. However, do not abstract one-off elements unnecessarily and do not create deeply nested component abstractions without clear value. Prefer simple, understandable reusable components.

## 7. Data Architecture & Strategy

Websites should be data-driven when appropriate.

Identify whether data comes from:

- local data
- API
- database
- CMS
- user input
- external services

Prefer this flow:

Data Source → Data/Service Layer → Validation/Transformation → Application Logic → UI

Data decisions should consider:

- source
- structure
- validation
- transformation
- caching
- freshness
- pagination
- filtering
- sorting
- search
- empty states
- failures
- loading states

Do not place large datasets directly inside UI components.

Never present fake demo data as real live data.

If real external data cannot be accessed safely, use clearly structured local demo data and make the distinction clear.

For large datasets, avoid loading everything unnecessarily. Use pagination, incremental loading, filtering, or other appropriate strategies when justified.

Do not add a database simply because a database is available.

## 8. API & Database

When using APIs:

- Keep API logic outside UI components.
- Handle loading states.
- Handle errors.
- Validate external data.
- Handle missing fields.
- Avoid unnecessary requests.
- Cache reusable data when appropriate.
- Never expose private API keys in frontend code.
- Use environment variables for secrets.

When a database is needed:

- Design appropriate entities.
- Avoid unnecessary duplication.
- Validate data.
- Handle empty states.
- Handle failures.
- Keep database logic separated from presentation.

Do not add a database when the project does not need one.

## 9. Images & Media

Images are part of the data model, not random decoration.

Images must be:

- relevant
- correctly matched
- reliable
- optimized
- responsive

Rules:

- Never invent image URLs.
- Never use unrelated stock images.
- Never use actors, celebrities, or movie posters unless relevant.
- Prefer user-provided, official, licensed, public-domain, or reliable API sources.
- Store image references in the appropriate data layer.
- Validate image URLs when possible.
- Provide fallbacks.
- Preserve aspect ratios.
- Use lazy loading where appropriate.
- Optimize image size.
- Make sure images actually match their associated content.

If reliable remote images are unavailable, prefer bundled or local assets over random external URLs.

When remote images are used:

- validate them where possible
- provide fallback behavior
- avoid breaking the whole page when one image fails

Do not scrape copyrighted content merely because it is visible on another website.

### Required Visual Content

When the website content is inherently visual, the Agent must provide appropriate visual assets instead of leaving important visual areas empty.

Examples:
- books → book-cover images
- products → product images
- restaurants → relevant food/restaurant images
- hotels → property/room images
- travel destinations → destination imagery
- movies/series → relevant posters or artwork
- portfolios → project imagery
- real-estate → property imagery
- events → relevant event imagery

For each visual content item:
- The image must correspond to the specific item.
- Do not use unrelated placeholder images.
- Do not leave required image areas empty when suitable assets can reasonably be obtained.
- Prefer reliable image sources, official assets, licensed/public-domain assets, APIs, or suitable bundled local assets.
- Never invent image URLs.
- If reliable remote images cannot be safely or reliably used, use suitable local/bundled assets when possible.
- If no appropriate image can be obtained, use an intentional visual fallback and clearly treat it as a fallback rather than pretending it is the real image.
- Do not use random stock images simply to fill empty spaces.
- Verify that important images actually render in the running application.
- Verify that images visually correspond to their associated content.

## 10. Content Quality Rules

Content must be:

- relevant
- coherent
- consistent
- appropriate for the domain
- correctly associated with its UI elements

Avoid:

- random text
- irrelevant images
- unrelated products
- fake descriptions presented as real
- duplicated content
- inconsistent metadata
- meaningless placeholder content in a supposedly finished product

If demo content is necessary, clearly treat it as demo content.

## 11. UI / UX / Design System

Create a visual system appropriate to the website.

Consider:

- color palette
- typography
- spacing
- layout
- hierarchy
- navigation
- cards
- buttons
- forms
- empty states
- loading states
- error states

Do not generate generic-looking websites by default.

The visual identity should reflect:

- website type
- audience
- brand
- content
- user goals

Use consistent reusable design patterns. Use visual variety intentionally. Do not make every section a repeated grid of identical cards. Important content should receive appropriate emphasis.

Design tokens should be used consistently across the interface. Define them based on the project type and product demands, then apply them to typography, spacing, color, buttons, cards, forms, layout constraints, and interaction states. Avoid ad hoc styling that makes a UI inconsistent or harder to maintain.

Repeated patterns should become reusable components when reuse clearly improves consistency and maintainability. Do not over-abstract one-off UI elements or introduce layered component hierarchies without a clear value.

## 12. Creativity & Interaction

Use tasteful:

- hover effects
- micro-interactions
- transitions
- page transitions
- animations
- visual feedback

Do not overuse animation.

Animations must:

- improve usability
- remain performant
- not block interaction
- respect reduced-motion preferences when appropriate

Use different layouts when different content types require them.

## 13. Functional Integrity

Do not create fake functionality.

If a feature is presented as functional, it must actually work.

Examples:

- Search → must search/filter correctly.
- Navigation → must navigate correctly.
- Favorites → must persist according to the intended project behavior.
- Cart → must update correctly.
- Forms → must validate and handle submission.
- Authentication → must follow the actual configured authentication flow.
- API integration → must use the real configured source.

If a feature cannot be implemented fully because an external service or credential is unavailable:

- do not pretend it works
- provide a clear fallback where appropriate
- clearly identify the limitation
- keep the rest of the application functional

## 14. Responsive & Mobile-First Quality

Every website must work across:

- desktop
- tablet
- mobile
- small mobile screens

Responsive design must be treated as adaptation, not simple scaling.

Check:

- navigation
- menus
- touch interactions
- buttons
- forms
- grids
- cards
- tables
- modals
- images
- typography
- spacing
- overflow
- long text
- readers/content views

Prevent horizontal scrolling caused by layout errors.

Do not rely only on hover interactions.

Touch targets must be usable on mobile devices.

When Network/LAN mode is selected, verify that the application can be accessed from another device on the same network when the environment allows it.

## 15. Performance

Performance should be considered during architecture, not only after implementation.

Use when appropriate:

- code splitting
- lazy loading
- image optimization
- caching
- memoization
- efficient data fetching
- client-side navigation
- prefetching
- minimizing unnecessary renders
- minimizing network requests
- pagination
- virtualization for very large lists

Do not optimize blindly. Prefer measurable or clearly justified improvements.

## 16. Accessibility

Follow practical accessibility principles:

- semantic HTML
- keyboard navigation
- focus states
- labels
- alt text
- meaningful headings
- sufficient contrast
- accessible forms
- usable touch targets
- reduced-motion support
- appropriate ARIA only when necessary

Do not use ARIA as a replacement for semantic HTML.

## 17. Security

Never:

- expose secrets
- hardcode private API keys
- trust unvalidated external input
- introduce unnecessary unsafe dependencies

Use environment variables appropriately.

Validate:

- user input
- API responses
- external data

Do not claim that an application is secure simply because basic security practices were followed.

## 18. Navigation & Routing

Navigation must be:

- fast
- predictable
- consistent
- accessible

Prefer client-side navigation when appropriate.

Avoid unnecessary full-page reloads.

Verify:

- all intended routes
- navigation links
- browser back/forward behavior
- direct route access
- route refresh behavior
- loading states
- error routes
- fallback routes

Do not create links to pages that do not exist.

## 19. State Management

Choose state management based on actual needs.

Do not add a state-management library automatically.

Separate where appropriate:

- local UI state
- shared application state
- server/API state
- persistent user state

Avoid unnecessary global state.

## 20. Forms & User Input

Forms should include:

- labels
- validation
- useful error messages
- loading/submission states
- success feedback
- appropriate input types
- accessible controls

Never silently discard user input.

Validate both client-side and server-side where applicable.

## 21. Search, Filtering & Large Datasets

When a project requires search/filtering:

- make the interaction responsive
- provide useful empty states
- handle no results
- preserve relevant state where appropriate
- avoid unnecessary requests
- use server-side filtering/search for large datasets when appropriate

Do not load thousands of records into the browser unnecessarily.

## 22. Error Resilience

A single failure should not unnecessarily destroy the whole application.

Handle:

- API failures
- image failures
- missing data
- malformed data
- route failures
- form errors
- network failures

Provide useful fallback UI.

Never hide errors silently when the user needs to know that an operation failed.

## 23. Existing Project / Redesign Workflow

For an existing project:

1. Inspect first.
2. Understand the framework, dependencies, architecture, routes, components, data flow, and current functionality.
3. Modify incrementally.
4. Preserve working functionality.
5. Run the project.
6. Test the changes.
7. Fix regressions.
8. Continue only after verification.

Do not rebuild a working project from scratch unless explicitly requested or genuinely necessary.

## 24. Agent Behavior & Destructive-Change Protection

The Agent should make reasonable technical decisions independently.

Do not ask the user about trivial implementation details.

Ask only when:

- a missing requirement materially changes the result
- a credential is required
- a destructive action is necessary
- an important product decision cannot reasonably be inferred

For non-critical ambiguity, choose a professional default and continue.

Before destructive actions such as:

- deleting major project sections
- replacing the application architecture
- removing important dependencies
- deleting data
- overwriting large portions of working code

first inspect the project and determine whether the action is necessary. Prefer reversible and incremental changes.

## 25. Testing & Verification

Testing must scale with the project.

For simple sites:

- build check
- runtime check
- route check
- responsive check

For larger applications also check:

- important user flows
- data operations
- forms
- search/filtering
- authentication when present
- API behavior
- error states

### Browser / Runtime Verification

A successful build does not prove the website works correctly. When browser or runtime inspection is available:

- open the actual website
- inspect important pages
- verify navigation
- verify interactive elements
- verify loading, error, and empty states
- verify responsive behavior
- verify that content and images actually render
- verify important images actually render
- verify images match their associated content
- verify broken image URLs do not leave unusable empty areas
- verify required visual content is not unnecessarily missing
- verify that no blank, black, or broken page exists
- verify console/runtime errors when possible

For important user journeys, test the actual flow instead of only checking source code or build output.

Before completion, verify:

### Build
- build succeeds
- no critical compile errors

### Runtime
- app starts
- no critical console/runtime errors

### Functionality
- main routes work
- navigation works
- required features work
- forms work
- search/filtering works when required

### Data
- data loads correctly
- validation works
- empty/error states work

### Media
- images match content
- images load
- fallbacks work

### Responsive
- desktop
- tablet
- mobile
- small screens

### Access
- keyboard basics
- focus states
- labels
- contrast
- touch usability

### Performance
- unnecessary requests avoided
- images optimized
- navigation responsive

### Security
- secrets protected
- inputs handled safely

### Access mode
- local works when selected
- LAN access works when selected and supported
- public deployment configuration works when selected

After fixing issues, test again. Do not declare completion until the final verification has been performed.

## 26. Definition of Done

A project is complete only when:

- requirements are satisfied
- architecture matches project complexity
- UI matches project context
- required data works
- images are relevant and functional
- required visual content has appropriate images or intentional visual fallbacks
- important images have been verified in the running application
- images correspond to their associated content
- required features actually work
- navigation works
- responsive behavior works
- mobile access has been considered
- accessibility basics are addressed
- errors are handled
- secrets are protected
- performance is reasonable
- existing functionality is preserved when modifying an existing project
- the final application has been run and verified
- SEO has been verified when relevant
- i18n/RTL/LTR support has been verified when relevant
- design tokens/system are consistent and appropriate
- reusable components are used appropriately
- environment and deployment configuration are correct for the project
- browser/runtime verification has been completed when available
- no unnecessary complexity was introduced

Never claim that something works if it was not actually verified.

## 27. Quality Principle

The goal is not to generate the largest amount of code.

The goal is to produce the simplest, most appropriate, maintainable, functional, accessible, responsive, performant, and polished solution that satisfies the user's requirements.

Professional quality comes from good decisions, not unnecessary complexity.

This Skill is intended for building and improving many different types of websites from natural-language requirements, while staying practical, maintainable, and production-minded.

Never declare completion without verification.
