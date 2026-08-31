# MUT-2026-08-31-P2-EJR-293-TO-432-IDENTITY-REPAIR-329 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-293-TO-432-IDENTITY-REPAIR-329
Protocol: GOV-013 / GOV-014A
Status: OPEN / FUNCTIONAL-APPLIED / VERIFICATION-PENDING
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 329-01 | `EJR/EJR-432_2026-08-21_HERMUZ_PRIOR_LEARNING_RETRIEVAL_GATE.md` | CREATE | displaced root EJR-293 content with first-H1 identity EJR-432; semantic body preserved | Y | N |
| 329-02 | `EJR/EJR-293_2026-08-21_HERMUZ_PRIOR_LEARNING_RETRIEVAL_GATE.md` | DELETE | old root identity absent in same atomic tree | Y | N |
| 329-03 | `EJR/EJR-294_2026-08-22_HERMUZ_BLIND_ACTIONS_BOUNDARY_EXPANSION.md` | UPDATE | root-learning semantic references EJR-293 → EJR-432 only | Y | N |
| 329-04 | `EJR/EJR-295_2026-08-22_HERMUZ_ACTIONS_IDENTITY_DISCOVERY_EXPERIMENT.md` | UPDATE | root-learning semantic reference EJR-293 → EJR-432 only | Y | N |
| 329-05 | `EJR/EJR-296_2026-08-22_HERMUZ_BLIND_REPOSITORY_PHENOMENA_AND_CONNECTOR_LAWS.md` | UPDATE | root-learning semantic reference EJR-293 → EJR-432 only | Y | N |
| 329-06 | `Memory/Engineering_Journal/EJR-293_2026-08-21_HERMUZ_P6_SCOPE_BOUNDARY_REPAIR_STEP02_FETCH.md` | KEEP | retained earlier allocation byte-for-byte | Y | N |
| 329-07 | MEMORY_TO_ROOT expected baseline | KEEP | remain 5 during repair; expected drift 5→4 is preserved for separate rebaseline | Y | Y |

## KEEP REQUIREMENT
Preserve the displaced root learning record body, date, provenance, decisions and chronology; change only path/first-H1 identity. Preserve Memory EJR-293 byte-for-byte. Rewrite only live semantic references whose referent is the root Prior-Learning Retrieval Gate record. Historical lease/baseline records remain historical and are not rewrite obligations. Do not change the census baseline, Runtime, REP-016, Priority ordering, or unrelated governance text.

## Prior Evidence
Lease327: `RETAIN = Memory EJR-293`; `DISPLACEMENT CANDIDATE = root EJR-293`.
Lease328: workflow run `33428317233` proved EJR-432 VACANT over all locally reachable refs; artifact `9771588196`, digest `sha256:4a72f53c58c9387f5cae065ca12b78b99590b2180e9eb635659ad20894312060`.
Semantic review identified live root-learning consumers in EJR-294, EJR-295, and EJR-296. Zero exact-path consumers was not treated as zero semantic consumers.

## Verification State
Functional mutation is staged atomically with this Matrix in the same change set. Closure remains blocked until exact diff and CI are inspected. Internal-ID cohort baseline remains intentionally 5 during this repair.

## Closure
Require exact diff bounded to the root identity move, the three semantic consumer rewrites, and this Matrix. Require Full-Stack success, Runtime/Integration success, relevant Matrix validation, and Internal-ID inspection if triggered. If the only Internal-ID failure is MEMORY_TO_ROOT expected=5/observed=4 `__COHORT_COUNT_DRIFT__`, preserve it and rebaseline separately. Any other failure is a HARD HOLD.
