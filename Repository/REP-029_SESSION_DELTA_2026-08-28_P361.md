# P361 — P6 Workflow Observation Boundary Correction

Date: 2026-08-28
Status: `CLOSED / VERIFIED / P6 EXECUTION-VERIFICATION-PENDING`
Protocol: `GOV-013 v1.1.3`

## RE-ENTRY
Returned from P360. Current P360 commit was verified as `dc53a15612e38f32a0d10f3f972150a3ff7ef1ed`.

## ANALYSIS
A new repository-state inspection found that `full-stack-audit.yml` exists on `main` and is configured for both `push` to `main` and `pull_request` to `main`, with `workflow_dispatch`. The workflow includes explicit P6 regressions and CI execution identity binding.

Therefore the earlier statement that absence of a PR-triggered observation established absence of workflow execution was too broad. The available commit-workflow observation endpoint is PR-trigger scoped and cannot by itself establish absence of push-triggered execution.

For commit `dc53a15612e38f32a0d10f3f972150a3ff7ef1ed`, the available status surface currently returns an empty status collection. This is evidence of `NO STATUS RECORD OBSERVED`, not proof that no GitHub Actions run exists.

## CORRECTED EVIDENCE CLASSIFICATION
Workflow definition exists: `PROVEN`
P6 regression definitions exist in workflow: `PROVEN`
Push-trigger configuration: `PROVEN`
PR-trigger configuration: `PROVEN`
Workflow dispatch configuration: `PROVEN`
Observed status record for P360 commit: `ABSENT`
Actual workflow run for P360 commit: `UNPROVEN / NOT OBSERVED BY AVAILABLE SCOPED QUERY`
P6-07 execution verification: `UNPROVEN`
P6-08/P6-09 promotion: `NOT JUSTIFIED`
Global PASS: `NOT CLAIMED`

## DECISION
Do not alter P6 canonical matrix.
Do not infer workflow non-execution from the PR-scoped observation alone.
Do not fabricate a workflow run or PASS.
Next action must obtain an actual workflow-run observation using an endpoint capable of covering the configured push trigger, then bind run/artifacts to the exact HEAD.

## LEARNING
`OBSERVATION SCOPE MUST MATCH TRIGGER SCOPE.`
A query that observes only PR-triggered runs cannot establish absence of push-triggered runs.

## MUTATION
Only this correction record is added. No Runtime, workflow, or canonical P6 mutation is performed.

## VERIFICATION
The record must be read back and its commit identity verified before closure.

## CHECKPOINT
`P361 → obtain push-trigger-capable workflow-run observation → identify run for exact HEAD → inspect jobs/artifacts → bind evidence to HEAD → classify P6-A..P6-E → reconcile → evaluate P6-08/P6-09`

## CLOSE
`CLOSED / VERIFIED / NO AUTHORITY PROMOTION`
