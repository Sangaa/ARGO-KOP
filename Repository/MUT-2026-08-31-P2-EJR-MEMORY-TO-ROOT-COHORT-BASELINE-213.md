# R71-20260831-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-213

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Parent verification lease: `R71-20260831-P2-EJR-211-IDENTITY-REPAIR-212`
Prewrite: `ecd9616a11a1e6026c52983196876aeb93c0d43e`
Functional head: `75160d7314bdcd79594447e3c50f2808ae1ccd5a`

## Trigger and diagnosis
Lease212 performed exactly one authorized repair: displaced root EJR-211 was re-identified to vacancy-proven EJR-401 with semantic-body preservation. Its exact-head Internal Document-ID Audit run `33354350722` triggered automatically and failed only at deterministic memory-to-root provenance census emission.

The Lease212 job proved all tests and all preceding deterministic audit/analyzer steps succeeded. Artifact `9744650333` then proved the isolated reason:
- expected_group_count=35;
- observed_group_count=34;
- history_complete=true;
- all 34 selected groups individually present;
- classification_complete=false only because `incomplete_group_ids=["__COHORT_COUNT_DRIFT__"]`.

Audit artifact `9744649112` proved neither EJR-211 nor EJR-401 remained ambiguous. This is an authorized one-group cohort reduction, not unexplained loss.

## Functional correction
Only one analyzer baseline constant changed:
- `EXPECTED_GROUP_COUNT = 35` → `EXPECTED_GROUP_COUNT = 34`.

Functional compare `ecd9616a11a1e6026c52983196876aeb93c0d43e...75160d7314bdcd79594447e3c50f2808ae1ccd5a` contains only:
- `Quality/Integration/ejr_memory_to_root_provenance_census.py` — 1 addition / 1 deletion;
- Lease213 Mutation Matrix synchronization.

Dynamic target selection, fail-on-drift behavior, complete-history gate, identity-source/cardinality validation, tests, evidence boundary, and EJR content remained unchanged.

## Exact-head execution evidence
On `75160d7314bdcd79594447e3c50f2808ae1ccd5a`:
- Internal Document-ID Audit `33354533694` — SUCCESS;
- Full-Stack Repository Audit `33354533731` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33354533715` — SUCCESS;
- M2 Multi-Channel Proposal Training `33354533677` — SUCCESS;
- Real Mutation Matrix Regression `33354533741` — SUCCESS.

Deterministic census artifact:
- artifact `ejr-memory-to-root-provenance-census` / ID `9744704885`;
- digest `sha256:4602e58755f39f1836c0194429ebc17f01220c246109028d14bac58a285d20b4`;
- expected_group_count=34;
- observed_group_count=34;
- history_complete=true;
- classification_complete=true;
- decision=CENSUSED;
- incomplete_group_ids=[].

Internal-ID artifact:
- artifact `internal-document-id-audit-report` / ID `9744702846`;
- digest `sha256:f0492f170a448a28fbfcdc375a4438a2b7eee3308d0ce35958b525577520042c`;
- EJR-211 absent from ambiguous_duplicate_records;
- EJR-401 absent from ambiguous_duplicate_records;
- remaining known path-bound candidates include EJR-219, EJR-301, and EJR-302.

## Learning promoted
`EACH AUTHORIZED REPAIR THAT REMOVES ONE CLASSIFIER-SELECTED AMBIGUITY GROUP MAY LEGITIMATELY MOVE THE DRIFT BASELINE BY ONE; PROVE THE POST-REPAIR COHORT FIRST, THEN REBASELINE IN A SEPARATE SUCCESSOR.`

## Boundaries preserved
Priority 2 remains OPEN. Phase 1 remains OPEN. Repository-wide identity/content/relationship reconciliation remains OPEN. Connected-Baseline/global graph validation remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS is claimed.

## Closure decision
Lease213 is CLOSED / EXECUTION-VERIFIED. Its successor evidence is sufficient to reconcile Lease212 while preserving Lease212's historical failed exact-head Internal-ID run accurately.
