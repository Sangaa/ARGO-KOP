# BRANCH DISPOSITION — hermuz/experience-spine-igt-20260828

Date: 2026-08-29  
Room: 71  
Lease: `R71-20260829-BRANCH-HYGIENE-025`  
Baseline: `main@797b5aa268363ffe9cf8c193722b8f33701eea0f`

## Classification

`MERGED_FUNCTIONAL_LINEAGE / MAIN_CONTAINS_HARDENED_SUCCESSOR / HISTORICAL_BRANCH / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

The branch diverges from current main with 17 branch-side commits from merge base `a4cc96203b689338a50b7233b46c15eae8449f5a`. Its bounded surfaces are the Experience Spine IGT harness, cases, tests, execution matrix and transaction records.

Current main contains those IGT surfaces and a hardened successor of the evaluator. The branch evaluator blob differs from main because main includes a later correction that also strips `authority_boundary` from the L1 decision view; replaying the branch would therefore regress information separation rather than improve it.

Current main transaction record explicitly identifies working branch `hermuz/experience-spine-igt-20260828`, PR #77, records hardened source-head Runtime/Integration and Full-Stack success, and preserves the boundary `PARTICIPANT RUNS UNSEEN / COGNITIVE EFFECT INCONCLUSIVE`.

## Decision

- Merge: `NO` — functional lineage is already represented on main and main contains a later hardened evaluator.
- Promote branch: `NO`.
- Preserve evidence/history: `YES`.
- Delete: `NOT AUTHORIZED`.
- Cognitive benefit: remains `UNPROVEN / INCONCLUSIVE`.

## Learning

Blob inequality does not automatically mean missing work. When main contains a hardened successor, branch replay can be a regression. Branch classification must establish direction of semantic evolution, not merely equality.

## Result

`HERMUZ_EXPERIENCE_SPINE_IGT_BRANCH = CLOSED_CLASSIFIED_MERGED_LINEAGE_MAIN_HARDENED_SUCCESSOR_NO_MERGE_NO_DELETE`
