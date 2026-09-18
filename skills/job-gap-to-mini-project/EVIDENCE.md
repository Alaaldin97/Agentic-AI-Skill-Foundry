# Evidence — job-gap-to-mini-project

This file contains actual test evidence for the `job-gap-to-mini-project` skill.

The tests verify that the skill:
- fires when both a CV and a specific job description are provided;
- stays dormant for a nearby but incorrect request;
- distinguishes project-demonstrable technical evidence gaps from formal requirements;
- preserves required/preferred qualifications and alternatives;
- does not invent an evidence gap when all target technical requirements are already demonstrated.

---

## Test 1 — Positive: Finds a technical evidence gap

### Request

```text
Here is my CV: Software Engineering student. Skills: Python, Java, SQL, Git, AWS. Projects: Built a REST API using FastAPI and PostgreSQL. Here is a Backend Developer Internship: Requirements: Python, REST APIs, SQL, Git, Docker, and Redis. Compare the job requirements with what my CV demonstrates and turn one useful technical gap into a small portfolio project.
```

### Routing

```text
SKILLS   5 on disk: jhf-brief, job-gap-to-mini-project, lab-grader, repo-onboarder, study-plan-builder
ROUTED   job-gap-to-mini-project
```

### Result excerpt

```text
### Job Gap Analysis

| Job Requirement | CV Evidence | Status |
| --- | --- | --- |
| Python | Listed in Skills | DEMONSTRATED |
| REST APIs | Built a REST API using FastAPI | DEMONSTRATED |
| SQL | Listed in Skills, used PostgreSQL in project | DEMONSTRATED |
| Git | Listed in Skills | DEMONSTRATED |
| Docker | Not mentioned in CV | EVIDENCE GAP |
| Redis | Not mentioned in CV | EVIDENCE GAP |

### Selected Evidence Gap

Skill/Technology:
Docker

Why this gap:
Docker is a key technology for backend development, especially for containerizing
applications to ensure consistent environments across development, testing, and
production. The job requires Docker, but the CV does not currently demonstrate
any experience with it. Redis is also a gap, but Docker is more foundational
and broadly applicable for backend roles.

### Mini-Project

Project title:
Containerized REST API with Docker

Goal:
Demonstrate the ability to containerize a backend REST API application using
Docker, showing understanding of Dockerfiles, container building, and running
containers.

Build:
1. Take the existing REST API project built with FastAPI and PostgreSQL.
2. Write a Dockerfile to containerize the FastAPI application.
```

### Progressive disclosure

```text
skills on disk .............. 5
menu shown to the router .... ~376 tokens
if we had loaded ALL of them. ~3,911 tokens
we actually loaded .......... ~1,528 tokens (job-gap-to-mini-project)
SAVED ....................... ~2,383 tokens
```

**Result: PASS**

The skill fired without its name being mentioned, identified technical evidence
gaps, selected one useful gap, and turned it into a relevant portfolio project.

---

## Test 2 — Near miss: General Docker learning request

### Request

```text
I want to learn Docker for backend development. Give me a small project I can build to practice Docker.
```

### Routing

```text
SKILLS   5 on disk: jhf-brief, job-gap-to-mini-project, lab-grader, repo-onboarder, study-plan-builder
ROUTED   NO_SKILL — answering directly
```

### Progressive disclosure

```text
skills on disk .............. 5
menu shown to the router .... ~376 tokens
if we had loaded ALL of them. ~3,911 tokens
we actually loaded .......... ~0 tokens (nothing)
SAVED ....................... ~3,911 tokens
```

**Result: PASS**

The request was related to technical projects and Docker, but it did not provide
both a CV and a target job description. The skill correctly stayed dormant.

---

## Test 3 — Formal requirements are not replaced by projects

### Request

```text
Here is my CV: Software Engineering student. Skills: Python and Git. Projects: Built a small Python web application. Here is a Backend Developer position: Requirements: Python, Docker, a completed Bachelor's degree, 3 years of professional software development experience, and fluent English. Compare the job requirements with what my CV demonstrates and turn an appropriate technical evidence gap into a small portfolio project.
```

### Routing

```text
ROUTED   job-gap-to-mini-project
```

### Result excerpt

```text
### Job Gap Analysis

| Job Requirement | CV Evidence | Status |
| --- | --- | --- |
| Python | Skills: Python; small Python web app | DEMONSTRATED |
| Docker | No mention of Docker | EVIDENCE GAP |
| Completed Bachelor's degree | Currently a student, no degree completed | EVIDENCE GAP |
| 3 years professional software development experience | No professional experience stated | EVIDENCE GAP |
| Fluent English | No explicit evidence of language proficiency | UNCLEAR |

### Selected Evidence Gap

Skill/Technology:
Docker

Why this gap:
Docker is a key technical skill required for the Backend Developer position but
is not demonstrated in the CV. Unlike degree completion or professional
experience, Docker proficiency can be effectively demonstrated through a small
portfolio project. This gap was selected because it is a concrete, technical
skill that can be showcased with a manageable project, directly relevant to
the job.
```

**Result: PASS**

The skill selected Docker as the project-demonstrable technical gap rather than
pretending that a portfolio project could replace a completed degree or
professional experience.

---

## Test 4 — Required/preferred qualifications and alternatives

### Request

```text
Here is my CV: Software Engineering student. Skills: Java, SQL, Git, and AWS. Projects: Built a Java REST API with PostgreSQL and deployed a small application on AWS. Here is a Backend Developer Internship. Required: Java or Python, SQL, and Git. Preferred: Docker and Kubernetes. Compare the job requirements with what my CV demonstrates and turn one useful technical evidence gap into a small portfolio project.
```

### Routing

```text
ROUTED   job-gap-to-mini-project
```

### Result excerpt

```text
### Job Gap Analysis

| Job Requirement | CV Evidence | Status |
| --- | --- | --- |
| Java or Python | Java demonstrated in skills and project (Java REST API) | DEMONSTRATED |
| SQL | SQL demonstrated in skills and project (PostgreSQL) | DEMONSTRATED |
| Git | Git demonstrated in skills | DEMONSTRATED |
| Docker (Preferred) | No evidence of Docker usage | EVIDENCE GAP |
| Kubernetes (Preferred) | No evidence of Kubernetes usage | EVIDENCE GAP |

### Selected Evidence Gap

Skill/Technology:
Docker

Why this gap:
Docker is a preferred skill for the Backend Developer Internship, indicating
it is valued though not mandatory. The CV does not currently demonstrate any
experience with Docker. Kubernetes is also a gap, but it is more complex and
typically builds on Docker knowledge. Docker is a more accessible and
foundational skill to demonstrate through a small project.
```

**Result: PASS**

The skill correctly treated `Java or Python` as an alternative requirement,
recognized Java as sufficient evidence, and preserved Docker and Kubernetes as
preferred rather than mandatory qualifications.

---

## Test 5 — No technical evidence gap

### Request

```text
Here is my CV: Software Engineering student. Skills: Python, SQL, Git, and Docker. Projects: Built and containerized a Python REST API using PostgreSQL and Docker, with the code managed in Git. Here is a Backend Developer Internship. Requirements: Python, SQL, Git, and Docker. Compare the job requirements with what my CV demonstrates and suggest an appropriate small portfolio project.
```

### Routing

```text
SKILLS   5 on disk: jhf-brief, job-gap-to-mini-project, lab-grader, repo-onboarder, study-plan-builder
ROUTED   job-gap-to-mini-project
```

### Result

```text
### Job Gap Analysis

| Job Requirement | CV Evidence | Status |
| --- | --- | --- |
| Python | Skills listed; used in building a REST API project | DEMONSTRATED |
| SQL | Skills listed; used PostgreSQL in the project | DEMONSTRATED |
| Git | Skills listed; code managed in Git for the project | DEMONSTRATED |
| Docker | Skills listed; project containerized using Docker | DEMONSTRATED |

### Selected Evidence Gap

No project-demonstrable technical evidence gap exists between the job requirements and your CV.

### Mini-Project

Not applicable, as all key technical requirements for the Backend Developer Internship are already demonstrated in your CV.

### Important Limitations

Your CV and the job requirements align well on the technical skills Python, SQL,
Git, and Docker. Other important job requirements such as professional
experience, soft skills, or education are not addressed here and are not
suitable for mini-project substitution.
```

### Progressive disclosure

```text
skills on disk .............. 5
menu shown to the router .... ~376 tokens
if we had loaded ALL of them. ~3,948 tokens
we actually loaded .......... ~1,565 tokens (job-gap-to-mini-project)
SAVED ....................... ~2,383 tokens
```

**Result: PASS**

The skill correctly recognized that all target technical requirements were
already demonstrated. It did not invent an evidence gap or generate an
unnecessary gap-remediation project.

---

## Summary

| Test | Expected behavior | Result |
| --- | --- | --- |
| Positive CV + job comparison | Skill fires and creates a gap-based mini-project | PASS |
| General Docker project request | Skill stays dormant | PASS |
| Formal/non-project requirements | Selects a project-demonstrable technical gap | PASS |
| Required/preferred + alternatives | Preserves job requirement semantics | PASS |
| No technical evidence gap | Does not invent a gap or unnecessary project | PASS |

The skill fires on its intended repeated task and stays dormant on a close but
incorrect request.
