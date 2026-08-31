# MUT — EJR-174 → EJR-427 Identity Repair — Repair 309

Date: 2026-08-31
Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Priority: P2 Internal Document-ID Audit

## Executed repair
At functional head `96c0794a2b7f40a0e8eaee6fa5144f1b9e43f4d2`:
- removed root `EJR/EJR-174_2026-08-14_MATRIX_UPDATE_NOTE.md`;
- created root `EJR/EJR-427_2026-08-14_MATRIX_UPDATE_NOTE.md` with substantive content preserved and successor H1;
- Memory `EJR-174` remained unchanged.

## Validation
- old root path absent;
- successor root present;
- Memory EJR-174 blob remained `09fdaf5e35174f1cf017ed0324b2adc75647d3c1`;
- Full-Stack run `33417186770`: SUCCESS;
- Internal-ID census artifact `9767484535` showed only deterministic cohort drift `expected=10 / observed=9`, with incomplete IDs only `__COHORT_COUNT_DRIFT__`.

That scalar drift was handed to separate Lease 310. No global promotion.
