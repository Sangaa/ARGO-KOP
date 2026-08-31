# Repair 325 — Root EJR-237 → EJR-431 Identity Repair

Status: OPEN / AUTHORIZED BY LEASE323 + LEASE324
Date: 2026-08-31

## Authorization
Lease323 explicitly retains the earlier Memory EJR-237 allocation and classifies the later root EJR-237 as displaced. Lease324 complete-history run `33426371329` proves EJR-431 VACANT.

## Bounded functional mutation
Execute in one Git tree:
1. create `EJR/EJR-431_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md` from the current root EJR-237 content, changing only the first H1 identity from EJR-237 to EJR-431;
2. remove `EJR/EJR-237_2026-08-17_P4_NEGATIVE_RUNTIME_EVIDENCE_TRANSFER.md`;
3. update only semantic evidence references in `EJR/EJR-418_2026-08-17_P322_RECONCILIATION_UPDATE.md` whose referent is the displaced root negative-runtime evidence;
4. update only the root-negative-runtime evidence heading/reference in `Repository/REP-020_RECONCILIATION_ADDENDUM_2026-08-17_P322.md`;
5. preserve `Memory/Engineering_Journal/EJR-237_2026-08-15_P55_SESSION_CLOSURE.md` byte-for-byte.

Historical P2 census/baseline evidence remains untouched.

## Drift boundary
Retain `EXPECTED_GROUP_COUNT = 6` during the repair. If the deterministic census observes 5 and fails only with `__COHORT_COUNT_DRIFT__`, preserve that failure as repair evidence and open a separate rebaseline lease. Any different failure blocks continuation.

Priority 2 remains OPEN.
