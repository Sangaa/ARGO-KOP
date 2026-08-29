# Branch Family Disposition — CI Runtime Prototype Reconciliation

Date: 2026-08-29
Baseline inspected: `main@98d78edab9cac1ab14b0e831d1c1c3ed0e585a61`

Leases:
- `R71-20260829-BRANCH-HYGIENE-064` — `ci/runtime-prototype-reconciled-20260814`
- `R71-20260829-BRANCH-HYGIENE-065` — `ci/runtime-prototype-reconciled-20260814-v2`
- `R71-20260829-BRANCH-HYGIENE-066` — `ci/runtime-prototype-reconciled-20260814-v3`
- `R71-20260829-BRANCH-HYGIENE-067` — `ci/runtime-prototype-verification`

## Evidence

The three reconciliation branches are deeply historical and differ from current main only around the early `Runtime/Prototype/cognitive_loop_harness.py` reconciliation and one historical test adjustment. Current main contains a later harness that retains the side-effect-free prototype boundary and additionally models explicit `REJECTED` state handling while preserving reversible `HOLD` semantics for absent authorization.

The verification branch is dominated by CI trigger/marker artifacts. Its own `Runtime/Prototype/CI_VERIFICATION_NOTE.md` describes itself as a `Non-executable marker for CI verification only.` It also contains older harness/acceptance-scenario variants.

## Disposition

For the three reconciliation variants:
`HISTORICAL_RUNTIME_PROTOTYPE_RECONCILIATION_STAGE / MAIN_CONTAINS_LATER_HARDENED_HARNESS / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

For `ci/runtime-prototype-verification`:
`HISTORICAL_CI_TRIGGER_AND_VERIFICATION_SCAFFOLD / NON_EXECUTABLE_MARKERS_PLUS_OLDER_RUNTIME_VARIANTS / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

## Boundary

This classification does not retroactively execution-verify old CI branches and does not claim that every historical test or trigger artifact has a one-to-one current successor. It closes only the merge/reconciliation question for these obsolete branch surfaces.

## Learning

CI trigger scaffolding is execution infrastructure evidence, not a reason to preserve an obsolete branch as a promotion unit. When the functional harness has a later mainline successor, retain the historical branch as provenance rather than replaying old trigger artifacts.
