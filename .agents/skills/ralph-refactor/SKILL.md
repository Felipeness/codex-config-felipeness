---
name: ralph-refactor
description: Apply a requested refactor in small behavior-preserving steps and stop at a defined completion condition.
---

# Iterative refactoring

Use `$refactoring` to set invariants and choose small transformations. After each step, inspect the diff and compare it with the stated goal. Continue only while a concrete gap remains; stop after six meaningful passes or at a blocker. Verify only as requested or required by acceptance criteria, and report any unverified behavior.
