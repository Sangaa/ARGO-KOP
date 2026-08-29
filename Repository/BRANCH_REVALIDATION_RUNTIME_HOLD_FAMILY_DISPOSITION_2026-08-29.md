# Branch Family Disposition — Historical Revalidation / Runtime-Hold Surfaces

Date: 2026-08-29

Leases:
- `R71-20260829-BRANCH-HYGIENE-083` — `reconcile/runtime-hold-current-main-20260814`
- `R71-20260829-BRANCH-HYGIENE-084` — `revalidate/main-current-20260814`
- `R71-20260829-BRANCH-HYGIENE-085` — `revalidate/p4-p6-execution-boundary-20260819`
- `R71-20260829-BRANCH-HYGIENE-086` — `revalidate/p4-p6-execution-boundary-20260819-v2`
- `R71-20260829-BRANCH-HYGIENE-087` — `revalidate/p4-p6-execution-boundary-20260819-v3`
- `R71-20260829-BRANCH-HYGIENE-088` — `revalidate/p6-execution-evidence-20260819`
- `R71-20260829-BRANCH-HYGIENE-089` — `revalidate/runtime-hold-current-main-20260814-v2`
- `R71-20260829-BRANCH-HYGIENE-090` — `revalidate/runtime-hold-current-main-20260814-v3`
- `R71-20260829-BRANCH-HYGIENE-091` — `revalidate/runtime-hold-current-main-20260814-v4`
- `R71-20260829-BRANCH-HYGIENE-092` — `revalidate/runtime-hold-current-main-20260814-v5`

## Fully ancestral refs

The following compare with `ahead_by=0` and no changed files:
- `revalidate/main-current-20260814`;
- `revalidate/p4-p6-execution-boundary-20260819`;
- `revalidate/p4-p6-execution-boundary-20260819-v2`;
- `revalidate/p4-p6-execution-boundary-20260819-v3`.

Disposition:
`FULLY_ANCESTRAL_TO_MAIN / NO_UNMERGED_WORK / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

## Historical runtime-hold variants

`reconcile/runtime-hold-current-main-20260814` and `revalidate/runtime-hold-current-main-20260814-v2/v3/v4` differ only by early variants of the side-effect-free cognitive-loop harness. Current main contains a later hardened harness with explicit reversible HOLD semantics and explicit REJECTED handling.

`revalidate/runtime-hold-current-main-20260814-v5` additionally contains one historical reconciliation EJR and an old REP-013 delta; current main has much later control-plane/content-tree state. Replaying that branch would regress current control surfaces.

Disposition for these historical variants:
`HISTORICAL_RUNTIME_HOLD_REVALIDATION_STAGE / MAIN_HAS_LATER_HARDENED_RUNTIME_AND_CONTROL_STATE / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

## P6 execution-evidence branch

`revalidate/p6-execution-evidence-20260819` differs only by two lines in the historical Full-Stack workflow. Current main's workflow is a later hardened successor: it explicitly asserts checkout SHA equals `github.sha`, emits CI execution identity, runs current bounded REL-009 semantics, and contains later P6 canonical/layered/reconciliation/runtime-lineage gates.

Disposition:
`HISTORICAL_P6_WORKFLOW_REVALIDATION_STAGE / MAIN_HAS_HARDENED_EXACT_CHECKOUT_BINDING_AND_LATER_GATES / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

## Boundary

These classifications close branch reconciliation only. They do not convert historical HOLD checkpoints into PASS and do not claim global P6 or Connected-Baseline closure.
