---
name: job-gap-to-mini-project
description: "Compare a provided CV or resume against a specific provided job or internship description to find technical evidence gaps and turn one gap into a small portfolio project. Requires both the candidate's CV/resume and a target job description. Does NOT fire on: general learning projects, general project ideas, CV editing, or requests that provide only a technology to practice."
---

## When to use this

Use this skill when the user:
- provides or refers to both a CV/resume and a specific job or internship description;
- wants to compare the job's technical requirements with evidence in the CV;
- wants to identify technical requirements that are not currently demonstrated by the CV;
- wants to turn one useful technical evidence gap into a small, practical portfolio project.

Typical requests include:
- "Compare my CV with this internship and give me a project that would help demonstrate one of the missing technical skills."
- "What technical requirements in this job are not demonstrated in my resume, and what can I build to show one of them?"
- "I want this backend internship. Find a useful technical evidence gap in my CV and turn it into a mini-project."

## Does NOT fire on

Do not use this skill when the user only wants to:
- find or search for jobs;
- rewrite, proofread, or improve a CV;
- write a cover letter;
- learn a technology or concept;
- generate a general project idea without a target job;
- evaluate a job without a CV/resume;
- evaluate a CV without a specific job description;
- automatically apply for a job;
- prepare for an interview.

## Steps

1. Read the job description and extract its requirements.
   Preserve how the job description qualifies each requirement, including
   required vs. preferred/nice-to-have and alternatives such as "X or Y".
   Do not turn a preferred qualification into a mandatory requirement or
   treat one missing alternative as a gap when another accepted alternative
   is demonstrated.

2. Classify the relevant requirements into categories such as:
   - technical skills and technologies;
   - experience requirements;
   - education or certifications;
   - soft skills;
   - other non-project requirements.

3. Read the entire CV for evidence relevant to the job requirements.
   Do not inspect only the Skills section. Look for evidence in projects,
   work experience, education, certifications, and other relevant sections.

4. Compare each relevant job requirement with the evidence found in the CV.

5. Classify each requirement as:
   - DEMONSTRATED — the CV contains reasonable evidence of the requirement;
   - EVIDENCE GAP — the job asks for it but the CV does not currently demonstrate it;
   - UNCLEAR — the available information is not enough to determine whether the CV demonstrates it.

6. Review the evidence gaps and identify which ones can reasonably be
   demonstrated through a small technical project.

  If no project-demonstrable technical evidence gap exists, say so explicitly
and do not invent one. In this case, do not generate a mini-project, because
this skill only creates projects to address job-related technical evidence gaps.

7. Do not turn requirements such as years of professional experience,
   degrees, language requirements, or general soft skills into fake
   substitutes or portfolio projects.

8. Select one useful, job-relevant technical evidence gap that can be
   demonstrated through a realistically small project.
   When multiple gaps qualify, prefer the gap that is more important to the
   target job, can build naturally on evidence already present in the CV,
   and has clear, observable proof of completion.

9. Design the smallest practical mini-project that clearly demonstrates
   the selected skill or technology.

10. Define:
    - the project goal;
    - what the user should build;
    - concrete deliverables;
    - proof of completion;
    - how the project connects to the target job.

## Rules

- Never claim that the user does not know a skill simply because it is absent from the CV.
- Use the term "evidence gap" when the CV does not currently demonstrate a requirement.
- Never invent skills, experience, achievements, certifications, education, or project history.
- Base CV matches only on evidence actually present in the provided CV.
- Distinguish between "not demonstrated" and "not qualified."
- Do not claim that completing the mini-project makes the user qualified for the job.
- Do not claim that the project replaces professional experience, education, certifications, language requirements, or other formal requirements.
- Prefer technical gaps that can be demonstrated through concrete work.
- Prefer one focused mini-project over several unrelated projects.
- Keep the project small enough to function as a portfolio exercise, not a full product.
- Aim for a project that can reasonably be completed within a weekend to one week of part-time work. If necessary, reduce the project scope rather than adding unnecessary complexity.
- Avoid adding unrelated technologies merely to make the project look more complex.
- Every project must have concrete deliverables.
- Every project must include a clear proof-of-completion condition.
- Keep the project directly relevant to the selected evidence gap and target job.
- If the CV or job description is missing, ask for the missing input instead of guessing.

## Output format

### Job Gap Analysis

| Job Requirement | CV Evidence | Status |
| --- | --- | --- |
| Requirement | Evidence found in the CV | DEMONSTRATED / EVIDENCE GAP / UNCLEAR |

### Selected Evidence Gap

**Skill/Technology:**  
Name the selected technical evidence gap.

**Why this gap:**  
Briefly explain why it is relevant to the target job, what evidence is currently
missing from the CV, and why this gap was selected over other project-demonstrable
gaps when relevant.

If no project-demonstrable technical evidence gap exists, stop after the
analysis and state that no gap-based mini-project is needed.

### Mini-Project

**Project title:**  
Give the project a clear, concise name.

**Goal:**  
Explain what technical capability the project is intended to demonstrate.

**Build:**  
Provide a short ordered list of the core implementation steps.

**Deliverables:**  
List the concrete artifacts the user should produce.

**Proof of completion:**  
State an observable condition that demonstrates the project works as intended.

**Connection to the job:**  
Explain which job requirement this project provides evidence for.

### Important Limitations

Mention any important job requirements that are not appropriate to address
through a mini-project, when relevant. 