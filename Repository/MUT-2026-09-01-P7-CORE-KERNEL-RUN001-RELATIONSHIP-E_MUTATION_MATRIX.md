# MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E`
Protocol: `GOV-013 / GOV-014A`
Status: `CI-HARD-HOLD / ROOT-CAUSE-CLASSIFIED / REPAIR-AUTHORIZED / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `5f56a732feba08f9c808dfe2672560d6b59625e5`
Prewrite Matrix HEAD: `b7218350659b18bdb24a315879ef5a9faa9b19ee`
Relationship Candidate HEAD: `edac3f8451dbaf8b38f73e067c095caca177e8de`
Regression HEAD: `960a3edddf5d7d04fc65d308ece5b90176ec2f09`
Status Sync HEAD: `33d617e9f60ef5db9d1842e2a8d084fc09c565b7`
Progress Record HEAD: `e050ee80972f69882f075cfcbd8d0f0f71030ad9`
Initial Matrix Candidate HEAD: `9f03dc9567f881a7899110b7650fb7b304bfd693`

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
5. `Memory/Engineering_Journal/EJR-179_2026-08-16_FOLDER_INVENTORY_IDENTITY_DRIFT_LEARNING.md`: an integrity assertion must target the semantic authority boundary being tested instead of freezing incidental/historical wording.
   - Classification for this CI failure: `TRANSFERABLE`.

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

## Authorized change set

| ID | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| E-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | add only one evidence-backed `CORE-KERNEL → RUN-001` REFERENCES row and bounded reconciliation note; do not create reverse dependency | Y | candidate |
| E-02 | `Quality/Integrity/test_core_kernel_run001_relationship_boundary.py` | CREATE/REPAIR | regression proving the one-way REFERENCES seam; repair only brittle prose assertion exposed by CI while preserving semantic guards | Y | repair authorized |
| E-03 | `Core/_FOLDER_STATUS.md` | UPDATE | record one material Core cross-layer seam validated while preserving remaining P7 relationship/certification hold | Y | candidate |
| E-04 | `Repository/P7_CORE_KERNEL_RUN001_RELATIONSHIP_2026-09-01_E.md` | CREATE | bounded progress/evidence record | Y | candidate |
| E-05 | this Matrix | UPDATE | record applied state, CI hard hold, root cause, repair and eventual closure evidence | Y | in progress |

## KEEP requirements

- `CORE-KERNEL`, `RUN-001`, `CORE-003`, `ARC-006`, and other authority documents must not be modified for this CI repair.
- `CORE-KERNEL → RUN-001` must not be classified as `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, or runtime-executable proof.
- No `RUN-001 → CORE-KERNEL` relationship may be created solely for symmetry.
- Existing `REL-037/038` (`CORE-003 ↔ RUN-001`) remain unchanged.
- The transaction does not claim all Core cross-layer relationships are validated.
- Priority 7, Core certification, Phase 1, and Global Connected Baseline remain open/unclaimed.

## CI hard-hold diagnosis

Initial matrix candidate HEAD `9f03dc9567f881a7899110b7650fb7b304bfd693`:

- Runtime/Integration run `33479748723` = `FAILURE`.
- `prototype-tests` = `SUCCESS`.
- `integrity-tests` = `SUCCESS`.
- failing job: `integration-tests` / `99766502846`.
- first failing step boundary: `Run integration quality suite`.

Deterministic source-level reproduction of the new regression establishes the first failing assertion in `test_core_kernel_references_run001_without_dependency_inversion()`:

- relationship-row assertion passes against current `REP-014`;
- path-presence assertion passes against current `CORE-KERNEL`;
- the next assertion expects the exact prose substring `current canonical runtime sequence defined by ...`;
- the canonical source says `The current canonical runtime sequence defined by ...`.

Root cause: `BRITTLE REGRESSION / PROSE-LEVEL STRING OVERREACH`.

This is not evidence that REL-062 is incorrect. The regression froze incidental sentence wording beyond the semantic boundary it was intended to protect.

Minimal authorized repair:

- keep the direct RUN-001 reference assertion;
- replace the brittle sentence-fragment assertion with durable semantic evidence that `CORE-KERNEL` does not duplicate or supersede the Runtime lifecycle definition;
- preserve all dependency-inversion and reverse-edge negative guards.

## Pre-write validation

- Live `main` = `5f56a732feba08f9c808dfe2672560d6b59625e5` at transaction entry.
- Transaction D was closed with exact closure-head CI green.
- `CORE-KERNEL`, `RUN-001`, `CORE-003`, `ARC-006`, `REP-014`, `REP-020`, current Core status and existing critical-graph test were directly inspected.
- No active `REL-062` row existed in the inspected relationship table before mutation.

## Post-write validation before repair

- `REP-014` re-read confirms `REL-062` exactly as one-way `REFERENCES / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY` and preserves `REL-037/038`.
- Core status advanced to v1.3.3 while retaining `INTEGRITY HOLD — CONTROL PLANE RECONCILED / CROSS-LAYER VALIDATION OPEN`.
- Progress record preserves Priority-7 open boundary.

## Recovery validation pending

After the E-02 minimal regression repair, require target re-read and exact-head review of all triggered applicable checks, including Runtime/Integration, Full-Stack, Real Mutation Matrix Regression and M2 where triggered.

## Closure rule

Close only after the recovery lineage and final closure write both receive applicable required CI success.

Priority 7 remains OPEN after this transaction; next Core seam must be recomputed from live repository evidence.
