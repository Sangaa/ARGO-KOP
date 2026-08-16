# EJR-184 — Relationship Registry State Drift Learning

Date: 2026-08-16

## Trigger
Current-main reconciliation found `REL-005` in `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` still marked:

`ENG-006 → SRV-009 | IMPLEMENTS | Revalidated within inspected scope`

while current executable evidence supports only a documented/contractual relationship and explicitly lacks a callable `SRV-009` consumer implementation.

## Root Cause
The source and target documents remained current, but the **relationship state/type** in the registry had become stale relative to later executable-path evidence.

This is a distinct defect class from:

- document identity drift;
- inventory-surface drift;
- control-plane path drift.

## Current Disposition

P259 records the current review-cycle state as:

`REL-005 = REVALIDATION REQUIRED`

with the safe semantic description:

`ENG-006 → SRV-009 = DOCUMENTED / CONTRACTUAL`

until executable consumer evidence is established.

## Verification

- Runtime Prototype / Integration / Integrity run #504: PASS.
- Full-Stack Repository Audit run #717: PASS.

## Learning Rule
**Relationship registry state is mutable evidence. A relationship must be revalidated whenever executable, consumer, identity or dependency evidence changes; a previously verified relationship type must not be treated as permanent truth.**

The registry must distinguish:

`DOCUMENTED → EXECUTABLE → TESTED → VERIFIED`

rather than collapsing these evidence levels.

## Reuse
Apply this rule to all high-impact relationships in REP-014, especially `IMPLEMENTS`, `CONSUMES`, `OWNS`, `GOVERNS`, and other relationships whose semantics can change after runtime implementation or consumer validation.
