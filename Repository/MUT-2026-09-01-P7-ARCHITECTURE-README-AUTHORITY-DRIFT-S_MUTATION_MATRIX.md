# MUTATION MATRIX — P7 ARCHITECTURE README AUTHORITY DRIFT — S

Transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-AUTHORITY-DRIFT-S`
Work Lease: `HERMUZ-P7-S-ARCHITECTURE-README-20260901`
Priority: `7 — Core cross-layer dependency/consumer validation`
State: `PRE-WRITE MATRIX / LEASE ACTIVE / CONTENT-RECONCILIATION`
Entry HEAD: `cb45d5fd9b6dbba1727e52060b9e181a54db3239`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / GOV-019 / GOV-020 / ARC-011 / ARC-006`

## Problem definition

`Architecture/README.md` is canonical and marked Absolute/Critical, but its current content predates the 2026-09-01 CORE-000 canonical-architecture reconciliation and does not reflect the current Architecture control boundary.

Direct current evidence shows four bounded material drifts:

1. it describes `Core/CORE-000_PLATFORM_ARCHITECTURE.md` as the `ultimate guiding text` and says it overrides project details, while current CORE-000 explicitly preserves Core-level platform architecture intent **aligned with** `ARC-011` and subordinate to Constitution/applicable Governance;
2. it omits `ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` from the listed canonical Architecture components even though ARC-011 is the current authoritative architectural reference for structural boundaries and dependency direction;
3. it says every valid Architecture artifact must be cataloged by the listed prefixes while the list omits multiple active ARC artifacts and does not distinguish ARC documents from the map/status/navigation artifacts;
4. it states the Architecture directory is `globally locked` and applies an `Anti-Patch Policy` instead of binding material mutation to the current controlled-mutation / pre-write-Matrix governance.

`Architecture/_FOLDER_STATUS.md` independently keeps Canonical Architecture Model alignment and cross-layer references OPEN, so the README's Approved/Canonical metadata is not domain certification evidence.

## Prior learning classification

- Transaction I — CORE-000 canonical architecture drift: `DIRECTLY APPLICABLE`.
- Transactions L/M — CORE-003 ↔ ARC-011 authority boundary: `DIRECTLY APPLICABLE` for constitutional/architecture authority separation.
- ARC-006 relationship discipline: `DIRECTLY APPLICABLE` for non-inference from paths/text alone.
- Transaction R incident/recovery: `DIRECTLY APPLICABLE` to write-action/atomicity discipline only; not semantic authority for this repair.
- Historical README claims predating current ARC-011/Core reconciliation: `STALE FOR CURRENT AUTHORITY INTERPRETATION`.

## Authorized material change set — exactly 5 paths

| ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| S-01 | `Architecture/README.md` | UPDATE | Align authority hierarchy, canonical artifact inventory semantics, legacy/navigation boundary and controlled-mutation rule | N | N |
| S-02 | `Architecture/_FOLDER_STATUS.md` | UPDATE | Record bounded README consumer alignment while preserving Architecture Integrity Hold and all broader open gates | N | N |
| S-03 | `Quality/Integrity/test_architecture_readme_authority_boundary.py` | CREATE | Regression for ARC-011 authority, CORE-000 alignment, inventory semantics and non-certification boundary | N | N |
| S-04 | `Repository/P7_ARCHITECTURE_README_AUTHORITY_ALIGNMENT_2026-09-01_S.md` | CREATE | Evidence, reasoning, scope, non-promotion and verification record | N | N |
| S-05 | this Matrix | UPDATE | Bind material candidate, atomicity and CI state | N | N |

Material candidate must be exactly one commit after this pre-write Matrix commit and exactly these five paths. Unexpected path expansion = `0`.

## KEEP / non-authority

- `Core/CORE-000_PLATFORM_ARCHITECTURE.md` unchanged.
- `Core/CORE-003_CONSTITUTION.md` unchanged.
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` unchanged.
- `Architecture/ARC-006_DEPENDENCY_MODEL.md` unchanged.
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` unchanged; S is content reconciliation, not relationship registration.
- `Core/_FOLDER_STATUS.md` unchanged by S.
- No new `CORE-000 ↔ Architecture/README`, `CORE-003 ↔ Architecture/README`, or `ARC-011 ↔ Architecture/README` registry edge is inferred merely from authority/reference text.
- No Architecture certification, Core certification, Priority-7 closure, Phase-1 closure, Connected-Baseline closure, repository-wide graph completion or Global PASS.
- `Architecture/01-System-Overview.md` remains preserved as existing foundation/legacy material; S does not promote, delete, or semantically certify it.

## Intended README correction boundary

The corrected README may:

- identify ARC-011 as the current canonical Architecture Model for structural boundaries/dependency direction, subordinate to Constitution/applicable Governance;
- describe CORE-000 as Core-level platform architecture intent aligned with that model, not a competing ultimate architecture authority;
- enumerate the current primary ARC-001..ARC-011 set and separately classify ARC_MAP / README / `_FOLDER_STATUS.md` as navigation/control surfaces;
- classify `01-System-Overview.md` as retained historical/foundation material whose physical presence does not create current architectural authority;
- replace the unsupported `globally locked` / Anti-Patch wording with controlled mutation under applicable Governance and required architectural review;
- advance README audit metadata only because the README itself receives current semantic review.

The correction must preserve the Architecture folder's `INTEGRITY HOLD` and must not claim all Architecture semantics or cross-layer consumers are validated.

## Verification contract

`PRE-WRITE MATRIX → GIT-DATA OBJECT PREPARATION → ONE-COMMIT/FIVE-PATH COMPARE BEFORE MAIN MOVES → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → REQUIRED WORKFLOW SET → FULL-STACK JOB/STEP REVIEW → RUNTIME JOB REVIEW → FAILURE/LEARNING ASSESSMENT → CLOSURE COMMIT → CLOSURE-HEAD VERIFICATION`.

Before every write-capable invocation verify:

`ACTION TYPE → EXACT PATH(S) → MATRIX AUTHORIZATION → REQUIRED ATOMICITY → WHETHER MAIN MOVES`.

Failure must remain evidence under GOV-016 and may not be erased by weakening the test or authority semantics.
