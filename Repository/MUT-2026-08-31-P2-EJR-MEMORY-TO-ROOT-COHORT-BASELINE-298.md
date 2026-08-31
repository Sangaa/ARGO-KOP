# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-298

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Opening repair head: `6fa1970e31c7e9da3a682b239bf3dc434e53c48d`
Pre-write Matrix298: `60b1487f8280c07dcfbea8a24938ac533a841fa9`
Lease open head: `9a975096d78c99f9508482f5a322705629a4d3b0`
Functional normalization head: `a943a179769968adb775e61293a3cecf99de861c`
Execution role: HERMUZ

## Trigger evidence

Repair297 removed EJR-246 from the deterministic MEMORY_TO_ROOT ambiguity cohort by retaining the earlier Memory allocation and atomically moving displaced root content to vacancy-proven EJR-423.

Repair-head evidence:
- Full-Stack run `33409682009`: SUCCESS.
- Internal Document-ID run `33409681899`: FAILURE solely at MEMORY_TO_ROOT census.
- census artifact `9764623489`, digest `sha256:0cb26d2057746949514bbf6cd5e77e9842d08fe720af1f0470039baf3319933b`.
- expected=14, observed=13, history_complete=true, decision=PARTIAL, sole incomplete group=`__COHORT_COUNT_DRIFT__`.

## Executed normalization

Exactly one functional line changed in `Quality/Integration/ejr_memory_to_root_provenance_census.py`:
`EXPECTED_GROUP_COUNT = 14` → `EXPECTED_GROUP_COUNT = 13`.

Exact compare from Lease298 open head `9a975096d78c99f9508482f5a322705629a4d3b0` to functional normalization head `a943a179769968adb775e61293a3cecf99de861c` shows one modified file, one addition and one deletion.

## Final verification

- Full-Stack run `33410030347`: SUCCESS.
- Internal Document-ID run `33410030407`: SUCCESS.
- final census artifact `9764755806`, digest `sha256:3afc1559b1bfb2d712d3cdd4899b853ffa693b985ca10b1e9db6a1ea2d9093f0`.
- expected=13, observed=13, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

No other functional or identity mutation was executed under Lease298.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
