# Evidence — `bug-report-triager`

**Tested on:** Windows · Python 3.12 · **Date:** 2026-09-19

---

## 1. It fired when it should

**What I typed:**

```text
Turn these notes into a bug report for the PC shop. On Windows 11 with an NVIDIA RTX 5060 Ti and driver 581.29, I started Total War: Warhammer III and loaded a campaign. The screen turned black while game audio continued, the case fans went to maximum speed, and I had to reboot. I expected the game to remain visible and responsive. Event Viewer recorded nvlddmkm Event ID 153 and WHEA-Logger Event ID 17. There is no workaround.
```

**Actual routing and execution transcript:**

```text
REQUEST  Turn these notes into a bug report for the PC shop. On Windows 11 with an NVIDIA RTX 5060 Ti and driver 581.29, I started Total War: Warhammer III and loaded a campaign. The screen turned black while game audio continued, the case fans went to maximum speed, and I had to reboot. I expected the game to remain visible and responsive. Event Viewer recorded nvlddmkm Event ID 153 and WHEA-Logger Event ID 17. There is no workaround.
SKILLS   4 on disk: bug-report-triager, jhf-brief, lab-grader, repo-onboarder
ROUTED   bug-report-triager

  -> run_script({'script_name': 'triage_bug_report.py', 'stdin_text': '{"raw...)
  -> save_output({'filename': 'bug-report.md', 'content': '# Bug Report\n\n- ...)
```

**Result produced by the skill:**

```text
# Bug Report

- Component: graphics-display (matched keyword: screen)
- Severity: S2 - High — crash/restart or a core function is unusable with no workaround; matched: reboot
- Environment: Windows 11 with an NVIDIA RTX 5060 Ti and driver 581.29
- Version: driver 581.29

Steps to reproduce
1. start Total War: Warhammer III and load a campaign

Expected result
the game to remain visible and responsive

Actual result
The screen turned black while game audio continued, the case fans went to maximum speed, and I had to reboot.

Impact
The game crashes and requires a reboot.

Workaround
There is no workaround.

Please provide
- Nothing else required for initial triage.
```

**Did it activate on its own?** Yes. The runner selected
`bug-report-triager`, called its deterministic script, and saved
`bug-report.md` without the skill being named explicitly in the request.

---

## 2. It stayed quiet when it should

**What I typed:**

```text
Explain what nvlddmkm Event ID 153 means and help me fix the crash.
```

**Actual routing transcript:**

```text
REQUEST  Explain what nvlddmkm Event ID 153 means and help me fix the crash.
SKILLS   4 on disk: bug-report-triager, jhf-brief, lab-grader, repo-onboarder
ROUTED   NO_SKILL — answering directly
```

This is a meaningful near-miss: it contains an error code and a crash, like the
positive case, but asks for diagnosis and repair rather than creation of a bug
report. The skill correctly stayed dormant.

---

## 3. What it cost

### Positive routing run

```text
skills on disk .............. 4
menu shown to the router .... ~329 tokens
if we had loaded ALL of them. ~2,229 tokens
we actually loaded .......... ~748 tokens (bug-report-triager)
SAVED ....................... ~1,481 tokens
```

### Near-miss run

```text
skills on disk .............. 4
menu shown to the router .... ~329 tokens
if we had loaded ALL of them. ~2,229 tokens
we actually loaded .......... ~0 tokens (nothing)
SAVED ....................... ~2,229 tokens
```

---

## 4. Anything a reviewer should know

- **Known limitation:** severity is intentionally conservative and keyword
  based. Ambiguous impact stays `Unassigned` instead of being guessed.
- **Needs an API key / network:** the deterministic script does not; the JHF
  runner needs `OPENROUTER_API_KEY` for automatic routing.
- **What surprised me:** requiring exact source quotes makes unsupported fields
  disappear automatically, which is safer than relying only on a “do not
  invent” instruction.
