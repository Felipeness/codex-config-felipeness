---
name: mirror-pr
description: Prepare a mirror change from a PR targeting master to a corresponding PR targeting develop in repositories that require both branches.
---

# Mirror PR

Use only when the repository actually maintains parallel `master` and `develop` branches.

1. Inspect the source PR, target branches, merge status, and commit range.
2. Identify conflicts and ensure the mirrored change is not already present in `develop`.
3. Prepare a cherry-pick or equivalent patch from the resolved `master` result onto the correct `develop` base.
4. Review the resulting diff and draft the mirror PR title/body, preserving issue references.

Treat a direct request to mirror and open the PR as authorization to push and create it. If the user only asks for analysis or preparation, stop with a reviewable local result and do not publish.
