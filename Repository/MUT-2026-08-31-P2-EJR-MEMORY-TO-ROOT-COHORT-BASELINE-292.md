# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-292

Status: OPEN / DETERMINISTIC NORMALIZATION
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair291.
Opening repair head: `7e0fbe49cc337070985bd646b2a12a884f9ff11a`
Pre-write Matrix292: `48251aa024d29747eb69b93241da2e255c1d0b2a`

## Trigger

Repair291 reduced observed MEMORY_TO_ROOT membership from 16 to 15 by retaining Memory EJR-244 and moving the displaced root record to complete-history-vacancy-proven EJR-421.

Repair-head Internal Document-ID run `33397181051` produced census artifact `9759797869`, digest `sha256:da8626225aa82d8e5201d9bcc7340434acca19b1e1ca1fb60ccde031eacb1a19`, proving expected_group_count=16, observed_group_count=15, history_complete=true, classification_complete=false, decision=PARTIAL, and sole incompleteness `__COHORT_COUNT_DRIFT__`.

Repair-head Full-Stack run `33397181070`: SUCCESS.

## Authorized normalization

Change only `EXPECTED_GROUP_COUNT = 16` to `EXPECTED_GROUP_COUNT = 15` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

No classifier/membership/test/workflow/EJR/Memory/GOV/REP/consumer/historical reference/authority/Global Integrity mutation is authorized under this lease.

Closure requires exact-head Full-Stack success and exact census expected=15, observed=15, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
