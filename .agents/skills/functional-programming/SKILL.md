---
name: functional-programming
description: Use functional programming techniques to make business rules, transformations, and asynchronous flows predictable and testable.
---

# Functional programming

- Separate pure decisions from I/O. Keep network, storage, clock, and process access at explicit boundaries.
- Prefer immutable inputs and return new values when mutation would obscure ownership or make retries unsafe.
- Compose small transformations; avoid a generic pipeline abstraction when named sequential steps are clearer.
- Parse and validate untrusted values into domain types once, then keep downstream functions total over those types.
- Make retryable effects idempotent or guard them with an explicit key/state transition.
- Use short-circuiting and early returns to keep preconditions visible. Avoid clever chains that hide errors or evaluation order.
- Apply these techniques selectively; local mutation can be clearer for simple, owned data.
