---
name: go
description: Implement or review Go programs, services, CLIs, and concurrency using idiomatic Go patterns.
---

# Go

- Follow the module's Go version, package boundaries, formatting, and existing error conventions.
- Return errors with enough operation context; wrap with `%w` when callers need to inspect the cause. Do not panic for ordinary input or I/O failures.
- Keep interfaces small and define them near consumers. Prefer concrete types until substitution is needed.
- Pass `context.Context` through request-scoped I/O and honor cancellation. Bound goroutines and protect shared state explicitly.
- Make ownership and resource cleanup clear with `defer` close patterns and deterministic shutdown.
- Use standard library packages when they solve the problem cleanly; add dependencies only for a concrete benefit.
