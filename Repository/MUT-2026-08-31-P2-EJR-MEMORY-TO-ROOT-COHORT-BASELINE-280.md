# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-280

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair279.
Opening repair head: `84409b606d24c3a9d6ee5ad04efcff72116c2c57`
Pre-write Matrix280: `88f244cb289415db468f8129677271eae19fb59b`
Functional normalized head: `b33a9240b09d228c52470dd3435adbb3ebd1da5d`

## Result

Changed only `EXPECTED_GROUP_COUNT = 20` → `EXPECTED_GROUP_COUNT = 19` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

Verification:
- Full-Stack #2439 / run `33386720871`: SUCCESS;
- Internal Document-ID Audit #70 / run `33386720774`: SUCCESS;
- final census artifact `9755873735`, digest `sha256:2fefd6c2b84d4012d8a39c651ea0de410a53cad0d43fd52c004db9c0c4f85190`;
- expected_group_count=19;
- observed_group_count=19;
- history_complete=true;
- classification_complete=true;
- decision=CENSUSED;
- incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
