# MUT-2026-08-31-P2-EJR-239-TO-419-IDENTITY-REPAIR-285

Status: OPEN / FUNCTIONAL MUTATION PENDING
Scope: one-record Priority-2 identity repair: displaced root EJR-239 → EJR-419.
Opening main: `c5165a375a3cd72671ee7d0062fb3c17dd43e133`
Pre-write Matrix285: `76bd48f16db35dc2c8299bda7e44c080432914d1`

## Authority

Lease284 retained the earlier Memory EJR-239, displaced the later root EJR-239, and proved EJR-419 VACANT across complete reachable history. EJR-419 is reserved solely for this repair.

## Authorized mutation

Retain Memory EJR-239 unchanged; rename only the displaced root record to EJR-419; replace only its first H1 identity; preserve all other bytes; zero consumer rewrites absent fresh executable/governed consumers.

MEMORY_TO_ROOT baseline remains 18 in this repair. Any 18→17 normalization is a separate successor lease and requires exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
