# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-243

Status: OPEN / PREWRITTEN / SUCCESSOR-ONLY
Scope: reconcile deterministic MEMORY_TO_ROOT cohort drift exposed by Repair242.

Repair242 exact-head Internal-ID run `33363043188` failed only at the deterministic MEMORY_TO_ROOT census after all prior audit/chronology/lineage/provenance stages passed. Artifact `9747340901`, digest `sha256:8c24177282fbbf7933f1460aa27c7c158568ba00b739123d1bd4d791335deafe`, proved:
- expected_group_count=29
- observed_group_count=28
- history_complete=true
- classification_complete=false solely due `__COHORT_COUNT_DRIFT__`
- EJR-210 absent from target_ids
- EJR-408 absent from target_ids

This successor authorizes exactly one functional change: `EXPECTED_GROUP_COUNT = 29` → `28` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

No classifier logic, tests, workflows, EJR identities, governance, repository reports, Memory records, history, or global integrity state may change in this successor.
