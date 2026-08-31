# R71-20260831-P2-EJR-402-REPLACEMENT-VACANCY-PROOF-215

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Baseline: `main@2b9564a1438df809fe119d83c39d5d9e4b2a712d`
Functional head: `08e217dc49c745ae566897781fff5ddd9069fe2c`
Target future repair: `EJR/EJR-219_REP016_RESYNC_AND_P5_BOUNDARY_2026-08-17.md`
Replacement candidate: `EJR-402`

## Target selection
Supplement214 and Plans 203–204 required one remaining displaced record by lowest rewrite risk. Two current-main exact path/name searches for the root EJR-219 record returned only analytical Plans 203/204; no current operational synchronous consumer rewrite was established. EJR-301 and EJR-302 carry explicit consumer/provenance rewrite obligations. Therefore EJR-219 is the lowest presently established rewrite-risk target.

## Candidate discovery versus proof
Current code search found no EJR-402 claim. This was candidate discovery only.

The dedicated complete-history workflow executed the existing `Quality/Integration/ejr_allocation_vacancy_gate.py` unchanged against EJR-402.

## Execution evidence
At `08e217dc49c745ae566897781fff5ddd9069fe2c`:
- EJR Replacement Vacancy Proof 215 run `33355086518` — SUCCESS;
- artifact `ejr-402-vacancy-proof` / ID `9744861014`;
- digest `sha256:e74883bda15fa25306e4f592da427014ef56d4938c41c38ac909b23c53e92fcd`;
- candidate=`EJR-402`;
- history_complete=`true`;
- history_scope=`all locally reachable refs`;
- current_claims=`[]`;
- historical_claims=`[]`;
- decision=`VACANT`.

## Closure decision
`EJR-402` is proven VACANT and is eligible for allocation only inside a separate governed one-record repair lease. Lease215 performs no EJR allocation or identity mutation.

## Preserved boundaries
Census baseline remains 34. Priority 2 OPEN. Phase 1 OPEN. Global integrity HOLD. No BOOTED/INTEGRITY PASS claim.

## Next legal action
Open a separate repair lease for exactly `EJR/EJR-219_REP016_RESYNC_AND_P5_BOUNDARY_2026-08-17.md`; re-enumerate consumers, preserve semantic content, re-identify it to EJR-402, and let Internal-ID expose any legitimate post-repair cohort drift before any separate rebaseline successor.
