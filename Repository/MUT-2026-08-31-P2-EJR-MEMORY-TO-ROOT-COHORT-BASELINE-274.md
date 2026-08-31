# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-274

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair273.
Opening repair head: `24cb04ef430316c2fb9b9f6ab6af7eaf82bbe5df`
Pre-write Matrix274: `46c6fd440dd7d58bf49fec54b49aea72aeb1c853`
Lease-open commit: `b450a43117bd0cc963ea2e581db46bb6a17fbb9e`
Functional baseline commit: `25668149d8e89d39ce8ef2bd66a29fb63bf3d293`

## Trigger and normalization

Repair273 reduced the MEMORY_TO_ROOT cohort by one. Repair-head artifact `9754096972`, digest `sha256:f6d40232ae5ee20b428e95b3fc5706ceca638c928afb03718510bbf68cffda1b`, proved history_complete=true, expected=22, observed=21, decision=PARTIAL, with sole incompleteness `__COHORT_COUNT_DRIFT__`.

Lease274 changed only `EXPECTED_GROUP_COUNT = 22` to `EXPECTED_GROUP_COUNT = 21` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`. Exact compare from Lease274 open to functional commit showed exactly that one file with +1/-1.

## Verification

- Internal Document-ID Audit #65 / run `33382121341`: SUCCESS.
- Full-Stack #2408 / run `33382121314`: SUCCESS.
- Final census artifact `9754166006`, digest `sha256:3b654b02d9d087c2e8b63ae22e34492014d5b3b42345d618384a2f4f95286c1c`.
- Final census: expected=21, observed=21, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

## Boundary and resume

Baseline 21 is now the deterministic MEMORY_TO_ROOT cohort baseline. No classifier, membership derivation, EJR, Memory, GOV/REP, consumer, or Global Integrity state changed in this lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Repair273 may close as execution-verified. Next target must be selected from the current 21-group census using fresh risk/consumer/chronology evidence.
