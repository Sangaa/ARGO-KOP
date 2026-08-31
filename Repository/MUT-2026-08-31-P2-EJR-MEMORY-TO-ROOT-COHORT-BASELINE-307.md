# MUT-2026-08-31-P2 — MEMORY_TO_ROOT Cohort Baseline Normalization — Lease 307

Status: CLOSED / EXECUTION-VERIFIED
Date: 2026-08-31
Scope: deterministic `MEMORY_TO_ROOT_EJR` provenance census expected-count normalization.

## Trigger

Repair306 reduced the actual cohort from 11 to 10. Its artifact showed only `__COHORT_COUNT_DRIFT__`.

## Executed Mutation

Functional head: `55571fa0cef3eccb533d17fe39815a23b385a0fd`.

Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` changed:

`EXPECTED_GROUP_COUNT = 11` → `10`.

Exact compare: one file, one addition, one deletion.

## Validation

Internal Document-ID Audit run `33413985956`: SUCCESS.
Full-Stack Repository Audit run `33413985972`: SUCCESS.

Inspected provenance artifact:
- `history_complete = true`
- `expected_group_count = 10`
- `observed_group_count = 10`
- `classification_complete = true`
- `decision = CENSUSED`
- `incomplete_group_ids = []`

Current cohort:
`EJR-165, EJR-174, EJR-234, EJR-237, EJR-240, EJR-248, EJR-293, EJR-294, EJR-295, EJR-296`.

## Closure

Lease307 is CLOSED. Cohort baseline is 10. Priority 2 remains OPEN; Phase 1 remains OPEN; Global Integrity remains HOLD.
