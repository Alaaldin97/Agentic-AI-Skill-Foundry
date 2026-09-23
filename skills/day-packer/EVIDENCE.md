# Evidence — `day-packer`

**Tested on:** Claude (claude.ai) · **Date:** 2026-09-23

---

## 1. It fired when it should

Two real runs. Full write-ups of both are in `resources/` as worked examples.

### Run A — two jobs, gym, job search, hard end time

**What I typed:**

```
i need to got to work 8 hours and then the second job after i need to look for a new job and i like to go to the gym fund time to add all of the above whil finishing everything by 5 or max 6 pm and then reach home to sleep at 10
```

**What happened:**

```
Parsed list shown back:
| Job 1 | 8h | — | / | Job 2 | ? | after Job 1 | / | Job search | ? | / | Gym | ? |
| Hard end | done by 17:00, 18:00 at the latest | / | Sleep | home and asleep by 22:00 |

Feasibility check up front: if Job 2 is ~4h and gym and job search ~1h each,
that's 14h+ before travel. Finishing by 18:00 means starting around 03:30–04:00.

One bundled round of questions: which day, length of Job 2, earliest start /
sleep block, gym and job-search length, travel times, is 18:00–22:00 free.
[...]
```

**My follow-up answer:**

```
tomorow an the second job is around 5 hours gym for 1.5 job serach in the internet can be after arriving home
```

**Final output:**

```
Binding constraint: 8h + 5h = 13h of work plus travel. To finish by 18:00,
Job 1 must start around 04:00 no matter where the gym goes.

Option A (exactly as asked): 01:45 wake, 02:00–03:30 gym, 04:00–12:00 Job 1,
12:30–17:30 Job 2, 18:00 home, 18:30–21:30 job search, 22:00 sleep.
Option B (gym moved to evening): 03:15 wake, 04:00–12:00 Job 1,
12:30–17:30 Job 2, 18:00–19:30 gym, 20:00–21:45 job search.
[...]
Sleep cost flagged once: Option A gives under 4h of sleep, Option B about 5¼h.
Assumptions listed: every trip ~30 min (est.); Job 1 can start at 04:00.
Closing question: which option, and what is the real earliest start?
```

### Run B — full workday, morning gym, evening course in Tel Aviv

**What I typed:**

```
course of 5.5 hr at the evening and needs to go to tel aviv for the course and you need to work around 8 hours a day also need to the gym at the morning before work and the way back
```

**What happened:**

```
Parsed list shown back (gym, ~8h work, travel to Tel Aviv, 5.5h course,
travel home, sleep), then one bundled round of questions: course start time,
home/work location and how I travel, whether the 8h includes a break, gym
length, sleep / next-day wake time, one day or weekly.
Flagged that the trip home will likely end after midnight and said to check
last train times rather than inventing a timetable.
[...]
```

The timetable in `resources/example-evening-course-travel.md` uses
illustrative answers (marked there as hypothetical); the prompt and the
question round above are from the real run.

**Did it activate on its own?** Not at first — in runs A and B (original description) I had to name the skill. I rewrote the description to lead with what the user types, reinstalled, and retested in a fresh chat without naming it (run C). It fired on its own.

### Run C — retest with the new description, skill not named

**What I typed** (fresh chat, same prompt as run A, no mention of the skill):

```
i need to got to work 8 hours and then the second job after i need to look for a new job and i like to go to the gym fund time to add all of the above whil finishing everything by 5 or max 6 pm and then reach home to sleep at 10
```

**What happened:**

```
Planning out the day's schedule and tasks.
Checking whether a packed daily schedule actually fits.

Before building this, I need a few details, because as written the plan may
not fit. An 8-hour job plus a second job, the gym, and job hunting, all done
by 17:00–18:00, means starting very early [...]

Here's what I understood:

Item                        Duration  Known?
Job 1                       8 h       ✅
Job 2 (right after Job 1)   ?         ❌
Job search                  ?         ❌
Gym                         ?         ❌
Finish everything           by 17:00, max 18:00  ✅
Home and asleep             22:00     ✅

To plan it properly, I need to know:
- Which jobs are these? Is the 8-hour one [job names redacted] ...
- Start time. What's the earliest you can start work ...
- Gym and job search. How long for each ...
- Travel. Roughly how long is the commute ...
- Breaks. Do you want a lunch break and short breaks built in, or pack
  everything tightly?
- Which day(s)? ...

Once you answer, I'll build a timetable and give you an Excel sheet plus a
calendar file you can import. If it truly can't all fit by 18:00, I'll show
you exactly what doesn't fit and suggest options [...]
```

It followed the skill's workflow unprompted: parsed list shown back, feasibility
warning with numbers, one bundled round of questions including breaks, and the
promise of .xlsx + .ics files.

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```
remind me to call [name]
```

(Exact wording not saved; the person's name is removed.)

**Did it stay dormant?** Yes. Claude just added a reminder to make the call; no timetable, no questions, no files.

**Why this one is a real test:** it names a task and a time, like a brain-dump does, but it's a single item with nothing to pack.

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~110 |
| Body, once it fired | ~2,000 |
| What stayed on disk because it did not fire | ~2,000 + resources |

---

## 4. Anything a reviewer should know

- Known limitation: travel times are estimates marked `est.`; the skill never invents train or bus timetables.
- Needs an API key / network: no. File output needs Python 3 with `openpyxl`.
- Anything that surprised you: with the original description the skill did not fire on its own, even on a long task brain-dump — I had to name it. Leading the description with the user's words fixed that.
