# MUTATION MATRIX — P7 ARCHITECTURE README AUTHORITY DRIFT — S

Transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-AUTHORITY-DRIFT-S`
Work Lease: `HERMUZ-P7-S-ARCHITECTURE-README-20260901`
Priority: `7 — Core cross-layer dependency/consumer validation`
State: `MATERIAL-CANDIDATE / CI-PENDING / CONTENT-RECONCILIATION / LEASE ACTIVE`
Entry HEAD: `cb45d5fd9b6dbba1727e52060b9e181a54db3239`
Pre-write Matrix HEAD: `cbba871330e9cb82486b7cbda73a20edd65f114e`
Rejected unpublished candidate: `c81500caacbd385b9706a09de57b0fce55c2dae3`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / GOV-019 / GOV-020 / ARC-011 / ARC-006`

## Problem definition

`Architecture/README.md` is canonical and Absolute/Critical, but its entry-state content predates the 2026-09-01 CORE-000 canonical-architecture reconciliation and does not reflect the current Architecture control boundary.

Direct current evidence establishes four bounded material drifts:

1. stale `CORE-000 = ultimate guiding text` / override interpretation conflicts with current CORE-000's explicit ARC-011 alignment and subordination to Constitution/applicable Governance;
2. ARC-011 is absent from the README's old canonical component list despite being the current authoritative architectural reference for structural boundaries and dependency direction;
3. the README's partial list is presented as if every valid Architecture artifact must be cataloged there, while current Architecture status identifies a wider primary ARC-001..ARC-011 review set plus distinct navigation/control surfaces;
4. stale `globally locked` / `Anti-Patch Policy` wording does not reflect the current controlled-mutation / pre-write-Matrix governance boundary.

## Prior learning classification

- Transaction I — CORE-000 canonical architecture drift: `DIRECTLY APPLICABLE`.
- Transactions L/M — CORE-003 ↔ ARC-011 authority boundary: `DIRECTLY APPLICABLE`.
- ARC-006 relationship discipline: `DIRECTLY APPLICABLE`.
- Transaction R incident/recovery: `DIRECTLY APPLICABLE TO EXECUTION DISCIPLINE ONLY`.
- Historical README authority claims predating current ARC-011/Core reconciliation: `STALE FOR CURRENT AUTHORITY INTERPRETATION`.

## Authorized material change set — exactly 5 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| S-01 | `Architecture/README.md` | UPDATE authority hierarchy, current primary ARC-set semantics, legacy/navigation boundary and controlled-mutation rule | Y | PENDING CI |
| S-02 | `Architecture/_FOLDER_STATUS.md` | UPDATE bounded README alignment while preserving Architecture Integrity Hold and broader open gates | Y | PENDING CI |
| S-03 | `Quality/Integrity/test_architecture_readme_authority_boundary.py` | CREATE section-scoped regression for authority/inventory/non-certification boundary | Y | PENDING CI |
| S-04 | `Repository/P7_ARCHITECTURE_README_AUTHORITY_ALIGNMENT_2026-09-01_S.md` | CREATE evidence/reasoning/failure/non-promotion record | Y | PENDING CI |
| S-05 | this Matrix | UPDATE/rebind material-candidate state | Y | PENDING CI |

Publishable material candidate must be exactly one commit after `cbba8713...` and exactly these five paths. Unexpected path expansion = `0`.

## Intended material result

`Architecture/README.md`:

- v3.2.0 → v3.2.1;
- `Approved` → `Approved / Integrity Hold`;
- current authority hierarchy expressed as Constitution/Governance → ARC-011 → other Architecture → repository/implementation;
- CORE-000 expressed as Core-level platform architecture intent aligned to ARC-011, not a competing ultimate Architecture authority;
- ARC-001..ARC-011 represented as the current primary ARC review set;
- ARC_MAP / README / `_FOLDER_STATUS.md` distinguished as navigation/control surfaces;
- `01-System-Overview.md` preserved as foundation/legacy material without authority promotion;
- stale `globally locked` and `Anti-Patch Policy` wording removed;
- controlled mutation bound to applicable GOV-014/GOV-014A.

`Architecture/_FOLDER_STATUS.md`:

- v1.5.1 → v1.5.2;
- current audit date advances because this evidence record itself is materially updated;
- Transaction-S README consumer alignment recorded as a bounded PASS;
- broader canonical Architecture Model alignment, layer/dependency consistency, stale references and cross-layer reviews remain OPEN;
- Architecture remains `INTEGRITY HOLD` and not globally certified.

## Pre-publish validation-design correction

The first object candidate `c81500caacbd385b9706a09de57b0fce55c2dae3` was created from the pre-write Matrix and structurally compared as one commit/five paths, but it was **not published**.

Exact candidate read-back revealed a validation-design defect in the initial focused test: it computed ARC-001..ARC-011 order using the first occurrence of each identifier across the whole README. ARC-011 is intentionally referenced earlier in the authority section, so that assertion could fail even when the primary-review-set inventory itself was correctly ordered.

Classification: `PRE-PUBLISH VALIDATION_DESIGN_DEFECT / NO MAIN MUTATION / NO CI FAILURE`.

The corrected test scopes the ordering assertion to Section 2 (`Current Primary Architecture Review Set`) and preserves the valid earlier ARC-011 authority reference.

No semantic authority was weakened and no repository rollback was required because `main` never moved to the rejected object candidate.

## KEEP / non-authority

- `Core/CORE-000_PLATFORM_ARCHITECTURE.md` unchanged.
- `Core/CORE-003_CONSTITUTION.md` unchanged.
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` unchanged.
- `Architecture/ARC-006_DEPENDENCY_MODEL.md` unchanged.
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` unchanged.
- `Core/_FOLDER_STATUS.md` unchanged.
- no README ↔ CORE-000 / CORE-003 / ARC-011 registry edge;
- no dependency/authority relationship inferred solely from textual references;
- no Architecture/Core certification, Priority-7 closure, Phase-1 closure, Connected-Baseline closure, repository-wide graph completion or Global PASS;
- `Architecture/01-System-Overview.md` is preserved, not promoted/deleted/certified.

## Search / evidence boundary

Three materially different repository searches preceded S selection:

1. `Core/CORE-003_CONSTITUTION.md`;
2. `CORE-003`;
3. `Core/CORE-`.

Search-index URLs lagged behind live main, so search output was used only for candidate discovery. All material findings were re-read from exact live S-entry sources before mutation.

Targeted follow-up searches localized the stale `ultimate guiding text`/override wording to `Architecture/README.md` and confirmed current CORE-000/ARC-011 alignment evidence and Transaction-I regression history.

## Verification contract

`PRE-WRITE MATRIX → GIT-DATA OBJECT PREPARATION → PRE-PUBLISH READ-BACK → ONE-COMMIT/FIVE-PATH COMPARE BEFORE MAIN MOVES → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → REQUIRED WORKFLOW SET → FULL-STACK JOB/STEP REVIEW → RUNTIME JOB REVIEW → FAILURE/LEARNING ASSESSMENT → CLOSURE COMMIT → CLOSURE-HEAD VERIFICATION`.

Before every write-capable invocation:

`ACTION TYPE → EXACT PATH(S) → MATRIX AUTHORIZATION → REQUIRED ATOMICITY → WHETHER MAIN MOVES`.

Failure remains evidence under GOV-016 and must not be erased by weakening the test or authority semantics.

## Learning disposition

No new governance rule is justified.

Retained validation-design lesson:

`SECTION-SCOPED SEMANTIC ASSERTION -> TEST WITHIN THAT SECTION; DO NOT USE WHOLE-DOCUMENT FIRST OCCURRENCE WHEN THE SAME ID MAY VALIDLY APPEAR IN AUTHORITY/REFERENCE CONTEXT ELSEWHERE`.

This is a bounded test-design refinement, not authority for unrelated test rewrites.

## Closure boundary

S is a bounded canonical-consumer content correction. Even after successful candidate verification, the Lease remains open until closure documentation is committed and the exact closure HEAD passes the applicable required verification surface.

Post-S continuation is not pre-authorized: a fresh live-main Priority-7 recomputation must decide whether another material Core consumer gap remains or whether explicit Core Certification Readiness review is the next legal action.
