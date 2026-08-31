# MUT-2026-08-31-P2-EJR-293-TO-432-IDENTITY-REPAIR-329 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-293-TO-432-IDENTITY-REPAIR-329
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / DRIFT-PRESERVED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 329-01 | `EJR/EJR-432_2026-08-21_HERMUZ_PRIOR_LEARNING_RETRIEVAL_GATE.md` | CREATE | displaced root EJR-293 content with first-H1 identity EJR-432; semantic body preserved | Y | Y |
| 329-02 | `EJR/EJR-293_2026-08-21_HERMUZ_PRIOR_LEARNING_RETRIEVAL_GATE.md` | DELETE | old root identity absent in same atomic tree | Y | Y |
| 329-03 | `EJR/EJR-294_2026-08-22_HERMUZ_BLIND_ACTIONS_BOUNDARY_EXPANSION.md` | UPDATE | root-learning semantic references EJR-293 → EJR-432 only | Y | Y |
| 329-04 | `EJR/EJR-295_2026-08-22_HERMUZ_ACTIONS_IDENTITY_DISCOVERY_EXPERIMENT.md` | UPDATE | root-learning semantic reference EJR-293 → EJR-432 only | Y | Y |
| 329-05 | `EJR/EJR-296_2026-08-22_HERMUZ_BLIND_REPOSITORY_PHENOMENA_AND_CONNECTOR_LAWS.md` | UPDATE | root-learning semantic reference EJR-293 → EJR-432 only | Y | Y |
| 329-06 | `Memory/Engineering_Journal/EJR-293_2026-08-21_HERMUZ_P6_SCOPE_BOUNDARY_REPAIR_STEP02_FETCH.md` | KEEP | retained earlier allocation byte-for-byte | Y | Y |
| 329-07 | MEMORY_TO_ROOT expected baseline | KEEP | remain 5 during repair; deterministic drift 5→4 preserved for separate rebaseline | Y | Y |

## KEEP REQUIREMENT
The displaced root learning record body, date, provenance, decisions and chronology were preserved except for path/first-H1 identity. Memory EJR-293 remained untouched. Only live semantic references whose referent is the root Prior-Learning Retrieval Gate record were rewritten. Historical lease/baseline records remain historical. Census baseline, Runtime, REP-016 and Priority ordering were unchanged under this repair.

## Prior Evidence
Lease327: `RETAIN = Memory EJR-293`; `DISPLACEMENT CANDIDATE = root EJR-293`.
Lease328: workflow run `33428317233` proved EJR-432 VACANT over all locally reachable refs; artifact `9771588196`, digest `sha256:4a72f53c58c9387f5cae065ca12b78b99590b2180e9eb635659ad20894312060`.

## Execution Evidence
Accepted functional commit: `e0db9a143abc8784c5e9f1768afe3d6b8343a269`.
Exact diff was bounded to the root identity move, EJR-294/EJR-295/EJR-296 semantic consumer rewrites, and this Matrix.

Exact-head verification:
- Full-Stack Repository Audit `33428723707` = SUCCESS, including current-change Mutation Matrix enforcement and repository-wide audit.
- ARGO Runtime Prototype and Integration Tests `33428723692` = SUCCESS across integrity, integration and prototype jobs.
- Real Mutation Matrix Regression `33428723682` = SUCCESS.
- M2 Multi-Channel Proposal Training `33428723700` = SUCCESS.
- Internal Document-ID Audit `33428723757` = FAILURE only at deterministic MEMORY_TO_ROOT census emission. All preceding identity/provenance tests passed.

Internal-ID artifact `9771754655`, digest `sha256:4e32ed63f7ce57c5e10dad99569f280e9b790e05a9a203a3b793654b8364e68c`, proves:
- expected_group_count = 5
- observed_group_count = 4
- incomplete_group_ids = [`__COHORT_COUNT_DRIFT__`]
- target_ids = EJR-165, EJR-294, EJR-295, EJR-296
- history_complete = true
- history_scope = all locally reachable refs

No other semantic, governance, runtime or regression failure was observed.

## Closure
Repair329 is `CLOSED / VERIFIED / DRIFT-PRESERVED / RESUME-SAFE`.

`ROOT EJR-293 -> EJR-432 = VERIFIED`
`MEMORY EJR-293 = RETAINED`
`LIVE ROOT-LEARNING CONSUMERS = REWRITTEN TO EJR-432`
`MEMORY_TO_ROOT COHORT = 4 OBSERVED / BASELINE STILL 5`

Next legal action: separate bounded rebaseline lease 330, changing only the deterministic MEMORY_TO_ROOT expected cohort baseline from 5 to 4, with its own pre-write Matrix and exact-head verification.
