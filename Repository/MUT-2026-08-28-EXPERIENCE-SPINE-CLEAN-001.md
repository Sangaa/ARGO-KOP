# Experience Spine Clean Extraction — Mutation Matrix

Transaction ID: `MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@51374901bc03503f3e5d90192e0e0c2adc02d01e`
Working branch: `hermuz/experience-spine-clean-20260828`
Status: `SOURCE/READ-BACK VERIFIED / FOCUSED-SUITE CI BINDING ADDED / FINAL EXACT-HEAD CI PENDING`

## Purpose

Extract the smallest useful Experience Spine capability from historical PR #66 and HORUS analysis PR #69 without rebasing or merging either workstream wholesale.

The capability is a governed semantic projection over already-promoted knowledge, not a second memory store, second promotion system, or new authority layer.

## Evidence Reassessment

Current-main retrieval is intentionally simple and primarily token-overlap based through `knowledge_retrieval.py` and `contextual_retrieval.py`.

Current knowledge promotion establishes `status=PROMOTED`, requires `validation=VALIDATED`, and preserves evidence/provenance. Experience Spine therefore preserves lifecycle, validation, evidence, authority, scope, and source as separate axes.

PR #66 is a useful tested prototype but diverged from current main by extraction time. PR #69 is analytical/non-authoritative guidance. Neither is a direct merge source.

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
12. A committed test file is not execution evidence; the focused mechanics suite must be bound to CI and observed executing.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Knowledge/Learning/experience_spine.py` | bounded semantic projection over promoted+validated records; conflict/correlation/supersession controls | Y | Y |
| C02 | `Knowledge/Learning/test_experience_spine.py` | 11 focused mechanics regressions; import made location-independent | Y | Y source/read-back |
| C03 | `Quality/Integration/test_experience_spine_integration.py` | CI-visible execution/source/authority, correlation, contradiction boundary tests | Y | Y source/read-back |
| C04 | `Knowledge/Learning/KNOWLEDGE_RECORD_SCHEMA.md` | optional nested `experience_profile`; promotion lifecycle unchanged | Y | Y |
| C05 | `Knowledge/Learning/TASK_CONTEXT_ENVELOPE.md` | bounded structural context + repository/multi-writer attribution | Y | Y |
| C06 | `Knowledge/Learning/KNOWLEDGE_REUSE_POLICY.md` | advisory projection, contradiction, supersession, correlation, provenance and cognitive-benefit boundaries | Y | Y |
| C07 | `Quality/Integration/test_experience_spine_integration.py` | invoke focused C02 suite in CI and require `11 passed` before integration gate can pass | Y | CI PENDING |

## Read-Back Evidence

- C01 blob: `6215fceb2ec76039f6bee55c29613278fc5579bf`;
- C02 current blob: `5045f10cd6a6122be6b42f1db8270dfa2cce4ed1`;
- C03/C07 current blob: `bdc3fdac7599f871eefa3d740d6a511b27046ce3`;
- C04 blob: `15de230bf70991adc81de672dcd90597844f4581`;
- C05 blob: `46db6dd3e12fbd6de0442982a5ae606676b9c769`;
- C06 blob: `c2bebe5050c335da4e4ea09c83f84d1361aab7fb`.

Branch comparison against exact base before C07 showed only the six declared payload targets plus this Mutation Matrix. No Runtime, Engine, Services, Memory, Governance, or repository-authority implementation mutation was introduced.

Unexpected changed paths observed: `0`.

## CI Observation and Learning

First exact-head CI on `db2f1e3950a6712e80756b43e11d5c3b9ae455e7`:

- Full-Stack Repository Audit `33200699127` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33200699104` — SUCCESS;
- integration job reported `298 passed, 1 warning, 11 subtests passed`.

Log inspection proved only the three Experience Spine tests located under `Quality/Integration` were included in that 298-test run. The 11 focused mechanics tests under `Knowledge/Learning/test_experience_spine.py` were present in source but not executed by the workflow.

Therefore `db2f1e...` proves repository compatibility and integration-smoke behavior, but it does **not** prove full focused mechanics execution.

C07 closes that evidence gap by making the CI-visible integration suite invoke the focused file as a separate pytest process and require the observable summary `11 passed`.

Reusable learning:

`TEST FILE EXISTS != TEST EXECUTED`.

`BROAD SUITE PASS != UNDISCOVERED FOCUSED SUITE PASS`.

Execution attribution must be established from workflow/job/log evidence, not inferred from repository presence.

## Clean-Extraction Differences from PR #66

The clean candidate rejects the prototype lifecycle set `{PROMOTED, REUSABLE, VERIFIED, CANONICAL}`. Only current governed lifecycle `PROMOTED` is eligible, and `validation=VALIDATED` is checked separately.

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

1. Exact-head Full-Stack + Runtime/Integration CI on the C07-inclusive head.
2. Inspect integration job log for actual nested `11 passed` evidence.
3. If PASS, record mechanics as `EXECUTION-VERIFIED / ADVISORY / NON-AUTHORITATIVE / COGNITIVE BENEFIT UNPROVEN`.
4. Freeze branch; perform fresh main/active-workstream reconciliation.
5. Squash merge only with expected frozen head SHA.
6. Require post-merge exact-main CI before advancing.
7. Cognitive-effectiveness testing remains a separate IGT transaction with materially novel cases and baseline comparison.

## Closure Boundary

This transaction does not authorize a claim that models reason better merely because a packet can be built deterministically.

`RETRIEVAL VERIFIED != COGNITIVE IMPROVEMENT VERIFIED`.
