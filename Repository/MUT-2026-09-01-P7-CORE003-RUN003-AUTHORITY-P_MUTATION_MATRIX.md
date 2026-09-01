# MUTATION MATRIX — P7 CORE-003 ↔ RUN-003 AUTHORITY VALIDATION — P

Transaction: `MUT-2026-09-01-P7-CORE003-RUN003-AUTHORITY-P`
Work Lease: `HERMUZ-P7-P-CORE003-RUN003-20260901`
Priority: `7 — Core cross-layer validation`
State: `PRE-WRITE / LEASE OPEN / VALIDATION-FIRST`
Entry HEAD: `1392b031a49c187453daa2f03cfa8250aa08e6db`
Pre-write Matrix HEAD: `PENDING THIS COMMIT`
Material candidate HEAD: `PENDING`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Problem / change definition

Priority 7 remains open for material Core authority dependency/consumer validation. Current direct source evidence identifies `Runtime/RUN-003_CONFIGURATION.md` as a canonical, critical Runtime configuration authority whose explicit Authority Boundary says Runtime configuration does not override `Core/CORE-003_CONSTITUTION.md` and whose guiding statement keeps repository authority above runtime assumptions.

`CORE-003` independently states that the Constitution defines the highest governing rules of ARGO and that all repository components shall comply with it within applicable scope.

Current REP-014 v1.2.13 already contains the analogous independently evidenced pair `CORE-003 → RUN-001 = GOVERNS` / `RUN-001 → CORE-003 = REFERENCES`, but contains no current RUN-003 pair. Because REP-014 is deliberately not a complete graph, this transaction does not assume every constitutional mention warrants registration. RUN-003 is selected because configuration can materially alter execution behavior while explicitly declaring a constitutional non-override boundary.

## Prior-learning retrieval and classification

| Prior evidence | Classification | Use in P |
|---|---|---|
| REL-037/038 `CORE-003 ↔ RUN-001` | DIRECTLY APPLICABLE | Same Constitution→critical Runtime authority pattern with independently evidenced reverse documentary reference. |
| Transactions L/M `CORE-003 ↔ ARC-011` | TRANSFERABLE | Reuses authority/subordination ≠ dependency discipline and validation-before-registry synchronization. |
| Transactions N/O validation-first then registry synchronization | TRANSFERABLE | Reuses split proof/synchronization workflow and clean closure discipline. |
| Broad repository-wide constitutional applicability | INSUFFICIENT ALONE | Does not justify enumerating every component in REP-014. |

## Candidate semantic boundary

Direct source evidence is expected to support only:

`CORE-003 → RUN-003 = GOVERNS`

`RUN-003 → CORE-003 = REFERENCES`

with disposition:

`BIDIRECTIONAL-AUTHORITY/DOCUMENTARY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY`

No `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, reverse `GOVERNS`, executable-reachability, Runtime certification, Core certification, Phase-1 closure, Connected Baseline closure or Global PASS may be inferred.

## Material change set

| Change ID | Target | Action | Expected content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| P-01 | `Quality/Integrity/test_core003_run003_authority_boundary.py` | CREATE | Assert direct CORE-003 governing language, RUN-003 constitutional non-override/reference language, registry absence during validation-first stage, forbidden stronger semantics, and continued Core hold. | N | N |
| P-02 | `Repository/P7_CORE003_RUN003_AUTHORITY_SEAM_2026-09-01_P.md` | CREATE | Record bounded validation finding, evidence, non-authority boundary and continuation rule. | N | N |
| P-03 | this Matrix | UPDATE IN SAME MATERIAL CHANGE SET | Bind pre-write HEAD, candidate, exact authorized paths and verification state. | N | N |

## KEEP / preservation requirements

- `Core/CORE-003_CONSTITUTION.md` — KEEP / no source mutation.
- `Runtime/RUN-003_CONFIGURATION.md` — KEEP / no source mutation.
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` — KEEP in P / no relationship registration yet.
- `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` — KEEP in P.
- `Core/_FOLDER_STATUS.md` — KEEP in P.
- Existing REL-001..REL-070 rows — KEEP unchanged.
- No reverse `RUN-003 → CORE-003 = GOVERNS`.
- No dependency/executable promotion.

## Pre-write validation state

- live `main` independently re-read immediately before Matrix creation: `1392b031a49c187453daa2f03cfa8250aa08e6db`;
- PROJECT_BOOTSTRAP and CORE-003 re-read from that exact HEAD;
- REP-016 confirms Priority 7 remains the active Core partition;
- Core status remains `INTEGRITY HOLD — CONTROL PLANE RECONCILED / CROSS-LAYER VALIDATION OPEN` with Folder Certification pending;
- REP-014 v1.2.13 explicitly states its graph is incomplete and contains no RUN-003 pair in the directly inspected current relationship table;
- RUN-003 direct source re-read establishes canonical/critical configuration scope, constitutional non-override language and direct Related Documents reference;
- unexpected target-path expansion authorized: `0`.

Pre-write decision: `AUTHORIZED FOR EXACT 3-PATH VALIDATION-FIRST MATERIAL UNIT ONLY`.

Work Lease remains `OPEN` until exact-head CI and closure verification complete.
