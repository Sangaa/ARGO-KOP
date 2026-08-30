# P2 REP-020 CURRENT-MANIFEST SYNCHRONIZATION — LEASE 195

Transaction ID: `MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195`
Lease: `R71-20260830-P2-REP020-MANIFEST-SYNC-195`
Protocol: HERMUZ / GOV-014
Status: `CLOSED / EXECUTION-VERIFIED / RESUME-SAFE`
Entry head: `855089a454ceab145d0c1c7bd0fb31014218c9d9`
Prewrite head: `33d983a9edb1c09f85277020f915a38829474d2e`
Functional head: `6bfd767d436eb29c1812f362035b7cfdaa193544`

## Bounded purpose

Repair the fail-closed cross-artifact synchronization gap revealed by Lease 194 by rebinding the current control-plane boundary manifest to the current REP-012 version `1.0.10`.

The manifest remains evidence, not semantic authority. This lease did not modify the REP-012 contract and did not weaken the reconciliation gate.

## Evidence basis

At the Lease-194 functional head:

- REP-012 was `Version: 1.0.10`;
- `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` still recorded REP-012 as `1.0.9`;
- the manifest refresh rule required synchronization after a listed identity/version/status mutation;
- `Quality/Integration/test_control_plane_current_manifest.py` correctly required zero mismatches and `boundary_pass = True`;
- Runtime run `33310995949` therefore failed closed in the integration job while prototype and integrity jobs passed.

Classification:

`CROSS-ARTIFACT CURRENT-MANIFEST SYNCHRONIZATION GAP / CORRECT FAIL-CLOSED DETECTION`.

## Applied functional scope

Exactly two paths changed at `6bfd767d436eb29c1812f362035b7cfdaa193544`:

1. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`
2. `Repository/MUT-2026-08-30-P2-REP020-CURRENT-MANIFEST-SYNC-195_MUTATION_MATRIX.md`

Source current-manifest blob: `41fd422abb52ca97471089db0da06fdb14d01991`.
Candidate/current manifest blob: `fe628c365a932cc1e8847813dbf928d6c9c7e9af`.

The manifest change was limited to:

- `Verified source baseline` → `main@855089a454ceab145d0c1c7bd0fb31014218c9d9`;
- REP-012 row version `1.0.9` → `1.0.10`;
- all status, boundary, closure, and global-hold semantics preserved unchanged.

## Exact-head verification

At functional head `6bfd767d436eb29c1812f362035b7cfdaa193544`:

- Full-Stack Repository Audit `33314345499` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33314345432` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33314345448` — `SUCCESS`.
- Real Mutation Matrix Regression `33314345446` — `SUCCESS`.

The previously failing Runtime/Integration path turned green without any REP-012 rollback, gate weakening, or test weakening.

## Lease 194 disposition

Lease 194 is accepted and closed through this governed corrective successor. Its original Runtime failure is retained as evidence of the synchronization gap rather than erased or reinterpreted.

Disposition:

`LEASE 194 FUNCTIONAL CONTRACT ACCEPTED / LEASE 195 MANIFEST CONSUMER SYNCHRONIZED / ORIGINAL FAIL-CLOSED EVIDENCE PRESERVED`.

## Learned rule

**A material identity/version/status mutation of an artifact listed in the current control-plane manifest is not verification-complete until the manifest consumer is synchronized in a governed change and the manifest-driven gate passes.**

This is a synchronization obligation, not permission to weaken the gate or downgrade the mutated source.

## Preserved boundaries

- no REP-012 semantic change in Lease 195;
- no gate/test weakening;
- no EJR migration, rename, delete, reassignment, or ambiguity suppression;
- REP-016 unchanged;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- Phase 1 remains `OPEN`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.
