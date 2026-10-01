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