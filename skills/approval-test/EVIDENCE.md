# Evidence — `_TEMPLATE`

> Delete every line of guidance in here as you fill it in. What remains should
> be a record of what actually happened on your machine, not a description of
> what you hope happens.

**Tested on:** <VS Code 1.13x / Claude Code / other> · **Date:** <YYYY-MM-DD>

---

## 1. It fired when it should

**What I typed:**

```
<the exact prompt — copy it, do not paraphrase it>
```

**What happened:**

```
<the real output. trim the middle if it is enormous, but mark the cut
 with [...] so a reviewer knows something was removed>
```

**Did it activate on its own?** <yes / no — I had to name it>

> If you had to name the skill to get it to fire, your description is not doing
> its job. Fix the description and run it again before you open the PR.

---

## 2. It stayed quiet when it should

The whole point of a narrow description is that the skill does **not** fire on
things that merely sound similar.

**A near-miss I tested:**

```
<a prompt that is close to your trigger but should NOT load this skill>
```

**Did it stay dormant?** <yes / no>

**Why this one is a real test:** <one line — what makes it genuinely close>

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~<n> |
| Body, once it fired | ~<n> |
| What stayed on disk because it did not fire | ~<n> |

> Read these from your client's token counter. Approximate is fine — the point
> is to notice that a skill has a standing cost even when dormant.

---

## 4. Anything a reviewer should know

- Known limitation:
- Needs an API key / network:  <yes — which / no>
- Anything that surprised you:
