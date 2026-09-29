---
name: codebase-analysis
description: Analyze a repository's architecture, quality, security, and validation when the user asks for a broad codebase assessment.
---

# Codebase analysis

For a broad repository audit, split independent read-only work across the available `codebase-explorer`, `quality-reviewer`, and `security-reviewer` agents when they are configured and the extra cost is justified. Add `test-analyst` when coverage is a central question. For a small or narrow question, analyze directly.

- Define the audit scope and inspect repository guidance before delegating.
- Ask agents for evidence with file/line references and prohibit edits. Keep each assignment narrow to reduce duplicated scanning.
- Reconcile findings against the source yourself. Remove duplicates and reject unsupported claims.
- Report an architecture map, the highest-impact verified findings, strengths relevant to the question, and important unknowns. Do not imply that every file or vulnerability was exhaustively verified.
