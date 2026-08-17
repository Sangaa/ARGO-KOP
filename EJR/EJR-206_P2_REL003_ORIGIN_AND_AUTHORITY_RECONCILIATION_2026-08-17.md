# EJR-206 — P2 REL-003 Origin and Authority Reconciliation

Date: 2026-08-17  
Status: RECORDED / SESSION-CLOSABLE / REVALIDATION REQUIRED  
Scope: Priority-2 relationship validation — `REL-003`  
Repository: Sangaa/ARGO-KOP  
Branch: main  
Development Baseline: 3.2.1  
Integrity State: INTEGRITY HOLD / CONNECTED-BASELINE AUDIT

## Starting Point

`EJR-205` identified a directional/type conflict:

`REP-014: REL-003 = ENG-004 → SRV-005 / PRODUCES`

while current endpoint documents state that `SRV-005` consumes `ENG-004`.

## Historical Origin

The initial `REP-014` creation commit `25666d313a0bc4a2bfdcd994ee6fcd4e33578a6d` introduced `REL-003` as:

`ENG-004 → SRV-005 = PRODUCES / SERVICE INPUT`

The record was described as already established during repository review, but the commit does not include a separate relationship-authority decision or endpoint evidence proving the semantic direction.

Subsequent registry reconciliation commit `166f2226ad26a3e923a1d1390665c0ae07379bd2` normalized the relationship type to the controlled value `PRODUCES` and retained the same direction/state, again without an independent decision artifact for the semantic direction.

Therefore history proves **origin and persistence of the registry record**, but not independent semantic authority for its direction/type.

## Current Endpoint Evidence

- `ENG-004_VALIDATION_ENGINE.md` states that the Validation Engine is consumed by `SRV-005` at the Service layer.
- `SRV-005_VALIDATION_SERVICE.md` states that `SRV-005` is the Service-layer consumer of `ENG-004`.

These current endpoint statements support `SRV-005 → ENG-004 = CONSUMES`, or at minimum do not support `ENG-004 → SRV-005 = PRODUCES`.

## Reconciliation Result

The provenance of the current registry entry is established, but its semantic authority is not.

`REL-003 = DIRECTION-TYPE CONFLICT / REVALIDATION REQUIRED`

No registry correction is authorized by the inspected historical evidence.

No mutation was made to `REP-014`.
No relationship type/direction was promoted.
No executable claim was created.

## Learning

1. Historical provenance of a registry row is not equivalent to semantic authority for that row.
2. A reconciliation commit can normalize controlled vocabulary without proving the underlying semantic decision.
3. Endpoint contracts currently provide a stronger semantic signal than the old registry row, but still do not independently authorize canonical registry mutation.
4. The safe distinction is now explicit: `Origin Evidence` ≠ `Semantic Authority`.

## P2 State

`P2 = OPEN / RELATIONSHIP_VALIDATION`

`REL-001 = RECONCILED / NOT PROMOTED`

`REL-002 = REVALIDATION REQUIRED / NOT PROMOTED`

`REL-003 = DIRECTION-TYPE CONFLICT / REVALIDATION REQUIRED`

## Next Safe Action

Recover an explicit relationship decision/approval, or inspect the applicable canonical relationship-authority layer if one exists. Only then use the controlled REP-014 mutation scaffold to correct `REL-003`.

This record is sufficient for safe continuation or session closure.
