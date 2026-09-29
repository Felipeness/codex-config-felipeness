---
name: refactoring
description: Improve code structure while preserving observable behavior and keeping the refactor within the requested scope.
---

# Refactoring

- Identify the specific maintenance problem and the behavior that must remain stable.
- Read callers, tests, public interfaces, and local conventions before moving boundaries.
- Prefer incremental transformations with clear checkpoints. Avoid bundling unrelated cleanup or new behavior.
- Preserve error semantics, timing, ordering, and side effects unless the task explicitly changes them.
- Choose targeted validation from the existing project workflow when requested. Summarize the structural improvement and any behavior you could not verify.
