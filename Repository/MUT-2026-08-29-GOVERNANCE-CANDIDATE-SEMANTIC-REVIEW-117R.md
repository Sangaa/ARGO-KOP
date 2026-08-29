# MUT-2026-08-29-GOVERNANCE-CANDIDATE-SEMANTIC-REVIEW-117R

Date: 2026-08-29
Parent transaction: `R71-20260829-GOV-CONTENT-SEMANTIC-117`
Baseline: `main@a9bde62b0762d51b39831a334f30b8eae8291e4c`
Status: `PREWRITE / CI-FAILURE REPAIR / NOT CLOSED`

## Failure evidence

Exact-head Runtime/Integration run `33257449825` failed only in `integration-tests`; integrity and prototype jobs passed. Integration result: `1 failed, 506 passed, 11 subtests passed`.

Failing contract:
`Quality/Integration/test_internal_document_id_audit.py::test_current_tree_governance_document_heading_identities_are_unique_after_migration`

The test correctly preserves the stable Governance status checkpoint phrase:
`IDENTITY + REP-001/REP-002 INVENTORY SYNC VERIFIED`.

Transaction 117 changed the status headline to insert new semantic-disposition wording before `VERIFIED`, breaking the stable checkpoint while not changing the underlying identity/inventory result.

## Classification

`CONTENT-PRESENTATION REGRESSION / EXISTING AUTHORITY CONTRACT PRESERVED`.

The new semantic review is not invalidated. The existing test is not weakened. The smallest correct repair is to restore the exact stable identity/inventory phrase and append the new semantic-disposition state after it.

## Authorized repair

- `Governance/_FOLDER_STATUS.md` — headline wording only: preserve exact `IDENTITY + REP-001/REP-002 INVENTORY SYNC VERIFIED`, then append current candidate semantic disposition and promotion holds.
- this Matrix — finalize in same protected change set.

No candidate content/status authority, GOV-012, CELM, REP-001/002, Runtime, Services, tests, release baseline, relationship authority, or Room71 state is authorized to change in this repair.

## Verification

`PREWRITE → PROTECTED STATUS + FINALIZED MATRIX SAME CHANGE SET → READ-BACK → EXACT-HEAD CI → CLOSE OR HOLD`.

## Learning

A status headline can itself be a tested compatibility surface. Extending status semantics must preserve stable machine-observed clauses when their underlying state remains true.

`SEMANTIC EXTENSION ≠ PERMISSION TO BREAK STABLE STATUS CONTRACT`.
