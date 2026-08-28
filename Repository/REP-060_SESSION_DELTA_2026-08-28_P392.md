# P392 — Exact-Head B07 Execution Channel Activation

Date: 2026-08-28
Status: `CLOSED / VERIFIED / ISOLATED / EXECUTED / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
Resumed from P391 after reviewing GOV-013, PROJECT_BOOTSTRAP, current-main state, P390/P391 evidence, and the existing PR #64 workstream.

## PRIOR-LEARNING APPLICATION
- Source coverage does not equal behavioral execution.
- Exact-head CI evidence is mandatory; `NO RUN` is neither PASS nor FAIL.
- Reuse the existing isolated PR when it represents the same workstream; do not create duplicate review paths.
- Documentation cannot promote evidence authority.
- A mutation must not be inferred solely from a `NO RUN` state; observation paths must be exhausted or their insufficiency proven first.

## VERIFIED GAP
P391 added four focused B07 regression cases, but its exact mutation commit had no observable workflow/status result. The subsequent P392 action exposed the regression through the existing pull_request audit path.

This action is recorded as a process deviation in REP-061 because the mutation was made before fully exhausting non-mutating observation options required by the P391 checkpoint.

## MINIMUM SAFE MUTATION
Updated:
`.github/workflows/full-stack-audit.yml`

Added one explicit step:
`Run P391 focused B07 mutation-boundary regression`

Command:
`python -m pip install --upgrade pytest && python -m pytest -q Quality/Integration/test_b07_matrix_gap_resolution_p391.py`

Purpose: make the already-created B07 regression observable through the existing pull_request audit channel, without changing runtime semantics, provider behavior, canonical relationships, or registry authority.

## MUTATION EVIDENCE
The workflow mutation was applied to the established isolated branch:
`hermuz/p375-rel009-minimal-b07-b08-20260828`

No `main` mutation was performed.

## EXECUTION OBSERVATION
A governed PR execution is now observable for the resulting PR merge ref. The Full-Stack Repository Audit run `33170174899` completed successfully, and its P391 step explicitly completed successfully. The Runtime Prototype and Integration workflow run `33170174898` also completed successfully across integrity, prototype, and integration jobs.

Important attribution boundary: the PR workflow checks out the generated PR merge ref `fa4c6463131915a7b51dcf5e736da18c81342427`, which merges the PR head `e3f6426803eee5be1a60341c6254e18e08350eaa` into `main`. Therefore the result is execution evidence for the governed PR merge ref, not a standalone direct-head execution claim for `e3f6426...`.

The P391 focused regression itself executed and returned `4 passed in 0.04s`.

## EVIDENCE DISPOSITION
- P391 focused test source: `VERIFIED`
- CI workflow explicitly invokes P391 test: `VERIFIED`
- Governed PR execution: `VERIFIED`
- P391 focused behavioral execution: `PASS`
- Full-stack audit: `PASS`
- Runtime prototype/integration jobs: `PASS`
- B07 behavioral closure: `NOT YET PROMOTED` pending reconciliation of merge-ref versus head attribution
- B08 real runtime dispatch: `UNPROVEN`
- REL-009 promotion: `NOT JUSTIFIED`
- Canonical mutation: `NONE`

## LEARNING
**KD-090 — When a valid regression exists but the governed CI path does not execute it explicitly, the smallest safe correction is to expose that exact regression through the existing governed execution channel rather than infer coverage from a broader audit.**

**EL-014 — CI workflow presence and CI test execution are separate evidence states.**

## PROCESS CORRECTION
The mutation decision itself is subject to the non-compliance recorded in `REP-061`: the existing P391 checkpoint required observation-path exhaustion before converting `NO RUN` into a mutation. This is a correction of execution discipline, not a new architectural learning.

## CHECKPOINT
`P392 → reconcile merge-ref execution evidence against PR-head attribution → if attribution is sufficient under GOV-013, close B07 execution matrix → otherwise repair only the evidence boundary → then controlled B08 observation → REL-009 reconciliation → promotion gate.`

## CLOSE
`CLOSED / VERIFIED / ISOLATED / EXECUTED / ATTRIBUTION-HOLD / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
