# P335 — Multi-Instance Amendment Reconciliation & Promotion Gate

Status: `CLOSED / RECONCILED / PROMOTION-PENDING / NO-RUNTIME-MUTATION`

## Re-entry
Current `main` was re-read before work. `GOV-013` is canonical v1.1.2. `GOV-013A` is explicitly `PROPOSED / GOVERNANCE-CONTROLLED / NOT YET CANONICAL`.

## Analysis
The proposed amendment materially strengthens multi-instance operation, but its rules must not be silently treated as canonical. The existing GOV-013 already requires repository-based continuation and evidence discipline; GOV-013A extends that foundation with explicit concurrency boundaries, shared evidence graph, evidence precedence, and handoff requirements.

## Decision
No direct replacement or version bump of GOV-013 is performed in this session. Promotion requires the existing governance/learning promotion mechanism and evidence that the amendment does not conflict with higher authority.

## Operational Benefit
Once promoted, the amendment will make parallel AI/window/platform execution operate against one repository truth while preserving bounded mutations and cross-instance revalidation.

## Next Safe Action
Run governance/learning promotion validation for GOV-013A, including conflict check against higher authority and existing GOV-013 rules. If approved, update the canonical protocol through a single minimal mutation and then run affected CI.

`GOV-013 = CANONICAL v1.1.2`
`GOV-013A = PROPOSED`
`RUNTIME = UNCHANGED`
`AUTHORITY = UNCHANGED`
`SESSION = CLOSED`
