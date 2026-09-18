---
name: lecture-timeline-mapper
description: >
  Match a timestamped lecture transcript to the user's notes, slides, topics,
  examples, or definitions so they can find where specific study material was
  explained. Use this when the user asks where a slide, topic, example, or note
  appears in a lecture, or when they want to build a study timeline from lecture
  timestamps. Does NOT fire on: ordinary video summaries, transcript extraction
  alone, generic note summarization, or requests that do not include timestamped
  lecture content.
---

# Lecture Timeline Mapper

Finds the exact lecture time ranges where study material was explained in a
timestamped transcript.

## When to use this

Use this skill when the user asks to:

- match notes or slide titles to lecture timestamps
- locate the time where a topic, example, or definition was explained
- build a study timeline that connects lecture sections to material
- identify all relevant time ranges where a concept appears in the lecture

**Do not use this skill for:**

- summarizing a lecture without mapping topics to timestamps
- extracting a transcript from a video
- shortening, rewriting, or condensing notes
- answering general study questions when no timestamped lecture content is provided

> This skill should only activate when the task requires mapping written study
> material to timestamped lecture content.

## Steps

1. Identify the user's study items, such as slide titles, topics, examples,
   definitions, or important notes.

2. Read the timestamped lecture transcript in chronological order.

3. Match each study item to the strongest relevant section of the transcript.

4. Use topic shifts and nearby timestamps to estimate the smallest useful
   start and end time range.

5. Label each result as MATCHED, UNCERTAIN, or NOT FOUND.

6. If a topic appears more than once, report all relevant time ranges.

7. Return a chronological lecture map showing the study item, timestamp range,
   and a short description of what was explained.

## Rules

- Never invent timestamps that are not supported by the transcript.
- Do not claim a topic was explained unless there is clear evidence in the transcript.
- Prefer the smallest useful timestamp range rather than a broad section.
- Mark weak or ambiguous matches as UNCERTAIN.
- Mark material that does not appear in the lecture as NOT FOUND.
- Preserve the user's slide names, topic names, and example names whenever possible.