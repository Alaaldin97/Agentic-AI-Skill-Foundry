# Worked example: two jobs, gym, job search, hard end time

Use this as a model for how to handle a brain-dump where the constraints may not physically fit. Adapt the behavior; don't copy the numbers.

## 1. The user's brain-dump

> i need to got to work 8 hours and then the second job after i need to look for a new job and i like to go to the gym fund time to add all of the above whil finishing everything by 5 or max 6 pm and then reach home to sleep at 10

Notes on reading it:
- The message is informal and has typos ("fund time" = "find time"). Read for intent.
- "Finishing everything by 5 or max 6" is a hard end time, and "sleep at 10" is a protected sleep start.
- The durations of Job 2, the gym, and the job search are missing, and so is the day.

## 2. Parsed list shown back to the user

| Item | Duration | Known timing |
|---|---|---|
| Job 1 | 8h | — |
| Job 2 | ? | after Job 1 |
| Job search | ? | — |
| Gym | ? | — |
| Hard end | — | done by 17:00, 18:00 at the latest |
| Sleep | — | home and asleep by 22:00 |

## 3. Feasibility check before asking

Do a quick sum before asking questions. If the known and likely durations can't fit the window, say so up front with the numbers, e.g.:

> If Job 2 is ~4h and gym and job search ~1h each, that's 14h+ before travel. Finishing by 18:00 means starting around 03:30–04:00, leaving about 5h of sleep.

This lets the user rethink the constraints before answering the questions.

## 4. One round of questions (bundled)

1. Which day: tomorrow only, or a repeating weekday plan?
2. Which job is which, and how long is Job 2? Are its hours fixed or flexible?
3. What is the earliest realistic start and wake time? Should a sleep block be protected?
4. How long for the gym and the job search? Can either happen before work or be split?
5. How long does travel take between home, Job 1, Job 2, and the gym?
6. Is 18:00–22:00 free time, or can tasks go there? Should breaks and meals be built in?

## 5. The user's answers (partial)

> tomorow an the second job is around 5 hours gym for 1.5 job serach in the internet can be after arriving home

- The day is tomorrow, Job 2 takes about 5h, and the gym takes 1.5h.
- The job search goes in the evening at home, so the 18:00 limit covers work and gym only.
- Travel time, start time, and whether Job 1 can start early went unanswered. Proceed anyway and label these as assumptions.

## 6. Output pattern

**Lead with the binding constraint:** 8h + 5h = 13h of work plus travel. To finish by 18:00, Job 1 must start around 04:00 no matter where the gym goes.

**Offer at most two options when the literal request is extreme:**

Option A, exactly as asked, with everything by 18:00:

| Start | End | Task | Notes |
|---|---|---|---|
| 01:45 | 02:00 | Wake up, get ready | |
| 02:00 | 03:30 | Gym | needs a 24h gym |
| 03:30 | 04:00 | Travel to Job 1 | est. |
| 04:00 | 12:00 | Job 1 | eat during break |
| 12:00 | 12:30 | Travel + quick lunch | est. |
| 12:30 | 17:30 | Job 2 | |
| 17:30 | 18:00 | Travel home | est. |
| 18:00 | 18:30 | Dinner | |
| 18:30 | 21:30 | Job search | |
| 21:30 | 22:00 | Wind down | |

Option B, with the gym moved to the evening so work still ends by 18:00:

| Start | End | Task | Notes |
|---|---|---|---|
| 03:15 | 03:30 | Wake up, get ready | |
| 03:30 | 04:00 | Travel to Job 1 | est. |
| 04:00 | 12:00 | Job 1 | |
| 12:00 | 12:30 | Travel + quick lunch | est. |
| 12:30 | 17:30 | Job 2 | |
| 17:30 | 18:00 | Travel home | est. |
| 18:00 | 19:30 | Gym | near home, est. |
| 19:30 | 20:00 | Dinner | |
| 20:00 | 21:45 | Job search | |
| 21:45 | 22:00 | Wind down | |

**Flag the sleep cost once, plainly, then respect the choice:**

> Option A gives under 4h of sleep, and Option B about 5¼h. After a 13-hour workday, that will likely hurt the gym session and the applications. It's your call.

**List assumptions:**
- Every trip takes about 30 minutes (est.).
- Job 1 can start at 04:00. This is the biggest assumption. If it can't, the 18:00 finish is impossible, and the plan should be rebuilt around the real start time.

**Close with one question** that settles the plan: which option, and what is the real earliest start? Generate the .xlsx and .ics files after the user confirms, since building files on an unconfirmed plan wastes effort.

## Lessons from this example

- Run the math before asking, and show it. A hard end time plus long fixed blocks decides the start time.
- Find the one binding constraint, which here was total work hours, and say it first.
- Don't quietly move items past the user's deadline. Offer that as a labeled option instead.
- Keep meals and travel as real blocks, marked `est.` when guessed.
