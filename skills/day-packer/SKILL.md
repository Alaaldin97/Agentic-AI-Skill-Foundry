---
name: day-packer
description: >
  Build a timetable from scratch, with no connected calendar, when the user dumps
  a list of tasks, errands, shifts or goals and asks to "fit everything in",
  "organize my day", or make a schedule / timetable / time blocks. Packs the dump
  into a timed plan that can cross midnight and writes .xlsx and .ics files.
  Does NOT fire on: adding or moving events in a connected calendar, a single
  reminder, date or time-zone questions, or sprint planning with no clock times.
---

# Day Packer

Build a timetable that fits as many of the user's tasks as realistically possible, starting from an unstructured brain-dump.

## When to use this

Fires when the user:

- lists several things they need to do and asks to plan the day or week ("i need to work 8 hours, then gym, then job search — fit it all in")
- asks for a schedule, timetable, time blocks, or daily plan
- asks "what should I do when" or "organize my day", even without saying "timetable"

**Does NOT fire on:**

- a single reminder or one calendar event ("remind me to call mom at 5") — nothing to pack
- questions about dates, time zones or opening hours — no plan is being built
- project or sprint planning with milestones but no clock times

## Core principles

1. **No default day boundaries.** Never assume a 9-to-5 day, a "normal" wake time, or that the day ends at midnight. The plan can begin at 04:00, run until 02:00, or span multiple days. Only the user's stated constraints limit the window.
2. **Pack tightly, but honestly.** The goal is maximum useful output. Leave no idle gaps unless the user asked for them. But never make a plan that is physically impossible (overlapping blocks, no travel time between two different places, a 3-hour task in a 1-hour slot).
3. **Don't fill gaps with guesses.** The user values accuracy over speed. When a missing detail would materially change the plan, ask. When a detail is minor, make an estimate and label it clearly as an estimate so the user can correct it.
4. **Nothing silently disappears.** If something doesn't fit, list it under "Didn't fit" with the reason, rather than dropping it.

## Steps

### Step 1 — Parse the brain-dump

Extract every item into a working list. For each item, capture what's known:
- Task name
- Duration (stated, or your estimate marked `est.`)
- Fixed time? (e.g. "meeting at 14:00", "class Tuesday 18:00")
- Deadline or priority, if mentioned
- Location / context (home, office, lab, car, phone-only, online)
- Energy type: deep focus / routine / physical / errand / social

Split vague items into concrete actions where obvious ("sort out car" → "call garage", "drive to garage").

### Step 2 — Ask ONE round of questions (always)

Always ask about sleep and breaks — the user wants to decide this fresh each time. Bundle it with any other genuinely blocking questions into a single message so there's only one round-trip. Keep it short. Use tappable options if the interface supports them.

Always ask:
- **Sleep & breaks for this plan:** protect a sleep block (which hours?), include short breaks, or pack everything with no protected blocks?
- **Start and end point:** when does this plan start, and is there a hard end (or should it run until everything is done)?

Ask only if it's unclear and would change the plan:
- Durations for big items you can't reasonably estimate
- Fixed times that were mentioned vaguely ("sometime in the morning")
- Travel time between locations
- Which items are must-do vs. nice-to-have, if clearly more than fits

Also show the parsed list back (compactly) so the user can catch misreadings. If the user says "just go" or answers only some questions, proceed and label your assumptions.

If the user chooses "no protected blocks" and the plan would run beyond roughly 18–20 hours awake, mention once, plainly, that the tail end will likely be lower-quality work and offer to move the heaviest-focus tasks earlier. Then respect their choice.

### Step 3 — Build the schedule

Place items in this order:
1. **Fixed-time items** first (meetings, classes, shifts, appointments).
2. **Protected blocks** the user chose (sleep, meals, breaks).
3. **Deadline and high-priority items** into the best remaining slots.
4. **Deep-focus tasks** into the longest uninterrupted gaps.
5. **Short tasks** (calls, emails, quick errands) batched together into small gaps and transition times.
6. **Remaining items** by priority until the window is full.

Packing techniques to maximize the day:
- **Batch by location:** group errands in the same area; group phone/online tasks.
- **Stack compatible tasks:** calls during a commute (if the user isn't driving or has hands-free), podcasts/lectures during physical chores. Only stack things that genuinely work together and mark them `(stacked)`.
- **Use transitions:** 5–15 minute gaps get quick tasks, not idle time.
- **Include travel time** as its own block whenever location changes. If unknown, estimate and mark `est.`.
- **Add a small buffer** (5–10 min) before fixed-time items that involve travel, since lateness there cascades.

### Step 4 — Deliver

Always give, in this order:

1. **Timetable table in chat**:

   | Start | End | Task | Where | Notes |
   |---|---|---|---|---|

   Use 24-hour times. If the plan crosses midnight or spans days, add the date or day name to each row or group rows under day headings.

2. **Summary line:** total scheduled time, number of tasks placed, and anything marked `est.`.

3. **Didn't fit** (if any): each item with the reason and a suggestion (another day, shorten, delegate).

4. **Files:** create the Excel and calendar files with the bundled script (see below) and give them to the user.

5. **Assumptions:** a short list of anything you estimated or assumed, so the user can correct it.

## Generating the files

Write the final schedule to a JSON file, then run the script:

```bash
python3 <skill-dir>/scripts/build_schedule.py schedule.json --out-dir /mnt/user-data/outputs
```

JSON format:

```json
{
  "title": "Plan for Thu 24 Sep",
  "blocks": [
    {"start": "2026-09-24T05:30", "end": "2026-09-24T06:00", "title": "Gym", "location": "Home", "category": "physical", "notes": ""},
    {"start": "2026-09-24T23:30", "end": "2026-09-25T00:45", "title": "Report draft", "location": "Home", "category": "deep", "notes": "est."}
  ],
  "did_not_fit": [
    {"title": "Clean car", "reason": "No slot left before end time"}
  ]
}
```

- Times are local, `YYYY-MM-DDTHH:MM`. Blocks may cross midnight — just use the next date for `end`.
- The script validates that no block ends before it starts and warns about overlaps. Fix any overlap it reports before delivering, unless the block is intentionally marked `(stacked)` in its title.
- It produces `<name>.xlsx` (schedule sheet + "Didn't fit" sheet) and `<name>.ics` (importable into Google Calendar, Outlook, Apple Calendar). The .ics uses floating local time, so events appear at the same clock time in whatever timezone the user's calendar is set to.

If the user only wants the chat table this time, skip the files.

## Resources

| File | What it holds | Loaded when |
|---|---|---|
| `resources/example-two-jobs.md` | Worked example: constraints that don't physically fit, hard end time | Step 3, when the request may be infeasible |
| `resources/example-evening-course-travel.md` | Worked example: fixed-time event in another city, late return past midnight | Step 3, when a far fixed-time item pins the day |

## Revising

When the user changes something ("move gym to evening", "the meeting got cancelled"), re-run the placement logic on the affected part of the day rather than just editing one row, so freed or lost time is used well. Regenerate the files after changes.
