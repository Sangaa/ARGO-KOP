# MUTATION MATRIX — P7 ARCHITECTURE README S-C1 CORRECTIVE COMPATIBILITY RECONCILIATION

Transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-S-C1`
Parent Transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-AUTHORITY-DRIFT-S`
Work Lease: `HERMUZ-P7-S-C1-ARCHITECTURE-README-20260901`
Priority: `7 — Core cross-layer dependency/consumer validation`
State: `CORRECTIVE MATERIAL CANDIDATE / CI-PENDING / LEASE ACTIVE`
Entry HEAD: `c51ffc4efec9eaded777eeb4f97311386cc0a289`
Pre-write Matrix HEAD: `b6cb16fc31637f336f57b6b3d0cf5b1592ea4ed3`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / GOV-019 / GOV-020 / ARC-011 / ARC-006`

## Failure evidence requiring correction

Parent S candidate `c51ffc4e...` preserved the intended authority repair but failed Runtime workflow `33530617715`.

First meaningful integrity failure evidence:

1. `test_architecture_folder_inventory_reconciliation.py` requires exact marker `Architecture ↔ Runtime / Interface boundary — OPEN`; S unnecessarily changed that established marker to include `/ AI`.
2. `test_canonical_reference_regressions.py` requires `../Core/CORE-000_PLATFORM_ARCHITECTURE.md` in `Architecture/README.md`; S retained the same target semantically but lost the protected relative-link representation.

The integrity suite reported `2 failed, 136 passed`; prototype tests succeeded. Full-Stack workflow `33530617711` succeeded but does not override Runtime failure.

Classification: `MATERIAL_CANDIDATE_CI_FAILURE / BACKWARD-COMPATIBILITY REGRESSION / AUTHORITY-SEMANTICS NOT INVALIDATED`.

## Corrective material decision

Restore only the two proven compatibility contracts while retaining S authority semantics:

- restore a Markdown reference whose target is exactly `../Core/CORE-000_PLATFORM_ARCHITECTURE.md`;
- restore the exact open-gate marker `Architecture ↔ Runtime / Interface boundary — OPEN`;
- preserve AI in the broader cross-reference-review narrative without changing that established gate marker;
- preserve Constitution/Governance → ARC-011 → other Architecture → repository/implementation;
- preserve CORE-000 as Core-level intent aligned to ARC-011, not a competing authority;
- preserve Architecture Integrity Hold and all broader open gates.

## Authorized corrective change set — exactly 5 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| C1-01 | `Architecture/README.md` | restore canonical relative CORE-000 Markdown link only; retain S semantics | Y | PENDING CI |
| C1-02 | `Architecture/_FOLDER_STATUS.md` | restore exact Runtime/Interface open marker; record S-C1; retain broader Hold/Open state | Y | PENDING CI |
| C1-03 | `Repository/P7_ARCHITECTURE_README_AUTHORITY_ALIGNMENT_2026-09-01_S.md` | preserve failed-candidate and corrective provenance | Y | PENDING CI |
| C1-04 | `Repository/MUT-2026-09-01-P7-ARCHITECTURE-README-AUTHORITY-DRIFT-S_MUTATION_MATRIX.md` | bind parent S to failed candidate and S-C1 | Y | PENDING CI |
| C1-05 | this Matrix | bind corrective candidate state | Y | PENDING CI |

Candidate must be exactly one commit after `b6cb16fc...`, exactly these five paths, unexpected path expansion `0`.

## Explicitly forbidden

- no change to `Quality/Integrity/test_architecture_readme_authority_boundary.py`;
- no change to either pre-existing regression that detected the failure;
- no CORE-000/CORE-003/ARC-011/ARC-006/REP-014/Core-status mutation;
- no removal or weakening of S authority hierarchy;
- no Architecture/Core certification or Priority-7/Phase-1/global closure;
- no rerun as substitute for material correction.

## Verification contract

`GIT-DATA PREP → ONE-COMMIT/FIVE-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → REQUIRED WORKFLOW SET → FULL-STACK SHA/MATRIX/AUDIT STEP REVIEW → RUNTIME INTEGRITY/PROTOTYPE/INTEGRATION REVIEW → FAILURE/LEARNING ASSESSMENT`.

The corrective candidate succeeds only if the previously failing assertions pass while the unchanged S focused authority regression also passes.

If candidate verification succeeds, S-C1 still requires a documentation/control closure and exact closure-head verification before the parent S lease can become Resume-Safe.

## Learning boundary

`SEMANTIC REPAIR MUST PRESERVE ESTABLISHED INTERFACE/TEST CONTRACTS UNLESS THOSE CONTRACTS ARE THEMSELVES PROVEN STALE OR WRONG.`

Existing Governance already requires evidence-based validation and controlled mutation; no new Governance rule is created here.
