# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-280

Status: OPEN / FUNCTIONAL NORMALIZATION PENDING
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair279.
Opening repair head: `84409b606d24c3a9d6ee5ad04efcff72116c2c57`
Pre-write Matrix280: `88f244cb289415db468f8129677271eae19fb59b`

## Trigger

Repair279 reduced observed MEMORY_TO_ROOT membership from 20 to 19. Artifact `9755813652`, digest `sha256:f16e386eec759e34757099271ab50f04dfca4d5c0b01bb008b2107b04ff2fad2`, proves history_complete=true and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Authorized normalization: change only `EXPECTED_GROUP_COUNT = 20` to `EXPECTED_GROUP_COUNT = 19`.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
