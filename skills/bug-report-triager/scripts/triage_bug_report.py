#!/usr/bin/env python3
"""Validate evidence and format a raw problem report as a bug report.

Input is one JSON object on stdin. Extracted fields must contain both a value
and an exact quote from raw_report. Unsupported fields are rejected and become
missing information rather than silently entering the final report.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any


REQUIRED_FIELDS = ("environment", "version", "expected", "actual", "steps")
OPTIONAL_FIELDS = ("impact", "workaround")

COMPONENT_RULES = (
    ("graphics-display", ("gpu", "graphics", "display", "screen", "nvidia", "amd", "nvlddmkm", "directx")),
    ("authentication", ("login", "log in", "sign in", "authentication", "password", "oauth", "token")),
    ("networking", ("network", "wifi", "wi-fi", "ethernet", "dns", "socket", "connection", "timeout")),
    ("data-storage", ("database", "sql", "firestore", "storage", "data loss", "corrupt")),
    ("user-interface", ("button", "menu", "layout", "dialog", "page", "form", "ui")),
    ("performance", ("slow", "latency", "freeze", "hang", "memory", "cpu")),
)

SEVERITY_RULES = (
    (
        "S1 - Critical",
        "production outage, confirmed data loss/security breach, or all users blocked",
        ("production outage", "data loss", "security breach", "all users", "everyone is blocked"),
    ),
    (
        "S2 - High",
        "crash/restart or a core function is unusable with no workaround",
        ("crash", "crashed", "restart", "reboot", "blue screen", "black screen", "unusable", "cannot continue", "no workaround"),
    ),
    (
        "S3 - Medium",
        "degraded or intermittent behavior, or a workaround exists",
        ("intermittent", "sometimes", "degraded", "slow", "workaround", "retry works"),
    ),
    (
        "S4 - Low",
        "cosmetic, wording, alignment, or documentation defect",
        ("cosmetic", "typo", "spelling", "alignment", "documentation", "wrong color"),
    ),
)


def normalized(text: str) -> str:
    return " ".join(text.casefold().split())


def supported(raw_report: str, item: Any) -> tuple[str | None, str | None]:
    if not isinstance(item, dict):
        return None, "field is not an object with value and quote"
    value = str(item.get("value", "")).strip()
    quote = str(item.get("quote", "")).strip()
    if not value:
        return None, "value is empty"
    if not quote:
        return None, "evidence quote is missing"
    if normalized(quote) not in normalized(raw_report):
        return None, f"quote not found in raw report: {quote!r}"
    return value, None


def classify_component(raw_report: str) -> tuple[str, str]:
    haystack = normalized(raw_report)
    for label, keywords in COMPONENT_RULES:
        matched = next((keyword for keyword in keywords if keyword in haystack), None)
        if matched:
            return label, f"matched keyword: {matched}"
    return "general", "no component keyword matched"


def classify_severity(raw_report: str) -> tuple[str, str]:
    haystack = normalized(raw_report)
    for label, criterion, keywords in SEVERITY_RULES:
        matched = next((keyword for keyword in keywords if keyword in haystack), None)
        if matched:
            return label, f"{criterion}; matched: {matched}"
    return "Unassigned", "insufficient impact evidence; ask the reporter for impact and workaround details"


def bullet(value: str | None) -> str:
    return value if value else "Not provided"


def validate(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON must be an object")
    raw_report = payload.get("raw_report")
    if not isinstance(raw_report, str) or not raw_report.strip():
        raise ValueError("raw_report must be a non-empty string")

    accepted: dict[str, Any] = {}
    invalid: list[str] = []

    for field in (*REQUIRED_FIELDS[:-1], *OPTIONAL_FIELDS):
        item = payload.get(field)
        if item is None:
            accepted[field] = None
            continue
        value, error = supported(raw_report, item)
        accepted[field] = value
        if error:
            invalid.append(f"{field}: {error}")

    accepted_steps: list[str] = []
    raw_steps = payload.get("steps", [])
    if raw_steps is None:
        raw_steps = []
    if not isinstance(raw_steps, list):
        invalid.append("steps: must be a list")
    else:
        for index, item in enumerate(raw_steps, start=1):
            value, error = supported(raw_report, item)
            if value:
                accepted_steps.append(value)
            if error:
                invalid.append(f"steps[{index}]: {error}")
    accepted["steps"] = accepted_steps

    missing = [field for field in REQUIRED_FIELDS[:-1] if not accepted.get(field)]
    if not accepted_steps:
        missing.append("steps")

    component, component_reason = classify_component(raw_report)
    severity, severity_reason = classify_severity(raw_report)

    lines = [
        "# Bug Report",
        "",
        f"- **Component:** `{component}` ({component_reason})",
        f"- **Severity:** **{severity}** — {severity_reason}",
        f"- **Environment:** {bullet(accepted.get('environment'))}",
        f"- **Version:** {bullet(accepted.get('version'))}",
        "",
        "## Steps to reproduce",
    ]
    if accepted_steps:
        lines.extend(f"{index}. {step}" for index, step in enumerate(accepted_steps, start=1))
    else:
        lines.append("Not provided")

    lines.extend(
        [
            "",
            "## Expected result",
            bullet(accepted.get("expected")),
            "",
            "## Actual result",
            bullet(accepted.get("actual")),
            "",
            "## Impact",
            bullet(accepted.get("impact")),
            "",
            "## Workaround",
            bullet(accepted.get("workaround")),
            "",
            "## Please provide",
        ]
    )
    requests = list(missing)
    if severity == "Unassigned":
        requests.append("impact and workaround details needed to assign severity")
    if requests:
        lines.extend(f"- {item}" for item in requests)
    else:
        lines.append("- Nothing else required for initial triage.")

    if invalid:
        lines.extend(["", "## Rejected unsupported claims"])
        lines.extend(f"- {item}" for item in invalid)

    return {
        "status": "PASS" if not invalid else "PASS_WITH_REJECTIONS",
        "component": component,
        "severity": severity,
        "severity_criterion": severity_reason,
        "missing_information": requests,
        "invalid_evidence": invalid,
        "report_markdown": "\n".join(lines) + "\n",
    }


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        result = validate(payload)
    except (json.JSONDecodeError, ValueError) as exc:
        print(json.dumps({"status": "INPUT_ERROR", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
