# EJR-318 — GitHub Connector Self-Training: GT-010 Search, Pagination & Filtering

Date: 2026-08-23
Protocol: GOV-017
Status: COMPLETED FOR THIS TRAINING CYCLE
Training mode: capability-first, not P6-first

## Objective

Train HERMUZ on generic repository, PR, and issue search semantics, including pagination, result limits, filtering, and argument/schema boundaries, without selecting the exercise because of P6.

## GT-010A — Repository search pagination

Operation: `search_repositories`

Probe A:
`query="Sangaa/ARGO-KOP", per_page=1, page=1`

Observed:
- Exact repository `Sangaa/ARGO-KOP` was returned on page 1.
- The same response also exposed repository metadata and connector-reported permissions.

Probe B:
`query="Sangaa/ARGO-KOP", per_page=1, page=2`

Observed:
- `CO-ARGO-KOP` was returned on page 2.

Learning:
1. Search result pagination is independent from repository identity.
2. A single page is not a complete search result set when multiple matches exist.
3. `per_page` directly changes how many candidate results are observable per page.
4. Exact repository naming can still produce related-name candidates; selection must use full repository identity, not name similarity alone.

## GT-010B — PR search result limits

Operation: `search_prs`

Probe A:
empty query scoped to `Sangaa/ARGO-KOP`, `topn=5`, sorted by updated descending.

Observed:
- Five recent PRs were returned, including diagnostic probes #25, #24, #23, #22, and #19.

Probe B:
Same search with `topn=2`.

Observed:
- Only #25 and #24 were returned.

Learning:
1. `topn` is a result limit, not a statement about total PR population.
2. A limited result set must not be interpreted as exhaustive.
3. Sorting is part of evidence semantics: "recent" is relative to the selected sort/order.
4. Empty query means "list/search within scope" for this operation rather than "no search".

## GT-010C — Issue search and schema-boundary behavior

Operation: `search_issues`

Initial probe supplied `state="all"`.

Observed:
- Connector rejected the call at schema validation because this operation exposes only `open`, `closed`, or omitted/null state.

Corrected probe omitted `state` and returned the two most recent issues (#21 and #20).

Learning:
1. Tool schema is itself part of connector capability knowledge.
2. Provider API concepts must not be assumed to be exposed identically by the connector wrapper.
3. A tool-argument validation error is different from a provider HTTP error and different from endpoint absence.
4. After a schema rejection, retry with a schema-valid representation only; do not infer provider behavior from the invalid call.

## GT-011A — General error taxonomy and Actions ID dependency

Training objective: classify error/result semantics without using P6 as the selection criterion.

Read-only observations:
- `get_commit_combined_status` on a known ARGO commit returned `statuses=[]`. This is a successful empty result and must not be classified as endpoint absence, provider failure, or proof that no CI execution exists.
- A historical Issue #21 comment records that an exact public workflow-run URL can be read when a valid run_id is already known, and that specialized workflow-job and job-log readers work with valid run/job IDs. It also records that no valid ARGO run_id had been recovered through the then-available discovery path. This establishes an ID-dependent downstream observation model, not non-existence of runs. 
- A deliberately cross-repository job lookup using a known run ID from a public control repository against `Sangaa/ARGO-KOP` returned provider `404 Not Found`. This was not promoted to "tool missing" or "run absent" because the run ID did not belong to ARGO-KOP. It is retained as a negative boundary example showing that resource identity must be validated before interpreting a 404.

Classification model reinforced:
`tool schema rejection` ≠ `connector allowlist rejection` ≠ `provider 4xx` ≠ `resource 404` ≠ `successful empty result`.

Important refinement:
A valid downstream Actions reader does not imply that the connector can discover a run ID. Conversely, failure to discover a run ID does not imply downstream readers are absent.

## Cross-operation behavioral laws

1. Search result sets are bounded observations unless pagination/exhaustion is established.
2. `topn`/`per_page` are observation limits, not existence limits.
3. Search ranking and scope must be recorded when interpreting absence.
4. Connector schemas can intentionally expose a narrower contract than the underlying GitHub API.
5. Invalid tool arguments reveal connector contract boundaries; they are not evidence of repository/provider failure.
6. Related repository names are not identity matches.
7. A search miss or limited result must never be promoted to non-existence without an appropriate exhaustive or exact lookup channel.
8. Successful empty results are distinct from failed calls.
9. A resource 404 is only meaningful after repository/resource identity has been validated.
10. Downstream CI observation capabilities are ID-dependent; discovery and inspection are separate capabilities.
11. Cross-repository control probes can characterize tool behavior, but their IDs and results must never be attributed to the target repository.

## P6 independence check

The GT-011A observations were selected to characterize generic error/result semantics and identity boundaries. They were not selected to solve P6. P6 remains an application to be mapped only after the broader capability model is sufficiently mature.

## Current training state

GT-010A — COMPLETED
GT-010B — COMPLETED
GT-010C — COMPLETED
GT-011A — COMPLETED

Training remains IN PROGRESS globally.

## Next task

`GT-011B — Read-only capability matrix across Issues, PRs, Git, and Actions, with explicit evidence type/scope/error semantics.`

Focus:
- expand the capability map without P6-driven selection;
- identify duplicate capabilities exposed through different operations;
- classify each operation by discovery, exact retrieval, mutation, observation, or evidence role;
- avoid further cross-repository Actions probes unless needed for a specific tool semantic.

No P6 promotion is authorized by this training record.
