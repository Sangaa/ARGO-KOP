# EJR-317 — GitHub Connector Self-Training

Date: 2026-08-23
Status: IN PROGRESS
Protocol: GOV-017
Primary objective: train HERMUZ on the active GitHub connector before further P6 planning.

## Current completed training

The training record has now reached GT-007E. Training remains read-first and evidence-scoped.

### GT-007E — Pull Request review/discussion surfaces
Operations: `list_pull_request_reviews`, `list_pull_request_review_threads`, `fetch_pr_comments`
Target: `Sangaa/ARGO-KOP#25`

Hypothesis: PR review submissions, inline review threads, and conversation comments are separate observation surfaces and may provide lineage evidence that is not present in PR metadata or diff/patch output.

Observed behavior:
- `list_pull_request_reviews` returned `reviews=[]`.
- `list_pull_request_review_threads` returned `review_threads=[]`.
- `fetch_pr_comments` returned `comments=[]`.

Interpretation:
1. The connector exposes three distinct read surfaces for PR review/discussion evidence.
2. An empty result across all three surfaces for PR #25 means no review submissions, inline review threads, or PR comments were returned through those operations at the time of the probe.
3. This does not prove that no workflow execution occurred.
4. Review/discussion surfaces are useful for corroborating human/PR process lineage, but they are not authoritative Actions execution evidence by themselves.

Additional boundary probe:
- `update_review_comment` with a deliberately nonexistent comment ID returned HTTP 404 / Not Found.
- This was a non-mutating negative probe because the target identifier was fabricated and no existing resource could be modified.

Interpretation of negative probe:
- The operation is exposed to the session.
- The connector reaches GitHub and returns a resource-level Not Found rather than an exposure-level "operation unavailable" error.
- Therefore operation exposure and resource existence are distinguishable in this surface.
- No write to an existing review comment was performed.

Reuse rule:
`PR metadata → reviews → review threads → comments → commit/Actions correlation`.
For write operations, never use a fabricated ID against a real resource; only bounded negative probes with guaranteed nonexistent identifiers are permitted during connector training.

Training classification: READ + SAFE-NEGATIVE-BOUNDARY + PR-LINEAGE + EVIDENCE-CLASSIFICATION.
Canonical mutation involved: NO.

## Behavioral laws added by GT-007E

17. Review submissions, review threads, and PR conversation comments are distinct evidence surfaces.
18. Empty review surfaces are scoped observations, not execution-absence evidence.
19. A resource-level 404 from an exposed operation is evidence that the operation reached the provider/resource lookup layer; it is not evidence that the operation is unavailable.
20. Connector self-training must avoid mutations to real resources; safe negative identifiers can test error classification without changing repository state.

## Next task

`GT-007F — Train repository Git-object surfaces: refs, blobs/trees, and commit lineage, then correlate the result with PR head/base identity.`

Required order:
`Inventory → safe read-only training → evidence classification → update EJR → derive P6 evidence plan → smallest justified probe → document → close session.`

No P6 promotion is authorized by this record.

## Model handoff

Every future model/session must read GOV-017 and EJR-317 before connector-dependent work, reuse validated observations, and perform freshness checks only where needed.
