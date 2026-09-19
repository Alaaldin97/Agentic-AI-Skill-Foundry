# Evidence

## Positive test — Website building request

**User request:** Build a professional fashion website.

**Observed behavior:** The agent activated the website-building workflow and first asked discovery questions about the website purpose, target users, pages/sections, features, visual direction, content/data, images, languages, and access mode before implementation.

**Result:** Pass. The Skill fired for a genuine website-building request and gathered project requirements before building.

## Positive test — Bookstore website

**User request:** Build a professional bookstore website.

**Observed behavior:** The agent built the website and performed implementation verification. The project build completed successfully and linting reported no errors. During verification, image requirements were identified as an area that needed stronger handling, which led to improving the Skill's visual-content requirements.

**Result:** Pass. The Skill supported implementation, testing, and iterative improvement of the website-building workflow.

## Near-miss test — Python debugging

**User request:** Help me debug a Python function that calculates the average of a list of numbers. Do not build or modify any website.

**Observed behavior:** The agent treated the request as a normal Python debugging task. It inspected the likely function issues, suggested a corrected Python implementation, and did not start the website-building workflow.

**Result:** Pass. The Skill stayed quiet for an unrelated programming task.
