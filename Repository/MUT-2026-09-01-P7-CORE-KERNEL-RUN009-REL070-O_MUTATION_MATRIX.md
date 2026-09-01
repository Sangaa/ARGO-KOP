# MUTATION MATRIX — P7 CORE-KERNEL → RUN-009 REL-070 RECONCILIATION — O

Transaction: `MUT-2026-09-01-P7-CORE-KERNEL-RUN009-REL070-O`
Work Lease: `HERMUZ-P7-O-REL070-20260901`
Priority: `7 — Core cross-layer validation / relationship reconciliation`
State: `MATERIAL-CANDIDATE / CI-PENDING / LEASE ACTIVE`
Entry HEAD: `fba9db310c17f3e3745db7062ee16a32b43182b2`
Pre-write Matrix HEAD: `9699e4859d6d1e60b04ce234d542ff1322e30ba2`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Reconstructed action

Transaction N exact-head validated `CORE-KERNEL → RUN-009 = REFERENCES / INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`. Live REP-014 v1.2.12 remained unsynchronized while current Core status explicitly requires relationship reconciliation where evidence requires. O synchronizes only that proven seam.

## Prior learning applied

N, K, M and E are directly applicable. M/R1 test-drift learning is explicitly applied by preserving N's source assertions verbatim and changing only the registry expectation.

## Atomic material change set

| ID | Path | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| O-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | v1.2.12→v1.2.13; add REL-070 only | Y | PENDING CI |
| O-02 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | sync REP-014 v1.2.13 / O refresh | Y | PENDING CI |
| O-03 | `Core/_FOLDER_STATUS.md` | v1.3.9→v1.3.10; record seventh bounded seam | Y | PENDING CI |
| O-04 | `Quality/Integrity/test_core_kernel_run009_recovery_boundary.py` | enforce exact unique REL-070; retain anti-overpromotion | Y | PENDING CI |
| O-05 | `Repository/P7_CORE_KERNEL_RUN009_REL070_RECONCILIATION_2026-09-01_O.md` | create evidence record | Y | PENDING CI |
| O-06 | this Matrix | same-change-set rebind | Y | PENDING CI |

Candidate must be exactly one commit after the pre-write Matrix HEAD and exactly these six paths. Unexpected path expansion must equal `0`.

## Semantic boundary

Registered relationship:

`REL-070 | CORE-KERNEL | RUN-009 | REFERENCES | INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`

No reverse edge and no `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, `GOVERNS` or executable-reachability promotion is authorized.

## KEEP / non-authority

CORE-KERNEL and RUN-009 sources remain unchanged. Phase 1 remains OPEN. Core remains CROSS-LAYER VALIDATION OPEN with Folder Certification pending. Connected Baseline, repository-wide graph closure and Global PASS remain unclaimed.

## Verification contract

`EXACT-HEAD READ-BACK → PREWRITE→CANDIDATE = ONE COMMIT / SIX AUTHORIZED PATHS / ZERO EXPANSION → REGISTRY PRESERVATION CHECK → FOUR REQUIRED WORKFLOWS → LEARNING ASSESSMENT → CLOSURE COMMIT → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`

Any failure is preserved under GOV-016 and cannot be hidden by weakening evidence assertions.
