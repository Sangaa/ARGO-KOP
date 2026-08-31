# MUT-2026-08-31-P2-EJR-236-TO-417-IDENTITY-REPAIR-279

Status: OPEN / FUNCTIONAL MUTATION PENDING
Scope: one-record Priority-2 identity repair: displaced root EJR-236 → EJR-417.
Opening main: `b6a7050d5290e059580287c971671d6a84c33562`
Pre-write Matrix279: `8175e78547f144f2edaedc05c163297922732683`

## Authority

Lease278 retained the earlier Memory EJR-236, displaced the later root EJR-236, and proved EJR-417 VACANT across complete reachable history. EJR-417 is reserved solely for this repair.

## Authorized mutation

Retain Memory EJR-236 unchanged; rename only the displaced root record to EJR-417; replace only its first H1 identity; preserve all other bytes; zero consumer rewrites absent fresh executable/governed consumers.

MEMORY_TO_ROOT baseline remains 20 in this repair. Any 20→19 normalization is a separate successor lease and requires exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
