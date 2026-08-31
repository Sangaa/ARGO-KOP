# ROOM071 RECONSTRUCTION SUPPLEMENT 222 — 2026-08-31

Status: CLOSED / SESSION CHECKPOINT / RESUME-SAFE
Scope: HERMUZ Priority-2 EJR-301→EJR-403 controlled identity repair, direct REP-021 consumer synchronization, and post-repair cohort rebaseline

## Re-entry and selection
Live `main` was independently rediscovered at `b354617d58b063cf8c9cef27b327fc673eaba127`. Supplement218, REP-016, Plan204, current EJR records, consumers, and current search evidence were re-read. EJR-301 was selected ahead of EJR-302 because it was the lower-risk bounded unresolved target: one displaced root record plus one known direct governed consumer, while EJR-302 contains two displaced root records plus Memory and broader provenance complexity.

## Construction completed
1. Candidate discovery found no EJR-403 claim by code search or commit search; absence was not treated as vacancy proof.
2. Lease219 executed an independent complete-history vacancy gate. Run `33356981274` / artifact `9745435896` proved EJR-403 VACANT with history_complete=true and no current/historical claims.
3. Lease220 atomically repaired one displaced record: root EJR-301 GT-040 → EJR-403, while retaining the earlier Memory EJR-301 allocation.
4. The directly bound consumer `Repository/REP-021_SESSION_DELTA_2026-08-24_GT-040.md` was rewritten in the same repair transaction to identify/link EJR-403.
5. Functional repair head `a78bf0dd8760b036656515c39378261a1c0a2a09` passed Full-Stack, Runtime, and M2. Internal-ID failed only at the deliberately preserved 33→32 cohort drift guard; artifacts proved neither EJR-301 nor EJR-403 remained ambiguous.
6. Lease221 separately rebaselined only `EXPECTED_GROUP_COUNT = 33` → `32` at `bab2d672773a633e404213d02f6ed9bf458d1c78`.
7. Exact-head Internal-ID `33357346467`, Full-Stack `33357346484`, Runtime `33357346422`, and M2 `33357346457` all succeeded. Census artifact `9745556033` proved 32/32, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[].
8. Lease220 is closed through successor verification; Lease221 is execution-verified and closed.

## Learning captured
- Direct governed consumers are part of the same bounded identity-repair transaction; leaving the consumer behind would create a semantic split.
- Search absence only discovers a candidate. Complete-history execution proves vacancy.
- A valid repair may reduce a classifier-selected ambiguity cohort; the guard must fail honestly before any separate rebaseline.
- Path-filtered workflow non-trigger means NOT APPLICABLE to that exact diff, not PASS or FAIL. Do not manufacture a trigger.
- One displaced record per repair lease remains the safe unit even when a reused ID has multiple displaced records.

## Current controlled Priority-2 boundary
Completed successor-verified displaced-root repairs now include:
- EJR-214 → EJR-400;
- EJR-211 → EJR-401;
- EJR-219 → EJR-402;
- EJR-301 → EJR-403 with direct REP-021 consumer synchronization.

Known next controlled item from current evidence:
- EJR-302 — retained Memory allocation plus two distinct displaced root records. Each displaced root record requires its own evidence/repair decision unless materially new evidence establishes a different bounded transaction.

This list is a checkpoint boundary, not proof that no other Priority-2 work exists.

## Repository boundary
- Priority 1: CLOSED / bounded inspected scope.
- Priority 2 exhaustive duplicate-ID work: OPEN.
- Phase 1: OPEN.
- Repository-wide identity/content/relationship reconciliation: OPEN.
- Connected-Baseline/global graph validation: OPEN.
- Global integrity: HOLD.
- `BOOTED / INTEGRITY PASS`: NOT CLAIMED.

## Resume instruction
Next HERMUZ session must independently rediscover live main, read this Supplement222 + REP-016 + Plan204 + current Internal-ID evidence, inspect both displaced root EJR-302 records and their consumers/provenance, select only one displaced record, candidate-discover a replacement ID, then prove vacancy through a separate complete-history lease before repair. Preserve memory→root census baseline 32 unless a separately authorized material repair proves another cohort change.
