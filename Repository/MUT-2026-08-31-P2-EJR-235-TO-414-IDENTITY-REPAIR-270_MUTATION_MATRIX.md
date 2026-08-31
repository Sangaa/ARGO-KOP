# MUTATION MATRIX — EJR-235 → EJR-414 IDENTITY REPAIR 270

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-235-TO-414-IDENTITY-REPAIR-270
Opening main: `3e462e1bb03924b7112fc4c540a90ce54957a4f8`
Pre-write Matrix commit: `96e4e66648b8331eb03886e9807cd5277518cbc6`
Execution lease commit: `14d3918cd270db6dbcdbe24802d6de683fd6663c`
Functional repair commit: `ad7fd5642941a398f915dad5c299e009346c38a7`
Successor baseline commit: `81322fdd20d21dce9b991c374cc60d9102cda1c2`

## Functional mutation reconciliation

| Surface | Final state |
|---|---|
| Memory EJR-235 | unchanged / retained |
| Root old EJR-235 path | absent |
| Root successor | `EJR/EJR-414_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md` present |
| Root H1 | EJR-414 |
| Semantic body/date/chronology | preserved except H1 identity |
| Historical footer/body | preserved, including `End of EJR-235` |
| Executable consumer rewrites | zero |
| Cohort baseline inside Repair270 | remained 23 |
| Global Integrity | HOLD |

Exact compare from the execution-lease head to functional repair head showed exactly the EJR rename (+1/-1) and Matrix270 update.

## Verification and successor normalization

Repair-head Full-Stack #2390 / run `33380217985`: SUCCESS.
Repair-head Internal-ID #61 / run `33380217984` isolated only deterministic cohort drift, artifact `9753468588`, digest `sha256:f0897d8869170a12046b836abc5b0ce2c0325402522b41826d455c499e97e6dc`, expected=23 / observed=22 / sole `__COHORT_COUNT_DRIFT__`.

Lease271 normalized only the expected baseline 23→22.

Final Internal-ID #62 / run `33380575170`: SUCCESS.
Final Full-Stack #2392 / run `33380575158`: SUCCESS.
Final census artifact `9753598303`, digest `sha256:dbf33fba9269544b7f48cbddd32ad19084b68331a0b717b37855ca44cd27bee7`, expected=22 / observed=22 / history_complete=true / classification_complete=true / decision=CENSUSED / incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
