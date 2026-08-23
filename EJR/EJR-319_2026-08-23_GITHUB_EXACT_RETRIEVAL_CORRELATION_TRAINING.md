# EJR-319 — GitHub Exact Retrieval / Cross-Search Correlation Training

Date: 2026-08-23
Status: COMPLETED / SESSION TRAINING RECORD
Protocol: GOV-017 + CELM-001
Parent knowledge: EJR-317 / EJR-318

## Objective

Train the connector on the transition from search discovery to exact object retrieval, and distinguish normalized connector output from provider-backed object state. Also record operational learning from a malformed training call.

This cycle remains independent of P6 execution evidence.

## GT-012A — Search → exact issue retrieval

Discovery operation:
`search_issues(query="GT-012", repository="Sangaa/ARGO-KOP", topn=10, sort="updated", order="desc")`

Observed candidate:
`issue #26 — GT-012 training probe: isolated GitHub mutation safety and rollback evidence`

Exact retrieval:
`fetch_issue(issue_number=26, repository_full_name="Sangaa/ARGO-KOP")`

Observed exact object state:
- state: `closed`
- state_reason: `completed`
- comments: `0`
- created_at: `2026-08-23T07:25:23Z`
- closed_at: `2026-08-23T07:25:31Z`
- body explicitly defines the artifact as controlled connector training and specifies CREATE → READ-BACK → VERIFY → CLEANUP.

Learning:

`search_issues` can discover a candidate identity, while `fetch_issue` supplies exact issue-level state and lifecycle metadata. Search output must not be treated as a substitute for exact retrieval when authoritative object state is required.

## GT-012B — Exact object → discussion surface

Operation:
`fetch_issue_comments(issue #26)`

Observed: empty comments list.

Learning:

The exact issue object has zero top-level issue comments according to the comments surface. This does not by itself prove absence of all activity in every possible GitHub surface.

Evidence classification:
`OBJECT-LEVEL STATE` + `DISCUSSION-SURFACE OBSERVATION`

## GT-012C — Cross-operation correlation

Correlation chain:

`Search candidate → exact issue identity → exact lifecycle state → comments surface`

Reusable rule:

`Discovery identifies candidates; exact retrieval establishes object state; subordinate surfaces establish scoped details.`

No single operation is assumed to contain all evidence.

## GT-012D — Existing isolated mutation artifact as training evidence

Issue #26 itself was created as an isolated mutation-training artifact and is now closed. Its body states that the intended lifecycle was:

`CREATE → READ-BACK → VERIFY → CLEANUP`

The current exact read confirms the final state `closed/completed`, while the artifact remains explicitly bounded away from production files, workflows, and P6.

Important distinction:

This session does not re-run the mutation. It learns from the already-existing isolated artifact to avoid unnecessary duplicate mutations. The artifact therefore serves as historical training evidence, not as a new mutation probe.

## Knowledge Delta KD-004 — Tool schema is itself behavioral evidence

During the initial GT-012 search call, `search_issues` rejected `state="all"` because the exposed callable schema accepts only `open`, `closed`, or null.

A corrected call without the unsupported state value succeeded and returned issue #26.

Classification:
`NEW OBSERVATION` + `SESSION EXPOSURE LIMITATION`

Learning:

The provider's broader query semantics must not be assumed to equal the current connector operation schema. Tool validation behavior is part of the observable connector contract.

Reusable rule:
`Before invoking an operation, inspect the callable schema; after rejection, classify the failure against the exposed schema before attributing it to the provider.`

## Knowledge Delta KD-005 — Exact retrieval is narrower than search

Classification:
`NEW OBSERVATION`

Observed:
Search returned a normalized candidate; exact retrieval exposed authoritative issue fields including lifecycle timestamps, state reason, and full training-artifact body.

Reusable rule:
`Search answers “which objects may match?”; exact retrieval answers “what is the state of this identified object?”`

## Behavioral laws added

64. Search-to-object workflows should use an explicit candidate identity handoff.
65. Exact retrieval is preferred when object-level state is required.
66. Subordinate surfaces such as comments remain independently scoped evidence.
67. Existing isolated artifacts should be reused for learning before creating duplicate mutations.
68. Connector schema validation is itself observable behavior and must be recorded when it changes the interpretation of a call.
69. A provider query feature must not be assumed to exist in the session-exposed operation schema.
70. A rejected call is not automatically a provider failure; first classify whether the input violates the connector's exposed contract.

## Safety / P6 boundary

- No production ARGO file was mutated by this training cycle.
- No workflow was changed.
- No P6 execution claim was made.
- Existing Issue #26 was used as a bounded historical training artifact; it was not reopened or mutated.

## Next task

`GT-013 — Study repository/Git object correlation: issue/PR identity → commit SHA → file/blob evidence, including exact ref-bound reads and comparison semantics. Then record any Knowledge Deltas.`

P6 remains a later capability-mapping/application phase.
