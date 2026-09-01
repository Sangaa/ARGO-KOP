# MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E`
Protocol: `GOV-013 / GOV-014A`
Status: `PREWRITE-OPEN / EVIDENCE-BOUNDED / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `5f56a732feba08f9c808dfe2672560d6b59625e5`

## Problem / change definition

Priority 7 has completed Core local inventory and control-plane reconciliation, but material Core cross-layer dependency/consumer validation remains open.

`Core/ARGO_KERNEL.md` (`CORE-KERNEL`) is a canonical Core/Runtime Contract surface. It explicitly names `Runtime/RUN-001_BOOT_SEQUENCE.md` as the canonical runtime lifecycle definition and states that Runtime/Architecture define the implementation mechanism. `REP-014` currently contains no `CORE-KERNEL` relationship row.

The current evidence must be classified without creating a forbidden Core → Runtime architectural dependency or manufacturing reverse graph symmetry.

## Prior-learning retrieval

1. `GOV-013` relationship discipline: reference is not dependency; validate forward and reverse evidence and use the strongest justified state.
2. `Architecture/ARC-006_DEPENDENCY_MODEL.md`: Core has no architectural-layer dependency on lower layers; dependencies must not reverse the canonical layer direction without explicit authority.
   - Classification: `DIRECTLY APPLICABLE`.
3. P4 / REL-009 directional disposition: absence of a reverse dependency must not be repaired merely to manufacture graph symmetry.
   - Classification: `TRANSFERABLE`.
4. Existing critical-graph regression covers `CORE-003 ↔ RUN-001`, not the `CORE-KERNEL → RUN-001` seam.
   - Existing-test review completed; no adequate direct regression for this seam was found in current inspected scope.

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

Current strongest justified classification candidate:

`CORE-KERNEL → RUN-001 = REFERENCES / INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY`

This is a candidate until post-write CI and relationship validation complete.

## Authorized change set

| ID | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| E-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | add only one evidence-backed `CORE-KERNEL → RUN-001` REFERENCES row and bounded reconciliation note; do not create reverse dependency | N | pending |
| E-02 | `Quality/Integrity/test_core_kernel_run001_relationship_boundary.py` | CREATE | regression proving the one-way REFERENCES seam and preventing Core→Runtime `DEPENDS_ON` or manufactured reverse edge | N | pending |
| E-03 | `Core/_FOLDER_STATUS.md` | UPDATE | record one material Core cross-layer seam validated while preserving remaining P7 relationship/certification hold | N | pending |
| E-04 | `Repository/P7_CORE_KERNEL_RUN001_RELATIONSHIP_2026-09-01_E.md` | CREATE | bounded progress/evidence record | N | pending |
| E-05 | this Matrix | UPDATE | record applied state, exact CI, closure boundary and resume point | Y | in progress |

## KEEP requirements

- Do not modify `CORE-KERNEL`, `RUN-001`, `CORE-003`, `ARC-006`, or other authority documents.
- Do not classify `CORE-KERNEL → RUN-001` as `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, or runtime-executable proof.
- Do not create `RUN-001 → CORE-KERNEL` solely for symmetry.
- Preserve existing `REL-037/038` (`CORE-003 ↔ RUN-001`) unchanged.
- Do not claim all Core cross-layer relationships are validated.
- Do not close Priority 7, Core certification, Phase 1, or Global Connected Baseline.

## Pre-write validation

- Live `main` = `5f56a732feba08f9c808dfe2672560d6b59625e5`.
- Transaction D is closed and exact closure-head CI was green.
- `CORE-KERNEL`, `RUN-001`, `CORE-003`, `ARC-006`, `REP-014`, `REP-020`, current Core status and existing critical-graph test were directly inspected.
- No active `REL-062` row exists in current `REP-014` inspected relationship table.
- Current highest-value bounded seam is the canonical Core/Runtime-contract reference from `CORE-KERNEL` to `RUN-001`.

## Closure rule

Close only after target re-read and applicable Runtime/Integration, Full-Stack, Real Mutation Matrix Regression and other triggered required checks succeed on the exact closure lineage.

Priority 7 remains OPEN after this transaction; next Core seam must be recomputed from live repository evidence.
