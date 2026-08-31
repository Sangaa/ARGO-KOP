# MUT-2026-08-31-P2-EJR-217-TO-411-IDENTITY-REPAIR-257

Status: PREWRITE / FUNCTIONAL MUTATION NOT YET APPLIED
Scope: One-record Priority-2 identity repair: displaced root EJR-217 → EJR-411.

## Authority
- Disposition255 retains the earlier Memory EJR-217 and classifies the later root EJR-217 as displaced.
- Vacancy256 is CLOSED / EXECUTION-VERIFIED and authorizes one bounded allocation of EJR-411.
- Current deterministic census baseline is 26.

## Authorized functional change
In one bounded atomic change set:
1. retain `Memory/Engineering_Journal/EJR-217_2026-08-14_P34_SESSION_CLOSURE.md` unchanged;
2. delete `EJR/EJR-217_CURRENT_BUILD_RECONCILIATION_POST_P3_2026-08-17.md`;
3. create `EJR/EJR-411_CURRENT_BUILD_RECONCILIATION_POST_P3_2026-08-17.md` with the same semantic body/date/chronology and only the record identity/H1 changed from EJR-217 to EJR-411;
4. perform no consumer rewrite because the complete deterministic census establishes zero external exact-ID references and zero exact-member-path consumers, with fresh repository search used only as secondary evidence;
5. preserve `EXPECTED_GROUP_COUNT = 26` inside this repair lease.

## Verification contract
After functional mutation:
- compare prewrite→repair to prove bounded scope;
- re-read retained Memory, new root and absence of old root;
- inspect exact-head Internal-ID and deterministic MEMORY_TO_ROOT artifact;
- preserve any legitimate cohort-drift failure rather than weakening the guard;
- verify Full-Stack/Runtime/M2/Real Mutation Matrix when applicable;
- if deterministic cohort changes, use a separate successor lease only.

## Boundaries
No unrelated EJR, Memory, GOV, REP, classifier logic, test, workflow, or global state is authorized to change. Priority 2 remains OPEN; Global Integrity remains HOLD.
