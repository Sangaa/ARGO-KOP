# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-238

Status: OPEN / PREWRITE
Scope: Separate successor after EJR-208→EJR-407 repair.
Parent repair: Lease237 functional head `070d11f6e4f8b19815485dabbf384d144c87802d`.

Repair-head deterministic census artifact `9746992753`, digest `sha256:fd28f7ed37dd863da865a98744545c116c79cdfb8b6dd8869151b4b9b7a1f4f4`, proves expected_group_count=30, observed_group_count=29, history_complete=true, decision=PARTIAL solely because `__COHORT_COUNT_DRIFT__`; neither EJR-208 nor EJR-407 remains in the cohort.

Authorized functional change: in `Quality/Integration/ejr_memory_to_root_provenance_census.py`, change only `EXPECTED_GROUP_COUNT = 30` to `29`.

Forbidden: classifier/scanner/evidence-boundary/test/workflow/EJR/consumer semantics changes. Exact-head Internal-ID + Full-Stack + Runtime + M2 verification and deterministic census artifact are required after rebaseline.
