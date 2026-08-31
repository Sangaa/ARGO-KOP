# R71-20260831-P2-EJR-302A-TO-404-IDENTITY-REPAIR-224

Status: OPEN / PREWRITE / ONE-RECORD+CONSUMER REPAIR
Baseline: `main@6639e061fdff9d838a86567b0044e6a75df0dd4f`
Source: `EJR/EJR-302_2026-08-24_GT-041_DEEP_ROOT_CONFLICT.md`
Replacement: `EJR-404` — vacancy proven by Lease223 / run `33358057935` / artifact `9745762164`.
Direct consumer: `Repository/REP-022_SESSION_DELTA_2026-08-24_GT-041.md`

## Authorized mutation
Atomically move only the GT-041 displaced root record from EJR-302 to EJR-404, preserving semantic body/chronology except identity H1, and synchronize the direct governed REP-022 learning-record path in the same transaction.

## Explicit exclusions
Retain unchanged:
- `Memory/Engineering_Journal/EJR-302_2026-08-22_HERMUZ_CURRENT_HEAD_STATUS_RECHECK.md`;
- `EJR/EJR-302_2026-08-25_CI_DECISION_BOUNDARY_AND_TOOL_SURFACE_LEARNING.md`;
- GOV-013B provenance references;
- analyzers/tests/workflows/census baseline (`EXPECTED_GROUP_COUNT=32`).

Expected classifier behavior: because retained Memory EJR-302 and the second root EJR-302 remain, the EJR-302 ambiguity group should remain in the memory→root cohort; therefore this repair does not pre-authorize any cohort rebaseline. Verification evidence governs.

Priority 2 remains OPEN; Global integrity remains HOLD.
