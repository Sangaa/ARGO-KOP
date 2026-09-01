# MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E`
Protocol: `GOV-013 / GOV-014A`
Status: `FUNCTIONAL-CANDIDATE / CI-PENDING / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `5f56a732feba08f9c808dfe2672560d6b59625e5`
Prewrite Matrix HEAD: `b7218350659b18bdb24a315879ef5a9faa9b19ee`
Relationship Candidate HEAD: `edac3f8451dbaf8b38f73e067c095caca177e8de`
Regression HEAD: `960a3edddf5d7d04fc65d308ece5b90176ec2f09`
Status Sync HEAD: `33d617e9f60ef5db9d1842e2a8d084fc09c565b7`
Progress Record HEAD: `e050ee80972f69882f075cfcbd8d0f0f71030ad9`

## Problem / change definition

Priority 7 has completed Core local inventory and control-plane reconciliation, but material Core cross-layer dependency/consumer validation remains open.

`Core/ARGO_KERNEL.md` (`CORE-KERNEL`) is a canonical Core/Runtime Contract surface. It explicitly names `Runtime/RUN-001_BOOT_SEQUENCE.md` as the canonical runtime lifecycle definition and states that Runtime/Architecture define the implementation mechanism. `REP-014` previously contained no `CORE-KERNEL` relationship row.

The current evidence was classified without creating a forbidden Core → Runtime architectural dependency or manufacturing reverse graph symmetry.

## Prior-learning retrieval

1. `GOV-013` relationship discipline: reference is not dependency; validate forward and reverse evidence and use the strongest justified state.
2. `Architecture/ARC-006_DEPENDENCY_MODEL.md`: Core has no architectural-layer dependency on lower layers; dependencies must not reverse the canonical layer direction without explicit authority.
   - Classification: `DIRECTLY APPLICABLE`.
3. P4 / REL-009 directional disposition: absence of a reverse dependency must not be repaired merely to manufacture graph symmetry.
   - Classification: `TRANSFERABLE`.
4. Existing critical-graph regression covers `CORE-003 ↔ RUN-001`, not the `CORE-KERNEL → RUN-001` seam.
   - Existing-test review completed; a direct regression gap existed for this seam.

## Evidence summary

### Forward evidence
- `CORE-KERNEL` is canonical and categorized `Core / Runtime Contract`.
- It states that the current canonical runtime sequence is defined by `Runtime/RUN-001_BOOT_SEQUENCE.md`.
- It states that the Kernel does not duplicate or supersede the Runtime lifecycle definition.
- It lists `Runtime/RUN-001_BOOT_SEQUENCE.md` under Related Authority.

### Reverse / consumer evidence
- Direct current read of `RUN-001` shows generic loading of applicable Core artifacts but does not identify `CORE-KERNEL` as a required consumer/dependency.
- Current repository searches for `ARGO_KERNEL` / `Core/ARGO_KERNEL.md` in Runtime-facing evidence did not establish a specific `RUN-001 → CORE-KERNEL` dependency or consumption contract.
- Therefore reverse dependency/consumer promotion is not justified by current evidence.

### Architecture boundary
- `ARC-006`: `Core — Depends on: None at the architectural layer level`.
- Therefore `CORE-KERNEL → RUN-001 = DEPENDS_ON` would invert the validated layer dependency model and is prohibited absent explicit architectural authority.

Applied classification:

`CORE-KERNEL → RUN-001 = REFERENCES / INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY`

This remains bounded by post-write CI and relationship validation.

## Authorized change set

| ID | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| E-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | add only one evidence-backed `CORE-KERNEL → RUN-001` REFERENCES row and bounded reconciliation note; do not create reverse dependency | Y | candidate |
| E-02 | `Quality/Integrity/test_core_kernel_run001_relationship_boundary.py` | CREATE | regression proving the one-way REFERENCES seam and preventing Core→Runtime `DEPENDS_ON` or manufactured reverse edge | Y | candidate |
| E-03 | `Core/_FOLDER_STATUS.md` | UPDATE | record one material Core cross-layer seam validated while preserving remaining P7 relationship/certification hold | Y | candidate |
| E-04 | `Repository/P7_CORE_KERNEL_RUN001_RELATIONSHIP_2026-09-01_E.md` | CREATE | bounded progress/evidence record | Y | candidate |
| E-05 | this Matrix | UPDATE | record applied state, exact CI, closure boundary and resume point | Y | in progress |

## KEEP requirements

- `CORE-KERNEL`, `RUN-001`, `CORE-003`, `ARC-006`, and other authority documents were not modified.
- `CORE-KERNEL → RUN-001` was not classified as `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, or runtime-executable proof.
- No `RUN-001 → CORE-KERNEL` relationship was created solely for symmetry.
- Existing `REL-037/038` (`CORE-003 ↔ RUN-001`) remain unchanged.
- The transaction does not claim all Core cross-layer relationships are validated.
- Priority 7, Core certification, Phase 1, and Global Connected Baseline remain open/unclaimed.

## Pre-write validation

- Live `main` = `5f56a732feba08f9c808dfe2672560d6b59625e5` at transaction entry.
- Transaction D was closed with exact closure-head CI green.
- `CORE-KERNEL`, `RUN-001`, `CORE-003`, `ARC-006`, `REP-014`, `REP-020`, current Core status and existing critical-graph test were directly inspected.
- No active `REL-062` row existed in the inspected relationship table before mutation.
- Current highest-value bounded seam was the canonical Core/Runtime-contract reference from `CORE-KERNEL` to `RUN-001`.

## Post-write validation

- `REP-014` re-read confirms `REL-062` exactly as one-way `REFERENCES / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY` and preserves `REL-037/038`.
- Direct regression added under `Quality/Integrity` and explicitly rejects `DEPENDS_ON`, `CONSUMES`, `IMPLEMENTS`, and a manufactured `RUN-001 → CORE-KERNEL` row.
- Core status advanced to v1.3.3 while retaining `INTEGRITY HOLD — CONTROL PLANE RECONCILED / CROSS-LAYER VALIDATION OPEN`.
- Progress record preserves Priority-7 open boundary.

## CI validation pending

Require exact-head review of all triggered applicable checks, including Runtime/Integration, Full-Stack, Real Mutation Matrix Regression, M2 where triggered, and the new integrity regression path.

## Closure rule

Close only after target re-read and applicable required checks succeed on the exact closure lineage.

Priority 7 remains OPEN after this transaction; next Core seam must be recomputed from live repository evidence.
