# ROOM071 RECONSTRUCTION SUPPLEMENT 259 — 2026-08-31

Status: CLOSED / SESSION CHECKPOINT / RESUME-SAFE
Scope: HERMUZ Priority-2 re-entry, EJR-217 disposition, EJR-411 vacancy proof, bounded root repair, cohort successor, and session closure.

## Re-entry
The session independently rediscovered live `main` at Checkpoint254 (`5a49351e474544d249687f997b9a5bbe724bfd77`) and reconstructed the current deterministic MEMORY_TO_ROOT baseline of 26 from repository evidence before selecting a new target.

## Target recomputation — EJR-217
EJR-217 was selected from the live 26-group cohort as a bounded two-member Memory→Root ambiguity with distinct semantic bodies, zero external exact-ID references, and zero exact-member-path consumers.

Direct reads and Git path history proved:
- Memory `Memory/Engineering_Journal/EJR-217_2026-08-14_P34_SESSION_CLOSURE.md` first allocated at `515549daf2580494b7a75f23c30d5752f2731796` on 2026-08-14;
- root `EJR/EJR-217_CURRENT_BUILD_RECONCILIATION_POST_P3_2026-08-17.md` first allocated at `f7716b1446cf5c7ee3fb2ba39a27754e8d6d0986` on 2026-08-17.

Because EJR-217 is outside Plan204's original five collision groups, Lease255 explicitly authorized disposition: retain the earlier valid Memory allocation and classify the later root record displaced. Search-index absence was treated only as secondary evidence, not absence authority.

## Lease256 — EJR-411 complete-history vacancy proof
Candidate discovery found no allocation evidence beyond the prior checkpoint warning not to assume vacancy. Dedicated workflow `EJR Replacement Vacancy Proof 256`, run `33368058506`, succeeded at prewrite head `a120a03ea0015190e7584c565344049940261396`.

Artifact `9748981322`, digest `sha256:9685d00ce7a4312b1a3c9d068ea467c48b0405da35ab03789327d289bf0dedcd`, proved current_claims=[], historical_claims=[], history_complete=true, history_scope=`all locally reachable refs`, occupied=false, vacant=true, decision=VACANT. Lease256 closed separately at `daf08b3d6c51a9d740081d8d755a26f86a743189` before allocation.

## Lease257 — EJR-217 → EJR-411
Prewrite `f177d6fa7e078f496937e8459499d8b516d39cbc`; functional head `bd0b833ed006118352dc1139f83de0a4e63a4194`.

The bounded mutation retained Memory EJR-217 unchanged, removed the displaced root EJR-217 path, and created `EJR/EJR-411_CURRENT_BUILD_RECONCILIATION_POST_P3_2026-08-17.md`, preserving semantic body/date/chronology and changing only record path/H1 identity. No consumer rewrite was required. Baseline stayed 26 inside the repair lease.

Compare prewrite→repair proved only the root rename/H1 identity change and Repair257 Mutation Matrix state update.

Repair-head verification preserved the expected classifier drift. Real Mutation Matrix `33368357951` succeeded; Internal-ID `33368357858` passed audit/chronology/lineage/provenance stages and failed only at MEMORY_TO_ROOT census.

Repair-head artifact `9749113045`, digest `sha256:354c7181f8b881e302828a3d7a311f7e06c9295ed4a14e2b58b78b19538d9558`, proved expected=26, observed=25, history_complete=true, decision=PARTIAL, incomplete only `__COHORT_COUNT_DRIFT__`, with EJR-217/EJR-411 absent from target_ids. This failure was preserved as legitimate repair evidence.

## Lease258 — separate cohort successor
Prewrite `e9f2f6eaacb92916b0e94ab23a8f8ded5847b375`; functional successor `e6111ec33574601d3e979451dedcb3e44d4a0c65` changed only `EXPECTED_GROUP_COUNT = 26`→`25`. Compare proved one modified file with one addition and one deletion.

Exact successor verification:
- Internal-ID `33368587229`: SUCCESS
- Full-Stack `33368587218`: SUCCESS
- Runtime `33368587225`: SUCCESS
- M2 `33368587254`: SUCCESS
- Real Mutation Matrix: NOT APPLICABLE to census-only diff.

Final census artifact `9749193758`, digest `sha256:6d3886048bed192173aab7f8a6edacf565af83501691e8305caca6026c303c5f`, proved expected=25, observed=25, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[], with EJR-217/EJR-411 absent from target_ids.

## Current controlled boundary
EJR-217→EJR-411 is successor-verified. Retained Memory EJR-217 is the surviving EJR-217 allocation. Current deterministic MEMORY_TO_ROOT baseline is 25.

Priority 2 remains OPEN; Phase 1 remains OPEN; repository-wide identity/content/relationship reconciliation remains OPEN; Connected-Baseline/global graph validation remains OPEN; Global Integrity remains HOLD. No BOOTED or global INTEGRITY PASS claim is authorized.

## Resume instruction
Next HERMUZ session must independently rediscover live `main`, read Supplement259 + REP-016 + Plan204 + current Internal-ID/census evidence, and recompute the next controlled Priority-2 target from the current 25-group cohort. Do not reopen EJR-217/EJR-411 or earlier repaired chains absent contradictory evidence. Any group outside Plan204 requires explicit disposition authorization. Do not assume EJR-412 or any other replacement identity is vacant; perform candidate discovery then a separate complete-history vacancy proof. Preserve baseline 25 unless a separately authorized repair and deterministic artifact prove new cohort drift.
