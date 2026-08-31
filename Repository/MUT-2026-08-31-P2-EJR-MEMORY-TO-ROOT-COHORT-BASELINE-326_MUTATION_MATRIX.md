# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-326 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-326
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 326-01 | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | UPDATE | change only `EXPECTED_GROUP_COUNT = 6` → `5` | Y | Y |
| 326-02 | classifier/membership logic | KEEP | no lineage, membership, identity, consumer, authority or selection logic change | Y | Y |
| 326-03 | EJR/Memory content, REP-016, 317/318 | KEEP | no identity/runtime/priority mutation under rebaseline | Y | Y |

## KEEP REQUIREMENT
The accepted rebaseline normalized only the deterministic expected cohort count proven by Repair325. Target derivation, lineage classifier, scan/audit logic, EJR/Memory identities and content, consumer references, authority artifacts, REP-016 ordering, Runtime implementation, 317/318, and Priority-2 closure state were preserved.

## Execution Evidence
Functional head `455de2b480cbef9b61459134450820a2a4284072` compared against prewrite `741180a5eb58c0b206a4389ef05c44ae3c2027b6` proves exactly one modified file and one line replacement: `EXPECTED_GROUP_COUNT = 6` → `5`.

Exact-head verification:
- Internal-ID `33427530380`: SUCCESS.
- Full-Stack `33427530398`: SUCCESS.
- Runtime/Integration `33427530477`: SUCCESS.
- M2 `33427530360`: SUCCESS.
- Census artifact `9771331682`, digest `sha256:f4a8ad4fd6f2d56ec41ddab34c4c50fc74da816bb1e87c5a2708bd24eb083db2`: expected=5, observed=5, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[], target_ids=EJR-165/EJR-293/EJR-294/EJR-295/EJR-296.

## Closure
Lease326 is CLOSED / VERIFIED / RESUME-SAFE. Current deterministic MEMORY_TO_ROOT baseline is 5. Priority 2 remains OPEN and no queue promotion is authorized by this local closure.
