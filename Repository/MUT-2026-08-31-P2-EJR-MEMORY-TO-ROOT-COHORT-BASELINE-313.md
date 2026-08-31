# Lease 313 — MEMORY_TO_ROOT_EJR Cohort Baseline Normalization

Status: OPEN / BASELINE-ONLY
Date: 2026-08-31
Scope: deterministic provenance census expectation only

## Trigger evidence
Repair 312 removed EJR-248 from the MEMORY_TO_ROOT_EJR ambiguity cohort by preserving the first-valid Memory allocation and moving the later root journal to EJR-428.

Post-repair artifact evidence:
- expected_group_count: 9
- observed_group_count: 8
- incomplete_group_ids: [`__COHORT_COUNT_DRIFT__`]
- no member-specific incomplete IDs
- Full-Stack Repository Audit: SUCCESS

## Authorized mutation
Change only `EXPECTED_GROUP_COUNT = 9` → `EXPECTED_GROUP_COUNT = 8` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

## Validation
Require exact compare proving a one-line value change, then Internal Document-ID Audit SUCCESS, provenance artifact `expected=8 / observed=8 / CENSUSED / incomplete=[]`, and Full-Stack SUCCESS.

Global Integrity remains HOLD.
