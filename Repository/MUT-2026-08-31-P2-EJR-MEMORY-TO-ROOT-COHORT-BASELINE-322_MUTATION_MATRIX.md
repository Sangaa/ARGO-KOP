# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-322 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-322
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 322-01 | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | UPDATE | change only `EXPECTED_GROUP_COUNT = 7` → `6` | Y | Y |
| 322-02 | classifier/membership logic | KEEP | no algorithm, lineage, identity, consumer, authority, or target-selection change | Y | Y |
| 322-03 | EJR/Memory identities and 317/318 | KEEP | no identity or runtime mutation under rebaseline | Y | Y |

## KEEP REQUIREMENT
This lease was deterministic baseline normalization only. Cohort derivation, namespace-lineage classifier, scan/audit logic, EJR or Memory content, consumer references, governance, REP-016 ordering, and 317/318 evidence were preserved.

## Execution Evidence
Repair321 functional head `dce9b40c7d013d3d7600812d7d9728ba4cafcb18` passed Full-Stack run `33422982316`. Internal-ID run `33422982303` preserved the expected 7→6 drift and failed only at the MEMORY_TO_ROOT census emission.

Rebaseline functional head `33d5784db1524c2785d3ee3f55146bc4b046b628` was compared against prewrite `fb877877d4327e00473412eed7d68d66d767925b`; the exact compare proves only one modified file and the single replacement `EXPECTED_GROUP_COUNT = 7` → `6`.

Final exact-head evidence:
- Internal-ID `33423363387`: SUCCESS.
- Census artifact `9769795299`, digest `sha256:6e958283241e57701a53573fbad582aa836bd3c2d07134a638b91766f4746c55`: expected=6, observed=6, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[], target_ids=EJR-165/EJR-237/EJR-293/EJR-294/EJR-295/EJR-296.
- Full-Stack `33423363336`: SUCCESS.
- Runtime/Integration `33423363394`: SUCCESS.
- M2 `33423363368`: SUCCESS.

## Closure
Lease322 is CLOSED / VERIFIED / RESUME-SAFE. Current deterministic MEMORY_TO_ROOT baseline is 6. Priority 2 remains OPEN and no queue promotion is authorized by this local closure.
