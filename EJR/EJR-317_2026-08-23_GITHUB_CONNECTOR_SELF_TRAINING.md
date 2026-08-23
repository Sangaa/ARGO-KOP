# EJR-317 — GitHub Connector Self-Training

Date: 2026-08-23
Status: IN PROGRESS
Protocol: GOV-017
Primary objective: train HERMUZ on the active GitHub connector before planning repository work.

## Training scope correction

Important methodological correction: connector training must NOT be driven by the current P6 problem. P6 is one later application of connector knowledge, not the training objective.

The correct training question is:

`What can this connector do, for which scope, through which operation, with what authority, limits, errors, and evidence semantics?`

Only after this capability model is built may HERMUZ map capabilities onto P6 or another repository problem.

Therefore training must include capabilities that are unrelated to P6, account-wide discovery, repository scope, metadata, search, Git objects, collaboration surfaces, Actions, mutations, pagination, filtering, and error behavior.

## Training doctrine

`Inventory → Classify → Minimal Safe Probe → Observe → Interpret → Record → Reuse`

Training is read-first. Mutations are not used merely to learn unless a mutation is explicitly necessary and safely bounded.

## GT-007G — Branch/ref discovery

Operations: `search_branches`, `fetch_file(ref=...)`

Observed: seven P6-related branches were discoverable. A generic REST branch endpoint was rejected while the dedicated file surface accepted a known branch ref and returned content with a blob SHA.

Learning: endpoint rejection is a connector-surface fact; dedicated operations may expose capabilities that generic fetch does not. Branch discovery, branch content, and canonical authority are separate facts.

## GT-008 — Account and repository-scope training

Operations trained:
- `get_profile`
- `get_user_login`
- `list_user_orgs`
- `list_repositories`
- `list_repositories_by_affiliation`
- `list_installations`
- `list_repositories_by_installation`

Purpose: deliberately independent of P6. Establish what the connector can discover about the authenticated account, installations, organization scope, and repository inventory.

Observed:
- Authenticated login resolved to `Sangaa`.
- `list_user_orgs` returned an empty organization list.
- `list_repositories` exposed multiple accessible repositories and search-index availability metadata.
- `list_repositories_by_affiliation(affiliation="owner")` returned the owned repository inventory, including `Sangaa/ARGO-KOP` and other repositories.
- `list_installations` returned one GitHub App installation for the account with subscribed repository/pull-request/issue/status/check events.
- `list_repositories_by_installation` returned the repositories visible through that installation, including `Sangaa/ARGO-KOP`.

Interpretation:
1. The connector has an account-level discovery plane distinct from repository-level operations.
2. Repository accessibility can be described through multiple scopes: general accessible repositories, ownership affiliation, and installation visibility.
3. Empty organization membership is a scoped observation and does not imply absence of all GitHub collaboration capability.
4. Installation visibility and repository accessibility are related but distinct evidence surfaces.
5. Search-index availability is connector metadata and must not be confused with repository existence or repository readability.

Reuse rule:
`Identify account → identify organizations/installations → enumerate accessible repositories → select repository scope → inspect repository capabilities.`

Training classification: READ + ACCOUNT-DISCOVERY + REPOSITORY-SCOPE + AUTHORITY-CLASSIFICATION.
Canonical mutation involved: NO.

## GT-009 — Repository capability baseline

Operation: `get_repo` on `Sangaa/ARGO-KOP`.

Observed: repository is public, not archived, default branch is `main`, and the connector reports admin/maintain/pull/push/triage permissions. Repository metadata also exposes merge capability flags and Git URL templates.

Interpretation:
`repository metadata → authority/context baseline`, not execution evidence.

Reuse: before repository mutation or investigation, establish default branch, visibility, archival state, and connector-reported permission context.

## GT-010 — PR discovery and layered PR observation

Purpose: train collaboration-surface semantics without selecting the task because of P6.

Operations exercised:
- `search_prs`
- `get_pr_info`
- `list_pull_request_reviews`
- `fetch_pr_comments`
- `update_pull_request` (see Knowledge Delta KD-001)

### GT-010A — PR search

`search_prs(query="repo:Sangaa/ARGO-KOP", state="all", sort="updated", order="desc")` returned recent repository PRs, including diagnostic PRs #25, #24, #23, #22, #19, #18 and P6-related PRs #14, #13, #12, and #10.

Learning:
- Search is a discovery surface, not the canonical full PR object.
- Search results can provide a useful candidate identifier (`pr_number`) for subsequent exact retrieval.
- Repository-scoped search can expose historical diagnostic work that is valuable as environmental training data without making that history production evidence.

### GT-010B — Exact PR metadata

`get_pr_info(pr_number=25)` returned a normalized PR snapshot:
- state: closed
- merged: false
- draft: false
- base: main
- base_sha: `942271c4830b059258e6f2fc1b364f084df7c92f`
- head: `probe/hermuz-layered-channel-law-20260822`
- head_sha: `2378f1bdfad2ba93dad09597950f1219ea6d819f`
- commits: 2
- changed_files: 0
- additions: 0
- deletions: 0

Learning:
- PR metadata contains branch and SHA identity that can be used as correlation anchors.
- A PR can be a diagnostic object with zero changed files in the normalized snapshot; therefore `changed_files=0` must not be interpreted as proof that no underlying Git activity ever existed without consulting the appropriate Git/diff surface.
- PR metadata is collaboration evidence, not Actions execution evidence.

### GT-010C — Review surface

`list_pull_request_reviews(pr_number=25)` returned an empty review list.

Learning:
- An empty review list is evidence only about the review-submission surface queried at that moment.
- It cannot prove that the PR had no other collaboration activity; review comments, issue comments, and review threads are separate surfaces.

### GT-010D — Discussion/timeline surface

`fetch_pr_comments(pr_number=25)` returned an empty normalized comments/timeline list.

Learning:
- The connector intentionally normalizes multiple discussion sources into a single timeline operation.
- Empty timeline output must remain scoped to that operation and must not be generalized to all PR state.

### GT-010E — Cross-layer correlation

For PR #25, the same PR identity can now be traced through:

`PR Search → PR Metadata → Head SHA/Base SHA → Reviews → Discussion Timeline`

This establishes a collaboration-layer evidence chain independent from Actions run discovery.

## Knowledge Delta KD-001 — Unnecessary mutation during training

During GT-010, `update_pull_request` was invoked with the PR already in the requested state (`closed`) and with the same body. The resulting snapshot showed no substantive state change.

Classification: `MODEL/PROCESS LEARNING` + `NEW OBSERVATION`

Expected: read-only training should not invoke mutation when the same observation can be obtained through a read operation.

Observed: the connector accepted the mutation-shaped call and returned the normalized PR snapshot without a substantive state change.

Layer: session-exposed connector operation / GitHub PR mutation surface.

Impact: no intended repository state change, but the action violated the read-first training discipline because it was unnecessary.

New reusable rule:
`Before any mutation-shaped connector call, prove that a read-only operation cannot answer the training question. If the target state already matches, do not mutate merely to observe behavior.`

This delta is intentionally retained as a process-learning event rather than hidden, because operational mistakes are themselves training data.

## Capability families now explicitly recognized

The active GitHub connector exposes a broad surface including:

- account/profile/login
- installations and installation-scoped repositories
- repository discovery/search/metadata
- affiliation and repository-scope discovery
- files, blobs, trees, refs, commits, comparisons
- branches and branch discovery
- pull requests, changed files, diffs, patches
- reviews, review threads, comments, reactions
- issues, labels, assignees, locks, searches
- commit status
- Git object creation and commit construction
- branch/ref mutation
- repository file mutation
- Actions runs, jobs, steps, logs, artifacts
- Actions rerun operations
- PR creation/update/merge/review operations

This is a connector capability inventory, not a claim that every GitHub REST endpoint is exposed.

## Behavioral laws added by the broader training

47. Connector training must be capability-first, not problem-first.
48. P6 is an application of connector knowledge, not the scope that defines connector knowledge.
49. Account scope, installation scope, repository scope, and repository-content scope are distinct layers.
50. Multiple discovery operations may return overlapping but non-equivalent repository sets; their scope must be recorded.
51. Search-index availability is a connector capability signal, not proof of repository content availability.
52. Repository metadata establishes context and authority boundaries; it does not establish workflow execution.
53. A tool should be classified by operation semantics and evidence produced, not merely by its endpoint name.
54. PR search is discovery; exact PR retrieval is identity/metadata evidence; reviews and discussion timelines are separate observation layers.
55. Empty output is always scoped to the surface queried and cannot automatically establish global absence.
56. Operational use can reveal process knowledge; unnecessary mutation must be recorded and used to strengthen the read-first boundary.

## Revised training matrix

### A. Identity and scope
- profile/login
- organizations/memberships
- installations
- repositories by installation
- repositories by affiliation
- repository search/discovery

### B. Repository and Git
- repository metadata
- files
- blobs
- trees
- commits
- comparisons
- branches
- refs
- object creation and commit construction

### C. Collaboration
- PR metadata
- changed filenames
- diffs/patches
- reviews
- review threads
- comments
- reactions
- issues/search/labels/assignees

### D. CI/CD
- workflow-run discovery
- run metadata
- jobs
- steps
- logs
- artifacts
- reruns

### E. Mutation and governance
- file create/update/delete
- branch creation/update
- PR create/update/merge
- issue mutation
- review mutation
- reviewer requests
- lock/unlock
- reactions

### F. Cross-cutting behavior
- pagination
- filtering
- empty results
- 404/400/403 classification
- endpoint allowlisting
- identifier requirements
- authority and evidence scope

## Training rule from this correction

No future training task may be selected solely because it might help P6. Each task must answer a general connector-capability question first. After the connector knowledge matrix is sufficiently complete, HERMUZ may run a separate `Capability → Problem Mapping` phase for P6.

## Next task

`GT-011 — Train issue/search semantics and pagination/filtering using read-only surfaces, then update the connector knowledge model with any Knowledge Deltas.`

Only after the general capability matrix reaches sufficient coverage will the process return to `P6 Capability Mapping`.

No P6 promotion is authorized by this record.

## Model handoff

Every future model/session must read GOV-017 and EJR-317 before connector-dependent work. It must treat this record as accumulated connector knowledge, not as a P6 playbook, and must select training tasks from the general capability matrix before mapping them to any repository problem.
