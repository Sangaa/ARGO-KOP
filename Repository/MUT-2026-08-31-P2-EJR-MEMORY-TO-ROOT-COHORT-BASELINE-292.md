# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-292

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair291.
Opening repair head: `7e0fbe49cc337070985bd646b2a12a884f9ff11a`
Pre-write Matrix292: `48251aa024d29747eb69b93241da2e255c1d0b2a`
Functional normalization head: `d481a4169a37ac086125b3853675c32f9aed8e14`

## Trigger

Repair291 reduced observed MEMORY_TO_ROOT membership from 16 to 15 by retaining Memory EJR-244 and moving the displaced root record to complete-history-vacancy-proven EJR-421.

Repair-head Internal Document-ID run `33397181051` produced census artifact `9759797869`, digest `sha256:da8626225aa82d8e5201d9bcc7340434acca19b1e1ca1fb60ccde031eacb1a19`, proving expected_group_count=16, observed_group_count=15, history_complete=true, classification_complete=false, decision=PARTIAL, and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Repair-head Full-Stack run `33397181070`: SUCCESS.

## Executed normalization

Changed only `EXPECTED_GROUP_COUNT = 16` to `EXPECTED_GROUP_COUNT = 15` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

Exact compare from Lease292 open head `1ef37ba8cac1b3900b1e2f62bad0221b156e8b32` to normalization head `d481a4169a37ac086125b3853675c32f9aed8e14` shows one modified file with one addition and one deletion.

## Verification

- Full-Stack Repository Audit run `33397585419`: SUCCESS.
- Internal Document-ID Audit run `33397585341`: SUCCESS.
- final census artifact `9759944326`, digest `sha256:a2a09aff7d6f6177b0abb0936807cc0b91764bd1d57331b9a04460aaa48f3612`.
- final census: expected_group_count=15, observed_group_count=15, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].
- final target cohort: EJR-165, EJR-174, EJR-218, EJR-234, EJR-237, EJR-240, EJR-245, EJR-246, EJR-247, EJR-248, EJR-293, EJR-294, EJR-295, EJR-296, EJR-297.

No classifier/membership/test/workflow/EJR/Memory/GOV/REP/consumer/historical reference/authority/Global Integrity mutation occurred under this lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
