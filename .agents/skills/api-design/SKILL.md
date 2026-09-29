---
name: api-design
description: Design or review HTTP APIs, webhooks, and service contracts where compatibility, validation, retries, or idempotency matter.
---

# API and webhook design

- Start from the consumer's task and existing versioning and naming conventions. Keep resource names and response shapes consistent.
- Validate untrusted input at the boundary and return stable, actionable error codes without exposing internals.
- Define authentication and authorization separately. Enforce access at the resource/action boundary, not only in the UI.
- Make retry behavior explicit. Use idempotency keys or naturally idempotent operations for effects that clients may repeat.
- Set limits and timeouts for request bodies, downstream calls, and fan-out. Propagate cancellation.
- Document compatibility expectations, pagination, rate limits, and webhook signature/replay handling when relevant.
- Add observability that identifies a request without logging secrets or unnecessary personal data.
