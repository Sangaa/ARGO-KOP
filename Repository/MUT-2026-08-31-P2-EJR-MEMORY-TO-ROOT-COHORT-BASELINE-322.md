# Lease 322 — MEMORY_TO_ROOT_EJR Cohort Baseline Normalization 7 → 6

Status: OPEN / BASELINE-ONLY
Date: 2026-08-31
Parent: Repair321

## Trigger
Repair321 resolved EJR-240 and removed it from the deterministic MEMORY_TO_ROOT cohort while retaining the earlier Memory allocation. Repair-head evidence intentionally preserved the baseline mismatch.

Repair-head census evidence:
- expected_group_count: 7
- observed_group_count: 6
- history_complete: true
- decision: PARTIAL
- incomplete_group_ids: [`__COHORT_COUNT_DRIFT__`] only
- remaining target_ids: EJR-165, EJR-237, EJR-293, EJR-294, EJR-295, EJR-296

## Authorized mutation
Change only `EXPECTED_GROUP_COUNT` in `Quality/Integration/ejr_memory_to_root_provenance_census.py` from `7` to `6`.

No cohort-membership rule, lineage classifier, identity, content, authority, consumer, relationship logic, REP-016 priority, or 317/318 evidence may change under this lease.

## Validation
Require exact one-line functional diff, Internal-ID 6/6 CENSUSED with no incomplete IDs, and Full-Stack SUCCESS.

Priority 2 remains OPEN regardless of this local baseline successor.