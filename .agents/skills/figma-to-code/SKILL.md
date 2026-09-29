---
name: figma-to-code
description: Turn a Figma frame or design reference into a repository-native UI while preserving its visual hierarchy and behavior.
---

# Figma to code

1. Inspect the requested frame and gather measurements, assets, typography, color, spacing, and responsive behavior before implementing.
2. Check the repository's design tokens and components. Reuse them where they match; call out genuine mismatches rather than silently inventing a parallel system.
3. Map the visual hierarchy and interactions to semantic components. Keep responsive states, loading/empty states, and accessibility in scope.
4. Implement in small sections and compare against the reference with available browser or screenshot tooling. Fix measured differences before polishing unrelated areas.
5. Use Figma or browser MCP tools only if they are connected. If the reference is inaccessible, ask for a screenshot or exported details instead of guessing.
