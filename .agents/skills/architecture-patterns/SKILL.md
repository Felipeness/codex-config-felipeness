---
name: architecture-patterns
description: Compare architectural options for system boundaries, migrations, reliability, and distributed workflows.
---

# Architecture patterns

Choose the simplest shape that satisfies known constraints. State the tradeoffs and the signals that would justify a more complex pattern.

- Use modular monolith or vertical slices when a single deployable still gives clear ownership and low operational cost.
- Consider CQRS or event sourcing only when distinct read/write needs or audit history justify the extra consistency and operational work.
- Use a saga for business transactions across independently committed services; define retries, idempotency, compensation limits, and observability.
- Use a circuit breaker or bulkhead when a failing dependency can exhaust shared resources or spread an outage.
- For gradual replacement, map the existing boundary and route one behavior at a time (Strangler Fig); preserve rollback and data reconciliation.
- Treat bounded contexts and team ownership as design constraints. Do not split services solely to match a diagram or organizational fashion.
- For systems of systems, identify which units must remain autonomous and which shared invariants require coordination.
