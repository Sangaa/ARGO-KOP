# Lease 322 — MEMORY_TO_ROOT_EJR Cohort Baseline Normalization 7 → 6

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
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

## Executed mutation
Functional head `33d5784db1524c2785d3ee3f55146bc4b046b628` changed only `Quality/Integration/ejr_memory_to_root_provenance_census.py`:

`EXPECTED_GROUP_COUNT = 7` → `6`.

Exact compare from prewrite head `fb877877d4327e00473412eed7d68d66d767925b` proves one modified file and one line replacement only.

## Final verification
Internal Document-ID Audit run `33423363387`: SUCCESS.
Census artifact `9769795299`, digest `sha256:6e958283241e57701a53573fbad582aa836bd3c2d07134a638b91766f4746c55`, proves:
- expected_group_count: 6
- observed_group_count: 6
- history_complete: true
- classification_complete: true
- decision: CENSUSED
- incomplete_group_ids: []
- target_ids: EJR-165, EJR-237, EJR-293, EJR-294, EJR-295, EJR-296

Full-Stack Repository Audit run `33423363336`: SUCCESS.
Runtime/Integration run `33423363394`: SUCCESS.
M2 run `33423363368`: SUCCESS.

## Outcome
Current deterministic MEMORY_TO_ROOT baseline is 6. No cohort-membership rule, lineage classifier, identity, content, authority, consumer, relationship logic, REP-016 priority, or 317/318 evidence changed under this lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
