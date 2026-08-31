# MUT-2026-08-31-P2-EJR-246-TO-423-IDENTITY-REPAIR-297

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Opening main: `97826ce6864ef667b47253d661b889bf924bcc66`
Pre-write Matrix297: `cae5fe0210d9c18928616416474a26f97f440269`
Repair open head: `1aadcd068850757b1e329420671fc7319e82c038`
Functional repair head: `6fa1970e31c7e9da3a682b239bf3dc434e53c48d`
Prerequisite: Lease296 CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

## Executed identity repair

- RETAINED unchanged: `Memory/Engineering_Journal/EJR-246_2026-08-15_P65_SESSION_CLOSURE.md`; blob remained `cae56a17e41cc3ea979d89a563158a29e7f80bdc` on the repair head.
- REMOVED displaced root path: `EJR/EJR-246_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md`.
- CREATED successor path: `EJR/EJR-423_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md`; blob `5abbebcfa13f50eeb512fa8328bdb8e06bdc284e`.
- Only the first H1 identity token changed from EJR-246 to EJR-423; remaining displaced-root body text was preserved, including historical narrative text.
- The move was committed atomically in one Git tree/commit; no intermediate duplicate state was introduced.

EJR-423 had been proven complete-history VACANT and reserved solely for this displaced root content by Lease296 workflow run `33409267610`, artifact `9764434172`, digest `sha256:f7ab8977442df306625d11897cfd79a7048ceb37af2a42efb7627729ed8ee202`.

## Repair-head verification

- Full-Stack run `33409682009`: SUCCESS.
- Internal Document-ID run `33409681899`: FAILURE solely at expected deterministic cohort-count drift.
- repair-head census artifact `9764623489`, digest `sha256:0cb26d2057746949514bbf6cd5e77e9842d08fe720af1f0470039baf3319933b`: expected=14, observed=13, history_complete=true, decision=PARTIAL, incomplete_group_ids=[`__COHORT_COUNT_DRIFT__`].

## Separate baseline normalization

Lease/Matrix298 normalized only `EXPECTED_GROUP_COUNT` from 14 to 13 at functional head `a943a179769968adb775e61293a3cecf99de861c`.

Final verification after Lease298:
- Full-Stack run `33410030347`: SUCCESS.
- Internal Document-ID run `33410030407`: SUCCESS.
- final census artifact `9764755806`, digest `sha256:3afc1559b1bfb2d712d3cdd4899b853ffa693b985ca10b1e9db6a1ea2d9093f0`: expected=13, observed=13, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Repair297 is closed without governance or integrity promotion.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
