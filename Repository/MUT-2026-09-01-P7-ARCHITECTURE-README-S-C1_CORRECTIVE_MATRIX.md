# MUTATION MATRIX — P7 ARCHITECTURE README S-C1 CORRECTIVE COMPATIBILITY RECONCILIATION

Transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-S-C1`
Parent Transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-AUTHORITY-DRIFT-S`
Work Lease: `HERMUZ-P7-S-C1-ARCHITECTURE-README-20260901`
Priority: `7 — Core cross-layer dependency/consumer validation`
State: `PRE-WRITE / CORRECTIVE / LEASE ACTIVE`
Entry HEAD: `c51ffc4efec9eaded777eeb4f97311386cc0a289`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016 / GOV-019 / GOV-020 / ARC-011 / ARC-006`

## Why S-C1 exists

Transaction S published material candidate `c51ffc4efec9eaded777eeb4f97311386cc0a289`. The candidate preserved its intended authority repair, but exact-head Runtime verification failed.

The first meaningful failure evidence identifies two compatibility regressions caused by S wording/link-format changes, not by the repaired authority semantics:

1. existing `test_architecture_folder_inventory_reconciliation.py` requires the exact open-gate marker `Architecture ↔ Runtime / Interface boundary — OPEN`; S changed that marker to include `/ AI`, creating an unnecessary textual compatibility break while the gate remained semantically open;
2. existing `test_canonical_reference_regressions.py` requires the canonical relative link `../Core/CORE-000_PLATFORM_ARCHITECTURE.md` inside `Architecture/README.md`; S retained the authoritative Core path semantically but rendered it as code text rather than the previously protected relative link.

Classification: `MATERIAL_CANDIDATE_CI_FAILURE / BACKWARD-COMPATIBILITY REGRESSION / AUTHORITY-SEMANTICS NOT INVALIDATED`.

The failed candidate remains evidence. No rerun is authorized before correction.

## Corrective decision

Restore the two established compatibility contracts without weakening S authority repair:

- restore the exact status marker `Architecture ↔ Runtime / Interface boundary — OPEN`;
- restore a valid Markdown link to `../Core/CORE-000_PLATFORM_ARCHITECTURE.md` in the README while preserving the statement that CORE-000 is Core-level intent aligned to ARC-011 and is not a competing Architecture authority.

Existing tests are evidence of current compatibility contracts and SHALL NOT be modified by S-C1.

## Authorized corrective material change set — exactly 5 paths

| ID | Target | Action |
|---|---|---|
| C1-01 | `Architecture/README.md` | UPDATE only as needed to restore canonical relative CORE-000 link while preserving S authority semantics |
| C1-02 | `Architecture/_FOLDER_STATUS.md` | UPDATE only as needed to restore exact Runtime/Interface open-gate marker and record S-C1 compatibility repair |
| C1-03 | `Repository/P7_ARCHITECTURE_README_AUTHORITY_ALIGNMENT_2026-09-01_S.md` | UPDATE S failure/correction evidence and state |
| C1-04 | `Repository/MUT-2026-09-01-P7-ARCHITECTURE-README-AUTHORITY-DRIFT-S_MUTATION_MATRIX.md` | UPDATE parent S failure/correction binding |
| C1-05 | this Matrix | UPDATE/rebind corrective candidate state in same material change set |

Unexpected path expansion = `0`.

## Explicitly forbidden

- no change to `Quality/Integrity/test_architecture_readme_authority_boundary.py`;
- no change to the two pre-existing tests that detected the regressions;
- no mutation of CORE-000, CORE-003, ARC-011, ARC-006, REP-014 or Core status;
- no weakening/removal of the S authority hierarchy;
- no Architecture/Core certification or Priority-7/Phase-1/global closure;
- no CI rerun used as substitute for material correction.

## Verification contract

`PRE-WRITE MATRIX → GIT-DATA OBJECT PREPARATION → ONE-COMMIT/FIVE-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → REQUIRED WORKFLOW SET → FULL-STACK JOB/STEP REVIEW → RUNTIME INTEGRITY/PROTOTYPE/INTEGRATION REVIEW → FAILURE/LEARNING ASSESSMENT → PARENT-S CLOSURE ONLY IF GREEN → CLOSURE-HEAD VERIFICATION`.

The correction is successful only if the previously failing compatibility assertions pass while the S focused authority regression remains unchanged and passes.

## Learning boundary

Retained bounded lesson:

`SEMANTIC REPAIR MUST PRESERVE ESTABLISHED INTERFACE/TEST CONTRACTS UNLESS THOSE CONTRACTS ARE THEMSELVES PROVEN STALE OR WRONG.`

No new Governance rule is claimed from this incident alone.
