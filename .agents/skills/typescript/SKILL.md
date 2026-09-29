---
name: typescript
description: Write or review TypeScript and JavaScript with the project's type system, runtime, and framework conventions.
---

# TypeScript and JavaScript

- Inspect the existing compiler, lint, and module settings before choosing syntax or introducing a dependency.
- Prefer precise types, discriminated unions, and control-flow narrowing. Avoid `any`; isolate unavoidable untyped boundaries and validate external data at runtime.
- Keep public interfaces explicit. Prefer named exports unless the surrounding framework convention calls for a default export.
- Use `async`/`await` for sequential asynchronous work. Handle rejected promises and cancellation where the operation can outlive its caller.
- Avoid hidden mutation and magic strings in shared logic. Add an enum or constant only when it clarifies a real domain concept.
- Reuse the repository's test and validation commands when the task calls for verification.
