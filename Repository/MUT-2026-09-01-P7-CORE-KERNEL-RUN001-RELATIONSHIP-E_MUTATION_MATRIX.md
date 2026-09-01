# MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E — Mutation Matrix

Transaction ID: `MUT-2026-09-01-P7-CORE-KERNEL-RUN001-RELATIONSHIP-E`
Protocol: `GOV-013 / GOV-014A`
Status: `ATOMIC-RECOVERY-CANDIDATE / E-07B-APPLIED / CI-PENDING / P7-OPEN`
Date: 2026-09-01
Entry HEAD: `5f56a732feba08f9c808dfe2672560d6b59625e5`
Prewrite Matrix HEAD: `b7218350659b18bdb24a315879ef5a9faa9b19ee`
Relationship Candidate HEAD: `edac3f8451dbaf8b38f73e067c095caca177e8de`
Regression HEAD: `960a3edddf5d7d04fc65d308ece5b90176ec2f09`
Status Sync HEAD: `33d617e9f60ef5db9d1842e2a8d084fc09c565b7`
Progress Record HEAD: `e050ee80972f69882f075cfcbd8d0f0f71030ad9`
Initial Matrix Candidate HEAD: `9f03dc9567f881a7899110b7650fb7b304bfd693`
First Repair HEAD: `cf42f7a19e61438227987c8d1725974b484c4fbb`
Second Repair HEAD: `a97bbad064ec7b02e8a5e9a23b9ab3abc07b9523`
Third Repair Content HEAD: `521dfcaa8da50543b6dceb44de1bc8aa2ec5c8a2`
E-07B Authorization HEAD: `2271d130d7bb3583a695d0bd4e4bddac8e235818`

## Problem / change definition

Priority 7 has completed Core local inventory and control-plane reconciliation, but material Core cross-layer dependency/consumer validation remains open.

`Core/ARGO_KERNEL.md` (`CORE-KERNEL`) is a canonical Core/Runtime Contract surface. It explicitly names `Runtime/RUN-001_BOOT_SEQUENCE.md` as the canonical runtime lifecycle definition. Current evidence justifies one bounded registry relationship without creating a forbidden Core → Runtime architectural dependency or manufacturing reverse graph symmetry.

Applied relationship candidate:

`CORE-KERNEL → RUN-001 = REFERENCES / INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY`

## Prior-learning retrieval

1. `GOV-013`: reference is not dependency; validate both directions and use only the strongest justified relationship state.
2. `Architecture/ARC-006_DEPENDENCY_MODEL.md`: Core has no architectural-layer dependency on lower layers. Classification: `DIRECTLY APPLICABLE`.
3. P4 / REL-009: do not manufacture reverse graph symmetry where evidence is absent. Classification: `TRANSFERABLE`.
4. `EJR-179_2026-08-16_FOLDER_INVENTORY_IDENTITY_DRIFT_LEARNING.md`: integrity assertions must target semantic authority boundaries rather than transient/incidental wording. Classification for CI holds #1 and #2: `TRANSFERABLE`.
5. `MUT-2026-08-29-CURRENT-CONTROL-PLANE-MANIFEST-REBIND-010.md`: a current-state executable gate must consume a refreshable current evidence manifest, and that manifest must be refreshed when listed identity/status/version changes. Classification for CI hold #3: `DIRECTLY APPLICABLE`.
6. `MUT-2026-08-30-P2-MATRIX-SAME-CHANGESET-REPAIR-187.md`: `PREWRITE MATRIX PRESENCE != SAME-CHANGE-SET MATRIX BINDING`; failed binding must be recovered by a new governed same-change-set mutation rather than retroactively promoted. Classification for CI hold #4: `DIRECTLY APPLICABLE`.

## Evidence boundary

- `CORE-KERNEL` explicitly references the canonical RUN-001 lifecycle and says it does not duplicate or supersede it.
- Direct RUN-001 review plus reverse searches do not establish a specific RUN-001 → CORE-KERNEL consumer/dependency edge.
- ARC-006 prevents interpreting the forward documentary alignment as Core → Runtime architectural `DEPENDS_ON`.
- Existing REL-037/038 (`CORE-003 ↔ RUN-001`) remain separate and unchanged.
- `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` is non-authoritative current evidence, but its executable gate intentionally fails closed when a listed artifact version/status/identity drifts.

## Authorized change set

| ID | Target | Action | Expected change | Applied | Verified |
|---|---|---|---|---:|---:|
| E-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | add only evidence-backed REL-062 one-way REFERENCES row and bounded reconciliation note | Y | candidate |
| E-02 | `Quality/Integrity/test_core_kernel_run001_relationship_boundary.py` | CREATE/REPAIR | direct seam regression; repair first brittle prose assertion only | Y | source-revalidated |
| E-03 | `Core/_FOLDER_STATUS.md` | UPDATE | record one validated bounded seam while preserving remaining P7/certification hold | Y | candidate |
| E-04 | `Repository/P7_CORE_KERNEL_RUN001_RELATIONSHIP_2026-09-01_E.md` | CREATE/UPDATE | bounded progress and eventual CI record | Y | candidate |
| E-05 | this Matrix | UPDATE | record hard holds, repairs, exact CI and closure evidence | Y | in progress |
| E-06 | `Quality/Integration/test_core_p7_status_sync.py` | UPDATE | preserve durable P7 remaining-work boundary while accepting current truthful `continued ... remaining material Core authority relationships` state | Y | source-revalidated |
| E-07 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | refresh REP-014 listed version `1.2.6 → 1.2.7` and source baseline, preserving all open/HOLD/non-authority semantics | Y | content-valid / same-change-set binding failed |
| E-07B | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` + this Matrix | ATOMIC REBIND | issue one Git-object commit containing the current manifest and this Matrix together; preserve REP-014 `1.2.7`, add bounded recovery-binding evidence, and bind the protected current manifest to this Matrix in the exact enforced change set | Y | candidate / exact-head CI pending |

## KEEP requirements

- Do not modify `CORE-KERNEL`, `RUN-001`, `CORE-003`, `ARC-006`, or other authority documents for CI repair.
- Do not promote REL-062 to `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, or executable proof.
- Do not add `RUN-001 → CORE-KERNEL` merely for symmetry.
- Preserve REL-037/038 unchanged.
- E-06 must not weaken the P7 hold: remaining material dependency/consumer validation, REP-014 reconciliation, explicit final Core certification, and no Phase-1/global closure must still be asserted.
- E-07/E-07B are current-evidence operations only: do not rewrite historical manifests, do not alter REP-014 to fit the manifest, do not change semantic authority, and do not close Phase 1, P7, broader graph work, or global integrity.
- The failed E-07 commit remains failure evidence and is not retroactively promoted.
- E-07B uses one atomic Git commit where the changed-file set visibly contains both the protected current manifest and this Matrix.
- Priority 7 remains OPEN.

## CI hard hold #1

Initial matrix candidate HEAD `9f03dc9567f881a7899110b7650fb7b304bfd693`:
- Runtime/Integration `33479748723` = FAILURE.
- prototype = SUCCESS; integrity = SUCCESS.
- failing job `integration-tests` / `99766502846`.
- failing step `Run integration quality suite`.

Root cause: `BRITTLE REGRESSION / PROSE-LEVEL STRING OVERREACH`.

Minimal E-02 repair replaced the incidental prose fragment with the durable Kernel contract assertion. Relationship evidence and authority text were untouched.

## CI hard hold #2

First Repair HEAD `cf42f7a19e61438227987c8d1725974b484c4fbb`:
- Runtime/Integration `33480178768` = FAILURE.
- failing job `integration-tests` / `99767817143`.
- failing step `Run integration quality suite`.

Root cause: `STALE REGRESSION / TRANSIENT STATUS-WORDING OVERREACH`.

EJR-179 applied `TRANSFERABLE`. E-06 changed only the stale assertion; all REP-014, certification, P7-open, and no-global-closure guards remained intact.

## CI hard hold #3

Second Repair HEAD `a97bbad064ec7b02e8a5e9a23b9ab3abc07b9523`:
- Runtime/Integration `33480949106` = FAILURE.
- prototype = SUCCESS; integrity = SUCCESS.
- failing job `integration-tests` / `99770211931`.
- failing step `Run integration quality suite`.

The executable current-manifest gate compares listed artifact versions against the live files. Transaction E advanced REP-014 to `1.2.7` while the current manifest still listed `1.2.6`.

Root cause: `REAL COMPANION EVIDENCE DRIFT / CURRENT-MANIFEST FRESHNESS VIOLATION`.

E-07 updated the non-authoritative current manifest to REP-014 `1.2.7`. On content HEAD `521dfcaa8da50543b6dceb44de1bc8aa2ec5c8a2`, Runtime/Integration `33484577149` = SUCCESS and M2 `33484577142` = SUCCESS, proving the content repair corrected the integration mismatch.

## CI hard hold #4

Third Repair Content HEAD `521dfcaa8da50543b6dceb44de1bc8aa2ec5c8a2`:
- Runtime/Integration `33484577149` = SUCCESS.
- M2 `33484577142` = SUCCESS.
- Full-Stack `33484577144` = FAILURE.
- failing job `repository-audit` / `99781570872`.
- first failing step `Enforce Mutation Matrix on current change set`.
- all preceding Full-Stack steps, including Mutation Matrix preflight/semantic regressions, passed.

The enforcer computes the exact Git diff for the pushed change set and requires at least one Matrix path whenever a protected `Repository/REP-*` path changes. E-07 was written by a single-file Contents operation after its prewrite Matrix commit, so the E-07 push contained the protected manifest but not the Matrix in that exact commit.

Root cause: `SAME-CHANGE-SET MATRIX BINDING VIOLATION / WRITE-SURFACE ATOMICITY GAP`.

The protected manifest content is semantically correct, but the E-07 commit is not execution-verified and is not retroactively promoted. Prior recovery 187 is directly applicable.

## E-07B atomic recovery candidate

E-07B was pre-authorized at exact main `2271d130d7bb3583a695d0bd4e4bddac8e235818`.

The recovery candidate is constructed through Git blob/tree/commit objects from that authorization parent. Its exact changed-file set is required to contain only:
1. `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` — REP-014 remains `1.2.7`; verified source baseline points to E-07 content HEAD `521dfcaa8da50543b6dceb44de1bc8aa2ec5c8a2`; bounded same-change-set recovery evidence is added while all OPEN/HOLD/non-authority boundaries remain unchanged;
2. this Matrix — E-07B is recorded as applied/candidate with CI pending.

The atomic recovery commit SHA is intentionally not self-embedded in this candidate blob. It is recorded after commit creation and exact-head CI in the E-05 evidence update. No other path is authorized. `main` may move only by `force=false` fast-forward from the authorization HEAD.

## Validation pending

After E-07B:
1. re-read both atomic targets and compare exact changed-file set;
2. verify Full-Stack same-change-set enforcement passes;
3. verify exact-head Runtime/Integration, Full-Stack, M2, Real Mutation Matrix Regression, and any other triggered required gate;
4. any failure remains a GOV-013 §9B hard hold;
5. if all green, update progress record and this Matrix with all four root causes and recovery evidence;
6. create a formal closure-lineage commit and verify its exact-head required CI before declaring E closed.

## Closure rule

Transaction E closes only after exact closure-lineage required CI is green. Priority 7 remains OPEN and the next Core seam must be recomputed from live repository evidence.
