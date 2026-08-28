# REP-051 — P448 B08 Authorized Placement Decision

Date: 2026-08-28
Protocol: GOV-013
Mode: PLACEMENT / PROVENANCE RECONCILIATION

## Objective
Determine the correct existing workstream for the B08 handoff proof before any new functional mutation.

## Evidence reviewed
- Canonical main is at `09b216e403fe99a6f1a4a35e3c3038831398f6a3` and contains the REL-009 boundary matrix requiring independent callable-consumer evidence and runtime execution evidence before promotion.
- The matrix explicitly states that ENG-006 -> SRV-009 evidence alone does not propagate to RUN-010 -> SRV-009.
- Historical P400 created `Runtime/Execution/run010_handoff_contract.py` and its test on isolated branch `hermuz/p400-b08-caller-contract-20260828` at `d6c1814c28082b9eb2265db32bd3baa2b5572e95`. The artifact is pure, performs no I/O or dispatch, and was intentionally not promoted.
- PR #63 is explicitly titled `P302: isolated RUN-010 to ENG-006 executable-boundary contract` and is described as governed isolated validation with no production runtime/registry mutation; REL-009 remains open pending executable evidence.
- PR #64 is explicitly titled `P382: isolated B07 execution observation`; its stated scope is exposing the existing isolated B07 consumer/test to pull_request Actions for exact-HEAD observation.

## Decision
The existing evidence supports treating the P400 handoff contract as the natural B08 contract artifact and PR #63 as the closer semantic workstream for RUN-010 -> ENG-006 executable-boundary validation. PR #64 should remain the B07/execution-observation workstream rather than become the container for unrelated B08 construction.

This is a placement decision, not authorization to merge either PR and not authorization to wire the connected spine.

## Mutation decision
No functional mutation is made in this checkpoint. The next safe mutation, if required, is to a dedicated isolated B08 observation workstream derived from the P400 contract, with exact-head CI and explicit runtime evidence. Reusing existing P400 artifacts is preferred over recreating equivalent tests.

## Learning classification
VALIDATED KNOWLEDGE:
- Workstream identity must follow semantic responsibility, not merely the most recent PR with available CI.
- A successful B07 observation channel does not make PR #64 a valid B08 implementation container.
- Existing isolated proof should be reused when its contract and provenance remain valid; duplication is not evidence.

These statements are not canonical governance rules unless separately promoted through the governance path.

## Status
P448 = CLOSED
B08 PLACEMENT = SEMANTICALLY RESOLVED
P400 CONTRACT = REUSABLE ISOLATED ARTIFACT
PR #63 = CLOSER B08 WORKSTREAM
PR #64 = B07 OBSERVATION WORKSTREAM
FUNCTIONAL MUTATION = NONE
PROMOTION = NOT AUTHORIZED
NEXT = EXACT-HEAD B08 OBSERVATION ON THE AUTHORIZED ISOLATED WORKSTREAM
