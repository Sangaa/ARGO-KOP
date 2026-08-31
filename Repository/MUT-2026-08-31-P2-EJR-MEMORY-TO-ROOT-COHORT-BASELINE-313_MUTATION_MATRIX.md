# MUTATION MATRIX — Lease 313 MEMORY_TO_ROOT Baseline 9 → 8

Transaction ID: MUT-2026-08-31-P2-EJR-BASELINE-313
Protocol: GOV-014
Status: CLOSED / VERIFIED

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 313-A | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | MODIFY | `EXPECTED_GROUP_COUNT = 8` only | Y | Y |

## KEEP REQUIREMENT
All classifier logic, tests, authority boundaries, cohort-member evidence logic, and unrelated files were preserved.

## Execution Evidence
Exact compare showed one file with one-line value change (+1/-1). Internal-ID SUCCESS; provenance artifact 8/8 CENSUSED with no incomplete IDs; Full-Stack SUCCESS.

## Closure
PASS. Current deterministic baseline = 8. Global Integrity remains HOLD.
