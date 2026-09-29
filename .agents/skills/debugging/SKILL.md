---
name: debugging
description: Investigate a bug or unexpected behavior, find its root cause, and implement a focused fix when requested.
---

# Debugging

- Capture the exact observed behavior and expected behavior. Reproduce it from available logs, code, or a minimal scenario before changing anything when practical.
- Trace inputs through the relevant path and distinguish the first incorrect state from later symptoms.
- Form and test one focused hypothesis at a time. Prefer instrumentation or a minimal reproduction over unrelated edits.
- Fix the cause with the smallest coherent change. Preserve adjacent behavior and explain any assumptions.
- Run only verification appropriate to the user's request and the repository's established workflow. Add a regression test when asked or required by the acceptance criteria.
- Report root cause, change, evidence, and remaining uncertainty.
