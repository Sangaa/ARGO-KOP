# MUT — MEMORY_TO_ROOT Cohort Baseline Normalization — Lease 310

Date: 2026-08-31
Status: OPEN / BASELINE-ONLY
Priority: P2 Internal Document-ID Audit

## Trigger
Repair 309 atomically displaced the later root EJR-174 allocation to EJR-427. Full-Stack passed on the exact repair head. The deterministic provenance-census artifact reported:
- expected_group_count: 10
- observed_group_count: 9
- incomplete_group_ids: [`__COHORT_COUNT_DRIFT__`]
- no member-specific incomplete group.

## Scope
Normalize only `EXPECTED_GROUP_COUNT` in `Quality/Integration/ejr_memory_to_root_provenance_census.py` from `10` to `9`.

## Forbidden
- no identity rename/delete/reassignment;
- no change to cohort classifier semantics;
- no REP/GOV/Architecture promotion;
- no rewrite of historical EJR references.

## Validation
- exact compare must show one file only and one scalar change;
- Internal Document-ID Audit must succeed;
- final provenance-census artifact must be `expected=9`, `observed=9`, `classification_complete=true`, `decision=CENSUSED`, `incomplete=[]`;
- Full-Stack Repository Audit must succeed on the same functional head.

## Integrity
Priority 2 and Phase 1 remain OPEN. Global Integrity remains HOLD.
