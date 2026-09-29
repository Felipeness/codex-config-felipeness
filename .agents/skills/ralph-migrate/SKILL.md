---
name: ralph-migrate
description: Plan and execute a migration in reviewable increments with explicit compatibility and rollback constraints.
---

# Iterative migration

- Map the current and target formats, data owners, consumers, and compatibility window.
- Define a safe checkpoint and rollback path for each consequential step before applying it.
- Migrate a narrow slice, inspect the result, and reconcile data or references before continuing.
- Stop after six meaningful passes, at the agreed completion condition, or if rollback assumptions fail. Do not run destructive production steps or publish without explicit authorization.
