# ROOM071 RECONSTRUCTION SUPPLEMENT 214 — 2026-08-31

Status: CLOSED / SESSION CHECKPOINT / RESUME-SAFE
Scope: HERMUZ Priority-2 continuation — EJR-401 vacancy proof, EJR-211 one-record identity repair, post-repair drift successor

## Re-entry truth
This session rediscovered live `main` independently at `f2c2c106dcb8fac38a8b8d41ec2d1523ea593214`, re-read Supplement210, REP-016, and the applicable EJR provenance/authority/repair-plan evidence before mutation. Priority 2 remained OPEN.

Lease203/204 showed the remaining displaced legitimate root records after the prior EJR-214 repair. EJR-211 was selected as the next bounded target because repeated current-main exact-path/name searches established no current operational synchronous consumer, while EJR-219/EJR-301/EJR-302 carry explicit consumer/provenance obligations.

## Construction completed
1. Opened Lease211 through atomic Lease+Matrix prewrite.
2. Proved candidate EJR-401 VACANT using the existing complete-history allocation-vacancy gate; no allocation was inferred from search absence.
3. Closed Lease211 execution-verified; vacancy artifact `9744595264` proved history_complete=true, current_claims=[], historical_claims=[], decision=VACANT.
4. Opened Lease212 through atomic prewrite for exactly one displaced record.
5. Re-identified root EJR-211 to EJR-401, preserving the record body/chronology and changing only first H1 identity; retained Memory EJR-211 unchanged.
6. Internal-ID triggered automatically and failed only because the correctly preserved memory→root drift guard observed cohort 35→34.
7. Inspected Lease212 artifacts before any correction: EJR-211/EJR-401 non-ambiguous; expected=35, observed=34, sole incomplete=__COHORT_COUNT_DRIFT__.
8. Opened bounded Lease213 atomically; changed only EXPECTED_GROUP_COUNT 35→34.
9. Verified Lease213 exact head with Internal-ID + Full-Stack + Runtime/Integration + M2 + Real Mutation Matrix all SUCCESS.
10. Inspected deterministic evidence: census 34/34 CENSUSED, classification_complete=true, incomplete=[]; EJR-211/EJR-401 remain non-ambiguous.
11. Closed Lease213 execution-verified and reconciled Lease212 as VERIFIED-THROUGH-SUCCESSOR without rewriting its historical failed exact-head run.

## Learning captured
- Search absence discovers a vacancy candidate; complete-history vacancy execution proves vacancy.
- Lowest rewrite-risk displaced record should be preferred when repair semantics are otherwise equivalent.
- A valid identity repair should be allowed to hit drift guards honestly; never normalize the expected count inside the repair transaction.
- If one authorized repair removes one classifier-selected ambiguity group, prove the new cohort first, then rebaseline in a separate successor.
- Successor verification can close a dependency gap while preserving the historical failed evidence that revealed it.

## Current Priority-2 identity boundary
Closed/repaired in this controlled sequence:
- displaced root EJR-214 → EJR-400;
- displaced root EJR-211 → EJR-401.

Still visibly unresolved in current Internal-ID evidence:
- EJR-219 — root + Memory ambiguity, with known consumer/provenance obligations;
- EJR-301 — root + Memory ambiguity, with known consumer obligation;
- EJR-302 — two root records + Memory ambiguity, requiring separate displaced-record decisions/repairs.

This list is a current checkpoint, not an exhaustive declaration that no other Priority-2 work exists.

## Current repository boundary
- Priority 1: CLOSED / bounded inspected scope.
- Priority 2 exhaustive duplicate-ID work: OPEN.
- Phase 1: OPEN.
- Repository-wide identity/content/relationship reconciliation: OPEN.
- Connected-Baseline/global graph validation: OPEN.
- Global integrity: HOLD.
- `BOOTED / INTEGRITY PASS`: NOT CLAIMED.

## Resume instruction
On next HERMUZ build session:
1. rediscover live main;
2. re-read this Supplement214, REP-016, Lease204 and current Internal-ID evidence;
3. compare current consumer/provenance rewrite risk across remaining EJR-219/EJR-301/EJR-302 displaced records;
4. select only one next displaced record;
5. candidate-discover a replacement ID, then prove vacancy through complete history in a separate lease before any allocation/repair;
6. preserve the current 34-group census baseline unless new contradictory evidence or another separately authorized repair proves a new cohort.

This session is CLOSED / RESUME-SAFE only as a work session. It does not close Priority 2, Phase 1, or global integrity.
