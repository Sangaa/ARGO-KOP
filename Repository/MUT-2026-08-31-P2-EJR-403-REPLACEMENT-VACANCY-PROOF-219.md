# R71-20260831-P2-EJR-403-REPLACEMENT-VACANCY-PROOF-219

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Baseline: `main@b354617d58b063cf8c9cef27b327fc673eaba127`
Functional head: `a52f3902690e28933de7f61977da6298921b55b6`
Target future repair: `EJR/EJR-301_2026-08-24_GT-040_MULTILEVEL_EXPLICIT_ROOT_AGREEMENT.md`
Replacement candidate: `EJR-403`

## Target selection
Supplement218 + Plan204 establish EJR-301 as the lowest presently bounded unresolved repair: one later root record is displaced while the earlier Memory EJR-301 retains identity. Unlike EJR-302, EJR-301 has one known direct governed consumer (`Repository/REP-021_SESSION_DELTA_2026-08-24_GT-040.md`) and does not require two independent displaced-record decisions.

## Candidate discovery versus proof
Current code search and commit search returned no EJR-403 claim. This was candidate discovery only.

## Execution evidence
Exact-head workflow `EJR Replacement Vacancy Proof 219` run `33356981274` — SUCCESS.
Artifact `ejr-403-vacancy-proof` / ID `9745435896`, digest `sha256:0b74ee5f1ecbe18e3bdddc269b93529e2a0928d9d3a03c28cb04c646eaae63e4`, proves:
- candidate=`EJR-403`;
- history_complete=`true`;
- history_scope=`all locally reachable refs`;
- current_claims=`[]`;
- historical_claims=`[]`;
- decision=`VACANT`.

## Closure decision
`EJR-403` is proven VACANT and may be allocated only inside a separate governed repair lease. This lease performs no EJR identity mutation or consumer rewrite.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS claim.
