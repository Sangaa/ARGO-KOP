# Lease 304 — MEMORY_TO_ROOT Cohort Baseline 12→11

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Date: 2026-08-31

## Mutation
Functional head: `4290ad4ff0b1b3f814bf24c5f12b5ee892344489`.
Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` changed:
`EXPECTED_GROUP_COUNT = 12` → `EXPECTED_GROUP_COUNT = 11`.

Exact compare from lease opening head showed one modified file, +1/-1.

## Validation
- Full-Stack run `33412869607`: SUCCESS.
- Internal Document-ID Audit run `33412869597`: SUCCESS.
- Final census artifact:
  - expected_group_count: 11;
  - observed_group_count: 11;
  - classification_complete: true;
  - decision: `CENSUSED`;
  - incomplete_group_ids: [].

## Closure
Baseline normalization verified. Current MEMORY_TO_ROOT cohort size: 11. Global Integrity remains HOLD.
