---
name: vague-opportunity-checker
description: Analyze vague internship, training, recruiting, mentorship, freelance, or other professional-opportunity messages. Separate confirmed facts from missing details, identify supported warning signs, draft verification questions, and recommend a safe next action. Use when the user provides a specific opportunity message that is unclear or difficult to verify. Does NOT fire on: CV-to-job comparisons, interview preparation, general job searches, company research, or application writing.
---

# Vague Opportunity Checker

Review an unclear professional-opportunity message before the user shares sensitive information, pays money, commits time, or assumes that a concrete offer has been made.

## When to use this

Use this skill when the user provides a specific internship, training, recruiting, mentorship, freelance, or other professional-opportunity message that is vague, incomplete, inconsistent, or difficult to verify.

Do not use it for CV comparisons, interview preparation, general job searches, or company research without a specific opportunity message.

## Steps

1. Read the complete opportunity message and the context supplied by the user.

2. Call `read_resource` exactly once to read `resources/opportunity-checklist.md`. After it returns, analyze the message and answer directly. Do not call any other tool, including `run_script` or `run_subagent`.

3. Extract only claims explicitly supported by the supplied message. Present them under **Confirmed facts**.

4. Identify important information that is absent, ambiguous, conditional, or merely implied. Present it under **Missing or ambiguous information**.

5. Compare the message with the checklist. Report a warning sign only when specific wording or behavior in the supplied material supports it.

6. Assign exactly one concern label:

   - `LOW CONCERN`
   - `NEEDS VERIFICATION`
   - `HIGH CONCERN`

7. Explain the label briefly while distinguishing confirmed facts, reasonable inferences, and unknown information.

8. Generate a short prioritized list of verification questions. Do not ask questions that the message already answers clearly.

9. Draft a concise professional reply in the same language as the user's request unless the user asks for another language.

10. Recommend one proportionate next action:

    - proceed with routine clarification;
    - pause until key details are verified;
    - stop and avoid sharing money, credentials, or sensitive information.

## Rules

- Use only `read_resource`, exactly once.
- Do not call `run_script`, `run_subagent`, or any other tool.
- After reading the checklist, produce the final answer directly.
- Keep the complete answer under 200 words.
- Use short bullets and no introductory paragraph.
- Preserve the strength and meaning of the original wording.
- Do not change phrases such as "work with" into stronger claims such as "partner with."
- Do not invent urgency, guarantees, relationships, or promises absent from the message.
- Never claim that an opportunity is legitimate merely because the message looks professional.
- Never call an opportunity a scam unless reliable evidence supplied by the user establishes that conclusion.
- Missing information alone is not proof of fraud.
- Clearly distinguish statements made by the sender from independently verified facts.
- Quote or closely reference relevant wording when reporting a warning sign.
- Prioritize questions that materially affect the user's decision.
- Do not request or reproduce passwords, verification codes, banking details, or unnecessary identity information.
- Preserve the user's language and professional tone in the drafted reply.
- If the opportunity message is missing, ask the user to provide it instead of guessing.

## Output format

### Confirmed facts

List only information explicitly supported by the message. Describe unverified statements as claims made by the sender.

### Missing or ambiguous information

List the important unanswered or unclear details.

### Warning signs

List each supported warning sign with its evidence. If none are supported, write:

`None identified from the supplied message.`

### Concern level

Write exactly one:

`LOW CONCERN`, `NEEDS VERIFICATION`, or `HIGH CONCERN`

Add brief reasoning that distinguishes facts, inferences, and unknowns.

### Questions to ask

Provide only the highest-priority unanswered questions.

### Suggested reply

Write a concise professional message in the user's language.

### Recommended next action

Provide one clear and proportionate next step.

## Resource

| File | Purpose | When to load |
| --- | --- | --- |
| `resources/opportunity-checklist.md` | Verification categories, warning signs, concern labels, and question priorities | Read exactly once during step 2 |