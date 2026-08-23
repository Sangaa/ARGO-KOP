# EJR-322 — GitHub Actions GT-015 Surface & Identity Training

Date: 2026-08-23
Status: COMPLETED / SESSION TRAINING RECORD
Protocol: GOV-017 + CELM-001
Parent: EJR-321

## Objective

Map the currently exposed GitHub Actions observation surfaces and test their dependency order using an existing real workflow run. The purpose is capability-first learning, not P6 promotion.

## Surface inventory observed in the current session

### Discovery
`fetch_commit_workflow_runs(repo_full_name, commit_sha)`

Connector contract explicitly states that this wrapper currently filters to pull-request-triggered runs and returns the first page only.

### Run inspection
`fetch_workflow_run_jobs(repo_full_name, run_id)`

Returns jobs for the latest attempt from the first page.

### Job inspection
`fetch_workflow_job_steps(repo_full_name, job_id)`

Returns step summaries for a known job.

### Job evidence
`fetch_workflow_job_logs(repo_full_name, job_id)`

Returns decoded job logs for a known job.

### Artifact inspection
`fetch_workflow_run_artifacts(repo_full_name, run_id, name?)`

Returns the first page of artifacts and supports optional name filtering.

### Artifact retrieval
`download_workflow_artifact(repo_full_name, artifact_id, file_name?)`

Downloads a known artifact archive. This is inspection/retrieval, not run discovery.

### Mutation-capable Actions operations exposed by the connector
The session tool surface also exposes:
- `rerun_workflow_job(job_id)`
- `rerun_failed_workflow_run_jobs(run_id)`

These are write/mutation operations and were NOT invoked in this training cycle.

## Dependency graph learned

`commit SHA → workflow run → job → step/log`

and independently:

`workflow run → artifact → artifact archive`

Inspection operations require an upstream identity. Therefore a job/log/artifact tool cannot substitute for run discovery.

## GT-015A — Existing real run discovery

Input commit SHA:
`2378f1bdfad2ba93dad09597950f1219ea6d819f`

`fetch_commit_workflow_runs` returned a real run:
- run_id: `32548603868`
- workflow: `Full-Stack Repository Audit`
- conclusion: `success`
- run_number: `1335`
- workflow_id: `333498182`

This disproves the earlier assumption that the exposed wrapper necessarily produces an empty result for this SHA. The current wrapper can discover a PR-triggered run associated with the supplied commit SHA.

## GT-015B — Run → jobs

Run `32548603868` returned job:
- job_id: `96971472720`
- name: `repository-audit`
- status: `completed`
- conclusion: `success`

This confirms that a discovered run ID unlocks the downstream inspection surface.

## GT-015C — Job → steps

The job returned 47 step summaries. Relevant successful steps include:
- checkout
- checkout SHA assertion
- P4 boundary gates
- P6 CI impact correlation regression
- P6 canonical repository boundary regression
- P6 layered boundary regressions
- P6 reconciliation boundary regressions
- P6 controlled runtime lineage adapter regression
- repository-wide audit
- runtime evidence emission
- evidence artifact uploads
- CI execution identity upload

This establishes step-level execution evidence for this specific run/job.

## GT-015D — Job → logs

Job logs were retrieved successfully. They provide runtime-level evidence including:
- workflow event: `pull_request`
- checkout ref: `refs/pull/25/merge`
- checkout SHA / `github.sha`: `400a50414a31c0e8537a06f46ff4bf580945874c`
- checkout assertion passed
- P6 regressions passed
- runtime evidence emitted
- artifacts uploaded successfully

## Critical Knowledge Delta KD-011 — PR head SHA vs workflow execution SHA

Classification: `NEW OBSERVATION / HIGH IMPACT`

Observed:
- Discovery was performed using commit SHA `2378f1bdfad2ba93dad09597950f1219ea6d819f`.
- The discovered run is a pull-request run whose artifact metadata reports head SHA `2378f1bdfad2ba93dad09597950f1219ea6d819f`.
- The actual workflow log shows `github.event_name=pull_request`, `github.ref=refs/pull/25/merge`, and `github.sha=400a50414a31c0e8537a06f46ff4bf580945874c`.
- The checkout assertion verifies the checked-out repository state against `github.sha`, therefore the executed checkout is the PR merge SHA, not the PR head SHA supplied to discovery.

Interpretation:
A PR-triggered Actions run can be discoverable through a PR head commit SHA while executing against a synthetic/merge ref and a different execution SHA.

Reusable rule:
`For pull_request runs, never equate run.head_sha with the exact checkout/execution SHA without reading event/ref/github.sha evidence.`

This is directly relevant to P6 identity correlation.

## Knowledge Delta KD-012 — Empty previous discovery was not universal

Classification: `MODEL MISUNDERSTANDING / CORRECTED`

Observed:
A prior model treated `fetch_commit_workflow_runs(... ) = []` as evidence that the wrapper could not discover the run. Current direct use returned a real run for a commit SHA.

Learning:
The wrapper is limited in event scope, not incapable of discovery. A previous empty result was therefore insufficient to establish a general connector exposure gap.

Reusable rule:
`Do not promote an exposure gap from a single empty result until the operation contract and a positive control are both tested.`

## Knowledge Delta KD-013 — Downstream evidence surfaces are reachable

Classification: `VERIFIED CAPABILITY`

Observed:
A real discovered run unlocked jobs, steps, logs, and artifacts through the same connector family.

Learning:
The downstream Actions observation chain is operationally exposed in this session when a valid run_id exists.

Boundary:
This does not establish general run discovery for push/workflow_dispatch/other events because the discovery wrapper explicitly filters to PR-triggered runs.

## Artifact evidence

Run `32548603868` returned four non-expired artifacts:
- `full-stack-audit-report` — id `9469321798`
- `runtime-evidence` — id `9469321973`
- `ci-impact-correlation` — id `9469322132`
- `ci-execution-identity` — id `9469322269`

The logs independently confirm their upload and finalization.

## Important architecture result

The current session surface is not accurately represented as simply:

`Actions unavailable`

The more accurate map is:

`PR-head-SHA discovery (bounded) → run → jobs → steps → logs/artifacts`

with separate mutation-capable rerun operations.

The remaining unknown is not whether downstream observation exists. The remaining discovery question is whether the connector exposes a general run-discovery operation for non-PR events (for example push/workflow_dispatch) or only this PR-scoped wrapper.

## P6 boundary

No rerun or workflow mutation was performed.
No workflow was changed.
P6 was not promoted.

The run proves real execution evidence for the discovered PR-triggered run, but identity correlation must respect the distinction:

`PR head SHA → run head SHA`
versus
`run event/ref → github.sha → actual checkout SHA`

Therefore this cycle is a capability and identity-model correction, not a P6 final verdict.

## Next task

`GT-016 — Actions discovery boundary: positive/negative controls for PR-head discovery versus push/workflow_dispatch discovery, using only existing evidence and read-only operations.`

Goal: determine whether the current exposed discovery surface is intentionally PR-scoped or whether another session-exposed operation can discover runs for a push SHA without mutation.

Session rule: Execute → document → read-back → verify → close.
