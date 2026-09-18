# Evidence — adaptive-calendar-planner

**Tested on:** VS Code Copilot Agent · **Date:** 2026-09-18

---

## 1. It fired when it should

**What I typed:**

```text
Tomorrow I have university from 9 AM to 12 PM. I need 2 hours to study and 1 hour for the gym. Add a realistic plan to my calendar around my existing events.
```

**What happened:**

```text
Read skill `adaptive-calendar-planner`

google-calendar-get-current-time
google-calendar-list-calendars
google-calendar-list-events

Added the following plan to my primary calendar for Saturday, September 19:

- 9:00 AM–12:00 PM: University
- 1:00–3:00 PM: Study session
- 4:00–5:00 PM: Gym

The events were visible in my real Google Calendar.
```

**Did it activate on its own?** yes

I did not mention the skill name in the prompt.

### Re-planning test

**What I typed:**

```text
Something came up tomorrow from 2 PM to 3 PM. Add it as a fixed appointment and reorganize the rest of my day without moving my university time.
```

**What happened:**

```text
Read skill `adaptive-calendar-planner`

google-calendar-get-current-time
google-calendar-list-events
google-calendar-create-event
google-calendar-update-event
google-calendar-update-event
google-calendar-list-events

Added the new fixed appointment and reorganized tomorrow’s plan without moving university:

- 9:00 AM–12:00 PM: University — unchanged
- 2:00–3:00 PM: Appointment — fixed
- 3:00–5:00 PM: Study session — moved
- 5:30–6:30 PM: Gym — moved
```

I checked Google Calendar and confirmed that the fixed university event stayed in place, the new appointment was added, and the flexible study and gym events were moved without overlap.

### Date-range project planning test

**What I typed:**

```text
I need 4 hours to work on my Adaptive Calendar Planner project across today and tomorrow. Read my existing calendar and split the work into realistic blocks across both days without moving my fixed commitments.
```

**What happened:**

```text
Read skill `adaptive-calendar-planner`

google-calendar-get-current-time
google-calendar-list-events
google-calendar-create-events
google-calendar-list-events

I read your calendar and scheduled 4 hours of Adaptive Calendar Planner project work across today and tomorrow:

- Today, Friday: 10:45–11:45 PM — 1 hour
- Tomorrow, Saturday: 10:00 AM–12:00 PM — 2 hours
- Tomorrow, Saturday: 3:00–4:00 PM — 1 hour

The blocks are separated for realistic breaks, and existing fixed commitments were left unchanged.
```

**Did it work?** yes

The skill read the calendar first, split the project work across two dates, created the calendar blocks, and checked the calendar again afterward.

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```text
What are some good tips for managing my time when I have a busy day?
```

**Did it stay dormant?** yes

The response only gave general time-management advice.

It did not load `adaptive-calendar-planner` and it did not use any `google-calendar-*` tools.

**Why this one is a real test:** It is about time management and planning, but it does not ask to read, create, move, or re-plan calendar events.

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | Not exposed by the VS Code client |
| Body, once it fired | Not exposed by the VS Code client |
| What stayed on disk because it did not fire | Not exposed by the VS Code client |

VS Code Copilot did not show a per-skill token count during this test, so I did not invent token numbers.

---

## 4. Anything a reviewer should know

- Known limitation: Real calendar changes require a working authenticated Google Calendar MCP connection.
- Needs an API key / network: yes — network access and Google Calendar OAuth are required; no API key is used.
- Anything that surprised me: The skill activated automatically from a normal planning request without naming the skill, stayed dormant for a closely related general time-management question, and successfully split project work across two calendar dates.
