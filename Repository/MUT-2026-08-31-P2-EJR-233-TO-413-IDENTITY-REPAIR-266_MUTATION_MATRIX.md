# MUTATION MATRIX — EJR-233 → EJR-413 IDENTITY REPAIR 266

Status: FUNCTIONAL MUTATION APPLIED / VERIFICATION PENDING
Transaction ID: MUT-2026-08-31-P2-EJR-233-TO-413-IDENTITY-REPAIR-266
Opening main: `c35d939f56dcc173f976f247d51fbb60816de1ea`
Pre-write Matrix commit: `1c8acaa26282f9901cb54863b0c539ed1bc2b542`
Execution lease commit: `af8a6027cdf5d6227f6dd8c703b160ccfcd6dcb7`
Source disposition: `MUT-2026-08-31-P2-EJR-233-DISPOSITION-AUTHORIZATION-264.md`
Vacancy authority: `MUT-2026-08-31-P2-EJR-413-REPLACEMENT-VACANCY-PROOF-265.md`

## Pre-write evidence retained

- Lease264 retained the earlier Memory EJR-233 and classified the later root EJR-233 allocation displaced.
- Lease265 proved EJR-413 VACANT across complete reachable history and reserved it for exactly one bounded replacement allocation.
- Immediately before mutation, main remained `af8a6027cdf5d6227f6dd8c703b160ccfcd6dcb7`; the source re-read at blob `f78a69c14793fb8331fe0096e656bfd1957a94a7`, and the exact successor path returned 404.
- Fresh consumer recheck established no direct executable/operational consumer requiring rewrite. Historical Lease264/265 references remain unchanged as provenance evidence.

## Functional mutation reconciliation

| Surface | Before | Applied Lease266 state |
|---|---|---|
| Memory EJR-233 | earlier retained allocation | unchanged / retained |
| Root old path | `EJR/EJR-233_2026-08-17_GOV-015_FIRST_EXECUTION_APPLICATION.md` | removed in atomic repair tree |
| Root successor path | absent / vacancy-proven | created as `EJR/EJR-413_2026-08-17_GOV-015_FIRST_EXECUTION_APPLICATION.md` |
| Root H1 | `# EJR-233 — ...` | changed to `# EJR-413 — ...` |
| Root semantic body/date/chronology | source blob `f78a69c14793fb8331fe0096e656bfd1957a94a7` | preserved byte-for-byte except H1 identity |
| Historical footer | `End of EJR-233` | preserved |
| Historical disposition/path references | provenance evidence | unchanged |
| Direct executable consumers | zero established | zero rewrites |
| MEMORY_TO_ROOT expected baseline | 24 | unchanged at 24 inside Repair266 |
| Classifier/audit logic | current | unchanged |
| Global integrity | HOLD | HOLD |

## Expected repair-head validation behavior

The repair resolves one MEMORY_TO_ROOT ambiguity while Repair266 intentionally preserves baseline 24. Therefore the exact repair-head census may report deterministic drift `expected=24 / observed=23`. This is acceptable only if identity/chronology/provenance stages are otherwise clean and the sole incompleteness is `__COHORT_COUNT_DRIFT__`. Baseline correction belongs to a separate successor lease.

## Verification pending

Functional completion now requires:
1. exact post-write read-back of old path absence, successor path/H1/body, and retained Memory EJR-233;
2. exact commit diff confirmation;
3. post-mutation CI and audit evidence;
4. classification of any expected cohort-count drift before opening a separate baseline-sync successor lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.