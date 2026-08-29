# MUT-2026-08-29-GOVERNANCE-CANDIDATE-SEMANTIC-REVIEW-117R2

Date: 2026-08-29
Parent transaction: `R71-20260829-GOV-CONTENT-SEMANTIC-117`
Baseline: `main@3e3a9684830e4a2f3414f1c6fc5f3f28641e44dc`
Status: `PREWRITE / SECOND STATUS-COMPATIBILITY REPAIR / NOT CLOSED`

## Failure evidence

Exact-head repair run `33257559732` failed only in integration-tests. Full-Stack run `33257559716` and M2 run `33257559729` succeeded.

Runtime/Integration result remained `1 failed, 506 passed, 11 subtests passed`.

The first stable phrase was restored successfully. The remaining failing contract requires:
`CONTENT REVIEW HOLDS REMAIN`.

## Semantic interpretation

The phrase remains true. Transaction 117 boundedly closed the semantic disposition of the **current identified candidate set**, but it did not close all possible Governance content review, repository-wide relationship integrity, future promotion reviews, or newly discovered semantic drift.

Therefore removing `CONTENT REVIEW HOLDS REMAIN` was not only a compatibility break; it overstated the breadth of closure.

## Authorized repair

- `Governance/_FOLDER_STATUS.md` — preserve both stable clauses while retaining the new bounded candidate disposition:
  `IDENTITY + REP-001/REP-002 INVENTORY SYNC VERIFIED / CURRENT CANDIDATE SEMANTIC DISPOSITION VERIFIED / CONTENT REVIEW HOLDS REMAIN`
- this Matrix — finalize in the same protected change set.

No tests are changed. No candidate status/authority is changed. No GOV-012/CELM repair is reverted. No REP-001/002, Runtime, Services, release baseline, relationship authority or Room71 state is mutated.

## Verification

`PREWRITE → STATUS + FINALIZED MATRIX SAME CHANGE SET → READ-BACK → EXACT-HEAD CI → CLOSE OR HOLD`.

## Learning

A bounded closure must remain visibly bounded in the aggregate status surface. Closing one reviewed set must not erase a broader hold that remains true.

`BOUNDED CONTENT DISPOSITION ≠ GLOBAL CONTENT REVIEW CLOSURE`.
