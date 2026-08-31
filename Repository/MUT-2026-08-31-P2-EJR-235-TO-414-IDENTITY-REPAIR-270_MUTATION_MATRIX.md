# MUTATION MATRIX — EJR-235 → EJR-414 IDENTITY REPAIR 270

Status: FUNCTIONAL MUTATION APPLIED / VERIFICATION PENDING
Transaction ID: MUT-2026-08-31-P2-EJR-235-TO-414-IDENTITY-REPAIR-270
Opening main: `3e462e1bb03924b7112fc4c540a90ce54957a4f8`
Pre-write Matrix commit: `96e4e66648b8331eb03886e9807cd5277518cbc6`
Execution lease commit: `14d3918cd270db6dbcdbe24802d6de683fd6663c`
Source disposition: `MUT-2026-08-31-P2-EJR-235-DISPOSITION-AUTHORIZATION-268.md`
Vacancy authority: `MUT-2026-08-31-P2-EJR-414-REPLACEMENT-VACANCY-PROOF-269.md`

## Pre-write evidence retained

- Lease268 retained the earlier Memory EJR-235 and classified the later root EJR-235 allocation displaced.
- Lease269 proved EJR-414 VACANT across complete reachable history and reserved it for exactly one bounded replacement allocation.
- Matrix270 commit `96e4e66648b8331eb03886e9807cd5277518cbc6` passed Full-Stack Repository Audit #2388 / run `33379925915`.
- Lease270 commit `14d3918cd270db6dbcdbe24802d6de683fd6663c` passed Full-Stack Repository Audit #2389 / run `33379991270` and Runtime run `33379991339`.
- Immediately before mutation, main remained at the Lease270 head; source blob remained `a326b6195ecd66b26d8b379706c8965e78bde153`; retained Memory blob remained `28216a14168c44875273f7edd5747dfd54e92f3d`; and the exact EJR-414 successor path returned 404.
- Fresh consumer recheck surfaced Lease268 historical disposition evidence only. No direct executable/operational consumer requiring rewrite was established.

## Functional mutation reconciliation

| Surface | Before | Applied Lease270 state |
|---|---|---|
| Memory EJR-235 | earlier retained allocation | unchanged / retained |
| Root old path | `EJR/EJR-235_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md` | removed in atomic repair tree |
| Root successor path | absent / vacancy-proven | created as `EJR/EJR-414_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md` |
| Root H1 | `# EJR-235 — ...` | changed to `# EJR-414 — ...` |
| Root semantic body/date/chronology | source blob `a326b6195ecd66b26d8b379706c8965e78bde153` | preserved byte-for-byte except H1 identity |
| Historical footer/body | includes `End of EJR-235` | preserved |
| Historical disposition/path references | provenance evidence | unchanged |
| Direct executable consumers | zero established | zero rewrites |
| MEMORY_TO_ROOT expected baseline | 23 | unchanged at 23 inside Repair270 |
| Classifier/audit logic | current | unchanged |
| Global integrity | HOLD | HOLD |

## Expected repair-head validation behavior

The repair resolves one MEMORY_TO_ROOT ambiguity while Repair270 intentionally preserves baseline 23. Therefore the exact repair-head census may report deterministic drift `expected=23 / observed=22`. This is acceptable only if identity/chronology/provenance stages are otherwise clean and the sole incompleteness is `__COHORT_COUNT_DRIFT__`. Baseline correction belongs to a separate successor lease.

## Verification pending

Functional completion now requires:
1. exact post-write read-back of old path absence, successor path/H1/body, and retained Memory EJR-235;
2. exact commit diff confirmation;
3. post-mutation CI and Internal-ID evidence;
4. classification of any cohort-count drift before opening a separate baseline-sync successor lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.