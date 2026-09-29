---
name: code-review
description: Review a diff or code path for concrete correctness, security, regression, and validation risks without changing files by default.
---

# Code review

Review the requested scope without editing it unless the user also asks for fixes.

1. Read the diff and surrounding code; trace affected paths far enough to understand actual behavior.
2. Look for correctness and data-loss risks first, then authorization/input handling, failure behavior, performance, accessibility, and maintainability where relevant.
3. Verify each suspected issue against code or a reproducible path. Do not report a hypothetical concern as a finding.
4. Return findings from highest severity to lowest. Include file and line, impact, and a concise explanation. If there are no findings, say so and mention the main remaining uncertainty.

Keep style preferences separate from defects. Do not run tests or mutate state as part of a read-only review unless the user requests it.
