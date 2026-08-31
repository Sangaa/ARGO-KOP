# Mutation Matrix — Lease 308 — EJR-174 Disposition / EJR-427 Vacancy Proof

Date: 2026-08-31
Status: OPEN

## Allowed changes
- this mutation matrix;
- Lease 308 evidence record;
- dedicated vacancy-proof workflow for EJR-427.

## Forbidden changes
- no rename/delete/rewrite of either EJR-174 member;
- no allocation of EJR-427 before complete-history vacancy proof;
- no REP/GOV/Architecture promotion;
- no cohort baseline normalization in this lease.

## Validation
1. Rediscover live main before each protected mutation.
2. Complete-history checkout (`fetch-depth: 0`).
3. Execute `ejr_allocation_vacancy_gate.py EJR-427`.
4. Inspect emitted artifact content; workflow success alone is insufficient.
5. Require Full-Stack Repository Audit success on the proof head.

## Promotion rule
A VACANT result authorizes only a separate repair lease. It does not itself mutate identity or Global Integrity.
