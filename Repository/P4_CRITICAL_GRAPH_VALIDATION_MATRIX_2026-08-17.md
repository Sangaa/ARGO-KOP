# P4 — CRITICAL BIDIRECTIONAL GRAPH VALIDATION MATRIX

Date: 2026-08-17
Status: Active / P4 Validation
Scope: Critical relationship edges requiring independent forward and reverse evidence.

## Validation Rule

`Forward Evidence → Reverse Evidence → Consumer/Dependency Evidence → Implementation/Executable Evidence → Integration Test Evidence → Matrix Classification`

A one-sided reference is insufficient for `BIDIRECTIONAL VERIFIED`.

| Edge | Forward Evidence | Reverse Evidence | Consumer / Dependency Evidence | Executable / Integration Evidence | Classification |
|---|---|---|---|---|---|
| REL-005 — ENG-006 → SRV-009 | `ENG-006` states repository-state operations MUST route through `SRV-009` and its validation/authorization controls. | `SRV-009` states it is the controlled mutation service consumed by `ENG-006` for repository state updates and lists `ENG-006` as a related document. | `ENG-006` dispatch binding + `SRV-009` relationship position are independently aligned. | P3 runtime E2E run `32021524046` executed CREATE + UPDATE through the production adapter and real GitHub connector; traces `TR-6e94cc825acc`, `TR-3d0dd3df6ce3`; read-back and cleanup succeeded. P4 REL-005 controlled mutation workflow `32023841791` applied the registry promotion with source blob `794d4b9e…`, candidate blob `d41d84d0…`, applied commit `e29af1e6…`, and verified post-write read-back. | **BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E / REGISTRY PROMOTED** |
| REL-009 — RUN-010 → SRV-009 | `RUN-010` explicitly describes the governed execution sequence ending in `ENG-006 Execution → SRV-009 Controlled Mutation → Post-Write Validation / Re-read`. | `SRV-009` does not independently name `RUN-010` in its Relationship Position or Related Documents. | Runtime execution path is now proven for the production adapter, but `RUN-010` itself explicitly states its sequence is a relationship description and does not claim every runtime operation follows it. | P3 E2E proves the concrete `ENG-006 → SRV-009` execution seam, not universal `RUN-010 → SRV-009` reachability. | **ONE-WAY / REVALIDATION REQUIRED** |
| REL-061 — GOV-013A → GOV-013 | `REP-014` registers `GOV-013A → GOV-013 = REFERENCES`; `GOV-013A` states it supplements `GOV-013`. | `GOV-013` current content does not independently reference `GOV-013A`. | Governance scope registration is revalidated in `REP-014`; no authority transfer is implied. | No executable evidence is applicable; this is governance/document relationship evidence. | **ONE-WAY / GOVERNANCE-REVALIDATED / REVERSE EVIDENCE REQUIRED FOR BIDIRECTIONAL CLOSURE** |

## P4 Result So Far

- `REL-005` is now promoted in `REP-014` to **BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E**.
- `REL-009` remains open because the reverse endpoint evidence is absent and the source contract itself limits the scope of its runtime sequence claim.
- `REL-061` remains governance-revalidated but one-way.

## Boundary

This matrix validates only the listed critical edges. It does not claim repository-wide graph closure.

## Next Safe Mutation

1. Investigate independent reverse evidence for `REL-009` without widening the relationship scope.
2. Investigate reverse governance evidence for `REL-061` if supported by canonical authority.
3. Keep P4 open until the current critical-edge set is either bidirectionally verified or explicitly dispositioned as intentional one-way relationships.

---

End of P4 Matrix
