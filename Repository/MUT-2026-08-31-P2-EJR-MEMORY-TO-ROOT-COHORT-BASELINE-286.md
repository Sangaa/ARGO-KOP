# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-286

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair285.
Opening repair head: `6db3cc4f571cfbb4a6405f0f59d4be7a1e2e155b`
Pre-write Matrix286: `957ac01dc64e3e9df99b91a76719904cbb6733cf`
Normalized head: `138c20007da5f30707438ca0c60ebec251f6a539`

## Trigger and execution

Repair285 reduced observed MEMORY_TO_ROOT membership 18→17. Repair-head artifact `9757343910` proved history_complete=true and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Only `EXPECTED_GROUP_COUNT = 18` → `EXPECTED_GROUP_COUNT = 17` was changed in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

## Verification

- Full-Stack #2472 / run `33390998775`: SUCCESS.
- Internal Document-ID Audit #77 / run `33390998617`: SUCCESS.
- Final census artifact `9757448096`, digest `sha256:0a56ee51e0eba2cfcea1b12e42814c4ff0c5d114fa091cc1c545b63b9fdd451d`.
- Final census: expected=17, observed=17, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
