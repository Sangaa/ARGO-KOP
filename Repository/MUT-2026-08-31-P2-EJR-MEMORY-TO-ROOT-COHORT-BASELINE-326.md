# Lease 326 — MEMORY_TO_ROOT_EJR Cohort Baseline Normalization 6 → 5

Status: OPEN / PRE-WRITE / BASELINE-ONLY
Date: 2026-08-31
Parent: Repair325

## Trigger
Repair325 resolved EJR-237→EJR-431 while preserving the required repair-head classifier drift. Deterministic artifact evidence proves the only incomplete marker is `__COHORT_COUNT_DRIFT__` with expected=6 and observed=5.

## Authorized mutation
Change only:
`Quality/Integration/ejr_memory_to_root_provenance_census.py`

`EXPECTED_GROUP_COUNT = 6` → `5`.

No identity, content, consumer, classifier, authority, relationship, REP-016 ordering, Runtime, 317 or 318 change is authorized.

## Verification boundary
Require exact one-line diff plus exact-head Internal-ID 5/5 CENSUSED and Full-Stack success before closure.

Priority 2 remains OPEN.
