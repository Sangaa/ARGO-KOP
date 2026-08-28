# P418 — E2E Authorization Contract Repair

Date: 2026-08-28
Status: `CLOSED / SOURCE-VERIFIED / EXECUTION-PENDING`
Protocol: `GOV-013`

## RE-ENTRY
Reviewed P417 and inspected the real production E2E workflow before any mutation. The workflow constructs `ProductionExecutionCandidate` objects with `authorized=True` but without the now-required `authorization_id`, while the adapter explicitly rejects missing authorization identity.

## OBSERVED GAP
The existing `.github/workflows/p3-runtime-github-e2e.yml` was structurally stale relative to the governed `ProductionExecutionCandidate` contract. This is a concrete source-level incompatibility, not a speculative gap.

## MINIMAL REPAIR
Added the existing explicit authorization identity field to both E2E create and update candidates:
`AUTH-P3-E2E-RUNTIME-001`.

No new authorization service, no change to the authorization gate, no change to the adapter, and no canonical authority was introduced.

## SAFETY BOUNDARY
The workflow is already constrained to `e2e/runtime-srv009-*` branches and uses a non-canonical `Quality/E2E/P3_RUNTIME_SRV009_LIVE_PROBE.md` artifact. It performs create, update, read-back, and cleanup on that isolated branch. No `main` mutation is intended.

## VERIFICATION
Commit: `767db61dece648327de830d3ba5207c616da5127`
Exact-head workflow observation: `NO RUN` because the workflow is push-triggered only for `e2e/runtime-srv009-*` branches; this branch does not trigger that workflow.

Therefore this repair is `SOURCE-VERIFIED / EXECUTION-PENDING`, not PASS.

## LEARNING DISPOSITION
No new learning. Existing rule applied: when a governed contract changes, inspect executable consumers and repair only the observed incompatibility. Also distinguish workflow trigger reachability from workflow correctness.

## CLOSE
`CLOSED / MINIMAL REPAIR / SOURCE-VERIFIED / E2E EXECUTION PENDING / MAIN UNCHANGED / NO PROMOTION`

## NEXT CHECKPOINT
Trigger or otherwise obtain the dedicated E2E workflow on its permitted isolated branch, then verify exact-head create/update/read-back/cleanup evidence. Do not treat ordinary PR CI as proof of this provider-backed E2E path.
