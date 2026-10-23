# Evidence — `python-bug-triage`

> This file uses only recorded observations from the original Bootcamp test session and the earlier supplied transcript excerpts. When the complete raw transcript was not available in this workspace, the excerpt below is kept intentionally partial and labeled as such. No terminal logs were fabricated or rerun for this update.

**Tested on:** Windows 11 · Python 3.12 · JHF skill runner · **Date:** 2026-10-23

---

## 1. It fired when it should

**What the user typed (recorded excerpt):**

```text
Triage this Python bug: AttributeError NoneType object has no attribute get. My AI agent crashes when processing a JSON response. Classify the severity and identify missing information.
```

**Recorded routing and tool trace excerpt:**

```text
ROUTED: python-bug-triage
Tools: read_resource, run_script, save_output
```

**Recorded answer excerpt:**

```text
Severity SEV1; likely component agent; missing expected result, actual result, reproduction steps, version/environment.
```

**Recorded progressive disclosure excerpt:**

```text
Progressive disclosure: 4 skills, menu ~291 tokens, all bodies ~1885 tokens, loaded ~404 tokens, saved ~1481 tokens.
```

**Did it activate on its own?** Yes. The session record shows the skill routed to `python-bug-triage` without the skill name being included in the request.

> Note: this is a genuine excerpt from the recorded session, not a reconstructed full transcript. Any omitted lines are intentionally left out rather than guessed.

---

## 2. It stayed quiet when it should

**A near-miss the user typed (recorded excerpt):**

```text
Explain this Python repository to a newcomer and show how to run it.
```

**Recorded routing excerpt:**

```text
ROUTED: repo-onboarder, not python-bug-triage
Tools: run_script, save_output
Loaded ~427 tokens, saved ~1458 tokens.
```

**Did it stay dormant?** Yes.

**Why this one is a real test:** It is close to a Python / repo-help request, but it asks for repository onboarding and run instructions rather than Python bug triage, severity classification, or missing-information triage. The routing record specifically identifies `repo-onboarder`, not `python-bug-triage`.

---

## 3. What it cost

| | Tokens (approx.) |
|---|---|
| Description in the menu (always loaded) | ~291 |
| Body, once it fired | ~1885 |
| What stayed on disk because it did not fire | ~404 |
| Saved by progressive disclosure | ~1481 |

**Confirmed from the recorded session:**

```text
4 skills, menu ~291 tokens, all bodies ~1885 tokens, loaded ~404 tokens, saved ~1481 tokens.
```

**Near-miss comparison from the recorded session:**

```text
Loaded ~427 tokens, saved ~1458 tokens.
```

---

## 4. Anything a reviewer should know

- The complete raw runner transcript is not preserved in this repository; the evidence here intentionally uses only the exact recorded excerpts already available from the original session and prior supplied observations.
- Known limitation: this skill is intentionally narrow; it does not claim root cause or invent missing evidence when a bug report is under-specified.
- Needs an API key / network: yes for the JHF runner to auto-route, but the deterministic script itself does not require an outbound network call to function.
- The adversarial near-miss shows the skill is domain-sensitive: a general “explain this Python repo” request routes elsewhere and does not trigger this triage skill.
- No API keys, credentials, personal paths, or sensitive information were added to this evidence file.
