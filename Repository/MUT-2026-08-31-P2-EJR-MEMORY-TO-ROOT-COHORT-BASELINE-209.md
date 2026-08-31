# R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-209

Status: PREWRITE / CORRECTIVE SUCCESSOR
Parent verification lease: `R71-20260830-INTERNAL-ID-EJR-TRIGGER-COVERAGE-208`
Baseline: `main@8b6ab2b830deafffec7ff725417d7fa31547937d`

## Trigger
Lease208 successfully restored automatic `EJR/**` trigger coverage for Internal Document-ID Audit. Exact-head run `33329835211` then exposed one isolated failure: the deterministic `ejr_memory_to_root_provenance_census.py` report exited PARTIAL because its established cohort baseline remained 36 while the current lineage-selected cohort is 35.

## Proven cause
This is not unexplained loss. Lease207 intentionally repaired the displaced root `EJR-214` record to proven-vacant `EJR-400`, removing exactly one `MEMORY_TO_ROOT_EJR` ambiguity group from the current lineage-selected cohort. The current report shows `observed_group_count = 35`, all 35 selected groups individually complete, and the sole incomplete marker is `__COHORT_COUNT_DRIFT__`.

## Prior-learning classification
- Lease202 rule that dynamic cohort membership must fail on count drift: `DIRECTLY APPLICABLE`; the gate correctly detected baseline drift and must remain intact.
- Lease207 one-record identity repair: `DIRECTLY APPLICABLE` causal evidence for the one-group reduction.
- Lease206 atomic prewrite lesson: `DIRECTLY APPLICABLE`; this lease and Matrix must be attached atomically before functional mutation.

## Authorized correction
Recalibrate only the established live cohort baseline in `Quality/Integration/ejr_memory_to_root_provenance_census.py` from `36` to `35`.

This is a post-repair baseline update, not scanner weakening. The dynamic classifier, drift failure behavior, history gate, membership checks, provenance evidence boundaries, and test semantics remain unchanged.

## Forbidden
- no EJR content/path/identity mutation;
- no suppression or removal of `__COHORT_COUNT_DRIFT__`;
- no dynamic target-ID hardcoding;
- no ownership/canonical/migration decision;
- no change to Internal Document-ID scanner semantics;
- no Priority2 / Phase1 / Connected Baseline closure.

## Required verification
1. functional diff limited to census baseline constant + this Matrix;
2. exact-head Internal Document-ID Audit SUCCESS;
3. census artifact: expected=35, observed=35, classification_complete=true, decision=CENSUSED;
4. audit evidence must still show repaired EJR-214 ambiguity removed and EJR-400 not ambiguous;
5. applicable Full-Stack / Runtime / M2 / Real Mutation Matrix checks PASS;
6. parent Lease208 and Lease207 may close only after their required evidence is reconciled.

## Candidate learning
`A DRIFT GUARD THAT CORRECTLY FAILS AFTER AN AUTHORIZED IDENTITY REPAIR MUST BE REBASELINED FROM PROVEN POST-REPAIR STATE; DO NOT DISABLE THE GUARD OR NORMALIZE THE DRIFT AWAY.`
