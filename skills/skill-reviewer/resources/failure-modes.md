# The seven ways a skill description goes wrong

The description is the only part of your skill the model sees before deciding
whether to load it. Everything below is a way that decision goes wrong.

---

## 1. It describes the feature, not the symptom

The author writes what they built. The user types what hurts. These are rarely
the same words.

| ❌ | ✅ |
|---|---|
| "A comprehensive LinkedIn content engine" | "when the user wants to write a viral LinkedIn post" |
| "Advanced repository analysis toolkit" | "when the user opens an unfamiliar repo and asks where to start" |

**Test:** would the description match a prompt written by someone who has never
heard of this skill?

---

## 2. No dormancy clause

A description that only says when to fire will fire on anything adjacent. With
one skill installed you never notice. With thirty, every turn is a fight.

**Fix:** add `Does NOT fire on:` and name the two or three nearest misses.

---

## 3. Trigger words too generic

"analyze", "help with", "improve", "manage", "handle" — these appear in a
quarter of all user prompts. A description built on them fires constantly.

**Fix:** anchor to a concrete noun. Not "analyse data" but "analyse a CSV export
from Google Analytics".

---

## 4. Assumes context the router does not have

"Use this for our standard process" — whose standard? The routing decision is
made with the description alone, not the body, and not the conversation history.

**Fix:** make the description self-contained.

---

## 5. Overlaps a neighbouring skill

Two skills whose descriptions both plausibly match the same prompt means the
model picks arbitrarily, and the user gets inconsistent behaviour across runs.

**Fix:** check the catalog first. Either narrow both descriptions until the
boundary is sharp, or merge the skills.

---

## 6. Too long

The description loads on **every turn, whether or not the skill fires**. Twenty
skills with 400-character descriptions is 8,000 tokens of standing cost before
anybody types anything.

**Fix:** aim for 200–400 characters. Detail belongs in the body.

---

## 7. Buries the trigger at the end

Routing attention is not uniform. A description that opens with two sentences of
background and names the actual trigger last is a weaker signal than one that
leads with it.

**Fix:** first clause names the job. Background, if any, goes after.
