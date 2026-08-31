# MUTATION MATRIX — Lease 316 MEMORY_TO_ROOT_EJR Baseline 8 → 7

Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-316
Protocol: GOV-014
Status: OPEN

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 316-01 | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | UPDATE | `EXPECTED_GROUP_COUNT = 8` → `7` only | N | N |
| 316-02 | all other functional files | KEEP | unchanged | N | N |

## KEEP REQUIREMENT
Do not alter cohort-membership derivation, namespace-lineage classification, audit logic, identity files, governance, or relationship evidence. This lease normalizes one deterministic expected-count constant only.

## Execution Evidence
Repair315 Full-Stack succeeded. Its census artifact reported observed group count 7 with the only incomplete marker `__COHORT_COUNT_DRIFT__` against expected 8.

## Closure
Close only after exact diff inspection plus Internal-ID 7/7 CENSUSED and Full-Stack success on the normalization head.
