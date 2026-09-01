# MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E`
Protocol: `GOV-013 / GOV-014A`
Status: `CI-HARD-HOLD / SECOND-ROOT-CAUSE-CLASSIFIED / E-06-REPAIR-AUTHORIZED / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `5f56a732feba08f9c808dfe2672560d6b59625e5`
Prewrite Matrix HEAD: `b7218350659b18bdb24a315879ef5a9faa9b19ee`
Relationship Candidate HEAD: `edac3f8451dbaf8b38f73e067c095caca177e8de`
Regression HEAD: `960a3edddf5d7d04fc65d308ece5b90176ec2f09`
Status Sync HEAD: `33d617e9f60ef5db9d1842e2a8d084fc09c565b7`
Progress Record HEAD: `e050ee80972f69882f075cfcbd8d0f0f71030ad9`
Initial Matrix Candidate HEAD: `9f03dc9567f881a7899110b7650fb7b304bfd693`
First Repair HEAD: `cf42f7a19e61438227987c8d1725974b484c4fbb`

## Problem / change definition

Priority 7 has completed Core local inventory and control-plane reconciliation, but material Core cross-layer dependency/consumer validation remains open.

`Core/ARGO_KERNEL.md` (`CORE-KERNEL`) is a canonical Core/Runtime Contract surface. It explicitly names `Runtime/RUN-001_BOOT_SEQUENCE.md` as the canonical runtime lifecycle definition. Current evidence justifies one bounded registry relationship without creating a forbidden Core → Runtime architectural dependency or manufacturing reverse graph symmetry.

Applied relationship candidate:

`CORE-KERNEL → RUN-001 = REFERENCES / INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY`

## Prior-learning retrieval

1. `GOV-013`: reference is not dependency; validate both directions and use only the strongest justified relationship state.
2. `Architecture/ARC-006_DEPENDENCY_MODEL.md`: Core has no architectural-layer dependency on lower layers. Classification: `DIRECTLY APPLICABLE`.
3. P4 / REL-009: do not manufacture reverse graph symmetry where evidence is absent. Classification: `TRANSFERABLE`.
4. `EJR-179_2026-08-16_FOLDER_INVENTORY_IDENTITY_DRIFT_LEARNING.md`: integrity assertions must target semantic authority boundaries rather than transient/incidental wording. Classification for both CI regressions: `TRANSFERABLE`.

## Evidence boundary

- `CORE-KERNEL` explicitly references the canonical RUN-001 lifecycle and says it does not duplicate or supersede it.
- Direct RUN-001 review plus reverse searches do not establish a specific RUN-001 → CORE-KERNEL consumer/dependency edge.
- ARC-006 prevents interpreting the forward documentary alignment as Core → Runtime architectural `DEPENDS_ON`.
- Existing REL-037/038 (`CORE-003 ↔ RUN-001`) remain separate and unchanged.

## Authorized change set

| ID | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| E-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | add only evidence-backed REL-062 one-way REFERENCES row and bounded reconciliation note | Y | candidate |
| E-02 | `Quality/Integrity/test_core_kernel_run001_relationship_boundary.py` | CREATE/REPAIR | direct seam regression; repair first brittle prose assertion only | Y | source-revalidated |
| E-03 | `Core/_FOLDER_STATUS.md` | UPDATE | record one validated bounded seam while preserving remaining P7/certification hold | Y | candidate |
| E-04 | `Repository/P7_CORE_KERNEL_RUN001_RELATIONSHIP_2026-09-01_E.md` | CREATE/UPDATE | bounded progress and eventual CI record | Y | candidate |
| E-05 | this Matrix | UPDATE | record hard holds, repairs, exact CI and closure evidence | Y | in progress |
| E-06 | `Quality/Integration/test_core_p7_status_sync.py` | UPDATE | preserve the durable P7 remaining-work boundary without freezing the pre-E exact wording; accept current truthful `continued ... remaining material Core authority relationships` state while still requiring REP-014 and final certification to remain open | N | pending |

## KEEP requirements

- Do not modify `CORE-KERNEL`, `RUN-001`, `CORE-003`, `ARC-006`, or other authority documents for CI repair.
- Do not promote REL-062 to `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, or executable proof.
- Do not add `RUN-001 → CORE-KERNEL` merely for symmetry.
- Preserve REL-037/038 unchanged.
- E-06 must not weaken the P7 hold: remaining material dependency/consumer validation, REP-014 reconciliation, explicit final Core certification, and no Phase-1/global closure must still be asserted.
- Priority 7 remains OPEN.

## CI hard hold #1

Initial matrix candidate HEAD `9f03dc9567f881a7899110b7650fb7b304bfd693`:
- Runtime/Integration `33479748723` = FAILURE.
- prototype = SUCCESS; integrity = SUCCESS.
- failing job `integration-tests` / `99766502846`.
- failing step `Run integration quality suite`.

Deterministic source-order reproduction identified the new E-02 assertion that froze `current canonical runtime sequence defined by ...` while canonical source says `The current canonical ...`.

Root cause: `BRITTLE REGRESSION / PROSE-LEVEL STRING OVERREACH`.

Minimal E-02 repair replaced that prose fragment with the durable Kernel contract assertion that the Kernel does not duplicate or supersede the Runtime lifecycle definition. Relationship evidence and authority text were untouched.

## CI hard hold #2

First Repair HEAD `cf42f7a19e61438227987c8d1725974b484c4fbb`:
- Runtime/Integration `33480178768` = FAILURE.
- failing job `integration-tests` / `99767817143`.
- failing step `Run integration quality suite`.
- current E-02 assertions were source-revalidated and are all satisfied on this HEAD.

Deterministic source-level reproduction then identified an older integration regression in `Quality/Integration/test_core_p7_status_sync.py`:

`test_remaining_priority7_boundary_is_preserved()` requires the pre-E exact phrase:

`dependency and consumer validation for material Core authority relationships`

Current `Core/_FOLDER_STATUS.md` v1.3.3 truthfully advances that line after validating one bounded seam to:

`continued dependency and consumer validation for remaining material Core authority relationships`

The semantic boundary is unchanged: material Core dependency/consumer work remains open, REP-014 reconciliation remains required, explicit final Core certification remains pending, and global closure remains forbidden.

Root cause: `STALE REGRESSION / TRANSIENT STATUS-WORDING OVERREACH`.

EJR-179 applies `TRANSFERABLE`: the regression must protect the remaining-work semantics, not freeze the exact wording from before a valid bounded progress step.

## E-06 minimal repair rule

Change only `test_core_p7_status_sync.py` and only the stale dependency/consumer assertion. Assert the current durable boundary using the truthful `continued ... remaining material Core authority relationships` text while leaving all other REP-014, certification, P7-open, and no-global-closure assertions intact.

## Validation pending

After E-06:
1. re-read E-06 target;
2. re-run exact-head Runtime/Integration and inspect all jobs;
3. verify Full-Stack, Real Mutation Matrix Regression and M2 where triggered;
4. if all green, update progress record and this Matrix with both root causes and recovery evidence;
5. verify the resulting final closure HEAD before declaring E closed.

## Closure rule

Transaction E closes only after exact closure-lineage required CI is green. Priority 7 remains OPEN and the next Core seam must be recomputed from live repository evidence.
