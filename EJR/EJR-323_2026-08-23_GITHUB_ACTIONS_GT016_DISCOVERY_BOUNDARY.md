# EJR-323 — GitHub Actions GT-016 Discovery Boundary Training

Date: 2026-08-23
Status: COMPLETED / SESSION TRAINING RECORD
Protocol: GOV-017 + CELM-001
Parent: EJR-322

## Objective
Determine the actual boundary of the session-exposed Actions discovery operation using positive and negative read-only controls. Do not mutate workflows or dispatch new runs.

## Canonical workflow capability
The canonical `Full-Stack Repository Audit` workflow declares all three relevant triggers:
- `push` to `main`
- `pull_request` to `main`
- `workflow_dispatch`

Therefore provider/workflow intent supports all three event classes. This does NOT imply that the session-exposed discovery wrapper can discover all three classes.

## GT-016A — Positive control: PR head SHA

Input:
`2378f1bdfad2ba93dad09597950f1219ea6d819f`

`fetch_commit_workflow_runs` returned:
- run_id `32548603868`
- workflow `Full-Stack Repository Audit`
- run number `1335`
- conclusion `success`

Result: POSITIVE.

## GT-016B — Negative control: PR merge/execution SHA

Input:
`400a50414a31c0e8537a06f46ff4bf580945874c`

The same discovery operation returned:
`workflow_runs = []`
with no connector error.

This SHA is independently established as the actual `github.sha` / checkout SHA of the PR execution through the workflow's execution identity artifact and log evidence.

Result: NEGATIVE / SCOPED.

## Interpretation

The two controls are deliberately different:

`PR head SHA 2378... → run discovered`
`PR execution/merge SHA 400a... → no run discovered`

The operation contract explicitly says the wrapper filters to pull-request-triggered runs. Therefore the negative result does not prove that no Actions execution exists for the merge SHA. It demonstrates that this discovery surface is keyed to a narrower PR-head association than a generic execution-SHA lookup.

This is a critical correction to the previous hypothesis. The current session surface is not a general `actions/runs?head_sha=` operation.

## GT-016C — Downstream confirmation using the positive run

The discovered run `32548603868` remains fully inspectable through:
- jobs
- steps
- logs
- artifacts

The `ci-execution-identity` artifact independently reports:
- event `pull_request`
- ref `refs/pull/25/merge`
- `github_sha = 400a50414a31c0e8537a06f46ff4bf580945874c`
- `checkout_sha = 400a50414a31c0e8537a06f46ff4bf580945874c`
- run id `32548603868`

This creates a verified two-key identity model:

`discovery key = PR head SHA`
`execution identity key = run_id + event/ref + github.sha`

## GT-016D — Workflow trigger surface inspection

The canonical workflow definition explicitly contains:

`push`
`pull_request`
`workflow_dispatch`

This proves workflow-level trigger capability, but no session-exposed general run-discovery operation was found in the current Actions tool surface. The available discovery wrapper is documented as PR-triggered only.

No workflow dispatch was attempted because the current training objective is discovery-boundary learning and dispatch would be a mutation.

## Knowledge Delta KD-014 — Discovery key is operation-specific

Classification: `NEW OBSERVATION / HIGH IMPACT`

Observed: the same Actions wrapper discovers a run from the PR head SHA but returns an empty set for the execution/merge SHA of that run.

Learning: a discovery operation's input field name (`commit_sha`) does not by itself establish that it accepts every SHA associated with an execution. The operation contract and observed controls define its actual semantic scope.

Reusable rule:
`Never generalize a connector parameter from its type name; validate the operation's semantic key and scope.`

## Knowledge Delta KD-015 — Workflow trigger capability != discovery capability

Classification: `NEW OBSERVATION`

Observed: the workflow supports push, pull_request, and workflow_dispatch, while the exposed discovery wrapper is PR-scoped.

Learning: provider/workflow trigger surface and connector discovery surface are separate layers.

Reusable rule:
`Do not infer session discovery coverage from workflow trigger coverage.`

## Knowledge Delta KD-016 — Negative control can identify semantic filtering

Classification: `VERIFIED METHOD`

A carefully selected negative control sharing the same execution lineage but using a different identity key can distinguish "no execution" from "discovery operation does not index this key" when combined with independent positive evidence.

Reusable rule:
`Use positive and negative controls before declaring an observation gap.`

## Current Actions capability map

### Verified in-session
- PR-head-SHA workflow-run discovery (bounded)
- run → jobs
- job → steps
- job → logs
- run → artifacts
- artifact → archive download
- job rerun operation exists
- failed-run-jobs rerun operation exists

### Verified workflow-level but not session discovery-level
- push trigger
- workflow_dispatch trigger

### Not established
- general run discovery for push SHA
- general run discovery for workflow_dispatch
- session-exposed workflow dispatch invocation

## P6 consequence

The earlier statement `Run-ID Discovery is unavailable` is no longer valid as a general statement.

The accurate statement is:

`Run-ID discovery is available for PR-scoped discovery through the exposed wrapper; general event-independent discovery remains unverified.`

P6 is still NOT promoted because the exact evidence chain required by the P6 contract must be correlated against the correct execution identity and event semantics.

## Safety

- No workflow mutation performed.
- No workflow dispatch performed.
- No rerun performed.
- No repository production logic changed.
- Only existing runs/artifacts and workflow definition were read.

## Next task

`GT-017 — Actions artifact evidence semantics and identity correlation.`

Study whether artifact metadata and downloaded artifact contents can serve as an independent evidence channel for execution identity, and define exactly which claims artifact evidence can and cannot prove.

Session rule: Execute → document → read-back → verify → close.
