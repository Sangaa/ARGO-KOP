# MUTATION MATRIX — P7 CORE-003 ↔ RUN-003 REL-071/072 RECONCILIATION — Q

Transaction: `MUT-2026-09-01-P7-CORE003-RUN003-REL071-072-Q`
Work Lease: `HERMUZ-P7-Q-REL071-072-20260901`
Priority: `7 — Core cross-layer relationship reconciliation`
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY-7-OPEN`
Entry HEAD: `194b23856a5f5b45c00bdb27a9c28c43288acf11`
Pre-write Matrix HEAD: `9ac7dc336f07673a5fb666915bb6673bcc3aaf01`
Material candidate HEAD: `9c5e8655800c74103fcf854d25e310525ba979f5`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Closed semantic input / synchronization-only result

Transaction P independently validated:

`CORE-003 → RUN-003 = GOVERNS`

`RUN-003 → CORE-003 = REFERENCES`

Disposition: `BIDIRECTIONAL-AUTHORITY/DOCUMENTARY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY`.

Q added no new semantic inference. It synchronized that exact validated pair into the active relationship registry and directly affected control surfaces.

## Authorized material change set — exactly 6 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| Q-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE v1.2.13→v1.2.14; add REL-071/072 and bounded Q evidence | Y | Y |
| Q-02 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE REP-014 binding to v1.2.14 and Q refresh | Y | Y |
| Q-03 | `Core/_FOLDER_STATUS.md` | UPDATE v1.3.10→v1.3.11; add eighth bounded seam | Y | Y |
| Q-04 | `Quality/Integrity/test_core003_run003_authority_boundary.py` | UPDATE to exact unique REL-071/072 assertions; preserve source/negative semantics | Y | Y |
| Q-05 | `Repository/P7_CORE003_RUN003_REL071_072_RECONCILIATION_2026-09-01_Q.md` | CREATE bounded synchronization evidence | Y | Y |
| Q-06 | this Matrix | UPDATE in same material change set | Y | Y |

Candidate comparison from `9ac7dc336f07673a5fb666915bb6673bcc3aaf01` to `9c5e8655800c74103fcf854d25e310525ba979f5` proved exactly one commit and exactly six authorized paths. Unexpected path expansion = `0`.

## Preservation proof

Pre-publish compare profile:

- REP-014: +34/-1, matching version bump + exactly two rows + one bounded Q evidence section;
- Core status: 13 changed lines;
- current manifest: 4 changed lines;
- focused test: 9 changed lines;
- Q record and this Matrix confined to authorized scope.

Direct candidate read-back confirmed REP-014 v1.2.14 with exact REL-071/072 rows and the pre-existing relationship table preserved in the inspected range; Core status v1.3.11 retains `CROSS-LAYER VALIDATION OPEN` and Folder Certification pending.

## Exact-head verification

Required workflows on material candidate `9c5e8655800c74103fcf854d25e310525ba979f5`:

- Full-Stack Repository Audit — `33526263644` — SUCCESS. Repository-audit and all reported steps succeeded, including exact checkout SHA binding, Mutation Matrix preflight, Matrix semantic regression, same-change-set enforcement, repository-wide audit and evidence emission.
- ARGO Runtime Prototype and Integration Tests — `33526263538` — SUCCESS. Integrity, prototype and integration jobs all succeeded with all reported steps successful.
- Real Mutation Matrix Regression — `33526263608` — SUCCESS.
- M2 Multi-Channel Proposal Training — `33526263559` — SUCCESS.

Result: `4/4 REQUIRED WORKFLOWS SUCCESS`.

No material failure occurred in Q.

## KEEP / non-authority

- CORE-003 and RUN-003 source files unchanged.
- REL-001..REL-070 retained; no reclassification authorized.
- REL-071/072 only use the P-validated controlled types.
- No `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, reverse RUN-003→CORE-003 GOVERNS, executable or runtime-coupling promotion.
- Manifest retains Phase 1 OPEN / Integrity HOLD / Global PASS NOT CLAIMED.
- Core status retains CROSS-LAYER VALIDATION OPEN and Folder Certification pending.
- No Priority-7, Phase-1, Connected Baseline, repository-wide graph or Global PASS closure.

## Learning assessment

Transaction P, REL-037/038 and Transactions M/O were directly applicable. L/N non-dependency discipline was transferable. The result is successful reuse, not a novel governance gap; no new rule is warranted.

Work Lease: `CLOSED / RESUME-SAFE`.

A future continuation must rediscover live `main` and recompute Priority 7. This Matrix does not pre-authorize a next mutation or certification decision.
