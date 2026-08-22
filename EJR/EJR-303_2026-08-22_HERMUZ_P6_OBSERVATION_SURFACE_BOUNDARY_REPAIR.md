# EJR-303 — HERMUZ P6 Observation-Surface Boundary Repair

Date: 2026-08-22
Status: Closed — Mutation + Verification Record

## 1. Trigger

Recent GitHub-channel experiments established three distinct outcomes:

- an observation surface can return an empty result;
- a resource/surface can return not-found;
- the connector can reject an endpoint before GitHub evidence is obtained.

These outcomes must not collapse into the same P6 state.

## 2. Prior-learning used

The current P6 reconciliation engine previously treated `run_id is None` as `NO_OBSERVATION`. That is correct only when the observation surface was successfully queried and the resulting evidence set contained no execution identity.

The newer learning established:

`NO OBSERVATION ≠ OBSERVATION SURFACE UNAVAILABLE ≠ OBSERVATION SURFACE REJECTED`

This is an evidence-boundary repair, not a claim that the GitHub execution root cause has been solved.

## 3. Mutation

`Quality/Integration/p6_reconciliation.py` now carries an explicit `observation_state` with default `OBSERVED` for backward compatibility.

New deterministic classifications:

- `SURFACE_UNAVAILABLE` → `OBSERVATION_SURFACE_UNAVAILABLE`
- `SURFACE_REJECTED` → `OBSERVATION_SURFACE_REJECTED`
- unknown observation state → `OBSERVATION_STATE_UNKNOWN`
- `EMPTY_RESULT` with no run identity → `NO_OBSERVATION`

Existing execution/identity/artifact boundaries remain unchanged.

## 4. Regression protection

`Quality/Integration/test_p6_reconciliation_boundaries.py` now verifies that surface failures are never collapsed into `NO_OBSERVATION`, while preserving the previous P6-08/P6-09 cases.

## 5. Verification

Repository read-back completed for both mutated files.

Local controlled execution of the exact updated decision logic exercised all nine regression cases: **9/9 passed**.

This local result is `CONTROLLED_SYNTHETIC` evidence only. It does not promote to canonical repository or runtime execution evidence.

The repository's Full-Stack workflow is configured on pushes to `main`, but the available `fetch_commit_workflow_runs` connector surface only returns pull-request-triggered runs. Therefore an empty result from that specific call cannot prove that the push-triggered workflow did not execute.

A direct combined-status query for the new commit returned an empty status set. This is likewise `NO_OBSERVATION`, not proof of non-execution.

## 6. Commit / integrity

Engine mutation commit: `d51363e5483864148345d0431c4af14b17c7a4e9`

Regression-test mutation commit: `f6296688e9373a123bc2cb9bedc9e818b9f66972`

Final engine blob SHA after read-back: `20085761d35f6bd3ab5ca9d01f2604d0b85a1144`

Final regression-test blob SHA after read-back: `436c75a5f06817a4962ba05a4f2e1d1d4b88cb19`

## 7. Learning

The diagnostic method itself is part of the system being tested. When an observation result is empty, first classify whether the observer successfully operated. Only then interpret the absence of returned evidence.

This prevents an observer capability boundary from becoming a false statement about repository reality.

## 8. Closure

Mutation: COMPLETE
Read-back: VERIFIED
Controlled regression: PASS (9/9)
Canonical CI execution: NOT VERIFIED
P6 root cause: NOT CLAIMED
Production relationship authority: UNCHANGED

Session step: `CLOSED — DOCUMENTED — VERIFIED TO AVAILABLE EVIDENCE LEVEL`.
