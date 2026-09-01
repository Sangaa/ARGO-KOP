# MUTATION MATRIX — P7 RUN-002 → CORE-003 INITIALIZATION AUTHORITY REFERENCE — R

Transaction: `MUT-2026-09-01-P7-RUN002-CORE003-REFERENCE-R`
Work Lease: `HERMUZ-P7-R-RUN002-CORE003-20260901`
Priority: `7 — Core cross-layer dependency/consumer validation`
State: `PRE-WRITE / LEASE OPEN / VALIDATION-FIRST`
Entry HEAD: `abfa867f2fa5d34ac1430f39e2c40143327f1018`
Pre-write Matrix HEAD: `PENDING THIS COMMIT`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Problem / legal action

After Transaction Q closed the validated RUN-003 constitutional configuration seam, fresh Priority-7 recomputation still leaves material Core dependency/consumer validation open.

`Runtime/RUN-002_INITIALIZATION.md` is `Canonical: Yes`, `Priority: Critical`, defines the Runtime initialization gate, requires dependency and authority resolution before readiness, explicitly stops/holds when required authority cannot be resolved, and directly lists `Core/CORE-003_CONSTITUTION.md` under Related Documents.

This is more material than a navigation-only reference because initialization is a fail-closed readiness gate. However, unlike RUN-003, RUN-002 does not contain a direct source-specific constitutional non-override declaration. Therefore current evidence supports only the one-way documentary candidate:

`RUN-002 → CORE-003 = REFERENCES`

Disposition:

`INTENTIONAL ONE-WAY / INITIALIZATION-AUTHORITY-RESOLUTION-ALIGNED / NON-DEPENDENCY`

The Constitution's general applicability to repository components is background authority and does not, by itself, authorize a new separately enumerated `CORE-003 → RUN-002 = GOVERNS` registry row.

## Prior-learning classification

| Evidence | Classification | Use in R |
|---|---|---|
| Transactions P/Q | DIRECTLY APPLICABLE | Distinguishes source-specific constitutional authority proof from generic constitutional applicability. |
| Transactions N/O | DIRECTLY APPLICABLE | One-way validation-first documentary seam followed by separate synchronization only if later required. |
| REL-037/038 CORE-003↔RUN-001 | TRANSFERABLE | Controlled Runtime precedent, but not copied because RUN-002 source evidence is weaker/different. |
| ARC_MAP navigation boundary | TRANSFERABLE NEGATIVE | Map/reference presence alone is insufficient for relationship registration. |

No new governance rule is required.

## Authorized material change set — exactly 3 paths

| ID | Target | Action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| R-01 | `Quality/Integrity/test_run002_core003_initialization_authority_reference.py` | CREATE | Bind RUN-002 critical initialization/authority-resolution/direct-reference evidence, require validation-first registry absence, forbid stronger/reverse semantics, preserve Core hold. | N | N |
| R-02 | `Repository/P7_RUN002_CORE003_INITIALIZATION_AUTHORITY_REFERENCE_2026-09-01_R.md` | CREATE | Record bounded one-way candidate and non-authority boundary. | N | N |
| R-03 | this Matrix | UPDATE IN SAME MATERIAL CHANGE SET | Bind candidate and verification state. | N | N |

Unexpected path expansion authorized: `0`.

## KEEP / forbidden promotion

- `Runtime/RUN-002_INITIALIZATION.md` — KEEP unchanged.
- `Core/CORE-003_CONSTITUTION.md` — KEEP unchanged.
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` — KEEP in R; no registration yet.
- `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` — KEEP in R.
- `Core/_FOLDER_STATUS.md` — KEEP in R.
- No `RUN-002 → CORE-003 = DEPENDS_ON/GOVERNS/IMPLEMENTS/CONSUMES`.
- No `CORE-003 → RUN-002` row of any type in R.
- No executable coupling, Runtime/Core certification, Priority-7 closure, Phase-1 closure, Connected Baseline closure, repository-wide graph closure or Global PASS.

## Pre-write evidence

- live main independently rediscovered as Q closure `abfa867f2fa5d34ac1430f39e2c40143327f1018` after closure-head 4/4 success;
- Core status v1.3.11 remains `CROSS-LAYER VALIDATION OPEN` with eight bounded seams and Folder Certification pending;
- REP-014 v1.2.14 remains deliberately incomplete and contains no RUN-002→CORE-003 row in the directly inspected current table;
- RUN-002 direct current source establishes canonical/critical initialization, required dependency/authority validation, fail-closed unresolved-authority handling, and direct CORE-003 Related Documents reference;
- RUN-004/005 were inspected for priority comparison: they are material Runtime controls but do not directly reference CORE-003, so no Core edge is inferred for them;
- ARC_MAP was rejected as a relationship target for this purpose because it explicitly describes itself as navigation/map authority and warns that a map does not create authority merely by listing a node.

Pre-write decision: `AUTHORIZED FOR EXACT THREE-PATH VALIDATION-FIRST UNIT ONLY`.

Work Lease remains `OPEN` until exact-head CI and closure-head verification complete.
