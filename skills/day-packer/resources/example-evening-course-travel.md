# Worked example: full workday, morning gym, evening course in another city, late trip home

Use this as a model for days built around a **fixed-time event far from home** that ends late. Adapt the behavior; don't copy the numbers.

> **Note:** The user gave the scenario only. The answers and times in sections 5–6 are **hypothetical illustrations**, marked as such. In a real run, get these from the user.

## 1. The user's brain-dump

> course of 5.5 hr at the evening and needs to go to tel aviv for the course and you need to work around 8 hours a day also need to the gym at the morning before work and the way back

Notes on reading it:
- The course has a fixed location (Tel Aviv) and a fixed duration (5.5h), but its start time isn't given, and "evening" is vague.
- "Around 8 hours" of work is approximate. It's unclear whether that includes a break.
- The gym has a fixed position: morning, before work. Its duration isn't given.
- "The way back" means the return trip after the course is a real block that must be planned. It probably ends late at night, possibly after midnight.

## 2. Parsed list shown back to the user

| Item | Duration | Known timing |
|---|---|---|
| Gym | ? | morning, before work |
| Work | ~8h | after gym |
| Travel to Tel Aviv | ? | before course |
| Course (Tel Aviv) | 5.5h | evening, start time ? |
| Travel home | ? | after course |
| Sleep | ? | ? |

## 3. Feasibility check before asking

Work backwards from the fixed-time item, because the course start pins the whole day:

> Course start − travel − buffer = latest time work must end.
> Latest work end − 8h = latest work start.
> Work start − commute − gym = wake-up time.

Also flag the other end of the day: a 5.5h evening course plus the trip home will likely put you home after midnight. Ask about the next morning.

## 4. One round of questions (bundled)

1. What time does the course start? The start time pins the whole day.
2. Where is home, and where is work? How long does the trip to Tel Aviv take, and how will you travel (car, train, bus)? If you're not driving, travel time can be used for light tasks.
3. Does the ~8h of work include a break? Are the work hours flexible?
4. How long is the gym session?
5. **Sleep & breaks for this plan:** what time do you need to wake the next day? Should I protect a sleep block?
6. Is this one day, or a repeating course day each week?

Do **not** invent transport schedules. If the return is late, tell the user to check the last train or bus times.

## 5. Hypothetical answers (illustration only)

- The course runs 17:30–23:00, and home and work are both in Jerusalem.
- The user takes the train, about 1h15 door to door (est.). This needs verifying.
- Work is flexible, 8h including a 30-minute break. The gym session is 1h.
- The next day is a normal workday, and sleep is flexible.

## 6. Output pattern

**Lead with the binding constraint:**

> The course at 17:30 in Tel Aviv means leaving by ~16:00 (1h15 travel + 15 min buffer). So work must run about 08:00–16:00, and the gym has to be done by ~07:30.

**Timetable (hypothetical):**

| Start | End | Task | Where | Notes |
|---|---|---|---|---|
| 05:30 | 05:50 | Wake up, get ready | Home | pack course bag + dinner |
| 05:50 | 06:00 | Travel to gym | | est. |
| 06:00 | 07:00 | Gym | Gym | |
| 07:00 | 07:30 | Shower, breakfast | | |
| 07:30 | 08:00 | Commute to work | | est. |
| 08:00 | 16:00 | Work | Work | includes 30 min break |
| 16:00 | 17:15 | Travel to Tel Aviv | Train | eat dinner on the way (stacked) |
| 17:15 | 17:30 | Buffer, find room | Tel Aviv | before a far fixed-time item |
| 17:30 | 23:00 | Course | Tel Aviv | |
| 23:00 | 00:15 (+1d) | Travel home | Train | **check last train time**; light review (stacked) |
| 00:15 | 00:30 | Wind down | Home | |
| 00:30 | — | Sleep | | |

**Flag the sleep cost once, then respect the choice:**

> Waking at 05:30 the next day gives about 5h of sleep. On a workday that follows a ~19-hour day, you could shorten or skip the gym tomorrow, or move it to the evening. Your call.

**List assumptions:**
- The train takes about 1h15 each way (est., hypothetical). Verify it, and check the last departure after 23:00.
- Work hours can shift to 08:00–16:00.
- The user isn't driving. If they are, remove the "(stacked)" tasks from the travel blocks.

**Close with one question:** Do these times match, and is the course start correct? Generate the .xlsx and .ics files after the user confirms.

## Lessons from this example

- A fixed-time event in another place decides the day. Work backwards from it: start time → travel → buffer → end of work → start of work → gym → wake.
- Add a buffer before a far fixed-time item, since lateness there can't be recovered.
- A late return is a real block and often crosses midnight. Write it as `00:15 (+1d)` and consider the effect on the next morning.
- Only stack tasks on travel blocks when the user isn't driving. Ask how they travel.
- Never invent train or bus times. Estimate the duration, mark it `est.`, and tell the user to verify it and check last departures.
