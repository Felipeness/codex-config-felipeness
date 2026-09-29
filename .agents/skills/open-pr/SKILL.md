---
name: open-pr
description: Prepare and, when requested, create a GitHub pull request with a clear summary and accurate verification notes.
---

# Open a pull request

- Inspect branch status, base branch, commits, and the complete diff. Confirm the change is coherent and identify any missing issue or Jira link.
- Draft a concise title and body covering behavior, rationale, risks, and only the validation actually completed.
- Do not create a commit just to satisfy this workflow unless the user requests it or the repository explicitly requires it.
- A direct user request to open/create the PR authorizes pushing the branch and creating that PR. If the request is only to draft or review, return the title and body without publishing.
- After creation, report the PR URL and any setup or validation steps still needed.
