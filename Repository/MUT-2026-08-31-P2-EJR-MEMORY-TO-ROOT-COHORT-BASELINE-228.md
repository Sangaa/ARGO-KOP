# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-228

Status: OPEN / PREWRITE AUTHORITY
Baseline repair head: `a7434269d28c2f4bf5510497091291a2579feb74`
Triggering repair: Lease227, remaining root EJR-302 → EJR-405
Evidence: Internal Document-ID Audit run `33359946109`; census artifact `9746355744`; digest `sha256:5cf5e30dc15fbd91dadddf810bb102e352ece47e99d4a9b2572435ef6ef05c51`

## Proven drift
The repair-head deterministic MEMORY_TO_ROOT census proved:
- expected_group_count=32;
- observed_group_count=31;
- history_complete=true;
- classification_complete=false only because `__COHORT_COUNT_DRIFT__` remained;
- EJR-302 is absent from the selected ambiguity cohort after the final displaced root was repaired;
- all pre-census Internal-ID tests/analyzers passed and only the deterministic memory-to-root census step failed.

This is legitimate classifier-state change caused by the authorized Lease227 repair, not a defect in classifier logic or the repair.

## Authorized successor mutation
Change only `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 32` → `EXPECTED_GROUP_COUNT = 31`.

No classifier logic, test, workflow, EJR, GOV, REP, Memory, or repair-history mutation is authorized.

## Verification
Exact functional-head Internal-ID must prove expected=31, observed=31, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[]. Full-Stack, Runtime and M2 must pass. Real Mutation Matrix is NOT APPLICABLE if the census-only functional diff does not match its path filter; no meaningless change may be added to force a run.
