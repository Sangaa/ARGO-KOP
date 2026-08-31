# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-326 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-326
Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE / BASELINE-ONLY
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 326-01 | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | UPDATE | change only `EXPECTED_GROUP_COUNT = 6` → `5` | N | N |
| 326-02 | classifier/membership logic | KEEP | no lineage, membership, identity, consumer, authority or selection logic change | Y | Y |
| 326-03 | EJR/Memory content, REP-016, 317/318 | KEEP | no identity/runtime/priority mutation under rebaseline | Y | Y |

## KEEP REQUIREMENT
Normalize only the deterministic expected cohort count proven by Repair325. Do not change target derivation, lineage classifier, scan/audit logic, EJR/Memory identities or content, consumer references, authority artifacts, REP-016 ordering, 317/318, or Priority-2 closure state.

## Execution Evidence
Accepted Repair325 head `49680f1eddd29a4a18336261ae5aec594087d3a0` passed Full-Stack `33427225861` and Runtime/Integration `33427225759`. Internal-ID `33427225894` failed only at MEMORY_TO_ROOT census emission. Artifact `9771215241`, digest `sha256:abf5b10e02459cad33d05944542549e6d3cf33760ea7fb48ab68155487c13df9`, proves expected=6, observed=5, history_complete=true, decision=PARTIAL, incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`] only, target_ids=EJR-165/EJR-293/EJR-294/EJR-295/EJR-296.

## Closure
Close only if exact compare proves a single one-line baseline replacement and exact-head Internal-ID succeeds with expected=5/observed=5, classification_complete=true, decision=CENSUSED, incomplete=[]; Full-Stack must also succeed. Any other result is a HARD HOLD.
