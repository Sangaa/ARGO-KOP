# Experience Spine Clean Extraction — Mutation Matrix

Transaction ID: `MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@51374901bc03503f3e5d90192e0e0c2adc02d01e`
Working branch: `hermuz/experience-spine-clean-20260828`
Status: `CLOSED / MERGED / POST-MERGE VERIFIED / COGNITIVE BENEFIT UNPROVEN`

## Purpose

Extract the smallest useful Experience Spine capability from historical PR #66 and HORUS analysis PR #69 without rebasing or merging either workstream wholesale.

The capability is a governed semantic projection over already-promoted knowledge, not a second memory store, second promotion system, or new authority layer.

## Final Design Invariants

1. `EXPERIENCE SPINE = SEMANTIC PROJECTION OVER PROMOTED KNOWLEDGE`.
2. `REUSE != PROMOTION != AUTHORITY`.
3. Lifecycle, validation, evidence, authority, scope, and source attribution remain separate axes.
4. Missing structural context narrows/holds retrieval; it never broadens it.
5. Structural exact keys are used; free-text similarity alone is not governed relevance.
6. Contradictions are exposed as review-required; they are never silently resolved.
7. Same-lineage records are correlated, not independent confirmation.
8. Superseded projections are excluded without erasing historical knowledge records.
9. Legacy promoted records remain valid without `experience_profile`; they are not guessed into the stricter projection.
10. Current evidence and applicable authority outrank advisory retrieved experience for the claims they legitimately govern.
11. Retrieval mechanics do not prove cognitive benefit.

## Applied Changes

| ID | Target | Result | Applied | Verified |
|---|---|---|:---:|:---:|
| C01 | `Knowledge/Learning/experience_spine.py` | bounded semantic projection over promoted+validated records; conflict/correlation/supersession controls | Y | Y |
| C02 | `Knowledge/Learning/test_experience_spine.py` | 11 focused mechanics regressions; import location independent | Y | Y |
| C03 | `Quality/Integration/test_experience_spine_integration.py` | CI-visible execution/source/authority, correlation and contradiction boundary tests | Y | Y |
| C04 | `Knowledge/Learning/KNOWLEDGE_RECORD_SCHEMA.md` | optional nested `experience_profile`; promotion lifecycle unchanged | Y | Y |
| C05 | `Knowledge/Learning/TASK_CONTEXT_ENVELOPE.md` | bounded structural context + repository/multi-writer attribution | Y | Y |
| C06 | `Knowledge/Learning/KNOWLEDGE_REUSE_POLICY.md` | advisory projection, contradiction, supersession, correlation, provenance and cognitive-benefit boundaries | Y | Y |
| C07 | `Quality/Integration/test_experience_spine_integration.py` | execute focused C02 suite under CI and require nested pytest success plus literal `11 passed` | Y | Y |

Unexpected changed paths at final pre-merge compare: `0`.

Final payload: six capability/policy targets plus this Mutation Matrix.

## Focused-Test Execution Learning

First exact-head compatibility observation on `db2f1e3950a6712e80756b43e11d5c3b9ae455e7`:

- Full-Stack `33200699127` — SUCCESS;
- Runtime/Integration `33200699104` — SUCCESS;
- outer integration suite `298 passed`.

Log inspection established that the 11 focused tests under `Knowledge/Learning/test_experience_spine.py` were not discovered by that workflow. Repository presence was not treated as execution proof.

C07 then bound the focused suite into the CI-visible integration path.

Exact head `343cc4bbfa933751566a49169f6f064ab7d0fcbc`:

- Full-Stack `33201187539` — SUCCESS;
- Runtime/Integration `33201187605` — SUCCESS;
- integration job `98950760048` — SUCCESS;
- outer integration suite increased to `299 passed`.

C07 is fail-closed: it executes the focused unit file and passes only when nested pytest returns `0` and captured stdout contains literal `11 passed`. Nested stdout is captured rather than printed on success, so this evidence proves the gate condition without falsely claiming the literal nested line appeared in the workflow log.

Reusable rule:

`TEST FILE EXISTS != TEST EXECUTED`.

`BROAD SUITE PASS != UNDISCOVERED FOCUSED SUITE PASS`.

## Final Frozen Head / CI

Final frozen PR head:

`9a8cef7ef1fd1a15760e5638923794bf01c3cf23`.

Exact-head CI:

- Full-Stack Repository Audit `33201300762` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33201300749` — SUCCESS.

Final compare against entry main:

- `ahead_by = 12`;
- `behind_by = 0`;
- changed paths = `7` exactly;
- unexpected paths = `0`.

## Merge

PR #76 was squash-merged with expected frozen head SHA.

Merged main commit:

`a4cc96203b689338a50b7233b46c15eae8449f5a`.

## Post-Merge Exact-Main Verification

On `main@a4cc96203b689338a50b7233b46c15eae8449f5a`:

- Full-Stack Repository Audit `33201440156` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests `33201440177` — integration / integrity / prototype jobs SUCCESS;
- M2 Multi-Channel Proposal Training `33201440226` — SUCCESS.

Result:

`EXPERIENCE SPINE MECHANICS = EXECUTION-VERIFIED / MERGED / POST-MERGE VERIFIED / ADVISORY / NON-AUTHORITATIVE`.

## Historical Workstream Disposition

After post-merge verification:

- PR #66 was closed, not merged: `HISTORICAL PROTOTYPE / SEMANTICALLY CONSUMED / PROVENANCE PRESERVED`;
- PR #69 was closed, not merged: `ANALYTICAL PROVENANCE / SEMANTICALLY CONSUMED / NON-AUTHORITATIVE`.

Open PR surface after closure: `0`.

The old branches remain historical evidence; they are not current authority or active integration surfaces.

## Clean-Extraction Corrections vs Historical Prototype

The clean implementation did not copy prototype lifecycle eligibility `{PROMOTED, REUSABLE, VERIFIED, CANONICAL}`. Current governed lifecycle remains `PROMOTED`, with `validation=VALIDATED` checked separately.

Retrieval metadata is nested under optional `experience_profile`.

The clean implementation added `evidence_group`, `superseded_by`, explicit correlated-evidence reporting and `REVIEW_REQUIRED` conflict behavior.

Historical session-delta/mutation documents from PR #66 were not copied into the capability payload.

## Explicit Non-Claims

- No new persistence layer was created.
- No Memory-domain or Engine authority was changed.
- No automatic enrichment/promotion/demotion was introduced.
- No provider/model dependency was introduced.
- No cognitive improvement was established by retrieval mechanics.

## Closure

`EXPERIENCE SPINE CLEAN TRANSACTION = CLOSED`.

`RETRIEVAL VERIFIED != COGNITIVE IMPROVEMENT VERIFIED`.

The next independent workstream is `MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001`, which evaluates the cognitive-effect evidence boundary without reopening this transaction.
