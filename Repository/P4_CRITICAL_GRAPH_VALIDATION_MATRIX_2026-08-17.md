# P4 — CRITICAL BIDIRECTIONAL GRAPH VALIDATION MATRIX

Date: 2026-08-17
Status: Active / REL-009 Directional Disposition / Registry Sync Pending
Scope: Critical relationship edges requiring independent forward and reverse evidence.

## Validation Rule

`Forward Evidence → Reverse Evidence → Consumer/Dependency Evidence → Implementation/Executable Evidence → Integration Test Evidence → Matrix Classification`

A one-sided reference is insufficient for `BIDIRECTIONAL VERIFIED` unless the relationship is explicitly and authoritatively dispositioned as intentionally one-way.

| Edge | Forward Evidence | Reverse Evidence | Consumer / Dependency Evidence | Executable / Integration Evidence | Classification |
|---|---|---|---|---|---|
| REL-005 — ENG-006 → SRV-009 | `ENG-006` states repository-state operations MUST route through `SRV-009` and its validation/authorization controls. | `SRV-009` states it is the controlled mutation service consumed by `ENG-006` for repository state updates and lists `ENG-006` as a related document. | `ENG-006` dispatch binding + `SRV-009` relationship position are independently aligned. | P3 runtime E2E run `32021524046` executed CREATE + UPDATE through the production adapter and real GitHub connector; traces `TR-6e94cc825acc`, `TR-3d0dd3df6ce3`; read-back and cleanup succeeded. P4 REL-005 controlled mutation workflow `32023841791` applied the registry promotion with source blob `794d4b9e…`, candidate blob `d41d84d0…`, applied commit `e29af1e6…`, and verified post-write read-back. | **BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E / REGISTRY PROMOTED** |
| REL-009 — RUN-010 → SRV-009 | `RUN-010` explicitly describes the governed execution sequence ending in `ENG-006 Execution → SRV-009 Controlled Mutation → Post-Write Validation / Re-read`, while explicitly stating this is not a universal runtime-path claim. | `SRV-009` does not independently name `RUN-010` as a caller. Current architecture does not require a service to create a reverse dependency on every consuming runtime reference; such a reverse dependency would require independent necessity and circularity justification. | Main `a538325b...` contains a pure RUN-010 handoff contract and an integration-only observation harness that composes the existing governed ENG-006/SRV-009 production adapter while preserving authorization/provenance. Normal connected-spine semantics remain simulation-only. | `Quality/Integration/test_rel009_run010_srv009_observation.py` observes a RUN-010-attributed dispatch through `execute_update`, asserts explicit `SRV-009` target, execution/task/session/source-trace continuity, authorization identity, downstream execution trace, side-effect status and post-read verification. Exact-main Full-Stack `33196013636` and Runtime/Integration `33196013609` passed. Provider-backed E2E separately verifies the reused adapter/connector boundary, not universal RUN-010 routing. | **INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL / REGISTRY SYNC PENDING** |
| REL-061 — GOV-013A → GOV-013 | `REP-014` registers `GOV-013A → GOV-013 = REFERENCES`; `GOV-013A` states it supplements `GOV-013`. | Reverse `GOV-013 → GOV-013A` reference is intentionally absent because the authoritative semantic is asymmetric: the addendum supplements the protocol. | Governance scope registration is revalidated in `REP-014`; no authority transfer is implied. | No executable evidence is applicable; this is a governance/document relationship. | **INTENTIONAL ONE-WAY / GOVERNANCE-REVALIDATED / DISPOSITION-CLOSED** |

## P4 Result So Far

- `REL-005` is promoted in `REP-014` to **BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E**.
- `REL-009` now has sufficient evidence for a bounded intentional-one-way semantic disposition. The remaining blocker is controlled synchronization of the canonical `REP-014` row; no reverse dependency is to be manufactured merely for symmetry.
- `REL-061` is explicitly dispositioned as an intentional one-way governance/document relationship; no reverse-reference promotion is required.
- P4 remains open until the REL-009 registry row is safely synchronized and exact-head validation passes.

## P4 Reverse-Evidence Revalidation — 2026-08-18

### REL-009 verification delta

This historical cycle did not recreate the prior P4 search campaign. It performed a bounded verification delta against the then-current canonical `main` checkpoint:

1. **Independent repository search** for `RUN-010` / `SRV-009` relationship evidence did not surface a new canonical reverse relationship owned by `SRV-009`.
2. **Direct canonical read** of `Runtime/RUN-010_RUNTIME_REFERENCE.md` confirmed the forward runtime sequence remains explicitly described as:
   `Decision Candidate → Validation → Authorization → ENG-006 Execution → SRV-009 Controlled Mutation → Post-Write Validation / Re-read`.
   The same authority explicitly states that this is a relationship description and not a claim that every runtime operation follows the exact path.
3. **Direct canonical read** of `Services/SRV-009_UPDATE_SERVICE.md` confirmed its Relationship Position identifies `SRV-009` as the controlled mutation service consumed by `ENG-006`, with `ENG-006` listed in Related Documents. `RUN-010` is not independently named as a consumer, relationship endpoint, or caller.

Historical disposition:

`REL-009 = ONE-WAY / REVALIDATION REQUIRED`

This historical finding is preserved for provenance and is superseded for current operational interpretation by the 2026-08-28 directional-disposition review below.

### Historical evidence boundary

The negative conclusion was intentionally limited to the inspected canonical endpoint/document scope. It was not a repository-wide absence claim.

## P4 Directional Disposition Reassessment — 2026-08-28

### New current-main evidence

P3 clean extraction was squash-merged to current main as:

`a538325bcde36d3a45f19583ca20d72d8f591e0a`

The merged evidence adds no normal connected-spine production dispatch. Instead it adds the smallest bounded evidence seam:

`RUN-010 execution identity → pure governed handoff → existing ENG-006/SRV-009 production adapter → controlled dispatch observation`.

Exact-main push verification on the merged commit:

- Full-Stack Repository Audit `33196013636` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33196013609` — SUCCESS;
- Real Mutation Matrix Regression `33196013638` — SUCCESS;
- M2 Multi-Channel Proposal Training `33196013623` — SUCCESS.

### Architectural directionality review

`ARC-006` requires every dependency to be necessary, justified and free of circular dependency. `ARC-007` states Runtime may consume approved service interfaces. Neither requires a consumed service to create a reverse dependency on each runtime consumer merely to establish graph symmetry.

Therefore the absence of `SRV-009 → RUN-010` is no longer treated as an unresolved defect by itself. The supported semantic is directional consumption.

### Current disposition candidate

`REL-009 = INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`

Boundary:

- this does not mean every RUN-010 operation reaches SRV-009;
- this does not convert connected spine to production dispatch;
- this does not establish `SRV-009 → RUN-010` dependency;
- provider-backed E2E for ENG-006/SRV-009 remains a separate evidence class from the RUN-010 integration observation;
- canonical registry persistence is still pending controlled `REP-014` mutation.

## Boundary

This matrix validates only the listed critical edges. It does not claim repository-wide graph closure.

## Next Safe Mutation

1. Build a complete full-content-preserving candidate for `REP-014`.
2. Change only the `REL-009` state to the bounded directional disposition; preserve source, target, type and all unrelated registry content.
3. Re-read the resulting registry and run exact-head governed CI.
4. Only after registry synchronization may P4 closure be reconsidered.

---

End of P4 Matrix
