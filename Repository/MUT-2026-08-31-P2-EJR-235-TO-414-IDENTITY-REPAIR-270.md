# MUT-2026-08-31-P2-EJR-235-TO-414-IDENTITY-REPAIR-270

Status: OPEN / EXECUTION-PENDING
Scope: One-record Priority-2 identity repair: displaced root EJR-235 → EJR-414.
Opening main: `3e462e1bb03924b7112fc4c540a90ce54957a4f8`
Pre-write Matrix270: `96e4e66648b8331eb03886e9807cd5277518cbc6`

## Authority

- Lease268 retained the earlier Memory EJR-235 and classified the later root EJR-235 allocation displaced.
- Lease269 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE and proves EJR-414 VACANT across complete reachable history; artifact `9752355789` proves `current_claims=[]`, `historical_claims=[]`, `history_complete=true`, `occupied=false`, `vacant=true`, `decision=VACANT`.
- EJR-414 is reserved for exactly one bounded replacement allocation: this repair.

## Fresh source evidence

Current displaced source:
`EJR/EJR-235_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md`

Source blob at pre-write read:
`a326b6195ecd66b26d8b379706c8965e78bde153`

Retained Memory member:
`Memory/Engineering_Journal/EJR-235_2026-08-14_P53_SESSION_CLOSURE.md`
blob `28216a14168c44875273f7edd5747dfd54e92f3d`.

The source H1 is `# EJR-235 — GOV-015 Fixture/Test Field Validation`. Historical body/footer text ends with `End of EJR-235` and must remain preserved.

## Consumer obligations

Fresh search for the exact old member filename/path surfaced Lease268 historical disposition evidence only. These references remain unchanged because they describe the historical path/identity accurately.

No direct executable/operational consumer requiring rewrite has been established. Repair270 therefore performs zero consumer rewrites unless a fresh executable consumer appears before execution.

## Pre-write validation

Matrix270 commit `96e4e66648b8331eb03886e9807cd5277518cbc6` passed Full-Stack Repository Audit #2388 / run `33379925915` with every repository-audit step successful.

## Authorized atomic mutation

One functional tree mutation may:
1. retain `Memory/Engineering_Journal/EJR-235_2026-08-14_P53_SESSION_CLOSURE.md` unchanged;
2. remove `EJR/EJR-235_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md`;
3. create `EJR/EJR-414_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md`;
4. preserve root semantic body/date/chronology byte-for-byte except H1 identity `EJR-235` → `EJR-414`;
5. preserve historical footer/body text including `End of EJR-235`;
6. update Matrix270 in the same functional commit to `FUNCTIONAL MUTATION APPLIED / VERIFICATION PENDING`.

## Baseline boundary

`EXPECTED_GROUP_COUNT = 23` must remain unchanged inside Repair270. An exact repair-head result `expected=23 / observed=22` is acceptable only when the sole incompleteness is `__COHORT_COUNT_DRIFT__`; any correction belongs to a separate successor lease.

## Hard gate

Immediately before mutation, re-discover live main and re-read the source, retained Memory member, target absence, and consumer state. Abort if main is not this lease commit, if either source blob changed, if the EJR-414 target path exists, or if a new executable consumer is established.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.