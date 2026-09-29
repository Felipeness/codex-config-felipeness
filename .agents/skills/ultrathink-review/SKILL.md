---
name: ultrathink-review
description: Perform a deep design and code review using SOLID, DRY, KISS, YAGNI, CUPID, and defensive programming as diagnostic lenses.
---

# Deep review

Review the requested diff or subsystem without editing files. Use design principles as questions, not as a scorecard:

- **Correctness and safety:** Can invalid input, partial failure, concurrency, or retries corrupt behavior or data?
- **Cohesion and dependencies:** Do modules have clear responsibilities and stable boundaries? Are interfaces narrower than implementations?
- **Clarity:** Are names, state transitions, and error paths easy to follow? Is there avoidable indirection or duplicated policy?
- **Scope and performance:** Is the change doing more than the requirement needs? Is any complexity justified by a real scale or latency constraint?
- **Changeability:** Does the design make the next likely change safe without building an unnecessary framework?

Report only concrete findings, ordered by impact, with file/line and consequences. Put lower-confidence design questions in a separate short section. If a principle does not reveal a defect, do not invent one to fill a category.
