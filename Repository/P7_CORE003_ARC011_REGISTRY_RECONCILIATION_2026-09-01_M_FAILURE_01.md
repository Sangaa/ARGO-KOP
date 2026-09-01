# P7 Transaction M — Failure Evidence 01

Date: 2026-09-01
Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M`
Failed candidate: `7ddb174f34019239e1806f8d724be02bc1309ed0`
State: `FAILURE PRESERVED / ROOT CAUSE CLASSIFIED / RECOVERY REQUIRED`

## Observed result

Three required workflows succeeded on the exact candidate HEAD:

- M2 Multi-Channel Proposal Training — `33519622054` — SUCCESS.
- Real Mutation Matrix Regression — `33519622023` — SUCCESS.
- Full-Stack Repository Audit — `33519622141` — SUCCESS.

ARGO Runtime Prototype and Integration Tests — `33519622061` — FAILURE.

Job-level evidence narrows the failure:

- `prototype-tests` — SUCCESS.
- `integration-tests` — SUCCESS.
- `integrity-tests` — FAILURE at `Run repository integrity gates`.

## Root cause

The newly rebound focused regression introduced an assertion for the phrase `Highest governing rules`, while current CORE-003 contains the exact sentence `The Constitution defines the highest governing rules of the ARGO Platform.`. The assertion was case-sensitive and therefore failed despite the underlying authority evidence being unchanged and correctly present.

This is classified as `TEST-ASSERTION DEFECT / EVIDENCE-MATCH CASE DRIFT`, not a source-authority contradiction and not a relationship-semantic failure.

## Learning

When converting a validation-first regression into a registered-relationship regression, preserve already-proven exact source assertions unless the source itself changed. Rephrasing an assertion during a registry-only transaction creates avoidable test drift and can falsely convert valid evidence into a failed integrity gate.

## Disposition

Failure is retained as evidence. Candidate `7ddb174...` is not promoted to closed/success. Transaction M Work Lease remains OPEN/HOLD pending a governed recovery. Recovery may change only the focused test assertion and transaction/matrix evidence required to bind the repair; no source-authority or relationship semantics may be altered to make the test pass.
