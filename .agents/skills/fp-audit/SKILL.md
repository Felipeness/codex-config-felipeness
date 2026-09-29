---
name: fp-audit
description: Audit a function or change for referential transparency, mutation, idempotency, parsing boundaries, and effect isolation.
---

# Functional programming audit

Trace the requested code path and report concrete places where hidden state or side effects make behavior hard to reason about.

- Identify which functions are pure and which depend on I/O, time, randomness, or shared state.
- Check whether external values are parsed into validated domain types before business logic uses them.
- Look for unsafe mutation, non-idempotent retries, duplicated decisions, and partial state changes.
- Suggest the smallest improvement that materially helps correctness or testability. Avoid converting straightforward imperative code into a functional abstraction without a clear benefit.
- Include file and line references. Do not edit unless the user asks for a fix.
