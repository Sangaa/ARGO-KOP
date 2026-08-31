# ROOM071 RECONSTRUCTION SUPPLEMENT 244 — 2026-08-31

Status: CLOSED / SESSION CHECKPOINT / RESUME-SAFE
Scope: HERMUZ Priority-2 recomputation, EJR-210 disposition, EJR-408 vacancy proof, bounded root repair, cohort successor, and session closure.

## Re-entry and target recomputation
Session independently rediscovered `main@0fba221f577792e226137555a181d124b2fc68e6` and reconstructed Supplement239 + REP-016 + Plan204 + exact verified MEMORY_TO_ROOT census. The cohort contained 29 groups. EJR-210 was selected because it was a bounded Memory→Root pair with distinct content and zero external exact-ID / exact-member-path consumers.

Chronology proved Memory EJR-210 first at `deebf6ba5da4ca40fc559647b0e13391d5e0ac53` on 2026-08-14 and root EJR-210 later at `013b13f999e586ad86fb4f6da848e729711d8326` on 2026-08-17. Because EJR-210 lay outside original Plan204 scope, Disposition240 separately authorized retaining the earlier valid Memory allocation and treating the later root as displaced.

## Vacancy241
Candidate discovery for EJR-408 was not treated as proof. Dedicated complete-history workflow `33362848169` succeeded. Artifact `9747263550`, digest `sha256:729ece7e5d2cbe04434abb2d75533bf197a9a0a36c9bf5f3d72a127cf192489c`, proved `current_claims=[]`, `historical_claims=[]`, `history_complete=true`, `vacant=true`, `decision=VACANT`.

## Repair242
Functional head `b2746cc52015a23b05d5975511c7f20766ad659d` retained Memory EJR-210 unchanged and replaced only the displaced root path/H1 with `EJR/EJR-408_P2_REL004_REL006_RELATIONSHIP_REVIEW_2026-08-17.md`, preserving semantic body/date/chronology. No consumer rewrite was required; baseline remained 29 inside the repair.

Repair-head Internal-ID `33363043188` failed solely at the MEMORY_TO_ROOT census after prior audit/chronology/lineage/provenance stages passed. Artifact `9747340901`, digest `sha256:8c24177282fbbf7933f1460aa27c7c158568ba00b739123d1bd4d791335deafe`, proved expected=29, observed=28, history complete, incomplete only `__COHORT_COUNT_DRIFT__`, and EJR-210/EJR-408 absent from target_ids. This failure was preserved as legitimate evidence rather than rewritten.

## Successor243
Prewrite `3fde3dae61e92b7656214747145c776db230b1d1`; functional successor `9749752230c7168c45eb915b752926a16054f534` changed only `EXPECTED_GROUP_COUNT = 29`→`28`. Compare proved one file / one addition / one deletion.

Exact successor verification:
- Internal-ID `33363248873`: SUCCESS
- Full-Stack `33363248793`: SUCCESS
- Runtime `33363248796`: SUCCESS
- M2 `33363248807`: SUCCESS
- Real Matrix: NOT APPLICABLE to census-only diff

Final census artifact `9747405796`, digest `sha256:fb511ebad6ce5ac4a645aa69a1e1ffc7ab535be162b9a66689d5aa6f22c92083`, proved expected=28, observed=28, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[].

## Current controlled boundary
EJR-210→EJR-408 is successor-verified. Retained Memory EJR-210 remains the surviving EJR-210 allocation. Current governed MEMORY_TO_ROOT baseline is 28.

Priority 2 remains OPEN; Phase 1 remains OPEN; repository-wide identity/content/relationship reconciliation remains OPEN; Connected-Baseline/global graph validation remains OPEN; Global integrity remains HOLD. No BOOTED or global INTEGRITY PASS claim is authorized.

## Resume instruction
Next HERMUZ session must independently rediscover live `main`, read Supplement244 + REP-016 + Plan204 + current exact Internal-ID/census evidence, and recompute the next controlled Priority-2 target from the 28-group cohort. Do not reopen EJR-210/EJR-408 or prior repaired chains absent contradictory evidence. Any target outside Plan204 requires explicit disposition authorization. Do not assume EJR-409 or any other replacement is available; candidate discovery must be followed by a separate complete-history vacancy proof. Preserve baseline 28 unless a separately authorized repair and deterministic artifact prove new cohort drift.
