# Evidence — Vague Opportunity Checker

## Problem

Professional opportunities received through LinkedIn, direct messages, or messaging applications are sometimes too vague to evaluate safely.

Important details may be missing, including:

- the organizer's identity;
- the type and structure of the opportunity;
- compensation or possible fees;
- the relationship with companies mentioned in the message;
- what happens after training;
- why communication must move to another platform.

The skill helps the user separate confirmed facts from assumptions, identify supported warning signs, ask focused verification questions, and choose a proportionate next action.

## Skill shape

**Knowledge skill**

The skill uses:

- `SKILL.md` for the workflow and behavioral boundaries;
- `resources/opportunity-checklist.md` for verification categories, warning signs, concern labels, and question priorities.

No executable scripts are required.

## Test environment

- Runner: Module 5B `skill_runner.py`
- Model: `openai/gpt-4o-mini`
- Skills discovered: 4
- Test date: 2026-10-01

## Positive trigger test

### Request

```text
I received this message: Join our exclusive tech career program. We work with companies like NVIDIA and Salesforce. Move to WhatsApp today and choose frontend or AI. We will explain who runs the program, whether it is paid, and what happens after training later. Help me separate confirmed facts from missing information, identify warning signs, and draft questions before I continue.
```

### Routing result

```text
ROUTED   vague-opportunity-checker
```

### Resource-use trace

```text
read_resource  {'relative_path': 'resources/opportunity-checklist.md'}
```

The resource was read exactly once. The skill did not call a script or subagent.

### Output excerpt

```text
### Confirmed facts
- The message invites you to join a "tech career program."
- It mentions working with companies like NVIDIA and Salesforce.
- You can choose between frontend or AI.

### Concern level
NEEDS VERIFICATION

Important details are missing or ambiguous, but the message does not support a stronger conclusion.

### Recommended next action
Pause until key details are verified.
```

### Output behavior

The result:

- separated confirmed facts from missing information;
- treated the NVIDIA and Salesforce statement as an unverified claim;
- identified supported warning signs;
- assigned `NEEDS VERIFICATION`;
- generated prioritized verification questions;
- drafted a professional reply;
- recommended pausing until key details were verified.

### Progressive-disclosure result

```text
skills on disk .............. 4
menu shown to the router .... ~359 tokens
if we had loaded ALL of them. ~2,520 tokens
we actually loaded .......... ~1,039 tokens (vague-opportunity-checker)
SAVED ....................... ~1,481 tokens
```

## Near-miss dormancy test

The following nearby request correctly stayed dormant and did not fire the skill.

### Request

```text
Compare my CV with a frontend internship description and tell me which technical skills are missing.
```

### Routing result

```text
ROUTED   NO_SKILL — answering directly
```

### Progressive-disclosure result

```text
skills on disk .............. 4
menu shown to the router .... ~359 tokens
if we had loaded ALL of them. ~2,520 tokens
we actually loaded .......... ~0 tokens (nothing)
SAVED ....................... ~2,520 tokens
```

### Why dormancy was correct

The request concerns CV-to-job comparison rather than evaluating an unclear opportunity message. The skill description explicitly excludes CV comparisons, so the skill body and bundled resource stayed unloaded.

## Iteration evidence

Testing revealed and corrected several issues:

1. The initial multiline YAML description appeared as `>` during discovery, so it was changed to a single-line description.
2. The model initially attempted to call a nonexistent script, so the skill was restricted to `read_resource`.
3. The model then attempted unnecessary subagent delegation, so the skill was instructed to answer directly after reading the checklist.
4. The runner displays only the first 1,500 characters of an answer, so the skill output was limited to 200 words.
5. The final positive test used one resource read, no unnecessary tools, and produced every required output section.
6. The near-miss test correctly kept the skill dormant and loaded zero skill-body tokens.

## Conclusion

The skill fires for an unclear professional opportunity, uses its bundled checklist, produces a cautious structured evaluation, and stays dormant for a nearby but excluded CV-comparison request.

## Reviewer verification (Alaaldin Ahmed, 2026-10-01)

Re-run before merging with the unmodified Module 5B `skill_runner.py` and `openai/gpt-4.1-mini`, the runner's default model (`gpt-4o-mini` cannot be given tools on the reviewer's OpenRouter account). Five skills were on disk so the router had a real choice, including `job-gap-to-mini-project`, whose trigger is this skill's own near-miss.

### Routing: 8 of 8 correct

| Prompt | Expected | Routed | Label |
| --- | --- | --- | --- |
| Aya's test message (NVIDIA and Salesforce, move to WhatsApp) | fire | `vague-opportunity-checker` | `NEEDS VERIFICATION` |
| LinkedIn "recruiter": refundable $50 fee, ID photo, bank card details, "expires tonight" | fire | `vague-opportunity-checker` | `HIGH CONCERN` |
| Arabic WhatsApp message asking for full name and ID number | fire | `vague-opportunity-checker` | `NEEDS VERIFICATION`, reply drafted in Arabic |
| Clear interview invitation: paid, dates, hours, no fee, named sender | fire | `vague-opportunity-checker` | `LOW CONCERN` |
| Compare my CV with a frontend internship description | dormant | `job-gap-to-mini-project` | - |
| Write a LinkedIn message to a recruiter asking about internship openings | dormant | `NO_SKILL` | - |
| What questions will a frontend internship interview ask? | dormant | `NO_SKILL` | - |
| Write a cover letter for a pasted internship advert | dormant | `NO_SKILL` | - |

### One fix: the answer did not fit the runner

The 200-word rule exists because the runner prints only the first 1,500 characters. On `gpt-4.1-mini` the four answers ran to 278-379 words, so **Suggested reply** and **Recommended next action** were cut off in all four. Models rarely meet a global word count, but they do follow per-section limits, so the output format now caps each section: 3 facts, 3 missing details as short noun phrases, 3 warning signs, 3 questions, a reply of at most 40 words, and a one-sentence next action. The method, checklist and safety rules are unchanged.

| Prompt | Before (chars) | After, two runs (chars) |
| --- | --- | --- |
| Aya's test message | 2,303 | 1,441 / 1,421 |
| Fee + ID + bank card | 2,309 | 1,445 / 1,480 |
| Arabic message | 1,778 | 1,346 / 1,286 |
| Clear invitation | 1,829 | 1,314 / 1,210 |

All seven sections are now visible on every run, and no concern label changed.

### Transcript after the fix (fee + ID + bank card)

```text
====================================================================
REQUEST  A recruiter messaged me on LinkedIn: "Hi! Our partner company is hiring remote junior developers. Pay is $1,800/month and no interview is needed. To reserve your place, pay a refundable $50 registration fee today and send a photo of your ID and your bank card details. The offer expires tonight." Should I go ahead?
SKILLS   5 on disk: bug-report-triager, job-gap-to-mini-project, screen-guide, student-code-reviewer, vague-opportunity-checker
ROUTED   vague-opportunity-checker
====================================================================
  -> read_resource({'relative_path': 'resources/opportunity-checklist.md'}...)

--------------------------------------------------------------------
ANSWER

### Confirmed facts
- The message claims a partner company is hiring remote junior developers.
- Pay is stated as $1,800/month with no interview required.
- A refundable $50 registration fee and photos of ID and bank card details are requested.

### Missing or ambiguous information
- Organizer's legal name and official website.
- Clear description of the opportunity type and responsibilities.
- Explanation for the need to send bank card details and ID photo.

### Warning signs
- Request for payment upfront ("pay a refundable $50 registration fee today").
- Request for sensitive personal information ("photo of your ID and your bank card details").
- Pressure to act quickly ("The offer expires tonight").

### Concern level
HIGH CONCERN due to requests for money and sensitive financial information combined with pressure to decide immediately, without clear organizer identity or opportunity details.

### Questions to ask
1. What is the legal name and official website of the organizer?
2. What type of opportunity is this exactly (employment, training, freelance)?
3. Why are photos of ID and bank card details required?

### Suggested reply
Thank you for the offer. Please provide your company's legal name, official website, and details about the opportunity and why sensitive information is needed.

### Recommended next action
Stop and avoid sharing money, credentials, or sensitive information until full verification is obtained.

--------------------------------------------------------------------
PROGRESSIVE DISCLOSURE — what it actually cost
  skills on disk .............. 5
  menu shown to the router .... ~552 tokens
  if we had loaded ALL of them. ~4,892 tokens
  we actually loaded .......... ~1,166 tokens (vague-opportunity-checker)
  SAVED ....................... ~3,726 tokens

  trace:
    read_resource  {'relative_path': 'resources/opportunity-checklist.md'}
--------------------------------------------------------------------
```
