---
name: observability
description: Add or improve logs, metrics, tracing, and error reporting for services and background jobs.
---

# Observability

- Begin with the failure or operational question the team needs to answer. Choose signals that can answer it.
- Use structured logs with stable fields and useful operation context. Never log credentials, tokens, or sensitive request bodies.
- Add metrics for rates, errors, latency, and saturation where an aggregate signal helps. Use bounded-cardinality labels.
- Propagate trace and request identifiers across service boundaries when the stack supports it.
- Preserve original errors and include recovery context. Avoid duplicate logs at every layer.
- Keep telemetry non-blocking or bounded so an observability outage does not become an application outage.
- Follow existing instrumentation libraries and naming conventions instead of adding a competing stack.
