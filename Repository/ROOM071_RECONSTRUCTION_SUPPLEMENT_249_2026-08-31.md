# ROOM071 RECONSTRUCTION SUPPLEMENT 249 — 2026-08-31

Status: CLOSED / SESSION CHECKPOINT / RESUME-SAFE
Scope: HERMUZ Priority-2 recomputation, EJR-213 disposition, EJR-409 vacancy proof, bounded root repair, cohort successor, and session closure.

## Re-entry and target recomputation
Session independently rediscovered live `main@bef761eb9faeccbdb83b77f28e55aa9fcc0ffbf8`, read Checkpoint244 / REP-016 / Plan204, and recomputed the next target from the exact governed 28-group MEMORY_TO_ROOT cohort.

EJR-213 was selected because it was a bounded Memory→Root pair with semantically distinct bodies and zero external exact-ID / exact-member-path consumers. Chronology proved the Memory allocation first at `6f26f19c9c6189eb1ee32a6f2e6f3d93b04308bb` on 2026-08-14 and the root allocation later at `b8e24cd632b8438a203774ed9507c2308cc554c7` on 2026-08-17. Because EJR-213 lay outside original Plan204 scope, Disposition245 separately authorized retaining Memory EJR-213 and classifying the later root as displaced.

## Vacancy246
Candidate discovery for EJR-409 was not treated as proof. Dedicated complete-history workflow `33364154573` succeeded. Artifact `9747679876`, digest `sha256:4a5ff50291739f626c4466e9251555cb52fa82227977a39089f19a1e3c441d61`, proved `current_claims=[]`, `historical_claims=[]`, `history_complete=true`, `vacant=true`, and `decision=VACANT`.

## Repair247
Prewrite `2165534f7e41031df4a6e28ca06a6b8d2b477e8e`; functional head `0ba12b1b9d989b39c2fa67dcd74787c6ada209b2` retained Memory EJR-213 unchanged and replaced only the displaced root path/H1 with `EJR/EJR-409_P2_REL010_REL014_KNOWLEDGE_SOURCE_RELATIONSHIP_REVIEW_2026-08-17.md`, preserving semantic body/date/chronology. No consumer rewrite was required and baseline remained 28 inside the repair.

Repair-head Internal-ID `33364385235` failed solely at the MEMORY_TO_ROOT census after the preceding audit/chronology/lineage/provenance stages passed. Artifact `9747775478`, digest `sha256:d2e8aabcfef6ea933828eefb55b2a5e7054b25caf149778d8ed6c3e8b6229c75`, proved expected=28, observed=27, history complete, incomplete only `__COHORT_COUNT_DRIFT__`, and EJR-213/EJR-409 absent from target_ids. This failure was preserved as legitimate evidence.

## Successor248
Prewrite `ace4b03855ca0c5593d7feafeeade0dafe211042`; functional successor `128664d8b6998ff6184eda0f5ad518879d6e0016` changed only `EXPECTED_GROUP_COUNT = 28`→`27`. Compare proved one file / one addition / one deletion.

Exact successor verification:
- Internal-ID `33364577371`: SUCCESS
- Full-Stack `33364577312`: SUCCESS
- Runtime `33364577338`: SUCCESS
- M2 `33364577305`: SUCCESS
- Real Mutation Matrix: NOT APPLICABLE to census-only diff

Final census artifact `9747836287`, digest `sha256:2d904d30cbe4a97e8f186ee1a03ad2d1d5292b0f4ecca5a15f716e895efa3e58`, proved expected=27, observed=27, history_complete=true, history_scope=all locally reachable refs, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

## Current controlled boundary
EJR-213→EJR-409 is successor-verified. Retained Memory EJR-213 remains the surviving EJR-213 allocation. Current governed MEMORY_TO_ROOT baseline is 27.

Priority 2 remains OPEN; Phase 1 remains OPEN; repository-wide identity/content/relationship reconciliation remains OPEN; Connected-Baseline/global graph validation remains OPEN; Global integrity remains HOLD. No BOOTED or global INTEGRITY PASS claim is authorized.

## Resume instruction
Next HERMUZ session must independently rediscover live `main`, read Supplement249 + REP-016 + Plan204 + current exact Internal-ID/census evidence, and recompute the next controlled Priority-2 target from the 27-group cohort. Do not reopen EJR-213/EJR-409 or prior repaired chains absent contradictory evidence. Any target outside Plan204 requires explicit disposition authorization. Do not assume EJR-410 or any other replacement is available; candidate discovery must be followed by a separate complete-history vacancy proof. Preserve baseline 27 unless a separately authorized repair and deterministic artifact prove new cohort drift.
