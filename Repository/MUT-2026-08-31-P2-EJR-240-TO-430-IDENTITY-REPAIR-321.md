# Repair 321 — Root EJR-240 → EJR-430 Identity Repair

Status: OPEN / AUTHORIZED BY LEASE319 + LEASE320
Date: 2026-08-31

## Authorization
Lease319 explicitly retains the earlier Memory EJR-240 allocation and classifies the later root EJR-240 record as displaced. Lease320 complete-history run `33422684323` proves EJR-430 VACANT.

## Bounded functional mutation
In one Git tree:
1. create `EJR/EJR-430_2026-08-17_GOV014_MATRIX_SEMANTIC_VALIDATION.md` from the current root EJR-240 content, changing the first H1 identity from EJR-240 to EJR-430 only;
2. remove `EJR/EJR-240_2026-08-17_GOV014_MATRIX_SEMANTIC_VALIDATION.md`;
3. update the live semantic provenance sentence in `EJR/EJR-416_2026-08-17_MATRIX_VARIANT_REPEAT_VALIDATION.md` from `EJR-240 established semantic validation...` to `EJR-430 established semantic validation...`;
4. preserve `Memory/Engineering_Journal/EJR-240_2026-08-15_P58_SESSION_CLOSURE.md` byte-for-byte.

Historical P2 census/baseline evidence remains untouched.

## Drift boundary
The repair must retain `EXPECTED_GROUP_COUNT = 7`. If the deterministic census observes 6 and fails only with `__COHORT_COUNT_DRIFT__`, preserve that failure as repair evidence and open a separate rebaseline lease. Any different failure blocks continuation.

Priority 2 remains OPEN.