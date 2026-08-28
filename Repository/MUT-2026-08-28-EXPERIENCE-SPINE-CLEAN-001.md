# Experience Spine Clean Extraction — Mutation Matrix

Transaction ID: `MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@51374901bc03503f3e5d90192e0e0c2adc02d01e`
Working branch: `hermuz/experience-spine-clean-20260828`
Status: `PRE-WRITE / CLEAN EXTRACTION`

## Purpose

Extract the smallest useful Experience Spine capability from historical PR #66 and HORUS analysis PR #69 without rebasing or merging either workstream wholesale.

The capability is a governed semantic projection over already-promoted knowledge, not a second memory store, second promotion system, or new authority layer.

## Evidence Reassessment

Current-main retrieval is intentionally simple and primarily token-overlap based:

- `Knowledge/Learning/knowledge_retrieval.py`;
- `Knowledge/Learning/contextual_retrieval.py`.

Current knowledge promotion establishes:

- `status = PROMOTED`;
- `validation = VALIDATED` before promotion;
- `knowledge_scope`;
- preserved evidence/provenance.

Therefore Experience Spine eligibility must preserve these axes rather than inventing additional lifecycle meanings such as `VERIFIED` or `CANONICAL` in the lifecycle field.

Historical PR #66 is a useful tested prototype but is diverged from current main. PR #69 is analytical/non-authoritative guidance. Neither is a direct merge base.

## Core Design Invariants

1. `EXPERIENCE SPINE = SEMANTIC PROJECTION OVER PROMOTED KNOWLEDGE`.
2. `REUSE != PROMOTION != AUTHORITY`.
3. Lifecycle, validation, evidence, authority, scope, and source attribution remain separate axes.
4. Missing structural context narrows/holds retrieval; it never broadens it.
5. Structural exact keys outrank free-text matching; the clean spine does not use free-text similarity as governed relevance.
6. Contradictions are exposed and require review; they are never silently resolved.
7. Multiple records sharing one evidence lineage are reported as correlated and are not represented as independent confirmation.
8. Packet size is bounded.
9. Current evidence and applicable authority outrank retrieved experience.
10. Cognitive benefit is not claimed by retrieval-mechanics tests; IGT remains the validation method for later transfer/cognition experiments.

## Planned Changes

| ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Knowledge/Learning/experience_spine.py` | ADD | deterministic bounded projection using only promoted+validated records with explicit `experience_profile` | N | N |
| C02 | `Knowledge/Learning/test_experience_spine.py` | ADD | focused mechanics tests: missing context, axis separation, scope/route, ranking, collision, contradiction, correlation, bounded packet | N | N |
| C03 | `Quality/Integration/test_experience_spine_integration.py` | ADD | CI-visible integration seam proving execution attribution and advisory authority boundary | N | N |
| C04 | `Knowledge/Learning/KNOWLEDGE_RECORD_SCHEMA.md` | UPDATE | define optional nested `experience_profile`; do not alter promotion lifecycle | N | N |
| C05 | `Knowledge/Learning/TASK_CONTEXT_ENVELOPE.md` | UPDATE | define bounded structural retrieval context and multi-writer attribution fields | N | N |
| C06 | `Knowledge/Learning/KNOWLEDGE_REUSE_POLICY.md` | UPDATE | state projection/reuse/conflict/correlation boundaries | N | N |

## Explicit Non-Changes

- No new persistence layer.
- No Memory-domain mutation.
- No Engine/Governance authority mutation.
- No automatic enrichment of legacy records.
- No automatic promotion/demotion.
- No loading of all EJR/history into every task.
- No vector/semantic model dependency.
- No new controlled relationship vocabulary.
- No merge/rebase/mutation of PR #66 or PR #69.
- No claim of cognitive improvement from retrieval tests.

## Clean-Extraction Differences from PR #66

The clean candidate intentionally does not copy PR #66 lifecycle eligibility `{PROMOTED, REUSABLE, VERIFIED, CANONICAL}`. Current knowledge promotion uses `PROMOTED`; validation and authority remain separate fields.

The clean candidate uses nested `experience_profile` metadata rather than broad top-level schema expansion.

The clean candidate adds an evidence-lineage correlation signal so multiple representations of one source do not look like independent support.

Contradiction is represented as a review-required packet state rather than silent resolution.

Historical session-delta/mutation documents from PR #66 are not copied into the payload.

## Verification Gates

1. Read back every changed target.
2. Compare branch to current main; unexpected paths must be zero.
3. Open a draft PR only after source/read-back reconciliation.
4. Require exact-head Full-Stack + Runtime/Integration CI.
5. Retrieval-mechanics PASS authorizes only a bounded capability claim.
6. Cognitive-effectiveness promotion remains blocked pending IGT-style baseline comparison on materially novel cases.
7. Re-read main and all active PR heads immediately before merge.

## Closure Boundary

Potential capability state after exact-head CI:

`EXPERIENCE SPINE MECHANICS = EXECUTION-VERIFIED / ADVISORY / NON-AUTHORITATIVE / COGNITIVE BENEFIT UNPROVEN`.

This transaction does not authorize a claim that models reason better merely because a packet can be built deterministically.
