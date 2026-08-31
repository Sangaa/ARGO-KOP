# R71-20260831-P2-EJR-302A-TO-404-IDENTITY-REPAIR-224

Status: CLOSED / EXECUTION-VERIFIED / ONE-RECORD+CONSUMER REPAIR / RESUME-SAFE
Baseline: `main@6639e061fdff9d838a86567b0044e6a75df0dd4f`
Prewrite: `b9918d1462845d7f11bd17cb2c103d408e1abbe5`
Functional head: `598101140b1dc43ef09ffc66928426372738453d`
Source: `EJR/EJR-302_2026-08-24_GT-041_DEEP_ROOT_CONFLICT.md`
Replacement: `EJR-404` — vacancy proven by Lease223 / run `33358057935` / artifact `9745762164`.
Direct consumer: `Repository/REP-022_SESSION_DELTA_2026-08-24_GT-041.md`

## Authorized mutation executed
Atomically moved only the GT-041 displaced root record from EJR-302 to EJR-404, preserving semantic body/chronology except identity H1, and synchronized the direct governed REP-022 learning-record path in the same transaction.

## Preserved exclusions
Unchanged:
- `Memory/Engineering_Journal/EJR-302_2026-08-22_HERMUZ_CURRENT_HEAD_STATUS_RECHECK.md`;
- `EJR/EJR-302_2026-08-25_CI_DECISION_BOUNDARY_AND_TOOL_SURFACE_LEARNING.md`;
- GOV-013B provenance references;
- analyzers/tests/workflows/census baseline (`EXPECTED_GROUP_COUNT=32`).

## Verification
- compare `b9918d1… → 5981011…` = one EJR rename/H1 identity change + REP-022 path rewrite + Matrix state synchronization only;
- new EJR-404 direct read-back PASS;
- old GT-041 EJR-302 path absent;
- second root EJR-302 direct read-back retained;
- Real Mutation Matrix run `33359300998` SUCCESS;
- Full-Stack run `33359301032` SUCCESS;
- Runtime run `33359301073` SUCCESS;
- M2 run `33359301047` SUCCESS;
- Internal Document-ID Audit run `33359301122` SUCCESS.

Internal-ID census artifact `9746165907`, digest `sha256:9b2a34248cc09747e974e8d6afac358205b6d962c4bd497874bbbbef13e59efd`, proved:
- expected_group_count=32;
- observed_group_count=32;
- history_complete=true;
- classification_complete=true;
- decision=CENSUSED;
- incomplete_group_ids=[];
- EJR-302 remains a two-member MEMORY_EJR + ROOT_EJR ambiguity group containing only the retained Memory record and the 2026-08-25 CI Decision Boundary root record.

## Closure decision
No cohort rebaseline is authorized or required. The first displaced EJR-302 root record is repaired and verified. The second displaced root record remains a separate Priority-2 repair decision because its provenance reaches GOV-013B.

Priority 2 remains OPEN; Phase 1 remains OPEN; Global integrity remains HOLD; no BOOTED/INTEGRITY PASS claim.
