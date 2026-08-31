# MUT-2026-08-31-P2-EJR-215-TO-410-IDENTITY-REPAIR-252

Status: PREWRITE / FUNCTIONAL MUTATION NOT YET APPLIED
Scope: One-record Priority-2 identity repair: displaced root EJR-215 → EJR-410.

## Authority
- Disposition250 retains the earlier Memory EJR-215 and classifies the later root EJR-215 as displaced.
- Vacancy251 is CLOSED / EXECUTION-VERIFIED and authorizes one bounded allocation of EJR-410.
- Current deterministic census baseline is 27.

## Authorized functional change
In one bounded atomic change set:
1. retain `Memory/Engineering_Journal/EJR-215_2026-08-14_P32_SESSION_CLOSURE.md` unchanged;
2. delete `EJR/EJR-215_P2_INDEX_SCOPE_MUTATION_SCAFFOLD_2026-08-17.md`;
3. create `EJR/EJR-410_P2_INDEX_SCOPE_MUTATION_SCAFFOLD_2026-08-17.md` with the same semantic body/date/chronology and only the record identity/H1 changed from EJR-215 to EJR-410;
4. perform no consumer rewrite because the governed census plus fresh exact-ID/exact-path searches establish zero direct consumer obligations;
5. preserve `EXPECTED_GROUP_COUNT = 27` inside this repair lease.

## Verification contract
After functional mutation:
- compare prewrite→repair to prove bounded scope;
- re-read retained Memory, new root and absence of old root;
- inspect exact-head Internal-ID and deterministic MEMORY_TO_ROOT artifact;
- preserve any legitimate cohort-drift failure rather than weakening the guard;
- verify Full-Stack and all other applicable triggered workflows;
- if deterministic cohort changes, use a separate successor lease only.

## Boundaries
No unrelated EJR, Memory, GOV, REP, classifier logic, test, workflow, or global state is authorized to change. Priority 2 remains OPEN; Global Integrity remains HOLD.
