# P4 — CRITICAL BIDIRECTIONAL GRAPH VALIDATION MATRIX

Date: 2026-08-17
Status: `REGISTRY SYNCHRONIZED / CLOSURE-CANDIDATE / FINAL CI PENDING`
Scope: Critical relationship edges requiring independent forward/reverse evidence or an explicitly justified intentional one-way disposition.

## Validation Rule

`Forward Evidence → Reverse Evidence → Consumer/Dependency Evidence → Implementation/Executable Evidence → Integration Test Evidence → Matrix Classification`

A one-sided reference is insufficient for `BIDIRECTIONAL VERIFIED` unless the relationship is explicitly and authoritatively dispositioned as intentionally one-way.

| Edge | Forward Evidence | Reverse Evidence | Consumer / Dependency Evidence | Executable / Integration Evidence | Classification |
|---|---|---|---|---|---|
| REL-005 — ENG-006 → SRV-009 | `ENG-006` states repository-state operations MUST route through `SRV-009` and its validation/authorization controls. | `SRV-009` states it is the controlled mutation service consumed by `ENG-006` for repository state updates and lists `ENG-006` as a related document. | `ENG-006` dispatch binding + `SRV-009` relationship position are independently aligned. | P3 runtime E2E run `32021524046` executed CREATE + UPDATE through the production adapter and real GitHub connector; traces `TR-6e94cc825acc`, `TR-3d0dd3df6ce3`; read-back and cleanup succeeded. P4 REL-005 controlled mutation workflow `32023841791` applied the registry promotion with source blob `794d4b9e…`, candidate blob `d41d84d0…`, applied commit `e29af1e6…`, and verified post-write read-back. | **BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E / REGISTRY PROMOTED** |
| REL-009 — RUN-010 → SRV-009 | `RUN-010` explicitly describes the governed execution sequence ending in `ENG-006 Execution → SRV-009 Controlled Mutation → Post-Write Validation / Re-read`, while explicitly stating this is not a universal runtime-path claim. | `SRV-009` does not independently name `RUN-010` as a caller. Current architecture does not require a service to create a reverse dependency on every consuming runtime reference; such a reverse dependency would require independent necessity and circularity justification. | Main `a538325b...` contains a pure RUN-010 handoff contract and an integration-only observation harness that composes the existing governed ENG-006/SRV-009 production adapter while preserving authorization/provenance. Normal connected-spine semantics remain simulation-only. | `Quality/Integration/test_rel009_run010_srv009_observation.py` observes a RUN-010-attributed dispatch through `execute_update`, asserts explicit `SRV-009` target, execution/task/session/source-trace continuity, authorization identity, downstream execution trace, side-effect status and post-read verification. P3/P4 exact-main CI passed. The canonical registry was then synchronized through controlled full-content mutation run `33197498585`, source blob `a6926b0b...`, candidate blob `d75f460d...`, with verified full read-back. | **INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL / REGISTRY SYNCHRONIZED** |
| REL-061 — GOV-013A → GOV-013 | `REP-014` registers `GOV-013A → GOV-013 = REFERENCES`; `GOV-013A` states it supplements `GOV-013`. | Reverse `GOV-013 → GOV-013A` reference is intentionally absent because the authoritative semantic is asymmetric: the addendum supplements the protocol. | Governance scope registration is revalidated in `REP-014`; no authority transfer is implied. | No executable evidence is applicable; this is a governance/document relationship. | **INTENTIONAL ONE-WAY / GOVERNANCE-REVALIDATED / DISPOSITION-CLOSED** |

## P4 Current Result

- `REL-005` is canonically synchronized as **BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E**.
- `REL-009` is now canonically synchronized as **INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL**. No reverse dependency was manufactured for symmetry.
- `REL-061` remains an explicitly dispositioned intentional one-way governance/document relationship.
- The listed critical-edge set has no remaining semantic or registry-synchronization blocker.
- **Final exact-head PR CI is still required before this matrix may declare the listed P4 set CLOSED.**

## Historical Reverse-Evidence Revalidation — 2026-08-18

A historical bounded search found no independent `SRV-009 → RUN-010` reverse relationship and retained:

`REL-009 = ONE-WAY / REVALIDATION REQUIRED`.

That finding remains valid for its original checkpoint. It is superseded for current operational interpretation by later direct callable/dispatch evidence plus the architectural directionality review; it is not rewritten as if the historical evidence had already existed.

## P4 Directional Disposition Reassessment — 2026-08-28

P3 clean extraction was squash-merged to main as:

`a538325bcde36d3a45f19583ca20d72d8f591e0a`

It established the bounded evidence seam:

`RUN-010 execution identity → pure governed handoff → existing ENG-006/SRV-009 production adapter → controlled dispatch observation`.

Exact-main verification on that state:

- Full-Stack Repository Audit `33196013636` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33196013609` — SUCCESS;
- Real Mutation Matrix Regression `33196013638` — SUCCESS;
- M2 Multi-Channel Proposal Training `33196013623` — SUCCESS.

P4 semantic reconciliation was then squash-merged to main as:

`94a9bbb43432f3e098854571130778a498f76299`.

Exact-main verification:

- Full-Stack Repository Audit `33196750118` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33196750113` — SUCCESS;
- M2 Multi-Channel Proposal Training `33196750126` — SUCCESS.

### Architectural directionality review

`ARC-006` requires dependencies to be necessary, justified and free of circular dependency. `ARC-007` states Runtime may consume approved service interfaces. Neither requires a consumed service to create a reverse dependency on every consuming runtime reference merely to establish graph symmetry.

Therefore the absence of `SRV-009 → RUN-010` is not treated as a defect by itself. The supported semantic is directional consumption.

## Registry Synchronization — 2026-08-28

Transaction:

`MUT-2026-08-28-P4-REL009-REGISTRY-CLOSURE-001`

Controlled mutation workflow:

- run `33197498585` — SUCCESS;
- builder regressions: `3 passed`;
- source REP-014 blob: `a6926b0b27e515b38b65594846fd82d1f1252ea9`;
- registry mutation commit: `dda16b3f2523fea03bf8d8c9724b237ab648046c`;
- candidate/read-back blob: `d75f460d152898709044a31433e8ae4c705d9191`;
- mutation request status: `APPLIED`;
- `verified_readback = true`.

The mutation changed the REL-009 row and its current reconciliation block only, with REL-005/REL-061 preservation guards and full runner-side content read-back.

## Current Evidence Boundary

- `REL-009` does not mean every RUN-010 operation reaches SRV-009.
- Normal connected spine remains simulation-oriented and without direct SRV-009 dispatch.
- No `SRV-009 → RUN-010` dependency exists or is required by this disposition.
- Provider-backed ENG-006/SRV-009 E2E and the isolated RUN-010 observation remain distinct evidence classes.
- This matrix validates only the listed critical edges; it does not claim repository-wide graph closure or Connected-Baseline completion.

## Next Safe Gate

`OPEN PR ON FINAL TRANSACTION PAYLOAD → EXACT-HEAD FULL-STACK + RUNTIME/INTEGRATION CI → IF PASS, RECORD FINAL P4 LISTED-EDGE CLOSURE → FINAL-HEAD CI → MERGE REVIEW`.

---

End of P4 Matrix
