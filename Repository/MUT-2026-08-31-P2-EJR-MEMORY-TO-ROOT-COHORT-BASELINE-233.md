# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-233

Status: PREWRITE / BASELINE-ONLY SUCCESSOR
Predecessor: Lease232 repair `EJR-173 → EJR-406`

Repair-head Internal-ID run `33361053387` failed only at `Emit deterministic EJR memory-to-root provenance census`; all prior tests/analyzers passed. Artifact `9746702793`, digest `sha256:841c5fa6b705703e3c095014d3a26db9b4611476d2f116577894cb0304eae857`, proved `expected_group_count=31`, `observed_group_count=30`, `history_complete=true`, `classification_complete=false`, `decision=PARTIAL`, `incomplete_group_ids=["__COHORT_COUNT_DRIFT__"]`, with neither EJR-173 nor EJR-406 in the cohort.

Authorized functional mutation: change only `EXPECTED_GROUP_COUNT = 31` to `30` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`. No classifier/scanner/evidence-boundary/test/workflow/EJR/consumer semantics may change.
