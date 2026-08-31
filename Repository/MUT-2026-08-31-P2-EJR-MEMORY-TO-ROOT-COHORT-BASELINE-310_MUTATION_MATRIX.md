# Mutation Matrix — Lease 310 — MEMORY_TO_ROOT Baseline 10→9

Date: 2026-08-31
Status: OPEN

## Allowed mutation
Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` may change functionally, and only `EXPECTED_GROUP_COUNT = 10` → `9`.

## Required evidence
1. Live-main re-entry before mutation.
2. Exact one-file compare.
3. Internal Document-ID Audit SUCCESS.
4. Census artifact inspection: 9/9, CENSUSED, no incomplete IDs.
5. Full-Stack SUCCESS on exact functional head.

## Forbidden
No identity mutation, no semantic classifier change, no authority promotion, no historical-reference cleanup.

## Closure
Close only after all evidence agrees; closure tail must remain documentation-only.
