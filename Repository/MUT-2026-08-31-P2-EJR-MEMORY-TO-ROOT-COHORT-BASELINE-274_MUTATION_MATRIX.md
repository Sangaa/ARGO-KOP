# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 274

Status: CLOSED / EXECUTION-VERIFIED
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-274
Opening repair head: `24cb04ef430316c2fb9b9f6ab6af7eaf82bbe5df`
Prewrite head: `46c6fd440dd7d58bf49fec54b49aea72aeb1c853`
Lease-open commit: `b450a43117bd0cc963ea2e581db46bb6a17fbb9e`
Functional baseline commit: `25668149d8e89d39ce8ef2bd66a29fb63bf3d293`
Execution role: HERMUZ

## Verified trigger

Repair273 repair-head census artifact `9754096972`, digest `sha256:f6d40232ae5ee20b428e95b3fc5706ceca638c928afb03718510bbf68cffda1b`, proved expected=22 / observed=21 with history complete and sole incompleteness `__COHORT_COUNT_DRIFT__`. Full-Stack #2405 succeeded on that repair head.

## Verified mutation

Lease274 changed exactly one functional line in `Quality/Integration/ejr_memory_to_root_provenance_census.py`: expected cohort baseline 22→21. Exact compare from Lease274 open to functional commit showed one file, +1/-1.

## Verified normalized state

- Internal Document-ID Audit #65 / run `33382121341`: SUCCESS.
- Full-Stack #2408 / run `33382121314`: SUCCESS.
- census artifact `9754166006`, digest `sha256:3b654b02d9d087c2e8b63ae22e34492014d5b3b42345d618384a2f4f95286c1c`;
- expected_group_count=21;
- observed_group_count=21;
- history_complete=true;
- classification_complete=true;
- decision=CENSUSED;
- incomplete_group_ids=[].

## Boundary

No classifier logic, membership derivation, tests/workflows, EJR, Memory, GOV/REP, consumers, or Global Integrity state changed in this baseline normalization.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
