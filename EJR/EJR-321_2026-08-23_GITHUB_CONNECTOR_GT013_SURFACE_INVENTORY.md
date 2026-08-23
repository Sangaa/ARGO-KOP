# EJR-321 — GitHub Connector Self-Training: GT-013 Surface Inventory & Evidence Mapping

Date: 2026-08-23
Protocol: GOV-017
Status: COMPLETED — INITIAL SURFACE/EVIDENCE MAP RECORDED
Training mode: capability-first, not P6-first

## Objective

Continue GitHub Connector training without selecting operations from P6. The objective is to map operation families, scope, evidence class, and composition boundaries before applying the knowledge to repository-specific problems.

## Operations exercised in this cycle

1. `get_repo` — exact repository identity/metadata and permission surface.
2. `search_commits` — repository-scoped historical commit discovery with explicit empty-query behavior for recent commits.
3. `list_pull_request_reviews` — review-submission discovery for a known PR.
4. `list_pull_request_review_threads` — inline review-thread discovery for the same PR.
5. `fetch_file` — exact repository file retrieval and read-back of training knowledge.
6. `update_file` — controlled documentation mutation followed by read-back.

## Observed evidence classes

### Repository identity
`get_repo` provides repository identity, visibility, default branch, and permissions. It is an identity/metadata operation, not a file-content or CI-evidence operation.

### Historical change discovery
`search_commits` returns commit identity and metadata. A recent-commit listing is useful for locating candidate changes, but it is not by itself proof of file contents, workflow execution, or runtime behavior.

### Review evidence
`list_pull_request_reviews` and `list_pull_request_review_threads` are separate collaboration-evidence surfaces. An empty review list is a successful empty result for that PR; it does not imply that the PR is absent or that collaboration features are unavailable globally.

### File mutation and verification
`update_file` returned a commit SHA and content SHA. `fetch_file` then provided independent read-back including the resulting file SHA. This is a positive mutation → read-back → verification chain for repository contents.

## New capability map

| Operation family | Example operation | Primary evidence | Not sufficient to prove |
|---|---|---|---|
| Repository identity | `get_repo` | repository identity/permissions | file state or CI execution |
| Discovery | `search_commits` | candidate historical commits | runtime execution |
| Collaboration | `list_pull_request_reviews` | review submissions | file changes or CI execution |
| Collaboration | `list_pull_request_review_threads` | inline discussion/resolution metadata | merge or runtime execution |
| Content read | `fetch_file` | exact file content + blob SHA | workflow execution |
| Content mutation | `update_file` | commit/content SHA | CI success |
| Actions discovery | `fetch_commit_workflow_runs` | commit-associated PR-triggered run records only | arbitrary event run discovery |
| Actions inspection | `fetch_workflow_run_jobs` / artifacts | jobs/artifacts for a known run ID | discovery of unknown run IDs |

## Important boundary findings

1. Repository capability, content capability, collaboration capability, and Actions observation capability are separate evidence surfaces.
2. A tool's name must not be used to infer its evidence class.
3. Successful empty collections are observations of the selected scope, not global absence proofs.
4. Discovery and inspection are distinct: an inspection operation that requires `run_id` cannot substitute for a general run-discovery operation.
5. Implementation capability, session exposure, and evidence capability remain three distinct layers.
6. A write result must be independently read back when the contract permits; this is now a preferred training pattern.
7. Training selection must remain capability-first. P6 is a later consumer of the capability map, not the criterion for selecting the next experiment.

## GT-013 decision

The current GitHub surface is broad enough to support a structured capability map, but the map is not yet complete. Continue inventorying remaining operations, especially collaboration mutation, Git refs/objects, Actions observation, artifact boundaries, and error semantics.

Do not claim that an operation is unavailable merely because it was not selected or not yet exercised. Distinguish:
- not inventoried;
- implemented in connector code;
- session-exposed;
- exercised successfully;
- exercised with bounded failure;
- evidence-limited.

## P6 independence

No P6-specific probe was selected or executed in this cycle. The observations are general Connector knowledge and must remain reusable for future problems.

## Next task

`GT-014 — Error Semantics & Observation-Boundary Matrix.`

Focus:
- distinguish schema validation, connector rejection, provider 4xx/404, empty result, and successful evidence;
- exercise safe read-only cases where possible;
- record which layer produced each outcome;
- continue capability-first training before repository-specific mapping.

Session rule: Execute → document → read-back → verify → close.
