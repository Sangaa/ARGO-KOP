# ROOM071 RECONSTRUCTION SUPPLEMENT 254 — 2026-08-31

Status: CLOSED / SESSION CHECKPOINT / RESUME-SAFE
Scope: HERMUZ Priority-2 re-entry, EJR-215 disposition, EJR-410 vacancy proof, bounded root repair, cohort successor, and session closure.

## Re-entry
The session independently rediscovered live `main` and found that a parallel HERMUZ chain had already advanced from Checkpoint239 through EJR-213→EJR-409 and closed as Checkpoint249. That work was reconstructed and not replayed. Checkpoint249 established a complete MEMORY_TO_ROOT cohort baseline of 27.

## Target recomputation — EJR-215
From the live 27-group census, EJR-215 was selected as a bounded zero-consumer pair with distinct semantic content.

Direct reads and Git path history proved:
- Memory `Memory/Engineering_Journal/EJR-215_2026-08-14_P32_SESSION_CLOSURE.md` first allocated at `fa54af3cbe141d24710ad8025931862e4df5ff75` on 2026-08-14;
- root `EJR/EJR-215_P2_INDEX_SCOPE_MUTATION_SCAFFOLD_2026-08-17.md` first allocated at `051dcbbba89c9fcbd4cdaa2205dfcdcaa4d534b2` on 2026-08-17.

Because EJR-215 is outside Plan204's original five collision groups, Lease250 explicitly authorized disposition: retain the earlier valid Memory allocation and classify the later root record displaced. No direct exact-ID or exact-member-path consumer obligation was established.

## Lease251 — EJR-410 complete-history vacancy proof
Candidate code/commit searches did not establish allocation but were treated only as discovery signals. Dedicated workflow `EJR Replacement Vacancy Proof 251`, run `33365364420`, succeeded at `729e52116771a1f90c302deb34274bb550bdaf44`.

Artifact `9748081220`, digest `sha256:d768a156daa894a30cfd2bf18f3f1a37e3cfdda97914383622e6933fd95800e5`, proved current_claims=[], historical_claims=[], history_complete=true, history_scope=`all locally reachable refs`, occupied=false, vacant=true, decision=VACANT. Lease251 was closed separately at `36b5f083696b54f5015b6dd68c3f7ba391420bc6` before any allocation.

## Lease252 — EJR-215 → EJR-410
Prewrite `8003c5bb7f1ea386bbb3e504774d2f480a9b6206`; functional head `2d17e029701e0a670cf45c08921bc9eb0e71a4df`.

The bounded mutation retained Memory EJR-215 unchanged, removed the displaced root EJR-215 path, created `EJR/EJR-410_P2_INDEX_SCOPE_MUTATION_SCAFFOLD_2026-08-17.md`, preserved semantic body/date/chronology and changed only record identity/H1/path. No consumer rewrite was required. Baseline stayed 27 inside the repair lease.

Repair-head exact CI:
- Full-Stack `33365725814`: SUCCESS
- Runtime `33365725833`: SUCCESS
- M2 `33365725831`: SUCCESS
- Real Mutation Matrix `33365725874`: SUCCESS
- Internal-ID `33365725799`: FAILURE solely at MEMORY_TO_ROOT census after prior audit/chronology/lineage/provenance stages passed.

Repair-head artifact `9748220566`, digest `sha256:719cde8a93ef85cc23be9d3482c22b1f0e4a1bca5e24330a4f13ca214fdb86ca`, proved expected=27, observed=26, history_complete=true, decision=PARTIAL, incomplete only `__COHORT_COUNT_DRIFT__`, with EJR-215/EJR-410 absent from target_ids. This failure was preserved as legitimate repair evidence.

## Lease253 — separate cohort successor
Prewrite `27b42d1a8009ecb6253a077cf93b38152d61db1e`; functional successor `210b805e1c35496679ecd0fa45b9654c196596f4` changed only `EXPECTED_GROUP_COUNT = 27`→`26`. Compare proved one file / one addition / one deletion.

Exact successor verification:
- Internal-ID `33365938857`: SUCCESS
- Full-Stack `33365938873`: SUCCESS
- Runtime `33365938869`: SUCCESS
- M2 `33365938854`: SUCCESS
- Real Mutation Matrix: NOT APPLICABLE to census-only diff.

Final census artifact `9748292997`, digest `sha256:565d4af481c37351895d22e56f1fb24cc102c7bc8356342d0eecc34857d983bd`, proved expected=26, observed=26, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[], and EJR-215/EJR-410 absent from target_ids.

## Current controlled boundary
Successor-verified repairs now include prior Checkpoint249 chains plus EJR-215→EJR-410. Retained Memory EJR-215 is the surviving EJR-215 allocation. Current MEMORY_TO_ROOT baseline is 26.

Priority 2 remains OPEN; Phase 1 remains OPEN; repository-wide identity/content/relationship reconciliation remains OPEN; Connected-Baseline/global graph validation remains OPEN; Global Integrity remains HOLD. No BOOTED or global INTEGRITY PASS claim is authorized.

## Resume instruction
Next HERMUZ session must independently rediscover live `main`, read Supplement254 + REP-016 + Plan204 + current Internal-ID/census evidence, and recompute the next controlled Priority-2 target from the current 26-group cohort. Do not reopen EJR-215/EJR-410 or earlier repaired chains absent contradictory evidence. Any group outside Plan204 requires explicit disposition authorization. Do not assume EJR-411 or any other replacement identity is vacant; perform candidate discovery then a separate complete-history vacancy proof. Preserve baseline 26 unless a separately authorized repair and deterministic artifact prove new cohort drift.
