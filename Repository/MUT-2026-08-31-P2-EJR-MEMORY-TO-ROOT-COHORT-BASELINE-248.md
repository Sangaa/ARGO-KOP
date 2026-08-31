# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-248

Status: PREWRITE / SUCCESSOR MUTATION PENDING
Scope: Deterministic MEMORY_TO_ROOT cohort baseline reconciliation after Repair247 only.

Repair247 preserved baseline 28 and its exact-head Internal-ID failed only at the deterministic MEMORY_TO_ROOT census. Artifact `9747775478`, digest `sha256:d2e8aabcfef6ea933828eefb55b2a5e7054b25caf149778d8ed6c3e8b6229c75`, proved:
- expected_group_count=28
- observed_group_count=27
- history_complete=true
- history_scope=all locally reachable refs
- incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`]
- EJR-213 absent from target_ids
- EJR-409 absent from target_ids.

Authorized successor change: modify only `Quality/Integration/ejr_memory_to_root_provenance_census.py` constant `EXPECTED_GROUP_COUNT = 28` to `27`. No classifier logic, workflow, EJR, Memory, Governance, REP, or historical evidence mutation is authorized.
