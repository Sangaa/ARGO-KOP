# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-274

Status: OPEN / FUNCTIONAL NORMALIZATION PENDING
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair273.
Opening repair head: `24cb04ef430316c2fb9b9f6ab6af7eaf82bbe5df`
Pre-write Matrix274: `46c6fd440dd7d58bf49fec54b49aea72aeb1c853`

## Trigger evidence

Repair273 reduced the current MEMORY_TO_ROOT ambiguity cohort by one. Repair-head artifact `9754096972`, digest `sha256:f6d40232ae5ee20b428e95b3fc5706ceca638c928afb03718510bbf68cffda1b`, proves history_complete=true, expected=22, observed=21, decision=PARTIAL, with sole incompleteness `__COHORT_COUNT_DRIFT__`.

Full-Stack #2405 succeeded on the repair head. Matrix274 prewrite Full-Stack #2406 / run `33382045979` completed SUCCESS.

## Authorized normalization

Change only `EXPECTED_GROUP_COUNT = 22` to `EXPECTED_GROUP_COUNT = 21` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

No other functional or authority mutation is authorized.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
