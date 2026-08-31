# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-322 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-322
Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE / BASELINE-ONLY
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 322-01 | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | UPDATE | change only `EXPECTED_GROUP_COUNT = 7` → `6` | N | N |
| 322-02 | classifier/membership logic | KEEP | no algorithm, lineage, identity, consumer, authority, or target-selection change | Y | Y |
| 322-03 | EJR/Memory identities and 317/318 | KEEP | no identity or runtime mutation under rebaseline | Y | Y |

## KEEP REQUIREMENT
This lease is deterministic baseline normalization only. Do not change cohort derivation, namespace-lineage classifier, scan/audit logic, EJR or Memory content, consumer references, governance, REP-016 ordering, or 317/318 evidence.

## Execution Evidence
Repair321 functional head `dce9b40c7d013d3d7600812d7d9728ba4cafcb18` passed Full-Stack run `33422982316`. Internal-ID run `33422982303` passed all tests/stages except MEMORY_TO_ROOT census emission. Artifact `9769651317` proved `expected_group_count=7`, `observed_group_count=6`, `history_complete=true`, `decision=PARTIAL`, and `incomplete_group_ids=[__COHORT_COUNT_DRIFT__]` only. Remaining target IDs are EJR-165, EJR-237, EJR-293, EJR-294, EJR-295, EJR-296.

## Closure
After the one-line normalization require an exact compare proving only 7→6, Internal-ID SUCCESS with expected=6/observed=6/CENSUSED/incomplete=[], and Full-Stack SUCCESS. Any other change or failure blocks closure.