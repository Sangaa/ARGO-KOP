# MUTATION MATRIX — MEMORY_TO_ROOT COHORT BASELINE 298

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-298
Opening repair head: `6fa1970e31c7e9da3a682b239bf3dc434e53c48d`
Execution role: HERMUZ
Functional normalization head: `a943a179769968adb775e61293a3cecf99de861c`

## Trigger and authorized scope

Repair297 resolved one MEMORY_TO_ROOT ambiguity; repair-head artifact `9764623489`, digest `sha256:0cb26d2057746949514bbf6cd5e77e9842d08fe720af1f0470039baf3319933b`, proved expected=14, observed=13, history_complete=true, with sole incomplete group `__COHORT_COUNT_DRIFT__`.

Lease298 authorized and executed exactly one functional line change:
`EXPECTED_GROUP_COUNT = 14` → `EXPECTED_GROUP_COUNT = 13` in `Quality/Integration/ejr_memory_to_root_provenance_census.py`.

Exact compare from `9a975096d78c99f9508482f5a322705629a4d3b0` to `a943a179769968adb775e61293a3cecf99de861c` shows one modified file, +1/-1.

## Final gate

- Full-Stack run `33410030347`: SUCCESS.
- Internal Document-ID run `33410030407`: SUCCESS.
- final census artifact `9764755806`, digest `sha256:3afc1559b1bfb2d712d3cdd4899b853ffa693b985ca10b1e9db6a1ea2d9093f0` proves expected=13, observed=13, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

No other functional mutation, identity rewrite, governance promotion, REP promotion, or Global Integrity change was executed under Lease298.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
