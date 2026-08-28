# Experience Spine Clean Extraction — Mutation Matrix

Transaction ID: `MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@51374901bc03503f3e5d90192e0e0c2adc02d01e`
Working branch: `hermuz/experience-spine-clean-20260828`
Status: `MECHANICS EXECUTION-VERIFIED / ADVISORY / NON-AUTHORITATIVE / COGNITIVE BENEFIT UNPROVEN / FINAL DOC-HEAD CI PENDING`

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
| C02 | `Knowledge/Learning/test_experience_spine.py` | 11 focused mechanics regressions; import made location-independent | Y | Y |
| C03 | `Quality/Integration/test_experience_spine_integration.py` | CI-visible execution/source/authority, correlation, contradiction boundary tests | Y | Y |
| C04 | `Knowledge/Learning/KNOWLEDGE_RECORD_SCHEMA.md` | optional nested `experience_profile`; promotion lifecycle unchanged | Y | Y |
| C05 | `Knowledge/Learning/TASK_CONTEXT_ENVELOPE.md` | bounded structural context + repository/multi-writer attribution | Y | Y |
| C06 | `Knowledge/Learning/KNOWLEDGE_REUSE_POLICY.md` | advisory projection, contradiction, supersession, correlation, provenance and cognitive-benefit boundaries | Y | Y |
| C07 | `Quality/Integration/test_experience_spine_integration.py` | invoke focused C02 suite in CI and require successful return plus literal `11 passed` in nested pytest output | Y | Y |

## Read-Back Evidence

- C01 blob: `6215fceb2ec76039f6bee55c29613278fc5579bf`;
- C02 blob: `5045f10cd6a6122be6b42f1db8270dfa2cce4ed1`;
- C03/C07 blob: `bdc3fdac7599f871eefa3d740d6a511b27046ce3`;
- C04 blob: `15de230bf70991adc81de672dcd90597844f4581`;
- C05 blob: `46db6dd3e12fbd6de0442982a5ae606676b9c769`;
- C06 blob: `c2bebe5050c335da4e4ea09c83f84d1361aab7fb`.

No Runtime, Engine, Services, Memory, Governance, or repository-authority implementation mutation was introduced.

Unexpected changed paths observed: `0`.

## CI Evidence

### First repository/integration compatibility observation

Exact head `db2f1e3950a6712e80756b43e11d5c3b9ae455e7`:

- Full-Stack Repository Audit `33200699127` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33200699104` — SUCCESS;
- integration job: `298 passed, 1 warning, 11 subtests passed`.

Log inspection showed the three `Quality/Integration` Experience Spine tests executed, but the 11 focused tests under `Knowledge/Learning/test_experience_spine.py` were not discovered by that workflow. This head therefore proved compatibility and integration-smoke behavior, not full focused mechanics execution.

### Focused-suite CI binding observation

C07 was added, then exact-head CI executed on:

`343cc4bbfa933751566a49169f6f064ab7d0fcbc`.

Results:

- Full-Stack Repository Audit `33201187539` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33201187605` — SUCCESS;
- integration job `98950760048` — SUCCESS;
- outer integration suite: `299 passed, 1 warning, 11 subtests passed`.

The one-test increase from 298 to 299 is the C07 CI-binding test. C07 executes the focused unit file as a nested pytest process and fails unless both conditions hold:

1. nested pytest return code equals `0`;
2. captured nested stdout contains literal `11 passed`.

Because C07 itself passed inside exact-head CI, the focused 11-test mechanics suite is execution-verified. The nested stdout is captured by the test and is not printed literally in the successful outer workflow log, so this record does not falsely claim direct log visibility of that string.

Result:

`EXPERIENCE SPINE MECHANICS = EXECUTION-VERIFIED / ADVISORY / NON-AUTHORITATIVE / COGNITIVE BENEFIT UNPROVEN`.

## Reusable Learning

`TEST FILE EXISTS != TEST EXECUTED`.

`BROAD SUITE PASS != UNDISCOVERED FOCUSED SUITE PASS`.

Execution attribution must be established from workflow/job evidence plus the exact executed gate condition, not inferred from repository presence.

A passing wrapper test may establish a hidden nested condition when the wrapper's source is exact-head read-back verified and the condition is fail-closed; however, do not claim literal log visibility for captured output that the workflow did not print.

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

## Remaining Merge Gates

1. Run exact-head Full-Stack + Runtime/Integration CI after this evidence-only documentation update.
2. Freeze branch if PASS; no further mutation.
3. Re-read main and active PR heads/changed paths immediately before merge.
4. Squash merge only with expected frozen head SHA.
5. Require post-merge exact-main CI before advancing.
6. Close historical PR #66/#69 only after the clean extraction is safely on main, preserving provenance in their PR bodies/history.
7. Cognitive-effectiveness testing remains a separate IGT transaction with materially novel cases and baseline comparison.

## Closure Boundary

This transaction does not authorize a claim that models reason better merely because a packet can be built deterministically.

`RETRIEVAL VERIFIED != COGNITIVE IMPROVEMENT VERIFIED`.
