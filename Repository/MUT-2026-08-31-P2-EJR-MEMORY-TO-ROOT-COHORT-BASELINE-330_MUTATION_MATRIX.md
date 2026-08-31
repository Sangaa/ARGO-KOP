# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-330 — Mutation Matrix

Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-330
Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 330-01 | `Quality/Integration/ejr_memory_to_root_provenance_census.py` | UPDATE | `EXPECTED_GROUP_COUNT = 5` → `4` only | Y | Y |
| 330-02 | current MEMORY_TO_ROOT cohort | KEEP | EJR-165, EJR-294, EJR-295, EJR-296 unchanged | Y | Y |
| 330-03 | all identity/runtime/governance surfaces | KEEP | no EJR mutation, consumer rewrite, Runtime or REP-016 change | Y | Y |

## KEEP REQUIREMENT
This was a rebaseline-only lease. No identity disposition, rename, delete, allocation, semantic consumer rewrite, Runtime mutation, REP-016 mutation, priority promotion, or census logic change occurred. Functional diff was limited to the single expected cohort constant 5→4 and this Matrix in the same change set.

## Execution Evidence
Accepted functional commit: `1c39565e2f09bdbe4ae72b0d5daceee014a8003d`.
Exact functional diff: one line `EXPECTED_GROUP_COUNT = 5` → `4` plus this Matrix.

Exact-head verification:
- Internal Document-ID Audit `33429186547` = SUCCESS.
- Full-Stack Repository Audit `33429186569` = SUCCESS, including current-change Mutation Matrix enforcement and repository-wide audit.
- ARGO Runtime Prototype and Integration Tests `33429186567` = SUCCESS across integrity, integration and prototype jobs.
- Real Mutation Matrix Regression `33429186527` = SUCCESS.
- M2 Multi-Channel Proposal Training `33429186557` = SUCCESS.

Internal-ID artifact `9771922478`, digest `sha256:7663b689c2d4e3452e1f2b8c7d23bb2408d812b697c13cc7c9383bf1fee93e38`, proves:
- history_complete = true
- history_scope = all locally reachable refs
- expected_group_count = 4
- observed_group_count = 4
- classification_complete = true
- decision = CENSUSED
- incomplete_group_ids = []
- target_ids = EJR-165, EJR-294, EJR-295, EJR-296

## Closure
Lease330 is `CLOSED / VERIFIED / RESUME-SAFE`.

`MEMORY_TO_ROOT BASELINE = 4`
`CURRENT COHORT = EJR-165 / EJR-294 / EJR-295 / EJR-296`
`COHORT DRIFT = NONE`
`PRIORITY 2 = OPEN`
`GLOBAL INTEGRITY = HOLD`

Next resume point: rediscover live main, then continue Priority 2 from the current four-member cohort. Prefer the lowest-risk unresolved member after fresh chronology, consumer and prior-learning review; do not assume the next successor ID is vacant without complete-history proof.
