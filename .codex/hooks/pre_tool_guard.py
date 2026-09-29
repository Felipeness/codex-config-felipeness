#!/usr/bin/env python3
"""Block a small set of shell commands with a high risk of data loss."""

from __future__ import annotations

import json
import re
import sys


RULES = (
    (
        "git reset --hard",
        re.compile(r"\bgit\s+(?:-[Cc]\s+\S+\s+)?reset\s+[^\n;&|]*--hard\b", re.I),
    ),
    (
        "git clean with force",
        re.compile(
            r"\bgit\s+(?:-[Cc]\s+\S+\s+)?clean\s+[^\n;&|]*(?:-[a-z]*f[a-z]*\b|--force\b)",
            re.I,
        ),
    ),
    (
        "git force push",
        re.compile(
            r"\bgit\s+(?:-[Cc]\s+\S+\s+)?push\s+[^\n;&|]*(?:--force(?:-with-lease)?\b|\s-f(?:\s|$))",
            re.I,
        ),
    ),
    (
        "forced branch deletion",
        re.compile(r"\bgit\s+(?:-[Cc]\s+\S+\s+)?branch\s+[^\n;&|]*\s-D\s", re.I),
    ),
    (
        "recursive deletion of a filesystem root",
        re.compile(
            r"\brm\s+-(?:[a-z]*r[a-z]*f[a-z]*|[a-z]*f[a-z]*r[a-z]*)\s+(?:--no-preserve-root\s+)?/(?:\s|\*|$)",
            re.I,
        ),
    ),
    ("download piped directly to a shell", re.compile(r"\b(?:curl|wget)\b[^\n;]*\|\s*(?:ba)?sh\b", re.I)),
    (
        "raw disk formatting or overwrite",
        re.compile(r"(?<!\w)(?:mkfs(?:\.\w+)?\b|dd\s+if=|format\s+[a-z]:)", re.I),
    ),
)


def read_command() -> str:
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return ""
    tool_input = event.get("tool_input", {})
    if not isinstance(tool_input, dict):
        return ""
    command = tool_input.get("command", "")
    return command if isinstance(command, str) else ""


def main() -> None:
    command = read_command()
    matches = [label for label, pattern in RULES if pattern.search(command)]
    if not matches:
        return

    reason = "Blocked high-risk shell operation: " + ", ".join(matches)
    response = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                reason
                + ". Review the exact command and edit or disable this optional guard if the operation is intentional."
            ),
        }
    }
    print(json.dumps(response))


if __name__ == "__main__":
    main()
