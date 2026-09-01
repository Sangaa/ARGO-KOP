# MUTATION MATRIX — P7 CORE-003 ↔ RUN-003 REL-071/072 RECONCILIATION — Q

Transaction: `MUT-2026-09-01-P7-CORE003-RUN003-REL071-072-Q`
Work Lease: `HERMUZ-P7-Q-REL071-072-20260901`
Priority: `7 — Core cross-layer relationship reconciliation`
State: `MATERIAL-CANDIDATE / CI-PENDING / LEASE ACTIVE`
Entry HEAD: `194b23856a5f5b45c00bdb27a9c28c43288acf11`
Pre-write Matrix HEAD: `9ac7dc336f07673a5fb666915bb6673bcc3aaf01`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Closed semantic input / synchronization-only scope

Transaction P independently validated:

`CORE-003 → RUN-003 = GOVERNS`

`RUN-003 → CORE-003 = REFERENCES`

Disposition: `BIDIRECTIONAL-AUTHORITY/DOCUMENTARY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY`.

Q adds no new semantic inference. It synchronizes that exact P-validated pair into the active relationship registry and the directly affected current control surfaces.

## Authorized material change set — exactly 6 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| Q-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE v1.2.13→v1.2.14; add REL-071/072 and bounded Q evidence | Y | PENDING CI |
| Q-02 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE REP-014 binding to v1.2.14 and Q refresh | Y | PENDING CI |
| Q-03 | `Core/_FOLDER_STATUS.md` | UPDATE v1.3.10→v1.3.11; add eighth bounded seam | Y | PENDING CI |
| Q-04 | `Quality/Integrity/test_core003_run003_authority_boundary.py` | UPDATE to exact unique REL-071/072 assertions; preserve source/negative semantics | Y | PENDING CI |
| Q-05 | `Repository/P7_CORE003_RUN003_REL071_072_RECONCILIATION_2026-09-01_Q.md` | CREATE bounded synchronization evidence | Y | PENDING CI |
| Q-06 | this Matrix | UPDATE in same material change set | Y | PENDING CI |

Candidate must be exactly one commit after the pre-write Matrix HEAD and contain exactly these six paths. Unexpected path expansion = `0`.

## Required preservation / non-authority

- CORE-003 and RUN-003 source files unchanged.
- REL-001..REL-070 preserved byte-for-semantic-content; no deletion or reclassification.
- Add only REL-071/072 with the P-validated controlled types.
- No `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, reverse RUN-003→CORE-003 GOVERNS, executable or runtime-coupling promotion.
- Manifest retains Phase 1 OPEN / Integrity HOLD / Global PASS NOT CLAIMED.
- Core status retains CROSS-LAYER VALIDATION OPEN and Folder Certification pending.
- No Priority-7, Phase-1, Connected Baseline, repository-wide graph or Global PASS closure.

## Prior learning

Transaction P is DIRECTLY APPLICABLE. REL-037/038 and Transactions M/O are DIRECTLY APPLICABLE structural precedent. L/N non-dependency discipline is TRANSFERABLE. No new governance rule is warranted.

## Verification contract

`EXACT-HEAD READ-BACK → ONE-COMMIT/SIX-PATH DIFF → REP-014 PRESERVATION CHECK → FOUR REQUIRED WORKFLOWS → FAILURE/LEARNING ASSESSMENT → CLOSURE COMMIT → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`

Work Lease remains `OPEN` until that sequence completes.
