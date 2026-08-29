# Branch Disposition — hermuz/p400-b08-caller-contract-20260828

Date: 2026-08-29
Lease: `R71-20260829-BRANCH-HYGIENE-044`
Authority: `OPERATIONAL CLASSIFICATION ONLY`

## Evidence

Compared against `main@876bc28ad7cf891ca0b0f4f8725a1b17c2023ab4`:
- status: diverged;
- ahead_by: 42;
- behind_by: 169;
- merge base: `09b216e403fe99a6f1a4a35e3c3038831398f6a3`.

The principal pure handoff artifact `Runtime/Execution/run010_handoff_contract.py` is already present on current main with the exact same blob SHA `1b0be5c76e02302a1a60b29e2fddba73869e8eab`.

The branch also contains the broader direct `run010_eng006_srv009_consumer.py` experiment that current main intentionally does not retain. Main's later P4 closure uses the pure handoff plus integration-only observation seam and explicitly preserves non-universal Runtime semantics.

## Disposition

`PURE_HANDOFF_FUNCTIONAL_BLOB_PRESENT_ON_MAIN / BROADER_B08_DIRECT_CONSUMER_EXPERIMENT_SUPERSEDED / HISTORICAL_EVIDENCE_PRESERVED / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

## Non-claims

- Exact handoff blob equality proves only that functional artifact is already present.
- It does not imply every branch-only checkpoint record is canonical.
- It does not authorize deletion.
- No new CI claim is made by this classification.

## Learning

A mixed experimental branch may contain both a canonicalized kernel and superseded exploratory scaffolding. Classification should split those semantic outcomes rather than label the entire branch simply merged or unmerged.
