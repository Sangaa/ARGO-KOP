# P2 REP-012 PRE-ALLOCATION VACANCY BINDING — LEASE 194

Transaction ID: `MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
Lease: `R71-20260830-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
Protocol: HERMUZ / GOV-014
Status: `CLOSED / FUNCTIONAL ACCEPTED VIA CORRECTIVE SUCCESSOR 195 / RESUME-SAFE`
Entry head: `b2eb68d7bb2dd5831ac5009103faba66b4922f6f`
Functional head: `855089a454ceab145d0c1c7bd0fb31014218c9d9`
Corrective successor functional head: `6bfd767d436eb29c1812f362035b7cfdaa193544`

## Bounded purpose

Bind the execution-verified EJR vacancy proof from Lease 193 into the REP-012 allocation control contract so an EJR identity candidate cannot reach `ALLOCATE` merely because the current tree appears unused.

This lease is control-plane binding only.

## Evidence basis

Lease 193 established an execution-verified vacancy gate with decisions `OCCUPIED`, `HISTORY_INCOMPLETE`, and `VACANT` across qualified Document ID metadata, first-H1 identity, filename prefix, and all locally reachable Git history.

REP-012 v1.0.9 previously began its material mutation sequence with:

`ALLOCATE → READ → VERIFY IDENTITY → ...`

That sequence lacked an explicit pre-allocation vacancy proof for new EJR identities.

## Applied functional scope

Exactly two paths changed at `855089a454ceab145d0c1c7bd0fb31014218c9d9`:

1. `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
2. `Repository/MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194_MUTATION_MATRIX.md`

REP-012 advanced to `1.0.10` and now requires vacancy proof before allocation for new EJR identity candidates, with fail-closed `HISTORY_INCOMPLETE` semantics and bounded locally reachable-history scope.

## Verification history and corrective disposition

Original exact-head evidence at `855089a454ceab145d0c1c7bd0fb31014218c9d9`:

- Full-Stack `33310995932` — SUCCESS.
- M2 `33310995989` — SUCCESS.
- Real Matrix `33310995957` — SUCCESS.
- Runtime/Integration `33310995949` — FAILURE in the integration job only.

The failure was preserved and diagnosed. It was caused by `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` still recording REP-012 as `1.0.9`; the current-manifest reconciliation gate correctly failed closed.

Lease 195 synchronized that required consumer without modifying REP-012 or weakening the gate. Exact-head evidence at corrective successor `6bfd767d436eb29c1812f362035b7cfdaa193544`:

- Full-Stack `33314345499` — SUCCESS.
- Runtime/Integration `33314345432` — SUCCESS.
- M2 `33314345448` — SUCCESS.
- Real Matrix `33314345446` — SUCCESS.

Disposition:

`LEASE 194 FUNCTIONAL CONTRACT ACCEPTED / ORIGINAL FAILURE RETAINED AS CROSS-ARTIFACT SYNCHRONIZATION EVIDENCE / CLOSED VIA GOVERNED CORRECTIVE SUCCESSOR 195`.

## Learned rule

**A material identity/version/status mutation of an artifact listed in the current control-plane manifest is not verification-complete until the manifest consumer is synchronized in a governed change and the manifest-driven gate passes.**

This is a synchronization obligation, not permission to weaken the gate or downgrade the mutated source.

## Preserved boundaries

- no EJR content/path/identity migration;
- no rename, delete, reassignment, or replacement EJR allocation;
- no ambiguity suppression or detector-membership reduction;
- REP-016 unchanged;
- Release Priority 20 not reopened;
- no authority promotion;
- Priority 2 historical/provenance scope remains OPEN;
- Phase 1 remains OPEN;
- Global Connected Baseline remains OPEN;
- Global `BOOTED / INTEGRITY PASS` remains NOT CLAIMED.
