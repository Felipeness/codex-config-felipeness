---
name: pr-jira-review
description: Compare a pull request with its Jira issue and review the change against acceptance criteria when both sources are available.
---

# PR and Jira review

- Locate the PR diff and linked Jira issue from the supplied identifiers or available integrations. If one source is unavailable, state that boundary and continue with the evidence that exists.
- Compare each acceptance criterion with the changed code and identify unimplemented scope, unintended additions, and mismatches.
- Review correctness and security risks in the diff. Keep Jira compliance findings separate from code defects.
- Return concise findings with PR file/line references and links to criteria when available.
- Draft comments by default. Post or reply in GitHub/Jira only when the user explicitly requests that external action.
