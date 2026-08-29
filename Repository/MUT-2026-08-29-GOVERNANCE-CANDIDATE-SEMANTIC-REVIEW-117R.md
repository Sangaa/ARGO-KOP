# MUT-2026-08-29-GOVERNANCE-CANDIDATE-SEMANTIC-REVIEW-117R

Date: 2026-08-29
Parent transaction: `R71-20260829-GOV-CONTENT-SEMANTIC-117`
Prewrite baseline: `main@a9bde62b0762d51b39831a334f30b8eae8291e4c`
Protected-change parent: `main@024b6d64dfbae899e18bee942c2c67aa91ad0443`
Status: `FINALIZED / CI-FAILURE REPAIR / SAME-CHANGE-SET / CI PENDING`

## Failure evidence

Exact-head Runtime/Integration run `33257449825` failed only in `integration-tests`; integrity and prototype jobs passed. Integration result: `1 failed, 506 passed, 11 subtests passed`.

Failing contract:
`Quality/Integration/test_internal_document_id_audit.py::test_current_tree_governance_document_heading_identities_are_unique_after_migration`

The existing regression correctly requires the stable status phrase:
`IDENTITY + REP-001/REP-002 INVENTORY SYNC VERIFIED`.

## Root cause

Transaction 117 extended the Governance folder headline by inserting semantic-disposition wording before the word `VERIFIED`. The underlying identity/inventory state remained verified, but the stable machine-observed checkpoint string was broken.

Classification:
`CONTENT-PRESENTATION REGRESSION / EXISTING AUTHORITY CONTRACT PRESERVED`.

## Repair changed set

| Change | Target | Action | Result |
|---|---|---|---|
| R1 | `Governance/_FOLDER_STATUS.md` | UPDATE | restore exact stable phrase, append candidate semantic disposition after it |
| R2 | this Matrix | UPDATE | finalize with R1 in same Git tree/commit |

No test is changed. No GOV-012/CELM semantic repair is reverted. No candidate authority/status is changed. No REP-001/002, Runtime, Services, release baseline, relationship authority or Room71 state is mutated.

## Corrected status contract

`IDENTITY + REP-001/REP-002 INVENTORY SYNC VERIFIED / CURRENT CANDIDATE SEMANTIC DISPOSITION VERIFIED / PROMOTION GATES REMAIN`

This preserves the historical verified clause and adds the new bounded semantic state without replacing it.

## Same-change-set discipline

R1 and this finalized Matrix are inserted into one Git tree and committed together after the prewrite checkpoint.

## Verification gate

Required exact-head CI after repair:
- ARGO Runtime Prototype and Integration Tests;
- Full-Stack Repository Audit;
- M2 Multi-Channel Proposal Training;
- Real Mutation Matrix Regression when emitted.

Until exact-head CI is observed, parent transaction 117 remains open.

## Learning

A status headline can be both human-readable content and a tested compatibility contract.

`SEMANTIC EXTENSION ≠ PERMISSION TO BREAK STABLE STATUS CONTRACT`.

When the old state remains true, additive status wording should preserve the exact tested clause rather than rewrite it stylistically.
