---
name: ralph-review
description: Review changes, address requested blocking findings, and repeat a bounded review until the result is clear.
---

# Iterative review

Review with `$code-review` or `$ultrathink-review`, depending on the requested depth. Fix findings only when the user asked for remediation. Re-review the changed paths after a fix, up to six meaningful passes, then stop when no blocking findings remain or report the remaining blocker. Do not expand into unrelated refactoring or publish the branch without a request.
