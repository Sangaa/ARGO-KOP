# R71-20260831-P2-EJR-404-REPLACEMENT-VACANCY-PROOF-223

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Baseline: `main@b1214dcf42c46d641a7d7e58b4727089eb1a121a`
Prewrite: `728e525a55d11d3a1929d3911c5fe3a41323828e`
Functional head: `5e2b658262af36b4119cca9ba7c99866107abd03`
Target future repair: `EJR/EJR-302_2026-08-24_GT-041_DEEP_ROOT_CONFLICT.md`
Replacement candidate: `EJR-404`

## Selection boundary
Supplement222 and Plan204 establish two displaced root records under reused EJR-302 while the earlier 2026-08-22 Memory allocation retains EJR-302. This vacancy lease selects only DISPLACE A (`GT-041`) because it has one explicit governed exact-path consumer, `Repository/REP-022_SESSION_DELTA_2026-08-24_GT-041.md`. DISPLACE B remains untouched because its provenance reaches GOV-013B and requires a separate decision/repair unit.

## Vacancy evidence
Code search and commit search found no EJR-404 claim but were treated only as candidate discovery.

Dedicated complete-history workflow `EJR Replacement Vacancy Proof 223` run `33358057935` completed SUCCESS at exact head `5e2b658262af36b4119cca9ba7c99866107abd03`.
Artifact `ejr-404-vacancy-proof` ID `9745762164`, digest `sha256:82c35b7cdd1b279609291604aff0dc5f10af2ef3c8b6de6902b95ea09ed0c897`, deterministically proved:
- candidate=`EJR-404`;
- current_claims=[];
- historical_claims=[];
- history_complete=true;
- history_scope=`all locally reachable refs`;
- occupied=false;
- vacant=true;
- decision=`VACANT`.

## Closure decision
EJR-404 is authorized as a replacement candidate for one separately governed repair transaction. No EJR rename, identity allocation, consumer rewrite, census rebaseline, analyzer weakening, or canonical promotion occurred inside Lease223.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS claim.
