---
name: review-staged
description: Review only changes in the Git index and report actionable findings without modifying the worktree.
---

# Review staged changes

- Inspect `git diff --cached` and the relevant surrounding code. Do not include unstaged or untracked changes in the review.
- If the staged diff is empty, report that and stop rather than reviewing a broader diff.
- Check correctness, security, regression risk, and whether important behavior is unverified. Keep comments tied to staged lines where possible.
- Return findings by severity with file and line references. Make no edits and do not stage, unstage, commit, or run tests.
