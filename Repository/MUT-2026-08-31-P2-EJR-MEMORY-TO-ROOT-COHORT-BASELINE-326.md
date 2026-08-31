# Lease 326 — MEMORY_TO_ROOT_EJR Cohort Baseline Normalization 6 → 5

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Date: 2026-08-31
Parent: Repair325

## Trigger
Repair325 resolved EJR-237→EJR-431 while preserving the required repair-head classifier drift. Deterministic evidence proved the only incomplete marker was `__COHORT_COUNT_DRIFT__` with expected=6 and observed=5.

## Executed mutation
Functional head `455de2b480cbef9b61459134450820a2a4284072` changed only:
`Quality/Integration/ejr_memory_to_root_provenance_census.py`

`EXPECTED_GROUP_COUNT = 6` → `5`.

Exact compare from prewrite head `741180a5eb58c0b206a4389ef05c44ae3c2027b6` proves one modified file with one addition and one deletion only.

## Final verification
Internal Document-ID Audit `33427530380`: SUCCESS.
Full-Stack Repository Audit `33427530398`: SUCCESS.
Runtime/Integration `33427530477`: SUCCESS across integrity/prototype/integration jobs.
M2 `33427530360`: SUCCESS.

Census artifact `9771331682`, digest `sha256:f4a8ad4fd6f2d56ec41ddab34c4c50fc74da816bb1e87c5a2708bd24eb083db2`, proves:
- expected_group_count: 5
- observed_group_count: 5
- history_complete: true
- classification_complete: true
- decision: CENSUSED
- incomplete_group_ids: []
- target_ids: EJR-165, EJR-293, EJR-294, EJR-295, EJR-296

## Outcome
Current deterministic MEMORY_TO_ROOT baseline is 5. No cohort-membership rule, lineage classifier, identity, content, authority, consumer, relationship logic, REP-016 priority, Runtime implementation, 317 or 318 evidence changed under this lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
