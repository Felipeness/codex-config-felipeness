---
name: react
description: Implement or review React and Next.js interfaces, components, hooks, and data flows using the conventions already present in the project.
---

# React and Next.js

- Inspect the framework version and existing component patterns first. In Next.js, keep server rendering as the default and add client boundaries only for browser state or interaction.
- Keep components focused on one UI responsibility. Move domain rules into named functions or hooks when that makes behavior easier to test and reuse.
- Follow the project's established data-fetching and cache library; do not add React Query or another package just because it is familiar.
- Model loading, empty, error, and success states. Clean up subscriptions, timers, and event listeners.
- Use semantic HTML, keyboard-accessible controls, visible focus, and labels. Check responsive behavior and contrast when changing visual UI.
- Prefer stable keys and derived state over redundant state. Add error boundaries where a local failure should not take down the whole interface.
