# Evidence — `lecture-timeline-mapper`

**Tested on:** VS Code 1.137 · Windows 11 · **Date:** 2026-09-18

---

## 1. It fired when it should

**What I typed:**

```text
Where was the definition of overfitting explained in this lecture, and what time range matches it?
```

**What happened:**

```text
Definition of overfitting — MATCHED
Time range: 00:02:10–00:05:19

The transcript explains that a model can perform very well on training data but poorly on new unseen data, which is described as overfitting.
```

**Did it activate on its own?** Yes — it fired without naming the skill.

---

## 2. It stayed quiet when it should

**A near-miss I tested:**

```text
Summarize this lecture in a few bullet points.
```

**Did it stay dormant?** Yes.

**Why this one is a real test:** It is lecture-related, but it asks for a general summary instead of mapping notes, slides, topics, examples, or concepts to exact lecture timestamps.

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~120 |
| Body, once it fired | ~600 |
| What stayed on disk because it did not fire | ~600 |

On the dormancy run only the ~120-token description was in play; the ~600-token
body was never loaded, so that is what staying quiet saved.

---

## 4. Anything a reviewer should know

- Known limitation: The skill requires a timestamped lecture transcript. It does not extract transcripts from videos or YouTube links.
- Needs an API key / network: no
- Anything that surprised you: Keeping the description narrow was important so the skill fires on timestamp-mapping requests while staying dormant for regular lecture summaries.