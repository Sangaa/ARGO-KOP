# MUTATION MATRIX — P7 RUN-002 → CORE-003 INITIALIZATION AUTHORITY REFERENCE — R

Transaction: `MUT-2026-09-01-P7-RUN002-CORE003-REFERENCE-R`
Work Lease: `HERMUZ-P7-R-RUN002-CORE003-20260901`
Priority: `7 — Core cross-layer dependency/consumer validation`
State: `MATERIAL-CANDIDATE / CI-PENDING / LEASE ACTIVE / VALIDATION-FIRST`
Entry HEAD: `abfa867f2fa5d34ac1430f39e2c40143327f1018`
Pre-write Matrix HEAD: `33ce1e490b07fa1a123930b3c7dd958c471924c3`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Bounded candidate

Current direct evidence supports only:

`RUN-002 → CORE-003 = REFERENCES`

Disposition: `INTENTIONAL ONE-WAY / INITIALIZATION-AUTHORITY-RESOLUTION-ALIGNED / NON-DEPENDENCY`.

RUN-002 is canonical/critical initialization, requires validation before execution, verifies dependencies, prevents READY under failed/held integrity, enters FAULT/HOLD when required authority cannot be resolved, and directly lists CORE-003. The Constitution's broad applicability remains background authority and does not authorize a separately enumerated CORE-003→RUN-002 row without stronger source-specific evidence.

## Authorized material change set — exactly 3 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| R-01 | `Quality/Integrity/test_run002_core003_initialization_authority_reference.py` | CREATE bounded direct-source/negative-semantics regression | Y | PENDING CI |
| R-02 | `Repository/P7_RUN002_CORE003_INITIALIZATION_AUTHORITY_REFERENCE_2026-09-01_R.md` | CREATE bounded validation record | Y | PENDING CI |
| R-03 | this Matrix | UPDATE in same material change set | Y | PENDING CI |

Candidate must be exactly one commit after pre-write Matrix HEAD and exactly these three paths. Unexpected path expansion = `0`.

## KEEP / non-authority

- RUN-002 source unchanged.
- CORE-003 source unchanged.
- REP-014 unchanged by R.
- REP-020 and Core status unchanged by R.
- No RUN-002→CORE-003 DEPENDS_ON/GOVERNS/IMPLEMENTS/CONSUMES.
- No CORE-003→RUN-002 row of any type.
- No executable coupling, Runtime/Core certification, Priority-7/Phase-1/Connected-Baseline/repository-wide-graph/Global-PASS closure.

## Prior learning

P/Q and N/O are directly applicable; REL-037/038 is transferable but not mechanically copied; ARC_MAP's explicit navigation-only boundary is negative transferable evidence against reference inflation. No new governance rule is warranted.

## Verification contract

`EXACT-HEAD READ-BACK → ONE-COMMIT/THREE-PATH DIFF → FOUR REQUIRED WORKFLOWS → FAILURE/LEARNING ASSESSMENT → CLOSURE COMMIT → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION`.

Failure must remain evidence under GOV-016 and may not be erased by weakening source/test semantics.
