# MUTATION MATRIX — Lease 316 MEMORY_TO_ROOT_EJR Baseline 8 → 7

Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-316
Protocol: GOV-014
Status: CLOSED / VERIFIED / RESUME-SAFE

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 316-01 | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | UPDATE | `EXPECTED_GROUP_COUNT = 8` → `7` only | Y | Y |
| 316-02 | all other functional files | KEEP | unchanged | Y | Y |

## KEEP REQUIREMENT
Cohort-membership derivation, namespace-lineage classification, audit logic, identity files, governance, and relationship evidence were unchanged.

## Execution Evidence
Functional head: `4532c480c8bc77373999ccdfc33a963d8c90fe8d`. Exact compare from the Lease316 opening head: one file with +1/-1 only. Internal-ID run `33419819450`: SUCCESS and census 7/7 CENSUSED with no incomplete IDs. Full-Stack run `33419819414`: SUCCESS.

## Closure
PASS / RESUME-SAFE. Global Integrity remains HOLD.
