# EJR-181 — Runtime Metadata Guard Learning

Date: 2026-08-16

## Trigger
A bounded Runtime candidate identity guard was added for `RUN-011` through `RUN-015` and failed in CI even though the Runtime artifacts and Folder Status were consistent.

## Evidence
The guard initially assumed a two-line `Document ID` layout. Current Runtime candidate artifacts use the valid inline form `Document ID: RUN-xxx`.

The same artifacts remain explicitly `Candidate / Integrity Hold` and the Runtime folder remains `CROSS-LAYER INTEGRATION HOLD`.

## Root Cause
The regression guard assumed textual uniformity instead of validating the semantic identity invariant across a known metadata variant.

## Correction
The guard was changed to accept both:

- two-line `Document ID` metadata;
- inline `Document ID: RUN-xxx` metadata.

The Runtime artifacts were not changed because they were not defective.

## Verification
- Runtime Prototype / Integration / Integrity run #491: PASS.
- Full-Stack Repository Audit run #704: PASS.

## Learning Rule
**Identity guards must treat metadata representation as an input format, not as the invariant itself. Validate the identity and authority semantics while accepting all currently verified repository representations.**

A guard failure is not automatically a source defect. First classify it as source defect, inventory inconsistency, guard/parser defect, or valid format variation.

## Reuse
Applies across Runtime, Services, Models, Interfaces, Core and future namespace identity gates.
