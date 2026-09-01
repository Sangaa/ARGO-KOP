# MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E`
Protocol: `GOV-013 / GOV-014A`
Status: `FUNCTIONAL-CLOSED / CI-VERIFIED / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `5f56a732feba08f9c808dfe2672560d6b59625e5`
Prewrite Matrix HEAD: `b7218350659b18bdb24a315879ef5a9faa9b19ee`
Relationship Candidate HEAD: `edac3f8451dbaf8b38f73e067c095caca177e8de`
Regression HEAD: `960a3edddf5d7d04fc65d308ece5b90176ec2f09`
Status Sync HEAD: `33d617e9f60ef5db9d1842e2a8d084fc09c565b7`
Initial Matrix Candidate HEAD: `9f03dc9567f881a7899110b7650fb7b304bfd693`
First Repair HEAD: `cf42f7a19e61438227987c8d1725974b484c4fbb`
Second Repair HEAD: `a97bbad064ec7b02e8a5e9a23b9ab3abc07b9523`
Third Repair Content HEAD: `521dfcaa8da50543b6dceb44de1bc8aa2ec5c8a2`
E-07B Authorization HEAD: `2271d130d7bb3583a695d0bd4e4bddac8e235818`
Atomic Recovery HEAD: `5e3020fe8c1bea33479edd1382c592aac3a7e64a`
Closure-Lineage HEAD: `adf8a10774ab8cf20b05aef2c66296b1f1054d6d`

## Problem / relationship result

Priority 7 remains open. This bounded transaction reconciles only:

`CORE-KERNEL → RUN-001 = REFERENCES / INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY`

ARC-006 prevents promotion to a Core → Runtime architectural dependency. Direct reverse review did not prove a specific `RUN-001 → CORE-KERNEL` dependency/consumer edge, so no reverse edge was manufactured for symmetry.

## Prior-learning retrieval

1. `GOV-013`: reference is not dependency; validate both directions and use only the strongest justified relationship state.
2. `Architecture/ARC-006_DEPENDENCY_MODEL.md`: Core has no architectural-layer dependency on lower layers — `DIRECTLY APPLICABLE`.
3. P4 / REL-009 one-way relationship rule — `TRANSFERABLE`.
4. `EJR-179_2026-08-16_FOLDER_INVENTORY_IDENTITY_DRIFT_LEARNING.md` — semantic-boundary assertions over incidental wording — `TRANSFERABLE` for holds #1/#2.
5. `MUT-2026-08-29-CURRENT-CONTROL-PLANE-MANIFEST-REBIND-010.md` — refresh current evidence manifest on listed identity/version/status drift — `DIRECTLY APPLICABLE` for hold #3.
6. `MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-REPAIR-187.md` — prewrite Matrix presence is not exact same-change-set binding; failed binding needs governed recovery — `DIRECTLY APPLICABLE` for hold #4.

## Authorized / applied change set

| ID | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| E-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | add only evidence-backed REL-062 one-way REFERENCES row and bounded reconciliation note | Y | CI-verified |
| E-02 | `Quality/Integrity/test_core_kernel_run001_relationship_boundary.py` | CREATE/REPAIR | direct seam regression; durable semantic boundary after brittle assertion repair | Y | CI-verified |
| E-03 | `Core/_FOLDER_STATUS.md` | UPDATE | record one validated bounded seam while preserving remaining P7/certification hold | Y | CI-verified |
| E-04 | `Repository/P7_CORE_KERNEL_RUN001_RELATIONSHIP_2026-09-01_E.md` | CREATE/UPDATE | bounded progress, learning, recovery and closure evidence | Y | CI-verified |
| E-05 | this Matrix | UPDATE | record hard holds, repairs, recovery and closure evidence | Y | CI-verified |
| E-06 | `Quality/Integration/test_core_p7_status_sync.py` | UPDATE | accept truthful bounded-progress wording while preserving P7-open/certification/no-global-close guards | Y | CI-verified |
| E-07 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | refresh REP-014 `1.2.6 → 1.2.7` | Y | content valid; original commit same-change-set binding failed |
| E-07B | current manifest + this Matrix | ATOMIC REBIND | bind protected manifest and Matrix in one exact Git change set | Y | CI-verified |

## KEEP requirements

- No modification of `CORE-KERNEL`, `RUN-001`, `CORE-003`, `ARC-006`, or other authority text for repair.
- REL-062 remains `REFERENCES`, not `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, or executable proof.
- No `RUN-001 → CORE-KERNEL` edge solely for symmetry.
- REL-037/038 unchanged.
- Remaining material Core dependency/consumer validation, REP-014 reconciliation, and explicit final Core certification remain open.
- Phase 1, repository-wide graph, broader Connected Baseline, and Global integrity are not closed/promoted by this transaction.
- Historical current-manifest snapshots are not rewritten.
- Failed E-07 same-change-set commit remains failure evidence and is not retroactively promoted.
- Priority 7 remains OPEN.

## CI hard hold #1

HEAD `9f03dc9567f881a7899110b7650fb7b304bfd693` — Runtime/Integration `33479748723` FAILURE; integration job `99766502846`.

Root cause: `BRITTLE REGRESSION / PROSE-LEVEL STRING OVERREACH`.

Repair: E-02 protected the durable Kernel lifecycle-boundary semantics rather than incidental prose.

## CI hard hold #2

HEAD `cf42f7a19e61438227987c8d1725974b484c4fbb` — Runtime/Integration `33480178768` FAILURE; integration job `99767817143`.

Root cause: `STALE REGRESSION / TRANSIENT STATUS-WORDING OVERREACH`.

Repair: E-06 changed only the stale remaining-work phrase while preserving REP-014, certification, P7-open and no-global-close guards.

## CI hard hold #3

HEAD `a97bbad064ec7b02e8a5e9a23b9ab3abc07b9523` — Runtime/Integration `33480949106` FAILURE; integration job `99770211931`.

Root cause: `REAL COMPANION EVIDENCE DRIFT / CURRENT-MANIFEST FRESHNESS VIOLATION`.

REP-014 was live at v1.2.7 while `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` still listed v1.2.6. E-07 refreshed the non-authoritative current manifest. Content HEAD `521dfcaa8da50543b6dceb44de1bc8aa2ec5c8a2` restored Runtime/Integration `33484577149` SUCCESS and M2 `33484577142` SUCCESS.

## CI hard hold #4

Content HEAD `521dfcaa8da50543b6dceb44de1bc8aa2ec5c8a2` — Full-Stack `33484577144` FAILURE; job `99781570872`; first failing step `Enforce Mutation Matrix on current change set`.

Root cause: `SAME-CHANGE-SET MATRIX BINDING VIOLATION / WRITE-SURFACE ATOMICITY GAP`.

The protected manifest was semantically correct, but its single-file Contents commit did not include the Matrix in the exact diff. Following directly applicable recovery 187, E-07B used Git blob/tree/commit operations and `force=false` fast-forward from authorization HEAD `2271d130d7bb3583a695d0bd4e4bddac8e235818`.

Atomic Recovery HEAD `5e3020fe8c1bea33479edd1382c592aac3a7e64a` changed exactly:
1. this Matrix;
2. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`.

Unexpected paths: `0`.

## Recovery CI evidence

Exact recovery HEAD `5e3020fe8c1bea33479edd1382c592aac3a7e64a`:
- Runtime/Integration `33485141412` — SUCCESS.
- Full-Stack Repository Audit `33485141368` — SUCCESS.
- M2 `33485141342` — SUCCESS.
- Real Mutation Matrix Regression `33485141435` — SUCCESS.

## Closure-lineage CI evidence

Exact closure-lineage HEAD `adf8a10774ab8cf20b05aef2c66296b1f1054d6d`:
- Runtime/Integration `33485367772` — SUCCESS.
- Full-Stack Repository Audit `33485367631` — SUCCESS.
- M2 `33485367723` — SUCCESS.
- Real Mutation Matrix Regression `33485367670` — SUCCESS.

All four discovered failure causes are repaired without authority promotion or P7/global closure.

## Closure decision

`TRANSACTION E = FUNCTIONAL-CLOSED / CI-VERIFIED / P7-OPEN`.

This closure applies only to the bounded `CORE-KERNEL → RUN-001` relationship reconciliation transaction. It does not certify Core or close Priority 7.

## Next legal action

Re-read live main and recompute the next material Core authority dependency/consumer seam from current repository evidence. Reconcile REP-014 only where evidence requires. Do not claim Core certification, Phase-1 closure, repository-wide graph closure, or Global Connected Baseline PASS.
