# EJR-318 — GitHub Search / Filtering Training

Date: 2026-08-23
Status: COMPLETED / SESSION TRAINING RECORD
Protocol: GOV-017 + CELM-001
Parent knowledge: EJR-317

## Objective

Train the active GitHub connector on issue/search semantics, filtering, sorting, result limits, and the boundary between search discovery and authoritative state.

This training is deliberately independent of P6 execution evidence.

## GT-011A — State filtering

Operation: `search_issues`

Query: `connector`
Repository: `Sangaa/ARGO-KOP`

Two controlled read-only searches were executed with identical repository/query scope but different state filters:

- `state=open`, `sort=updated`, `order=desc`, `topn=10`
- `state=closed`, `sort=updated`, `order=asc`, `topn=10`

Observed:

- The open query returned open issues matching `connector`, including #21, #17, and #11.
- The closed query returned the closed training issue #26.
- The result sets therefore changed materially when the state filter changed.

Learning:

`search_issues` is a filtered discovery surface. Its output is a function of query + repository scope + state + sort/order + result limit. A missing item from one filtered result cannot establish global absence.

## GT-011B — Result-limit behavior

Operation: `search_issues`

Query: `P6`
Repository: `Sangaa/ARGO-KOP`

Input: `state=open`, `sort=created`, `order=asc`, `topn=2`.

Observed:

- Exactly two matching results were returned: #11 and #15.
- The connector accepted the requested result limit and returned a bounded result set.

Learning:

A bounded result set is not a complete inventory unless the connector contract guarantees completeness for the requested limit. `topn` must therefore be treated as an observation-window parameter, not as a proof that no additional matches exist.

## GT-011C — Search semantics vs exact state

The same issue can appear in a search result and later be inspected through an exact operation such as `get_pr_info` or an issue-specific read operation.

Reuse rule:

`Search → candidate identity → exact retrieval → evidence classification`

Search should normally provide candidate discovery; exact retrieval should provide authoritative object-level evidence where available.

## GT-011D — Pagination / exposure boundary

The exposed `search_issues` session operation does not expose an explicit page number or opaque cursor parameter. Therefore the current session cannot claim direct control over search pagination from this operation.

This must be distinguished from provider capability or connector-internal pagination. The operation may internally handle pagination, but that behavior was not independently observed in this training.

Classification:

`SESSION EXPOSURE LIMITATION / UNRESOLVED INTERNAL PAGINATION`

No conclusion is made that GitHub lacks pagination, nor that the connector cannot paginate internally.

## GT-011E — Cross-operation search coverage

`search_commits` exposes an explicit `topn` parameter but no explicit page/cursor parameter in the current callable surface. A recent-commit listing for `Sangaa/ARGO-KOP` returned the newest commits in descending committer-date order.

Learning:

Different search families expose different controls. ARGO must inspect each operation's callable contract instead of assuming uniform pagination/filtering semantics across the provider.

## Knowledge Delta KD-002 — Search result absence is scoped

Classification: `NEW OBSERVATION` + `CONNECTOR LIMITATION`

Previous model:

Search could be treated as a broad repository inventory when repository scope was supplied.

Observed:

State filters, sort order, and `topn` materially constrain the returned observation window, while explicit pagination controls are not exposed on the issue-search operation.

New reusable rule:

`A search result is an observation window defined by its query and exposed controls. Absence from that window is not global absence unless completeness is established.`

## Knowledge Delta KD-003 — Pagination cannot be inferred from provider API knowledge

Classification: `NEW OBSERVATION` + `SESSION LIMITATION` + `UNRESOLVED`

Observed:

The callable issue-search contract has no explicit page/cursor argument.

Boundary:

This proves only the current session-exposed contract, not the provider's underlying pagination capability or the connector's internal implementation.

Reusable rule:

`Provider pagination capability ≠ connector pagination implementation ≠ session pagination controls.`

## Behavioral laws added

57. Search is an observation window, not automatically a complete inventory.
58. Query filters, state, sorting, ordering, and result limits are part of evidence semantics.
59. `topn` defines a bounded observation window unless completeness is separately established.
60. Search absence must not be generalized beyond the filter scope used.
61. Pagination controls must be learned from the exposed operation contract, not assumed from provider API knowledge.
62. Lack of a page/cursor parameter proves a session exposure fact, not provider incapability.
63. Different search families may expose different filtering and pagination controls and must be trained independently.

## Training safety

No repository production file, workflow, branch, PR, or issue state was mutated during this training cycle.

## Next task

`GT-012 — Train issue/PR exact-object retrieval and cross-search correlation, then study the connector's mutation/read-back boundary only where an isolated reversible training artifact is already available.`

P6 remains an application phase and is not promoted by this record.
