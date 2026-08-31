# MUT-2026-08-31-P2 — MEMORY_TO_ROOT Cohort Baseline Normalization — Lease 307

Status: OPEN / BASELINE-ONLY
Date: 2026-08-31
Scope: deterministic `MEMORY_TO_ROOT_EJR` provenance census expected-count normalization.

## Trigger Evidence

Repair306 completed the atomic displacement of root `EJR-247` to vacant successor `EJR-426` while preserving Memory `EJR-247` unchanged.

Exact repair-head evidence:

- Full-Stack Repository Audit: SUCCESS.
- Post-state: old root absent, successor root present, Memory blob preserved.
- Provenance census: `expected_group_count = 11`, `observed_group_count = 10`.
- Only incomplete marker: `__COHORT_COUNT_DRIFT__`.
- No member-specific incompleteness was reported.

## Authorized Mutation

Change only:

`Quality/Integration/ejr_memory_to_root_provenance_census.py`

from:

`EXPECTED_GROUP_COUNT = 11`

to:

`EXPECTED_GROUP_COUNT = 10`

No other semantic or identity mutation is authorized.

## Validation Gate

- compare must show exactly one file changed with one replacement;
- Internal Document-ID Audit must succeed;
- provenance census artifact must report expected=10, observed=10, `classification_complete=true`, `decision=CENSUSED`, and no incomplete IDs;
- Full-Stack Repository Audit must succeed.

## Non-Claims

This normalization does not resolve another cohort member and does not promote Global Integrity.
