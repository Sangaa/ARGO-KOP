# Lease 316 — MEMORY_TO_ROOT_EJR Cohort Baseline Normalization 8 → 7

Status: OPEN / BASELINE-ONLY
Date: 2026-08-31

## Trigger
Repair315 removed one resolved EJR-234 ambiguity from the deterministic MEMORY_TO_ROOT_EJR cohort.

Repair-head evidence:
- expected_group_count: 8
- observed_group_count: 7
- history_complete: true
- incomplete_group_ids: [`__COHORT_COUNT_DRIFT__`]
- Full-Stack Repository Audit: SUCCESS

## Authorized mutation
Change only `EXPECTED_GROUP_COUNT` in `Quality/Integration/ejr_memory_to_root_provenance_census.py` from `8` to `7`.

No membership rule, lineage classifier, identity, content, authority, or relationship logic may change under this lease.

## Validation
After normalization require:
- compare = one file, one-line value replacement only;
- Internal Document-ID Audit = SUCCESS;
- census = expected 7 / observed 7 / `CENSUSED` / `incomplete_group_ids=[]`;
- Full-Stack Repository Audit = SUCCESS.

Global Integrity remains HOLD.
