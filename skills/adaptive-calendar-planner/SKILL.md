---
name: adaptive-calendar-planner

description: >
  Plan, add, move, or re-plan my schedule in my connected calendar when I give you
  tasks, appointments, date changes, date ranges, or progress updates such as
  "I am late", "I finished", "move this to Friday", or "plan this project from
  September 12 to 13". Read the existing calendar before scheduling and adapt
  flexible time blocks when plans change.
  Does NOT fire on: general productivity advice, simple date/time questions,
  requests that only ask what is already on the calendar without planning or
  changing it, or long-term project planning that is not being scheduled into
  the calendar.
---

# Adaptive Calendar Planner

Keeps a user's real calendar aligned with their schedule as tasks, appointments,
projects, dates, and progress change.

## When to use this

Fires when the user asks to:

- add tasks or appointments to their calendar and fit them around existing events
- plan a day using the free time already available in the calendar
- move an existing flexible task or event from one day or time to another
- schedule a task or project on a specific date
- schedule a project across a date range and distribute its work across available time
- report progress such as "I finished", "I am late", "I did not do this", or
  "something came up" and needs the remaining schedule adjusted
- add a new appointment and reorganize flexible tasks around it
- re-plan the rest of today, tomorrow, or another requested date based on what actually happened

**Does NOT fire on:**

- general time-management or productivity advice that does not require changing a calendar
- simple questions about the current date or time
- requests that only ask what events are already on the calendar without planning or changing them
- long-term project planning that is not being scheduled into the calendar

## Steps

1. Read the relevant calendar period before planning, moving, or changing anything.

2. Separate the user's items into:
   - fixed commitments: appointments, classes, meetings, or events that should not move
   - flexible tasks: study, gym, applications, project work, personal work, or other tasks that can be rescheduled

3. Identify whether the request is:
   - a new schedule
   - a move to another time or date
   - a date-range project
   - a progress update that requires re-planning

4. Check the available time, existing events, task durations, deadlines, priorities,
   requested dates, and date ranges. Ask only for missing information that is necessary
   to create a realistic schedule.

5. For a task or project with a date range, treat the range as a planning window.
   Spread the required work across realistic free calendar slots within that range.

6. If the user gives a date range but does not provide enough information to know whether
   they want a continuous multi-day event or separate work blocks, ask one focused question
   before writing to the calendar.

7. Build a realistic plan using free calendar slots. Avoid overlaps and leave reasonable
   transition or break time when needed.

8. Write the agreed plan to the connected calendar using the available calendar tool.

9. When the user asks to move an existing flexible task, read both the current date and the
   target date, then update the existing event instead of creating a duplicate.

10. When the user sends a progress update, read the calendar again and compare the current
    plan with what actually happened.

11. Re-plan only the remaining flexible work. Preserve fixed commitments, use the remaining
    time realistically, and move lower-priority work when the original plan no longer fits.

12. If the user is significantly behind, use recovery mode:
    prioritize urgent or important work, keep fixed commitments, reduce unnecessary gaps,
    and move lower-priority flexible work when needed instead of blindly pushing everything
    to the next day.

13. Report what was added, moved, split across dates, kept unchanged, or could not be scheduled.

## Rules

- Never claim that a calendar event was added, moved, or deleted unless the calendar tool
  successfully completed the action.
- Always read the current calendar before making or revising a schedule.
- When moving an existing event to another date, read the target date before choosing a new time.
- Never move or delete a fixed appointment unless the user explicitly asks for that change.
- Never create overlapping calendar events.
- Treat planning blocks created for flexible tasks as movable when the user asks to re-plan.
- Treat a project date range as a planning window by default, not as one continuous multi-day event.
- Split project work into realistic calendar blocks across the requested date range when the
  user provides enough duration or workload information.
- Only create an all-day or continuous multi-day event when the user explicitly asks for that format.
- Do not duplicate an event when the user's intent is to move or reschedule the existing one.
- If a new fixed appointment conflicts with another fixed event, ask the user instead of
  silently replacing or moving either one.
- Do not guess critical details such as an appointment time, hard deadline, or required project duration.
- Use the calendar's current timezone when creating or moving events.
- When the user reports that all planned work is complete, do not make unnecessary calendar changes.
- If calendar read/write access is unavailable, clearly say that the calendar could not be
  changed and do not pretend the action succeeded.
