# MUTATION MATRIX — P7 CORE-003 ↔ RUN-003 AUTHORITY VALIDATION — P

Transaction: `MUT-2026-09-01-P7-CORE003-RUN003-AUTHORITY-P`
Work Lease: `HERMUZ-P7-P-CORE003-RUN003-20260901`
Priority: `7 — Core cross-layer validation`
State: `MATERIAL-CANDIDATE / CI-PENDING / LEASE ACTIVE / VALIDATION-FIRST`
Entry HEAD: `1392b031a49c187453daa2f03cfa8250aa08e6db`
Pre-write Matrix HEAD: `86fe1d5d4ea905dd70104b8d3d9bb15753a659f8`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Boot-proof and legal action

Current `main`, bootstrap, REP-016, REP-014 and Core status were re-proven before the first write. Priority 7 remains open. Direct current source evidence supports only the bounded candidate pair:

`CORE-003 → RUN-003 = GOVERNS`

`RUN-003 → CORE-003 = REFERENCES`

Disposition: `BIDIRECTIONAL-AUTHORITY/DOCUMENTARY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY`.

REL-037/038 CORE-003↔RUN-001 is directly applicable prior learning. Transactions L/M and N/O are transferable. Broad constitutional applicability is insufficient by itself to justify registry enumeration.

## Material change set

| Change ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| P-01 | `Quality/Integrity/test_core003_run003_authority_boundary.py` | CREATE | Y | PENDING CI |
| P-02 | `Repository/P7_CORE003_RUN003_AUTHORITY_SEAM_2026-09-01_P.md` | CREATE | Y | PENDING CI |
| P-03 | this Matrix | UPDATE IN SAME MATERIAL CHANGE SET | Y | PENDING CI |

Candidate must be exactly one commit from the pre-write Matrix HEAD and exactly these three paths. Unexpected path expansion must equal `0`.

## Required evidence boundary

The focused regression preserves exact current source assertions:

- CORE-003 is the highest governing rule surface and applies to repository components within scope;
- RUN-003 is canonical/critical Runtime configuration;
- RUN-003 says configuration controls runtime behavior without modifying architecture or authority;
- RUN-003 explicitly says Runtime configuration does not override CORE-003;
- RUN-003 directly references CORE-003 and keeps repository authority above runtime assumptions;
- REP-014 absence of this pair during validation-first P;
- prohibition on reverse governing edge and dependency/consumer/implementation promotion;
- Core status remains cross-layer validation open / certification pending.

## KEEP / non-authority

No mutation to CORE-003, RUN-003, REP-014, REP-020 or Core status. Existing REL-001..REL-070 remain unchanged. No executable/dependency promotion. No Runtime/Core certification, Priority-7 closure, Phase-1 closure, Connected Baseline closure, repository-wide graph closure or Global PASS.

## Verification contract

`EXACT-HEAD READ-BACK → DIFF SCOPE = 3 AUTHORIZED PATHS / ONE COMMIT → FOUR REQUIRED WORKFLOWS → LEARNING ASSESSMENT → CLOSURE COMMIT → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`

Failure is preserved and governed under GOV-016; source/test semantics are not weakened to manufacture PASS.
