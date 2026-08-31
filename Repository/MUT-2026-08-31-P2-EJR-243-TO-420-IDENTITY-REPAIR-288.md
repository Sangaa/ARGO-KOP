# MUT-2026-08-31-P2-EJR-243-TO-420-IDENTITY-REPAIR-288

Status: OPEN / FUNCTIONAL MUTATION PENDING
Scope: one-record Priority-2 identity repair: displaced root EJR-243 → EJR-420.
Opening main: `e3574912aa3502de7c070d7df084df9b783e8420`
Pre-write Matrix288: `8fb0a43c361592431ee6d29f455814e11d088193`

## Authority

Lease287 retained the earlier Memory EJR-243, displaced the later root EJR-243, and proved EJR-420 VACANT across complete reachable history. EJR-420 is reserved solely for this repair.

## Authorized mutation

Retain Memory EJR-243 unchanged; rename only the displaced root record to EJR-420; replace only its first H1 identity; preserve all other bytes; zero consumer rewrites absent fresh executable/governed consumers.

MEMORY_TO_ROOT baseline remains 17 in this repair. Any 17→16 normalization is a separate successor lease and requires exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
