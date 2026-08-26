# KRS-003 Mutation Matrix — P260

Status: `APPLIED / ASSESSMENT ONLY`
Parent: `afc85d60829e677723838b31dac7a2b1c6195489`

## Scope
Adds the three-class compression comparison and does not alter existing artifacts, authority, runtime dependencies, IDs or relationships.

## Change
- Add `Repository/KRS-003_THREE_CLASS_COMPRESSION_PILOT_P260.md`.

## Protected Controls
- No deletion, retirement or migration.
- KRS-002 remains non-canonical.
- Governance and journal authority remain unchanged.
- No relationship is promoted without evidence.

## Required Validation
Post-write read-back → exact-SHA CI/full-stack validation → reconcile workflow/jobs/steps and affected matrix state → session closure.

## Promotion Gate
No compression or migration decision until semantic/evidence equivalence is demonstrated on concrete representative artifacts and human + machine reviewability are tested.
