# P2 REP-020 CURRENT-MANIFEST SYNCHRONIZATION — LEASE 195

Transaction ID: `MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195`
Lease: `R71-20260830-P2-REP020-MANIFEST-SYNC-195`
Protocol: HERMUZ / GOV-014
Status: `OPEN / PREWRITE / FUNCTIONAL MUTATION NOT YET APPLIED`
Entry head: `855089a454ceab145d0c1c7bd0fb31014218c9d9`

## Bounded purpose

Repair the fail-closed cross-artifact synchronization gap revealed by Lease 194 by rebinding the current control-plane boundary manifest to the now-current REP-012 version `1.0.10`.

The manifest is evidence, not semantic authority. This lease does not modify the REP-012 contract and does not weaken the reconciliation gate.

## Evidence basis

- REP-012 at the entry head is `Version: 1.0.10`.
- `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` still records REP-012 as `1.0.9`.
- the manifest refresh rule requires synchronization when a listed artifact materially changes identity, version, or status;
- `Quality/Integration/test_control_plane_current_manifest.py` requires the current manifest to produce no missing artifacts or mismatches and to pass its boundary gate;
- Runtime exact-head run `33310995949` failed only in the integration job while prototype and integrity jobs passed.

## Authorized functional scope

1. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`
2. `Repository/MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195_MUTATION_MATRIX.md`

Expected manifest changes are narrowly limited to:

- rebinding `Verified source baseline` to the Lease-194 functional head;
- changing only the REP-012 manifest row version from `1.0.9` to `1.0.10`;
- preserving all status, boundary, closure, and global-hold semantics.

All unrelated manifest content is `KEEP`.

## Forbidden scope

- no REP-012 semantic change;
- no gate/test weakening;
- no EJR migration, rename, delete, reassignment, or ambiguity suppression;
- no REP-016 change;
- no Release Priority 20 reopening;
- no authority promotion;
- no Priority 2, Phase 1, Connected Baseline, or global closure.

## Closure conditions

- Mutation Matrix exists before functional write;
- complete current manifest source is preserved;
- functional compare contains only the two authorized paths;
- final live parent is rechecked before `force=false` fast-forward;
- post-write read-back proves REP-012 `1.0.10` and preserved hold semantics;
- exact-head Runtime/Integration, Full-Stack, M2, and Real Matrix evidence is observed;
- Lease 194 disposition is explicitly reconciled through this corrective successor;
- session checkpoint is persisted as CLOSED / RESUME-SAFE only after verification succeeds.
