# Lease 316 — MEMORY_TO_ROOT_EJR Cohort Baseline Normalization 8 → 7

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Date: 2026-08-31

## Trigger
Repair315 resolved EJR-234 and reduced the deterministic MEMORY_TO_ROOT_EJR cohort from 8 to 7. Repair-head evidence showed the only incomplete marker was `__COHORT_COUNT_DRIFT__`.

## Executed mutation
Functional head `4532c480c8bc77373999ccdfc33a963d8c90fe8d` changed only:
`Quality/Integration/ejr_memory_to_root_provenance_census.py`

`EXPECTED_GROUP_COUNT = 8` → `7`.

Exact compare: one file, +1/-1 only.

## Final verification
Internal Document-ID Audit run `33419819450`: SUCCESS.
Final census artifact:
- expected_group_count: 7
- observed_group_count: 7
- history_complete: true
- classification_complete: true
- decision: CENSUSED
- incomplete_group_ids: []
- target_ids: EJR-165, EJR-237, EJR-240, EJR-293, EJR-294, EJR-295, EJR-296

Full-Stack Repository Audit run `33419819414`: SUCCESS.

## Outcome
Baseline normalization is verified. No membership rule, classifier, identity, authority, or relationship logic changed. Priority2 and Phase1 remain OPEN. Global Integrity remains HOLD.
