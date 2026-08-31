# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-277

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: deterministic MEMORY_TO_ROOT cohort baseline normalization after Repair276.
Opening repair head: `652a96b1b4dd123ae38c9f4c43a8dc71e9899eca`
Functional normalization head: `a51f45d49ac31b6b8701fbfe8ca1c9f7c5e1881c`

## Result

Only `EXPECTED_GROUP_COUNT = 21` → `EXPECTED_GROUP_COUNT = 20` changed functionally. Exact compare: one file, +1/-1.

Verification:
- Internal Document-ID Audit #67 / `33384391125`: SUCCESS.
- Full-Stack #2423 / `33384391234`: SUCCESS.
- final census artifact `9755000334`, digest `sha256:fc907835259c4fb4fadb1c318bdf24c7001ac07c1897a4d91b5f3c0428072cb2`.
- final census: expected=20, observed=20, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
Next safe entry: select the next target from the current 20-group cohort using fresh risk/consumer/chronology evidence, not numeric ordering.
