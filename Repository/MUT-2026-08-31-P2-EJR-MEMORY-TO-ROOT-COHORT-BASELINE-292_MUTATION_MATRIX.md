# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 292

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-292
Opening repair head: `7e0fbe49cc337070985bd646b2a12a884f9ff11a`
Execution role: HERMUZ
Functional normalization head: `d481a4169a37ac086125b3853675c32f9aed8e14`

## Trigger evidence

Repair291 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-244 and atomically moving the displaced root allocation to complete-history-vacancy-proven EJR-421.

Repair-head Internal Document-ID run `33397181051` produced census artifact `9759797869`, digest `sha256:da8626225aa82d8e5201d9bcc7340434acca19b1e1ca1fb60ccde031eacb1a19`, proving expected=16, observed=15, history_complete=true, decision=PARTIAL, with sole incomplete group `__COHORT_COUNT_DRIFT__`.

Repair-head Full-Stack run `33397181070`: SUCCESS.

## Executed mutation

Exactly one line changed in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 16` → `EXPECTED_GROUP_COUNT = 15`.

Exact compare from Lease292 open head `1ef37ba8cac1b3900b1e2f62bad0221b156e8b32` to normalization head `d481a4169a37ac086125b3853675c32f9aed8e14` shows one modified file with one addition and one deletion.

## Final verification

- Full-Stack run `33397585419`: SUCCESS.
- Internal Document-ID run `33397585341`: SUCCESS.
- final census artifact `9759944326`, digest `sha256:a2a09aff7d6f6177b0abb0936807cc0b91764bd1d57331b9a04460aaa48f3612`.
- expected=15, observed=15, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

No other mutation was authorized or executed by Matrix292.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
