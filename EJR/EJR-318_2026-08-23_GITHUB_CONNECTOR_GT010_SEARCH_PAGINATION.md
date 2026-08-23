# EJR-318 — GitHub Connector Self-Training: GT-010 Search, Pagination & Filtering

Date: 2026-08-23
Protocol: GOV-017
Status: COMPLETED FOR THIS TRAINING CYCLE
Training mode: capability-first, not P6-first

## Objective

Train HERMUZ on generic repository, PR, and issue search semantics, including pagination, result limits, filtering, argument/schema boundaries, and reusable capability classification without selecting the exercise because of P6.

## GT-010A — Repository search pagination

Operation: `search_repositories`

Probe A:
`query="Sangaa/ARGO-KOP", per_page=1, page=1`

Observed:
- Exact repository `Sangaa/ARGO-KOP` was returned on page 1.
- The response exposed repository metadata and connector-reported permissions.

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
- Five recent PRs were returned.

Probe B:
Same search with `topn=2`.

Observed:
- Only two results were returned.

Learning:
1. `topn` is a result limit, not a statement about total PR population.
2. A limited result set must not be interpreted as exhaustive.
3. Sorting is part of evidence semantics.
4. Empty query means list/search within scope for this operation.

## GT-010C — Issue search and schema-boundary behavior

Operation: `search_issues`

Initial probe supplied `state="all"`.

Observed:
- Connector rejected the call at schema validation because this operation exposes only `open`, `closed`, or omitted/null state.

Corrected probe omitted `state` and returned recent issues.

Learning:
1. Tool schema is itself part of connector capability knowledge.
2. Provider API concepts must not be assumed to be exposed identically by the connector wrapper.
3. Tool-argument validation error differs from provider HTTP error and endpoint absence.
4. After schema rejection, retry only with a schema-valid representation.

## GT-011A — General error taxonomy and Actions ID dependency

Read-only observations:
- `get_commit_combined_status` on a known ARGO commit returned `statuses=[]`. This is a successful empty result and must not be classified as endpoint absence, provider failure, or proof that no CI execution exists.
- A historical Issue #21 record established that exact workflow-run retrieval and downstream job/log readers are ID-dependent. It did not establish non-existence of runs.
- A deliberate cross-repository job lookup using a known run ID from a control repository against ARGO-KOP returned provider `404 Not Found`. This is retained only as a negative boundary example: resource identity must be validated before interpreting a 404.

Classification model:
`tool schema rejection` ≠ `connector allowlist rejection` ≠ `provider 4xx` ≠ `resource 404` ≠ `successful empty result`.

Important refinement:
A valid downstream Actions reader does not imply that the connector can discover a run ID. Conversely, failure to discover a run ID does not imply downstream readers are absent.

## GT-011B — Read-only capability matrix

Training objective: build a reusable map of connector capabilities without selecting operations because they might solve P6.

### Account / installation / repository discovery

| Surface | Operation | Role | Evidence | Scope / limitation |
|---|---|---|---|---|
| Account | `list_user_orgs` | discovery | organization list | Empty result is a successful observation; it does not imply connector failure |
| Installation | `list_installations` | discovery / scope | installed-account + event permissions | Describes installation scope, not repository execution |
| Installation | `list_repositories_by_installation` | discovery | repositories visible to installation | Paginated; first page is bounded |
| Repository | `list_repositories` | discovery | accessible repositories + permissions | Paginated; broad account-visible scope |
| Repository | `list_repositories_by_affiliation` | discovery | repositories by ownership/collaboration relation | Different semantic scope from general listing |
| Repository | `get_repo` | exact retrieval | canonical repository metadata | Requires exactly one repository identity selector |

### Git / repository content

| Surface | Operation | Role | Evidence | Scope / limitation |
|---|---|---|---|---|
| Repository search | `search` | discovery | matching files/code | Search semantics and index availability matter |
| File | `fetch_file` | exact retrieval | file content + blob SHA | Exact ref/path; strong identity evidence |
| Commit | `search_commits` | discovery | commit candidates | Bounded by `topn`; search terms affect population |
| Compare | `compare_commits` | lineage/evidence | ahead/behind/base/files | Compares supplied refs; not execution evidence |

### PR / collaboration

| Surface | Operation | Role | Evidence | Scope / limitation |
|---|---|---|---|---|
| PR metadata | `get_pr_info` | exact retrieval | refs/status/title | Does not contain code changes |
| PR changes | `list_pr_changed_filenames` | discovery/exact change scope | changed paths | Must precede per-file patch retrieval |
| PR patch | `fetch_pr_patch` | change evidence | patch across changed files | Empty patch is evidence about that PR change surface only |
| Review | `list_pull_request_reviews` | collaboration evidence | review submissions | Empty result ≠ execution absence |
| Review thread | `list_pull_request_review_threads` | collaboration evidence | inline threads/resolution | Separate surface from top-level comments |
| PR timeline | `fetch_pr_comments` | collaboration evidence | normalized discussion timeline | Evidence scope is discussion, not CI execution |

### Issues / search

| Surface | Operation | Role | Evidence | Scope / limitation |
|---|---|---|---|---|
| Issue search | `search_issues` | discovery | matching issues | Connector schema exposes only `open/closed`; `all` is not an accepted argument |
| Recent issues | `list_recent_issues` | bounded discovery | recent accessible issues | `top_k` is a result limit, not an existence guarantee |

### Actions / CI

| Surface | Operation | Role | Evidence | Scope / limitation |
|---|---|---|---|---|
| Run discovery | `fetch_commit_workflow_runs` | discovery | workflow runs for a commit | **Currently documented as PR-triggered only; first page only** |
| Jobs | `fetch_workflow_run_jobs` | inspection | jobs for a known run | Requires a valid run ID; first page/latest attempt only |
| Artifacts | `fetch_workflow_run_artifacts` | inspection | artifacts for a known run | Requires a valid run ID; first page only |
| Artifact download | `download_workflow_artifact` | retrieval | artifact bytes | Requires a valid artifact ID |

Key distinction:
`run discovery` and `run inspection` are separate capabilities. An inspection operation requiring `run_id` cannot be used as a discovery operation merely because it exists.

## Cross-operation behavioral laws

1. Search result sets are bounded observations unless pagination/exhaustion is established.
2. `topn`/`per_page` are observation limits, not existence limits.
3. Search ranking and scope must be recorded when interpreting absence.
4. Connector schemas can intentionally expose a narrower contract than the underlying GitHub API.
5. Invalid tool arguments reveal connector contract boundaries; they are not evidence of repository/provider failure.
6. Related repository names are not identity matches.
7. A search miss or limited result must never be promoted to non-existence without an appropriate exhaustive or exact lookup channel.
8. Successful empty results are distinct from failed calls.
9. A resource 404 is meaningful only after repository/resource identity has been validated.
10. Downstream CI observation capabilities are ID-dependent; discovery and inspection are separate capabilities.
11. Cross-repository control probes can characterize tool behavior, but their IDs and results must never be attributed to the target repository.
12. Capability inventory must precede problem-specific capability selection.
13. Duplicate-looking operations may have different scope, pagination, normalization, or evidence semantics and must be mapped separately before consolidation.

## P6 independence check

GT-011B was selected to characterize the connector broadly. The repository/installation/account operations were deliberately exercised because they expand knowledge of the connection surface, not because they are expected to solve P6. P6 remains an application to be mapped only after the broader capability model is sufficiently mature.

## Current training state

GT-010A — COMPLETED
GT-010B — COMPLETED
GT-010C — COMPLETED
GT-011A — COMPLETED
GT-011B — COMPLETED FOR CURRENT EXERCISE

Training remains IN PROGRESS globally.

## Next task

`GT-011C — Capability equivalence and boundary matrix across read, write, discovery, retrieval, and observation operations.`

Focus:
- identify operations that appear equivalent but differ in scope or evidence;
- map safe mutation surfaces without changing production logic;
- document which capabilities are currently session-exposed versus repository-implemented;
- continue capability-first training without making P6 the selection criterion.

No P6 promotion is authorized by this training record.
