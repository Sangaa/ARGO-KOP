# Lease 304 — MEMORY_TO_ROOT Cohort Baseline 12→11

Status: OPEN / BASELINE-ONLY
Date: 2026-08-31

Repair303 removed one verified ambiguity member from the MEMORY_TO_ROOT cohort without introducing any additional incomplete group. The deterministic census on the repair head reports:
- expected_group_count: 12;
- observed_group_count: 11;
- incomplete_group_ids: [`__COHORT_COUNT_DRIFT__`].

## Allowed Mutation
Update only `Quality/Integration/ejr_memory_to_root_provenance_census.py` from `EXPECTED_GROUP_COUNT = 12` to `EXPECTED_GROUP_COUNT = 11`.

## Required Closure
- exact single-file +1/-1 diff;
- Full-Stack Repository Audit SUCCESS;
- Internal Document-ID Audit SUCCESS;
- final census `11/11`, `classification_complete=true`, `decision=CENSUSED`, no incomplete IDs.

No identity mutation and no Global Integrity promotion are authorized by this lease.
