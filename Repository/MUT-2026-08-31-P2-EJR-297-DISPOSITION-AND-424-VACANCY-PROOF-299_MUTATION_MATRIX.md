# MUTATION MATRIX — EJR-297 DISPOSITION + EJR-424 VACANCY PROOF 299

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-297-DISPOSITION-AND-424-VACANCY-PROOF-299
Opening main: `2981ed42ed8c48a93ce659d5d7ba7fe0ee068ba8`
Execution role: HERMUZ
Proof head: `7ce6cbec0a21567e22834c48f972a32e0817451b`

## Selection and disposition evidence

Final 13-member MEMORY_TO_ROOT census selected EJR-297 as the lowest-exposure current ambiguity: 3 external exact-ID references and zero exact-member-path consumers for either member.

Chronology proves Memory allocation `edf6f4d2586ac2449b2b46cac3d94d2738144ce0` at 2026-08-21T16:20:41Z predates root allocation `ae7955021133b8e31c85e8b2a7915349f257b0ea` at 2026-08-22T02:01:56Z. Both records were directly read and are legitimate independent content. The root record is diagnostic learning and explicitly states that no P6 logic, relationship, runtime evidence, or governance state was promoted. Under the first-valid historical allocation rule, Memory EJR-297 is RETAINED and root EJR-297 is DISPLACED legitimate content.

## Executed evidence gate

Dedicated workflow used complete checkout history and `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-424`.

- vacancy workflow run `33410673926`: SUCCESS;
- artifact `9764977768`, digest `sha256:68d1f7e5ea2cf9590f9477376c15edeaccd1cbeb5f4782057b5f907acadf5230`;
- decision=VACANT;
- current_claims=[];
- historical_claims=[];
- history_complete=true;
- history_scope=`all locally reachable refs`;
- proof-head Full-Stack run `33410673865`: SUCCESS.

EJR-424 is reserved solely for displaced root EJR-297. No identity repair, cohort normalization, consumer rewrite, governance promotion, REP promotion, or Global Integrity change was executed under Lease299.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
