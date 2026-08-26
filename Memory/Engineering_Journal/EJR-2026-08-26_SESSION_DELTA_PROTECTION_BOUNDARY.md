# EJR — Session-Delta Protection Boundary Learning

Status: `PROMOTED / VERIFIED`
Date: 2026-08-26

## Failure Pattern
A `Repository/REP-*` session-delta record was classified as a protected canonical repository mutation because the preflight rule matched the broad `Repository/REP-` prefix. This caused a Full-Stack failure when no Mutation Matrix accompanied documentation-only session evidence.

## Root Cause
The protection rule distinguished by directory/prefix but did not distinguish **canonical Repository control artifacts** from **session-delta evidence records**.

## Correct Boundary
- `Repository/REP-*_SESSION_DELTA_*.md` = session/governance evidence record; no Mutation Matrix required.
- Other `Repository/REP-*` artifacts remain protected and require a Mutation Matrix.
- This is a classification correction, not a weakening of protection for canonical Repository control artifacts.

## Preventive Control
The preflight classifier now has an explicit session-delta predicate and its regression suite asserts both sides of the boundary: session delta exempt; ordinary REP control artifact protected.

## Reuse Rule
Do not solve this failure by adding a Matrix to every documentation/session record. First classify whether the file is a canonical implementation/control artifact or a governance/session evidence record.
