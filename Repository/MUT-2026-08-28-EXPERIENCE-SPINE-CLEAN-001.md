# Experience Spine Clean Extraction — Mutation Matrix

Transaction ID: `MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@51374901bc03503f3e5d90192e0e0c2adc02d01e`
Working branch: `hermuz/experience-spine-clean-20260828`
Status: `ALL PLANNED ROWS APPLIED / SOURCE-READBACK VERIFIED / EXACT-HEAD CI PENDING`

## Purpose

Extract the smallest useful Experience Spine capability from historical PR #66 and HORUS analysis PR #69 without rebasing or merging either workstream wholesale.

The capability is a governed semantic projection over already-promoted knowledge, not a second memory store, second promotion system, or new authority layer.

## Evidence Reassessment

Current-main retrieval is intentionally simple and primarily token-overlap based:

- `Knowledge/Learning/knowledge_retrieval.py`;
- `Knowledge/Learning/contextual_retrieval.py`.

Current knowledge promotion establishes `status=PROMOTED`, requires `validation=VALIDATED`, and preserves evidence/provenance. Experience Spine therefore preserves lifecycle, validation, evidence, authority, scope, and source as separate axes.

PR #66 is a useful tested prototype but diverged from current main by the time of extraction. PR #69 is analytical/non-authoritative guidance. Neither is a direct merge source.

## Core Design Invariants

1. `EXPERIENCE SPINE = SEMANTIC PROJECTION OVER PROMOTED KNOWLEDGE`.
2. `REUSE != PROMOTION != AUTHORITY`.
3. Lifecycle, validation, evidence, authority, scope, and source attribution remain separate axes.
4. Missing structural context narrows/holds retrieval; it never broadens it.
5. Structural exact keys are used; free-text similarity alone is not governed relevance.
6. Contradictions are exposed and require review; they are never silently resolved.
7. Multiple records sharing one evidence lineage are reported as correlated and not independent confirmation.
8. Superseded projections are excluded without deleting their historical knowledge records.
9. Packet size is bounded.
10. Current evidence and applicable authority outrank retrieved experience.
11. Retrieval mechanics do not prove cognitive benefit; IGT remains the later validation method.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Knowledge/Learning/experience_spine.py` | bounded semantic projection over promoted+validated records; conflict/correlation/supersession controls | Y | Y |
| C02 | `Knowledge/Learning/test_experience_spine.py` | mechanics regressions for context, axes, legacy compatibility, scope/route, ranking, bounds, collision, conflict, correlation, supersession, multi-writer attribution | Y | Y |
| C03 | `Quality/Integration/test_experience_spine_integration.py` | CI-visible execution/source/authority, correlation, and contradiction boundary tests | Y | Y |
| C04 | `Knowledge/Learning/KNOWLEDGE_RECORD_SCHEMA.md` | optional nested `experience_profile`; promotion lifecycle unchanged | Y | Y |
| C05 | `Knowledge/Learning/TASK_CONTEXT_ENVELOPE.md` | bounded structural context + repository/multi-writer attribution | Y | Y |
| C06 | `Knowledge/Learning/KNOWLEDGE_REUSE_POLICY.md` | advisory projection, contradiction, supersession, correlation, provenance and cognitive-benefit boundaries | Y | Y |

## Read-Back Evidence

- C01 blob: `6215fceb2ec76039f6bee55c29613278fc5579bf`;
- C02 blob: `280b206be1df3901652b5e52561e70b51351dca4`;
- C03 blob: `e53859a8ada57b982a3176a1a6dc6f5c479dd61f`;
- C04 blob: `15de230bf70991adc81de672dcd90597844f4581`;
- C05 blob: `46db6dd3e12fbd6de0442982a5ae606676b9c769`;
- C06 blob: `c2bebe5050c335da4e4ea09c83f84d1361aab7fb`.

Branch comparison against exact base `51374901...` before this matrix reconciliation showed:

- `ahead_by = 7`;
- `behind_by = 0`;
- exactly seven changed paths: the six declared payload targets plus this Mutation Matrix;
- no Runtime, Engine, Services, Memory, Governance, or repository authority implementation mutation.

Unexpected changed paths observed: `0`.

## Clean-Extraction Differences from PR #66

The clean candidate intentionally rejects the prototype lifecycle set `{PROMOTED, REUSABLE, VERIFIED, CANONICAL}`. Only current governed lifecycle `PROMOTED` is eligible, and `validation=VALIDATED` is checked separately.

Retrieval-only metadata is nested under `experience_profile` rather than expanding every knowledge record with broad top-level fields.

The clean candidate adds `evidence_group`, `superseded_by`, and a `REVIEW_REQUIRED` conflict state.

Legacy promoted records without `experience_profile` remain valid for existing retrieval and are simply not guessed into the stricter Experience Spine packet.

Historical session-delta and mutation records from PR #66 are not copied.

## Explicit Non-Changes

- No new persistence layer.
- No Memory-domain mutation.
- No Engine/Governance authority mutation.
- No automatic enrichment of legacy records.
- No automatic promotion/demotion.
- No broad historical preload.
- No vector/semantic model dependency.
- No new controlled relationship vocabulary.
- No mutation/rebase/merge of PR #66 or PR #69.
- No cognitive-improvement claim.

## Verification Gates Still Open

1. Open draft PR from this clean branch.
2. Require exact-head Full-Stack + Runtime/Integration CI.
3. If CI exposes a missed semantic consumer, repair the consumer rather than weakening the new boundary.
4. Mechanics PASS authorizes only:
   `EXPERIENCE SPINE MECHANICS = EXECUTION-VERIFIED / ADVISORY / NON-AUTHORITATIVE / COGNITIVE BENEFIT UNPROVEN`.
5. Cognitive-effectiveness testing remains a separate IGT transaction with baseline comparison on materially novel cases.
6. Re-read main and active PR heads/changed paths immediately before merge.

## Closure Boundary

This transaction does not authorize a claim that models reason better merely because a packet can be built deterministically.

`RETRIEVAL VERIFIED != COGNITIVE IMPROVEMENT VERIFIED`.
