# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 292

Status: PREWRITE / DETERMINISTIC NORMALIZATION AUTHORIZED
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-292
Opening repair head: `7e0fbe49cc337070985bd646b2a12a884f9ff11a`
Execution role: HERMUZ

## Trigger evidence

Repair291 resolved one MEMORY_TO_ROOT ambiguity by retaining Memory EJR-244 and atomically moving the displaced root allocation to complete-history-vacancy-proven EJR-421.

Repair-head Internal Document-ID run `33397181051` produced census artifact `9759797869`, digest `sha256:da8626225aa82d8e5201d9bcc7340434acca19b1e1ca1fb60ccde031eacb1a19`, proving:
- expected_group_count=16;
- observed_group_count=15;
- history_complete=true;
- classification_complete=false;
- decision=PARTIAL;
- incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`] and no other incomplete group.

Repair-head Full-Stack run `33397181070`: SUCCESS.

## Authorized mutation

Exactly one line may change in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 16` → `EXPECTED_GROUP_COUNT = 15`.

No classifier, membership logic, test, workflow, EJR, Memory, GOV, REP, consumer, historical reference, authority, or Global Integrity mutation is authorized.

After the one-line normalization, exact-head Internal Document-ID and Full-Stack evidence must be inspected. Closure requires expected=15, observed=15, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
