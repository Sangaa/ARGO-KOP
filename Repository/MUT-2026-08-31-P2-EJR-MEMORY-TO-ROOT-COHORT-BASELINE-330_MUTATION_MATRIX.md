# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-330 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-330
Protocol: GOV-013 / GOV-014A
Status: OPEN / FUNCTIONAL-APPLIED / VERIFICATION-PENDING
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 330-01 | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | UPDATE | `EXPECTED_GROUP_COUNT = 5` → `4` only | Y | N |
| 330-02 | current MEMORY_TO_ROOT cohort | KEEP | EJR-165, EJR-294, EJR-295, EJR-296 unchanged | Y | N |
| 330-03 | all identity/runtime/governance surfaces | KEEP | no EJR mutation, consumer rewrite, Runtime or REP-016 change | Y | N |

## KEEP REQUIREMENT
This is a rebaseline-only lease. No identity disposition, rename, delete, allocation, semantic consumer rewrite, Runtime mutation, REP-016 mutation, priority promotion, or census logic change is authorized. The functional change is limited to the single expected cohort constant 5→4 and this Matrix is included in the same functional change set.

## Evidence
Repair329 accepted functional commit `e0db9a143abc8784c5e9f1768afe3d6b8343a269`. Internal-ID run `33428723757` produced artifact `9771754655`, digest `sha256:4e32ed63f7ce57c5e10dad99569f280e9b790e05a9a203a3b793654b8364e68c`, proving history_complete=true, expected_group_count=5, observed_group_count=4, incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`], and target_ids EJR-165/EJR-294/EJR-295/EJR-296. Full-Stack, Runtime/Integration, Real-Matrix and M2 all passed at the repair head.

## Verification State
Functional rebaseline is applied atomically with this Matrix. Closure remains blocked pending exact diff and exact-head CI verification.

## Closure
Require exact functional diff of this Matrix plus the single constant 5→4. Internal-ID must pass with expected=4/observed=4 and no incomplete IDs. Full-Stack and applicable Runtime/Integration, Real-Matrix and M2 gates must pass. Any other change or failure is a HARD HOLD.
