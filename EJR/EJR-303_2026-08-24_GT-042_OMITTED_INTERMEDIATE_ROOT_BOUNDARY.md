# EJR-303 — GT-042 Omitted Intermediate Root Boundary

Date: 2026-08-24
Status: CONTROLLED REGRESSION RECORDED / CI EXECUTION PENDING

## Observation

The provenance chain is:

`ROOT-A → PARENT → CHILD`

with:

- `ROOT-A.root = ROOT-A`
- `PARENT.root = omitted`
- `CHILD.root = ROOT-A`

The child therefore names the same root that is reachable through its parent, but the immediate parent does not repeat the root declaration.

## Current Boundary

The current ARGO provenance rule treats this explicit child root as invalid when it skips an intermediate node whose root declaration is omitted.

Expected controlled result:

`INVALID PROVENANCE`

## Why This Is Recorded

This case is distinct from GT-040 (all levels explicitly agree) and GT-041 (an explicit deep-root conflict). It isolates the semantics of an omitted intermediate root declaration.

No canonical promotion is made from this test. The test records current boundary behavior only; it does not claim that omission must be universally invalid outside the present ARGO contract.

## Verification Boundary

Test file commit:
`c6f6c23387386636a1aa767e9e92049258ab794b`

CI/runtime execution is not claimed because no workflow run was exposed by the available GitHub surface.

## Learning

An omitted intermediate provenance root is materially different from an explicit matching root. The current implementation does not infer an explicit child's root through that omission; it rejects the chain instead of silently normalizing the missing declaration.
