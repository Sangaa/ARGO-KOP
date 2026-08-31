# R71-20260831-P2-EJR-401-REPLACEMENT-VACANCY-PROOF-211

Status: PREWRITE / VACANCY-PROOF ONLY
Baseline: `main@f2c2c106dcb8fac38a8b8d41ec2d1523ea593214`
Target future repair: `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`
Replacement candidate: `EJR-401`

## Re-entry and target selection
Room210 was re-read from live main. Priority 2 remains OPEN. Lease203/204 prove that the later root EJR-211 record is a legitimate displaced identity while the earlier Memory EJR-211 retains the historical allocation. Lease204 requires one displaced record per governed execution and recommends minimizing rewrite risk.

Two current-main searches for the exact displaced EJR-211 path/name returned only the historical Lease203/204 analysis records and established no current operational consumer requiring synchronous rewrite. By contrast, the remaining displaced EJR-219/EJR-301/EJR-302 records have explicit consumer/provenance rewrite obligations in Lease204. EJR-211 is therefore the bounded next candidate with the lowest presently established rewrite risk.

## Replacement-candidate discovery
Current-main code search for exact `EJR-401` returned no result. Commit-history search for `EJR-401` also returned no result. These are candidate-discovery signals only, not a vacancy decision.

## Prior-learning classification
- Lease193 complete-history vacancy gate: DIRECTLY APPLICABLE; only its execution may authorize allocation.
- Lease204 first-valid-allocation retention rule: DIRECTLY APPLICABLE.
- Lease206 vacancy-proof separation and atomic-prewrite lesson: DIRECTLY APPLICABLE.
- Lease207 one-record repair pattern: PARTIALLY APPLICABLE only after a new candidate is proven VACANT.
- Lease208 trigger-coverage rule: DIRECTLY APPLICABLE to any later EJR mutation, not to this vacancy-only proof.

## Authorized scope
Create a dedicated complete-history workflow that runs the existing `Quality/Integration/ejr_allocation_vacancy_gate.py` against `EJR-401`, uploads deterministic evidence, and fails unless decision=`VACANT`.

No allocation or EJR mutation is authorized by this lease.

## Forbidden
- no EJR rename/content/H1 mutation;
- no consumer rewrite;
- no vacancy assumption from search absence;
- no scanner/gate semantic change;
- no REP-012/014/016/020 mutation;
- no Priority2/Phase1/Connected-Baseline/global closure.

## Required verification
1. functional diff limited to dedicated workflow + this Matrix;
2. workflow checkout is complete-history (`fetch-depth: 0` + shallow=false assertion);
3. exact-head vacancy workflow SUCCESS;
4. artifact reports candidate EJR-401, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT;
5. applicable Full-Stack / Runtime / M2 / Real Mutation Matrix checks remain PASS;
6. close resume-safe before any repair lease.
