# R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-213

Status: PREWRITE / CORRECTIVE SUCCESSOR
Parent verification lease: `R71-20260831-P2-EJR-211-IDENTITY-REPAIR-212`
Baseline: `main@89c51d6aff95f86652a01153f2d842f4db0e7960`

## Trigger and proven diagnosis
Lease212 performed exactly one authorized displaced-record repair: root EJR-211 was re-identified to vacancy-proven EJR-401 with semantic body preservation. Internal Document-ID Audit run `33354350722` triggered automatically and failed only at deterministic `ejr_memory_to_root_provenance_census.py` emission.

The job proves all tests plus deterministic audit, ambiguity, chronology, namespace-lineage, non-monotonic, and reverse-direction analyzers succeeded. Only memory-to-root provenance census failed.

Artifact `ejr-memory-to-root-provenance-census` / ID `9744650333` proves:
- expected_group_count=35;
- observed_group_count=34;
- history_complete=true;
- the 34 selected groups are present;
- classification_complete=false solely because `incomplete_group_ids=["__COHORT_COUNT_DRIFT__"]`;
- neither EJR-211 nor EJR-401 remains in the classifier-selected MEMORY_TO_ROOT_EJR ambiguity cohort.

Internal-ID artifact `9744649112` proves neither EJR-211 nor EJR-401 appears in `ambiguous_duplicate_records`; remaining path-bound groups include EJR-219, EJR-301, and EJR-302.

## Prior-learning classification
- Lease202/209 fail-on-drift and post-repair rebaseline rule: DIRECTLY APPLICABLE.
- Lease212 one-record identity repair: DIRECTLY APPLICABLE causal evidence for the one-group reduction.
- Lease206 atomic prewrite rule: DIRECTLY APPLICABLE.

## Authorized correction
Recalibrate only `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
- `EXPECTED_GROUP_COUNT = 35` → `EXPECTED_GROUP_COUNT = 34`.

This is a post-repair baseline synchronization from proven live state. The dynamic classifier, count-drift failure behavior, complete-history gate, membership validation, provenance evidence boundary, and tests remain unchanged.

## Forbidden
- no EJR content/path/H1 mutation;
- no suppression/removal of `__COHORT_COUNT_DRIFT__`;
- no dynamic target-ID hardcoding;
- no ownership/canonical/migration decision;
- no scanner/test semantic change;
- no Priority2/Phase1/Connected-Baseline/global closure.

## Required verification
1. functional diff limited to one census baseline constant + Matrix;
2. exact-head Internal Document-ID Audit SUCCESS;
3. census artifact expected=34, observed=34, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[];
4. EJR-211 and EJR-401 remain non-ambiguous;
5. applicable Full-Stack / Runtime / M2 / Real Mutation Matrix PASS;
6. close this successor, then reconcile Lease212 without rewriting its historical failed exact-head run.

## Candidate learning
`EACH AUTHORIZED REPAIR THAT REMOVES ONE CLASSIFIER-SELECTED AMBIGUITY GROUP MAY LEGITIMATELY MOVE THE DRIFT BASELINE BY ONE; PROVE THE POST-REPAIR COHORT FIRST, THEN REBASELINE IN A SEPARATE SUCCESSOR.`
