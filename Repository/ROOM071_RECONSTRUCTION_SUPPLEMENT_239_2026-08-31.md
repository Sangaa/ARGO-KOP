# ROOM071 RECONSTRUCTION SUPPLEMENT 239 — 2026-08-31

Status: CLOSED / SESSION CHECKPOINT / RESUME-SAFE
Scope: HERMUZ Priority-2 recomputation, EJR-208 disposition, EJR-407 vacancy proof, bounded root repair, cohort successor, and session closure.

## Re-entry and target recomputation
The session independently rediscovered `main@69f8c2649143c3c25589f3e20b68f026b3f2ca7b` from Supplement234 and reconstructed the current Priority-2 boundary. The exact verified MEMORY_TO_ROOT census contained 30 groups. EJR-208 was selected as a bounded pair with distinct content and zero exact-ID / exact-member-path consumers.

Chronology proved:
- Memory `EJR-208_2026-08-14_P26_SESSION_CLOSURE.md` first appeared at `34b05a37c627956daea5ac5962363b8a17e12fc5` on 2026-08-14;
- root `EJR-208_P2_REL003_CONTROLLED_MUTATION_PREPARATION_2026-08-17.md` first appeared at `98947c873eed9bfe0f294b47b143d05c83612cf8` on 2026-08-17.

Because EJR-208 was outside Plan204's original bounded set, Lease235 explicitly authorized disposition for EJR-208 only: retain the earlier valid Memory allocation and classify the later root record displaced.

## Lease236 — EJR-407 complete-history vacancy
Discovery code/commit searches found no EJR-407 claim, but were not treated as proof. Dedicated workflow `33361829696` succeeded at `8723febea9f2569fcc4347290996a2c26a63f68e`. Artifact `9746936355`, digest `sha256:91a8065e6c99013a388ad16476b0ee9d3ac885cbb7cafc34c611d39ad75da5ad`, proved current_claims=[], historical_claims=[], history_complete=true, occupied=false, vacant=true, decision=VACANT.

## Lease237 — EJR-208 → EJR-407
Functional head `070d11f6e4f8b19815485dabbf384d144c87802d`:
- retained Memory EJR-208 unchanged;
- renamed only the displaced root to `EJR/EJR-407_P2_REL003_CONTROLLED_MUTATION_PREPARATION_2026-08-17.md`;
- preserved semantic body and chronology; changed only identity/H1/path;
- no consumer rewrite was required by deterministic zero-consumer evidence;
- baseline stayed 30 inside the repair.

Compare proved one renamed file only. M2 `33361956427` and Full-Stack `33361956462` succeeded. Internal-ID `33361956415` failed solely at the MEMORY_TO_ROOT census after prior audit/chronology/lineage/provenance stages passed. Runtime and Real Matrix did not trigger for the EJR-only diff and are NOT APPLICABLE, not PASS/FAIL.

Repair-head census artifact `9746992753`, digest `sha256:fd28f7ed37dd863da865a98744545c116c79cdfb8b6dd8869151b4b9b7a1f4f4`, proved legitimate expected=30/observed=29 cohort drift, history complete, incomplete only `__COHORT_COUNT_DRIFT__`, and EJR-208/EJR-407 absent from the remaining cohort.

## Lease238 — separate cohort successor
Prewrite `927a851309359b93603107e62f11e4bfa8741555`; functional head `c25874dddb57c0adcbddce51f2bbe40f6115f972` changed only `EXPECTED_GROUP_COUNT = 30`→`29`. Compare proved one file / one addition / one deletion.

Exact functional-head verification:
- Internal-ID `33362098103`: SUCCESS;
- Full-Stack `33362098152`: SUCCESS;
- Runtime `33362098072`: SUCCESS;
- M2 `33362098095`: SUCCESS;
- Real Matrix: NOT APPLICABLE to census-only diff.

Artifact `9747038968`, digest `sha256:6c0384953491f06e88d50f37bb39e14fe8dd3d1ae5e60ff640f47d85caa80005`, proved expected=29, observed=29, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[].

## Current controlled boundary
Successor-verified repairs now include prior Supplement234 chains plus `EJR-208 → EJR-407`. Retained Memory EJR-208 remains the surviving EJR-208 allocation. Current MEMORY_TO_ROOT baseline is 29.

Priority 2 remains OPEN; Phase 1 remains OPEN; repository-wide identity/content/relationship reconciliation remains OPEN; Connected-Baseline/global graph validation remains OPEN; Global integrity remains HOLD. No BOOTED or global INTEGRITY PASS claim is authorized.

## Resume instruction
Next HERMUZ session must independently rediscover live `main`, read Supplement239 + REP-016 + Plan204 + current Internal-ID/census evidence, and recompute the next controlled Priority-2 target from the current 29-group cohort. Do not reopen EJR-208/EJR-407 or earlier repaired chains absent contradictory evidence. Any group outside Plan204 requires explicit disposition authorization. Do not assume EJR-408 or any other replacement is available; perform candidate discovery then a separate complete-history vacancy proof. Preserve baseline 29 unless a separately authorized repair and deterministic artifact prove new cohort drift.
