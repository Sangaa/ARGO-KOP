# EJR-305 — HERMUZ Mandatory P6 Observation Provenance

Date: 2026-08-22
Status: Closed — Mutation + Read-back Verified
Scope: P6 evidence boundary

## Trigger

EJR-304 converted the observation-state distinction into an explicit vocabulary and regression contract, but the `Evidence` model still supplied a default `OBSERVED` state. That left a silent compatibility path through which a caller could omit observation provenance.

## Analysis

The learned rule is stronger than the previous implementation:

`Observation provenance must be explicit before evidence can enter P6 reconciliation.`

A default is unsafe because omission itself carries meaning. It can hide an adapter defect and make a connector capability failure appear to be an ordinary observation path.

Repository search found the observation-state implementation and its boundary test as the active consumers; no separate production constructor was identified through the available repository search surface. This absence is not treated as proof that no other consumer exists outside that surface.

## Mutation

Removed the default value from `Evidence.observation_state` so callers must provide an explicit observation state.

Updated the boundary fixtures to pass `OBSERVED` explicitly and added a regression asserting that omission raises `TypeError`.

## Verification

Read-back completed after both writes.

- `p6_reconciliation.py` blob SHA: `96dfcadc8b5f4c6513e7e3b2cfd99ab95d687f00`
- `test_p6_reconciliation_boundaries.py` blob SHA: `12d12d9b81302faf764010ab3da76579d71985ad`
- Engine mutation commit: `5a58ad13ddc1a9945d49d1b24432f02b8f02600f`
- Test mutation commit: `47724a9f11f2be44060c5431cc3ff54984b7cb5b`

The controlled test file contains the explicit omission regression plus the existing P6-08/P6-09 boundary matrix. Execution of the repository test suite is not claimed through the connector until an execution surface produces authoritative evidence.

## Learning

A rule is not fully enforced when the code permits an implicit path that contradicts the rule. The provenance requirement therefore moves from documentation to constructor-level enforcement.

This also yields a reusable design principle:

> When omission can change the epistemic meaning of evidence, omission must be invalid rather than silently defaulted.

## Closure

Mutation: COMPLETE
Read-back: VERIFIED
Controlled regression definition: UPDATED
Canonical CI execution: NOT CLAIMED
P6 root cause: NOT CLAIMED
Relationship authority: UNCHANGED

Session step: `CLOSED — DOCUMENTED — READ-BACK VERIFIED`.
