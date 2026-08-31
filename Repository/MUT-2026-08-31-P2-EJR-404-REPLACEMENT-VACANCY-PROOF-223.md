# R71-20260831-P2-EJR-404-REPLACEMENT-VACANCY-PROOF-223

Status: OPEN / PREWRITE / VACANCY PROOF ONLY
Baseline: `main@b1214dcf42c46d641a7d7e58b4727089eb1a121a`
Target future repair: `EJR/EJR-302_2026-08-24_GT-041_DEEP_ROOT_CONFLICT.md`
Replacement candidate: `EJR-404`

## Target selection
Supplement222 and Plan204 establish two later root records under reused EJR-302 while the 2026-08-22 Memory allocation retains EJR-302. This lease selects only DISPLACE A (`GT-041`) because it has one explicit governed exact-path consumer, `Repository/REP-022_SESSION_DELTA_2026-08-24_GT-041.md`. DISPLACE B remains untouched because its semantic provenance reaches GOV-013B and requires its own separate decision/repair unit.

## Candidate discovery versus proof
Current code search and commit search returned no EJR-404 claim. This is candidate discovery only and does not establish vacancy.

## Authorized execution
Run the existing `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-404` on a complete-history checkout through a dedicated exact-head workflow. Allocation is blocked unless the deterministic result proves `history_complete=true`, no current/historical claims, and `decision=VACANT`.

## Prohibitions
This lease performs no EJR rename, identity allocation, consumer rewrite, census rebaseline, analyzer weakening, or canonical promotion.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS claim.
