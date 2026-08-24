# EJR-301 — GT-040 Multilevel Explicit Root Agreement

Date: 2026-08-24
Status: VERIFIED BY CONTROLLED REGRESSION / CI EXECUTION PENDING
Scope: `Quality/Integration/test_evidence_reasoning_classification.py`

## Problem

GT-040 extends the GT-039 parent/root consistency boundary from a direct root-child pair to a multilevel chain:

- `ROOT-A` is the provenance anchor.
- `PARENT` declares `provenance_root = ROOT-A` and `provenance_parent = ROOT-A`.
- `CHILD` declares `provenance_root = ROOT-A` and `provenance_parent = PARENT`.

The child therefore repeats the explicit root across a non-root parent rather than relying on an omitted/inherited root.

## Decision

The chain remains **VALID PROVENANCE** when every explicitly declared root agrees with the resolved parent-chain root.

The dependent comparison remains:

`CONSISTENT / CORRELATED`

because the parent/child relationship establishes provenance correlation even though both observations are marked independently sourced.

## Boundary

GT-040 does not introduce a new canonical provenance rule. It records a regression boundary proving that the existing GT-039 consistency rule remains stable when the explicit root declaration is repeated at multiple levels of the parent chain.

The test is intentionally narrow: it does not infer behavior for conflicting roots, missing anchors, cycles, or omitted child roots because those cases already have separate regression coverage.

## Evidence

Test mutation commit:
`94f683bbe6816260131832a597eaa57aee143c59`

Test:
`test_gt040_explicit_root_agreement_across_multilevel_parent_chain`

## Verification Boundary

The modified test file was re-read from commit `94f683bbe6816260131832a597eaa57aee143c59` and the GT-040 assertion is present.

CI/runtime PASS is not claimed because no workflow execution was exposed by the repository connector for this mutation at verification time.

## Learning

A provenance root declaration remains structurally valid when it is explicitly repeated across multiple levels, provided every declared value agrees with the root resolved through the parent chain. Explicit repetition does not by itself create independence; provenance connectivity still governs the classification as correlated.
