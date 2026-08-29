# Branch Family Disposition — Legacy Runtime / Experience Precursors

Date: 2026-08-29
Baseline inspected before classification: current `main` lineage through `12e8813d84b3ccc2f931953ed3d4a2ddc4d971ef`.

Leases:
- `R71-20260829-BRANCH-HYGIENE-074` — `e2e/p3-srv009-isolated-20260817`
- `R71-20260829-BRANCH-HYGIENE-075` — `feature/experience-spine-p375`
- `R71-20260829-BRANCH-HYGIENE-076` — `hermuz/p302-rel009-executable-boundary-20260827`
- `R71-20260829-BRANCH-HYGIENE-077` — `hermuz/p302-rel009-contract-test-20260827`

## 074 — Isolated P3 repository roundtrip

The branch-only closure explicitly proves live GitHub create/update/read-back/delete on an isolated branch and explicitly does **not** prove ARGO runtime production invocation. Current main later records the stronger bounded P3/P4 evidence, including production adapter/GitHub connector E2E for REL-005.

Disposition:
`HISTORICAL_ISOLATED_REPOSITORY_ROUNDTRIP / OWN_BOUNDARY_RUNTIME_INVOCATION_NOT_PROVEN / LATER_MAIN_P3_P4_BOUNDED_EVIDENCE / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

## 075 — Early Experience Spine feature branch

The branch carries an early Experience Spine implementation. Current main contains a later hardened implementation with stricter lifecycle/validation/provenance profile requirements, evidence-group correlation handling, conflict review state, and explicit evidence/authority boundaries. The branch blob and current-main blob differ in the direction of hardening, not missing functionality.

Disposition:
`HISTORICAL_EXPERIENCE_SPINE_PRECURSOR / MAIN_HAS_HARDENED_SUCCESSOR / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

## 076 — P302 executable-boundary branch

Git comparison establishes `ahead_by=0`; the branch is fully ancestral to current main.

Disposition:
`FULLY_ANCESTRAL_TO_MAIN / NO_UNMERGED_WORK / NO_MERGE_REQUIRED / NO_DELETE_AUTHORIZED`

## 077 — P302 contract-test workstream

This branch accumulated early RUN-010/ENG-006 consumer experiments, provider-factory work, OpenHands qualification experiments, session deltas and the candidate repository-first multi-instance amendment. Its P331 record explicitly states the amendment was candidate/promotion-pending and main unchanged. Current main now has the governed successor as `GOV-021_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md`, promoted after the Room71 reconstruction test, while P4 has since closed REL-009 only under the bounded intentional-one-way non-universal architecture.

Disposition:
`HISTORICAL_MIXED_PRECURSOR_WORKSTREAM / REPOSITORY_FIRST_CONTRACT_PROMOTED_LATER_AS_GOV021 / REL009_ARCHITECTURE_LATER_BOUNDEDLY_RECONCILED / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

## Learning

A later canonical successor should close the old promotion question without rewriting the old branch's epistemic status. Candidate amendments remain candidate at their checkpoint; later promotion is a separate evidence event.
