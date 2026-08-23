# EJR-317 — GitHub Connector Self-Training

Date: 2026-08-23
Status: IN PROGRESS
Protocol: GOV-017
Primary objective: train HERMUZ on the active GitHub connector before further P6 planning.

## 1. Training doctrine

The connector is treated as an operating environment, not merely a transport path. Training follows:

`Inventory → Classify → Minimal Probe → Observe → Interpret → Record → Reuse`

No training mutation is allowed merely to learn a capability.

## 2. Current capability families

The exposed GitHub surface has been inventoried at the connector level and contains 89 operations. Relevant families identified so far:

- account / installation
- repository discovery and metadata
- files / blobs / trees / commits / refs
- branches / comparisons
- pull requests / reviews / comments
- issues / search / reactions
- commit status
- Actions runs / jobs / steps / logs / artifacts
- repository mutations
- retry / re-execution operations

The inventory is a session observation and must not be generalized to the complete GitHub REST API.

## 3. Training cases completed in this cycle

### GT-001 — Repository identity and authority
Operation: `get_repo`
Target: `Sangaa/ARGO-KOP`
Observation: repository is accessible; current connector result reports admin/maintain/pull/push/triage permissions.
Interpretation: repository read/write authority is observable through this connector.
Reuse: establish repository identity and mutation authority before planning repository changes.

### GT-002 — Branch discovery
Operation: `search_branches`
Target: `Sangaa/ARGO-KOP`
Observation: P6-related branches are discoverable, including `fix/p6-head-binding-20260819`, `probe/hermuz-execution-observation-20260822`, and `revalidate/p6-execution-evidence-20260819`.
Interpretation: branch discovery is an independent lineage/evidence channel and should be considered before concluding that Actions observation is unavailable.
Reuse: correlate branches → commits → PRs → evidence.

### GT-003 — Commit status
Operation: `get_commit_combined_status`
Target: commit `8af28e47428f6550f92581f795428a433eb97be0`
Observation: `statuses=[]`.
Interpretation: this proves only that the combined-status surface returned no status records for this commit. It does NOT prove that no Actions execution occurred.
Reuse: status is an independent evidence channel; empty status must remain scoped to the status surface.

### GT-004 — Commit-to-workflow helper
Operation: `fetch_commit_workflow_runs`
Target: `Sangaa/ARGO-KOP`, commit `8af28e47428f6550f92581f795428a433eb97be0`
Observation: `workflow_runs=[]`.
Known wrapper scope: this helper currently filters to pull-request-triggered runs.
Interpretation: empty result is not general Actions execution absence.
Reuse: never use this helper as universal `head_sha` run discovery.

### GT-005 — Commit comparison
Operation: `compare_commits`
Target: base `54cb4a36b1dcb3e58286898edcf77ef9e2dfb4b0`, head `8af28e47428f6550f92581f795428a433eb97be0`
Observation: head is 3 commits ahead; returned changed files were EJR-313, EJR-314, and EJR-315.
Interpretation: Git-object/commit comparison can establish lineage and exact changed-file evidence independently of Actions runs.
Reuse: use commit comparison to validate what changed before selecting CI evidence.

### GT-006 — Issue search / learning retrieval
Operation: `search_issues`
Target: `Sangaa/ARGO-KOP`
Observation: retrieved P6 issue #11 and architectural learning issue #21.
Interpretation: Issues are a durable learning/evidence surface and can prevent repetition of known connector probes.
Reuse: mandatory prior-learning retrieval for connector-related investigations.

### GT-007A — Repository search → exact file retrieval
Operations: `search`, then `fetch_file`
Target: `Sangaa/ARGO-KOP`, `PROJECT_STATUS.md`
Hypothesis: repository search can discover relevant canonical files, after which exact file retrieval can be used for authoritative bounded reading.
Observed behavior: search located `PROJECT_STATUS.md`; `fetch_file` then retrieved its canonical content and SHA. The file reports Version 3.3.7, `INTEGRITY WARNING / CONNECTED-BASELINE AUDIT`, canonical status, and `Sangaa/ARGO-KOP` on `main` as the primary repository source of truth.
Interpretation: search is a discovery surface; `fetch_file` is a deterministic exact-file read surface. Search result metadata can identify a candidate, but authoritative content and file identity should be confirmed by exact retrieval.
Reuse rule: `SEARCH → SELECT EXACT PATH → FETCH FILE → VERIFY SHA/CONTENT` before relying on repository state claims.
Training classification: READ + DISCOVER; direct repository file retrieval after discovery.
Canonical mutation involved: NO.

### GT-007B — Commit comparison / Git-object lineage
Operation: `compare_commits`
Target: `Sangaa/ARGO-KOP`, base=`8af28e47428f6550f92581f795428a433eb97be0`, head=`8af28e47428f6550f92581f795428a433eb97be0`.
Hypothesis: the compare surface can validate whether two refs represent the same Git object and therefore act as a low-level lineage sanity check independent of PR or Actions surfaces.
Observed behavior: response classified the refs as `identical`, with `ahead_by=0`, `behind_by=0`, `total_commits=0`, and `files=[]`; the merge-base was the same SHA.
Interpretation: `compare_commits` is useful not only for changed-file discovery but also for proving ref identity/equivalence when the same SHA is supplied. It must not be treated as an execution-evidence source.
Reuse rule: before comparing downstream evidence from two refs, establish whether the refs actually diverge; identical refs produce no change set and do not justify further change-analysis assumptions.
Training classification: READ + GIT-LINEAGE; no repository mutation.
Canonical mutation involved: NO.

### GT-007B-NEG — Invalid/partial SHA behavior
Operation: `fetch_commit`
Target: `Sangaa/ARGO-KOP`, SHA=`0844d9`.
Observed behavior: connector returned `No commit found for SHA: 0844d9`.
Interpretation: this connector requires a resolvable commit SHA and does not treat a short, non-resolved value as a valid commit identity in this call. This is a connector input-validation observation, not evidence that the commit itself is absent.
Reuse rule: when a Git object is required for evidence, use a verified full SHA obtained from the connector rather than a guessed/partial identifier.
Training classification: ERROR / INPUT-VALIDATION; no repository mutation.
Canonical mutation involved: NO.

## 4. Preliminary behavioral laws

1. Repository access does not imply Actions execution observability.
2. A filtered wrapper's empty result is scoped to that wrapper.
3. Status, Git objects, PRs, and Actions are separate evidence channels.
4. A downstream Actions operation requires a real upstream identifier such as run_id or job_id.
5. Provider capability, repository implementation, connector contract, session exposure, and observed behavior must remain distinct.
6. Repository search is discovery, not authoritative content; exact file retrieval must establish the content and SHA before state claims are reused.
7. Commit comparison can establish Git-ref identity and change lineage, but it is not an execution-evidence channel.
8. Invalid or partial object identifiers must be classified as connector input behavior, not repository absence.

## 5. Training still required

The following families remain to be trained before this record can be promoted from IN PROGRESS:

- repository discovery/search across account scope
- file/blob/tree/ref operations
- PR lineage and review surfaces
- issue/comment mutation boundaries (read-first only unless explicitly authorized)
- Actions downstream operations using a known real run/job identifier if one becomes available
- artifact inspection/download behavior if a real artifact identifier becomes available
- retry/re-execution behavior: inventory first; no execution training without explicit authorization
- pagination and filtering behavior where exposed
- error classification and wrapper restrictions
- alternative evidence channels for P6 Run-ID discovery

## 6. Current P6 implication

Do not conclude that the execution boundary is external yet.

First complete the connector capability training and test the independent evidence channels available to the current session. Only after that may HERMUZ decide whether `list_workflow_runs(head_sha=...)` exposure is the actual blocking boundary or whether another exposed channel can establish authoritative execution lineage.

## 7. Next task

`GT-007C — Train blob/tree/ref read surfaces using verified Git objects.`

Required order:

`Inventory → safe read-only training → evidence classification → update this record → derive P6 evidence plan → execute the smallest justified P6 probe → document result → close session.`

No P6 promotion is authorized by this record.

## 8. Model handoff

Every future model/session must read GOV-017 and this EJR before performing connector-dependent work. It must reuse validated observations and perform only freshness checks for unchanged connector surfaces.

End of current training cycle.
