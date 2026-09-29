---
name: code-quality
description: Apply practical code quality principles while implementing or reviewing software; use when readability, maintainability, or design tradeoffs matter.
---

# Code quality

Use these principles as heuristics. Follow repository conventions when they serve the task, and explain meaningful exceptions.

- Optimize for clarity and low cognitive load. Prefer explicit names, one level of abstraction per function, and control flow that reads from top to bottom.
- Prefer small cohesive functions and composition. Extract a helper only when it gives a concept a useful name or removes meaningful duplication.
- Make invalid states difficult to represent. Validate at system boundaries, use precise types, and keep side effects visible.
- Handle errors at the layer that can recover or provide useful context. Do not silently swallow failures.
- Put timeouts on network and process operations. Avoid logging credentials or sensitive payloads.
- Apply KISS, YAGNI, DRY, SOLID, and CUPID to the actual constraints; none is a reason by itself to add abstraction.
- Consider complexity and data volume before optimizing. Keep performance claims tied to a measured or evident bottleneck.
