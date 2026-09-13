# Review report format

Use this structure exactly. Keep it short enough that the author reads all of it.

---

```markdown
## Review — `<skill-name>`

**Verdict: <Ready to submit | Needs work | Reconsider the scope>**

<One sentence saying why.>

### Mechanical check
<Paste the script output verbatim. Do not summarise it.>

### Routing test

| Prompt | Should fire? | Would it? | |
|---|---|---|---|
| `<must-fire prompt>` | yes | yes | ✅ |
| `<near-miss prompt>` | no | yes | ❌ |
| `<ambiguous prompt>` | ? | no | ⚠️ |

<One line on what the misses reveal.>

### Findings

**1. <Highest-severity finding>**
> <the exact line being criticised, quoted>

<What is wrong and the concrete fix.>

**2. <Next finding>**
...

<Maximum five. Ordered by severity.>

### What is already good
<One or two lines. Real, not flattery — it tells the author what to preserve.>
```

---

## The three verdicts

**Ready to submit** — mechanical checks pass, the routing test is clean, and any
remaining findings are cosmetic. Say so plainly; do not invent objections to look
thorough.

**Needs work** — the idea is sound but something concrete is wrong: a leaky
description, a missing dormancy test, a critical rule left in prose. The author
has a clear list and can fix it in one pass.

**Reconsider the scope** — the deeper problem. The skill overlaps something that
already exists, or tries to do four unrelated jobs, or encodes something the
model already does unaided. No amount of description editing fixes it. Say this
gently but say it clearly — it is the most useful review a person can get.
