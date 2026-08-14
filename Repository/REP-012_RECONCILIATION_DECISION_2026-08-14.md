# REP-012 Reconciliation Decision — 2026-08-14

Status: Governance Decision Record

## Authority Finding

`Release/VERSION.md` and `PROJECT_STATUS.md` establish Development Baseline **3.2.1** as the current authoritative baseline within the inspected repository control plane.

`Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md` currently declares **3.3.0**, which conflicts with that authority.

## Decision

- Treat **3.2.1** as the current authoritative Development Baseline.
- Treat REP-012's `3.3.0` declaration as a stale/conflicting declaration pending controlled correction.
- Do not interpret REP-012's technical registry content as authority to override Release/VERSION.md.

## Required Mutation

A controlled full-file update of REP-012 is required to change its Development Baseline declaration to 3.2.1 while preserving all existing allocation and recovery records.

The mutation must be followed by:

1. full-file re-read;
2. REP-001 / REP-002 cross-check;
3. REP-020 matrix update;
4. integration/relationship revalidation where affected;
5. session evidence closure.

No authority is changed by this decision record alone.

## Current Integrity State

INTEGRITY HOLD.
