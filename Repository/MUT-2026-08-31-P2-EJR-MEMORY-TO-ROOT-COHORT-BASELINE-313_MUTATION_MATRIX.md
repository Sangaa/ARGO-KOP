# MUTATION MATRIX — Lease 313 MEMORY_TO_ROOT Baseline 9 → 8

Transaction ID: MUT-2026-08-31-P2-EJR-BASELINE-313
Protocol: GOV-014
Status: OPEN

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 313-A | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | MODIFY | `EXPECTED_GROUP_COUNT = 8` only | N | N |

## KEEP REQUIREMENT
Preserve all classifier logic, cohort-member evidence logic, tests, authority boundaries, and unrelated files unchanged.

## Execution Evidence
Repair 312 post-state artifact identified only deterministic cohort-count drift 9→8; no member-specific incomplete IDs were present.

## Closure
Close only after exact compare, Internal Document-ID SUCCESS, 8/8 CENSUSED artifact, and Full-Stack SUCCESS.
