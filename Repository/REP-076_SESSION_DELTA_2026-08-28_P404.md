# P404 — Observed P403 Contract Failure Repair

Date: 2026-08-28
Status: `CLOSED / REPAIR-APPLIED / EXECUTION-PENDING / NO CANONICAL MUTATION`
Protocol: `GOV-013`

## PRE-EXECUTION ANALYSIS
P403 was not treated as a generic failure. Exact CI observation showed 304 passed and one focused B08 test failed with `TypeError: ProductionExecutionCandidate.__init__() got an unexpected keyword argument 'authorization_id'`. The failure is inside the isolated handoff candidate contract, not connected-spine reachability.

Prior learning applied: first failure boundary, exact-head attribution, repair only observed failures, mutation matrix before protected change, and no promotion from isolated evidence.

## REPAIR
Updated `Services/ENG006_SRV009_PRODUCTION_ADAPTER.py` so `ProductionExecutionCandidate` explicitly preserves `authorization_id` emitted by `build_handoff_candidate`, and `execute_update` rejects a missing authorization identity before governed dispatch.

Added mutation matrix:
`Repository/MUT-2026-08-28-P404-P403_AUTH_ID_MUTATION_MATRIX.md`

No connected-spine, canonical registry, provider, or main-branch mutation was performed.

## EXPECTED VERIFICATION
The required proof is exact-head CI on the resulting commit. P404 is not declared execution-closed until the focused failure is re-run and the full regression remains green.

## DISPOSITION
`SOURCE-REPAIR-VERIFIED`
`CI-REPAIR-EXECUTION-PENDING`
`B08-LIVE-DISPATCH-UNPROVEN`
`PROMOTION-NOT-JUSTIFIED`
`CANONICAL-UNCHANGED`

## CHECKPOINT
`P404 -> exact-head CI -> first-failure reconciliation -> if green, close repair -> reassess live RUN-010 caller only after proof gate.`
