# R71-20260831-P2-EJR-403-REPLACEMENT-VACANCY-PROOF-219

Status: OPEN / PREWRITE AUTHORITY
Baseline: `main@b354617d58b063cf8c9cef27b327fc673eaba127`
Target future repair: `EJR/EJR-301_2026-08-24_GT-040_MULTILEVEL_EXPLICIT_ROOT_AGREEMENT.md`
Replacement candidate: `EJR-403`

## Target selection
Supplement218 + Plan204 establish EJR-301 as the lowest presently bounded unresolved repair: one later root record is displaced while the earlier Memory EJR-301 retains identity. Unlike EJR-302, EJR-301 has one known direct governed consumer (`Repository/REP-021_SESSION_DELTA_2026-08-24_GT-040.md`) and does not require two independent displaced-record decisions.

## Candidate discovery versus proof
Current code search and commit search return no EJR-403 claim. This is candidate discovery only and is NOT vacancy proof.

## Allowed execution
Add a dedicated workflow that executes existing `Quality/Integration/ejr_allocation_vacancy_gate.py` unchanged against EJR-403 with complete history (`fetch-depth: 0`), uploads deterministic evidence, and fails unless decision=VACANT.

No EJR identity allocation/rename/delete, no consumer rewrite, no analyzer change, no census baseline change, and no REP authority promotion are authorized in this lease.

## Exit
Close only if exact-head workflow evidence proves history_complete=true, current_claims=[], historical_claims=[], decision=VACANT. OCCUPIED or HISTORY_INCOMPLETE blocks allocation.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS claim.
