# MUT-2026-08-29-GOVERNANCE-CANDIDATE-SEMANTIC-REVIEW-117R2

Date: 2026-08-29
Parent transaction: `R71-20260829-GOV-CONTENT-SEMANTIC-117`
Prewrite baseline: `main@3e3a9684830e4a2f3414f1c6fc5f3f28641e44dc`
Protected-change parent: `main@b23eed8d1c3c97fede200f3d8696d31a898ca970`
Status: `FINALIZED / SECOND STATUS-COMPATIBILITY REPAIR / SAME-CHANGE-SET / CI PENDING`

## Failure evidence

Exact-head repair run `33257559732` failed only in integration-tests. Full-Stack run `33257559716` and M2 run `33257559729` succeeded.

Runtime/Integration result: `1 failed, 506 passed, 11 subtests passed`.

The first stable status phrase was restored. The remaining failing contract requires:
`CONTENT REVIEW HOLDS REMAIN`.

## Root cause

Transaction 117 boundedly closed the semantic disposition of the current identified candidate set, but its aggregate status headline dropped the broader hold phrase. Repository-wide relationship/content review and future evidence-triggered semantic review remain open, so the dropped phrase was both a compatibility regression and an over-broad closure signal.

Classification:
`BOUNDED-CLOSURE PRESENTATION REGRESSION / BROADER HOLD REMAINS TRUE`.

## Repair changed set

| Change | Target | Action | Result |
|---|---|---|---|
| R2-1 | `Governance/_FOLDER_STATUS.md` | UPDATE | restore `CONTENT REVIEW HOLDS REMAIN` while preserving candidate-set bounded closure |
| R2-2 | this Matrix | UPDATE | finalize with R2-1 in same Git tree/commit |

Corrected aggregate status:

`IDENTITY + REP-001/REP-002 INVENTORY SYNC VERIFIED / CURRENT CANDIDATE SEMANTIC DISPOSITION VERIFIED / CONTENT REVIEW HOLDS REMAIN`

No test is changed. No GOV-012/CELM repair is reverted. No candidate authority/status is changed. No REP-001/002, Runtime, Services, release baseline, relationship authority or Room71 state is mutated.

## Verification gate

Required exact-head CI after R2:
- ARGO Runtime Prototype and Integration Tests;
- Full-Stack Repository Audit;
- M2 Multi-Channel Proposal Training;
- Real Mutation Matrix Regression when emitted.

Until exact-head CI is green, transaction 117 remains open.

## Learning

`BOUNDED CONTENT DISPOSITION ≠ GLOBAL CONTENT REVIEW CLOSURE`.

Aggregate status surfaces must preserve broader holds that remain true even when one subordinate review set is closed.
