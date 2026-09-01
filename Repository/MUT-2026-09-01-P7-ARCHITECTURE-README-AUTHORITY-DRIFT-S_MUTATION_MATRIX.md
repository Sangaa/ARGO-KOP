# MUTATION MATRIX — P7 ARCHITECTURE README AUTHORITY DRIFT — S

Transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-AUTHORITY-DRIFT-S`
Work Lease: `HERMUZ-P7-S-ARCHITECTURE-README-20260901`
Priority: `7 — Core cross-layer dependency/consumer validation`
State: `MATERIAL-CANDIDATE FAILED / CORRECTIVE S-C1 ACTIVE / LEASE ACTIVE`
Entry HEAD: `cb45d5fd9b6dbba1727e52060b9e181a54db3239`
Pre-write Matrix HEAD: `cbba871330e9cb82486b7cbda73a20edd65f114e`
Rejected unpublished candidate: `c81500caacbd385b9706a09de57b0fce55c2dae3`
Published failed material candidate: `c51ffc4efec9eaded777eeb4f97311386cc0a289`
Corrective pre-write Matrix HEAD: `b6cb16fc31637f336f57b6b3d0cf5b1592ea4ed3`
Corrective transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-S-C1`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / GOV-019 / GOV-020 / ARC-011 / ARC-006`

## Problem definition

S repairs stale canonical-consumer authority/inventory semantics in `Architecture/README.md` after current CORE-000/ARC-011 reconciliation. The intended authority result remains:

`Constitution / applicable Governance → ARC-011 → other applicable Architecture → repository / implementation`.

CORE-000 remains Core-level platform architecture intent aligned to that boundary, not a competing Architecture authority. Architecture remains on Integrity Hold.

## Original S material authorization

The original publishable S material candidate was required to be exactly one commit after `cbba8713...` and exactly these five paths:

1. `Architecture/README.md`
2. `Architecture/_FOLDER_STATUS.md`
3. `Quality/Integrity/test_architecture_readme_authority_boundary.py`
4. `Repository/P7_ARCHITECTURE_README_AUTHORITY_ALIGNMENT_2026-09-01_S.md`
5. this Matrix

Candidate `c51ffc4e...` satisfied the one-commit/five-path structural contract and was published.

## Pre-publish defect preserved

Earlier object candidate `c81500ca...` was never published. Exact read-back found a section-scoping defect in the first focused test. The corrected focused regression scopes ARC ordering to the primary-review-set section and preserves valid earlier ARC-011 authority references.

Classification: `PRE-PUBLISH VALIDATION_DESIGN_DEFECT / NO MAIN MUTATION / NO CI FAILURE`.

## Published candidate failure preserved

Runtime workflow `33530617715` on exact candidate `c51ffc4e...` failed. The first meaningful integrity log showed two compatibility regressions:

- established status marker `Architecture ↔ Runtime / Interface boundary — OPEN` was unnecessarily changed to include `/ AI`;
- established canonical relative link `../Core/CORE-000_PLATFORM_ARCHITECTURE.md` disappeared when the README represented the path only as code text.

The same log reported `2 failed, 136 passed`; prototype job succeeded. Full-Stack workflow `33530617711` succeeded, but the Runtime failure keeps S open.

Classification: `MATERIAL_CANDIDATE_CI_FAILURE / BACKWARD-COMPATIBILITY REGRESSION / AUTHORITY-SEMANTICS NOT INVALIDATED`.

No rerun substitutes for correction and no test is weakened.

## S-C1 corrective binding

Because original S required its published candidate to be exactly one commit after the pre-write Matrix, the corrective work is not misrepresented as another original S candidate. S-C1 has its own pre-write Matrix at `b6cb16fc...` and authorizes exactly five corrective paths:

1. README — restore canonical relative CORE-000 link only, preserving S authority semantics;
2. Architecture status — restore exact Runtime/Interface open marker and record S-C1;
3. S evidence record — preserve failure/correction provenance;
4. this parent Matrix — bind failed candidate to S-C1;
5. S-C1 Matrix — bind corrective candidate and verification state.

No test path is authorized in S-C1.

## KEEP / non-authority

- CORE-000 unchanged;
- CORE-003 unchanged;
- ARC-011 unchanged;
- ARC-006 unchanged;
- REP-014 unchanged;
- Core status unchanged;
- no README relationship edge manufactured;
- no Architecture/Core certification;
- no Priority-7, Phase-1, Connected-Baseline, repository-wide graph or Global-PASS closure.

## Verification contract

S cannot close from the failed `c51ffc4e...` candidate. S-C1 must satisfy:

`PRE-WRITE MATRIX → ONE-COMMIT/FIVE-PATH CORRECTIVE DIFF → EXACT-HEAD READ-BACK → REQUIRED WORKFLOW SET → FULL-STACK STEP REVIEW → RUNTIME INTEGRITY/PROTOTYPE/INTEGRATION REVIEW → FAILURE/LEARNING ASSESSMENT`.

Only then may a documentation-only S/S-C1 closure commit be made, followed by exact closure-head verification.

## Learning disposition

Retained bounded lessons:

`SECTION-SCOPED SEMANTIC ASSERTION → SECTION-SCOPED TEST.`

`SEMANTIC REPAIR MUST PRESERVE ESTABLISHED INTERFACE/TEST CONTRACTS UNLESS THOSE CONTRACTS ARE PROVEN STALE OR WRONG.`

No new Governance rule is warranted.
