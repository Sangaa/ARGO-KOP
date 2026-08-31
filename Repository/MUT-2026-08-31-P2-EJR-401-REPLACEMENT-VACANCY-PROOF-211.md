# R71-20260831-P2-EJR-401-REPLACEMENT-VACANCY-PROOF-211

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Prewrite: `71b3137f2dc7f98617cca069fafbf81345911c1c`
Functional head: `6be367acac7d20fb309d60ac24c0feff21023400`
Target future repair: `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md`
Replacement candidate: `EJR-401`

## Target selection
Lease203/204 prove the later root EJR-211 record is a legitimate displaced identity while the earlier Memory allocation retains EJR-211. Lease204 requires one-record execution and recommends minimizing rewrite risk. Two current-main searches for the exact displaced path/name returned only historical Lease203/204 analysis records; no current operational synchronous consumer rewrite was established. Other remaining displaced groups carry explicit consumer obligations, so EJR-211 is the lowest presently established rewrite-risk target.

## Candidate discovery versus proof
Current-main code search and commit-history search found no EJR-401 claim. Those searches were treated only as candidate discovery and did not authorize allocation.

The dedicated complete-history workflow then ran the existing Lease193 vacancy gate unchanged.

## Execution evidence
At `6be367acac7d20fb309d60ac24c0feff21023400`:
- EJR Replacement Vacancy Proof 211 run `33354205430` — SUCCESS;
- artifact `ejr-401-vacancy-proof` / ID `9744595264`;
- digest `sha256:1fba5b9bd583db6df8a7e68334232b9a9f3c35c4bf0602f640f247fc102b02b7`;
- candidate=`EJR-401`;
- history_complete=`true`;
- history_scope=`all locally reachable refs`;
- current_claims=`[]`;
- historical_claims=`[]`;
- decision=`VACANT`.

Supporting exact-head workflows:
- Full-Stack Repository Audit `33354205358` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33354205377` — SUCCESS;
- M2 Multi-Channel Proposal Training `33354205365` — SUCCESS;
- Real Mutation Matrix Regression `33354205355` — SUCCESS.

## Closure decision
`EJR-401` is proven VACANT and is eligible for allocation only inside a separate governed one-record repair lease. This lease performs no allocation and no EJR mutation.

## Preserved boundaries
Priority 2 remains OPEN. Phase 1 remains OPEN. Repository-wide identity/content/relationship reconciliation remains OPEN. Connected-Baseline/global graph validation remains OPEN. Global integrity remains HOLD. No BOOTED/INTEGRITY PASS is claimed.

## Next legal action
Open a separate repair-execution lease for exactly the displaced root EJR-211 record. Re-enumerate consumers, atomically move/re-identify it to EJR-401 with semantic preservation, allow Internal-ID to verify the post-repair state, and treat any correctly detected cohort drift as a separate verification-surface successor rather than weakening the guard.
