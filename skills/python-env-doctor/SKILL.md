---
name: python-env-doctor
description: "Use when the user asks to fix Python version mismatches, missing virtual environments, failed activation, pip packages installed in the wrong interpreter, or VS Code selecting the wrong Python. Does NOT fire on: syntax errors, regular code bugs, or Python lessons."
---

# Python Environment Doctor

Help developers identify and fix Python environment
configuration problems safely.

## When to use this

Fires when the user asks to:
- Fix an incorrect Python version.
- Find or activate a missing virtual environment.
- Fix ModuleNotFoundError caused by environment mismatch.
- Resolve pip installing into the wrong environment.
- Fix VS Code using the wrong Python interpreter.
- Resolve Python executable path errors.

**Does NOT fire on:**
- Python syntax errors or ordinary application bugs.
- Requests to explain Python concepts.
- Code refactoring or optimization.
- General programming questions.

## Steps

1. Identify the operating system, terminal,
   required Python version, and reported error.

2. Request relevant diagnostic output.
   Use commands appropriate to the user's system:
   - `python --version`
   - `python -m pip --version`
   - `Get-Command python` (PowerShell)
   - `py -0p` (Windows with Python launcher)
   - `command -v python3` (Linux/macOS)

3. Analyze the results and identify possible
   causes of the environment problem.

4. Recommend the smallest safe fix.
   Prefer existing compatible environments.
   Use explicit Python paths when appropriate.

5. Ask the user to verify the solution
   by rerunning the failing command.

6. Explain the cause, recommended fix,
   and expected result in simple language.

## Rules

- Never invent file paths or Python versions.
- Never delete environments without user approval.
- Never modify system PATH automatically.
- Prefer `python -m pip` over standalone `pip`.
- Never request API keys or passwords.
- Do not claim a problem is fixed without evidence.
- Clearly distinguish confirmed and possible causes.
- Provide commands appropriate to the user's shell.
