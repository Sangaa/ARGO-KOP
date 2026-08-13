# EJR-171 — Relationship Matrix Phase-1 Seed

Date: 2026-08-13  
Status: Recorded / Session Continuation Evidence  
Development Baseline: 3.2.1

## What was executed

During the repository relationship review, the provisional `REP-020` Dependency & Consumer Impact Matrix was created and seeded from inspected evidence rather than assumptions.

The seed currently covers the control-plane relationships among `REP-001` through `REP-016`, plus the documented/provenance relationship between `REP-012` and `DIAG-001`.

The matrix was re-read after creation and its persisted content was confirmed on `main`.

## Evidence basis

`REP-013` identifies the physical control-plane artifacts `REP-011` through `REP-016` and explicitly states that their review, allocation and relationship states require cross-registry reconciliation. `REP-014` provides the controlled relationship types and the current relationship records used for the seed.

## Important design decision

`REP-020` is **Provisional / Phase-1 Seed / Not Authority**.

It narrows future review scope but does not replace proof. A relationship marked verified in the matrix remains bounded by the inspected scope and must be revalidated when a relevant mutation occurs.

## Seeded impact model

For a changed artifact, the minimum lookup is:

`outgoing edges + incoming/reverse edges + consumers + dependencies + authority + content contract + derived/provenance artifacts + session/audit records`

The resulting set is the targeted revalidation scope. Newly discovered relationships expand that scope.

## Current limitation

This is not yet an exhaustive repository graph. Partial inventories, wildcard entries, domain semantics, and global bidirectional validation remain open.

## Session safety

If the session terminates here, resume from the `REP-020` persisted seed and this journal entry. Do not infer global graph closure or Integrity PASS.
