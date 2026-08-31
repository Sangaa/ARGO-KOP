# MUT-2026-08-31-P2-EJR-238-TO-418-IDENTITY-REPAIR-282

Status: OPEN / FUNCTIONAL MUTATION PENDING
Scope: one-record Priority-2 identity repair: displaced root EJR-238 → EJR-418.
Opening main: `b993e0640453c1a433572a86b8f9fe53005f9e28`
Pre-write Matrix282: `68fe711a45e891b4d795863afda6a5e578c579c4`

## Authority

Lease281 retained the earlier Memory EJR-238, displaced the later root EJR-238, and proved EJR-418 VACANT across complete reachable history. EJR-418 is reserved solely for this repair.

## Authorized mutation

Retain Memory EJR-238 unchanged; rename only the displaced root record to EJR-418; replace only its first H1 identity; preserve all other bytes; zero consumer rewrites absent fresh executable/governed consumers.

MEMORY_TO_ROOT baseline remains 19 in this repair. Any 19→18 normalization is a separate successor lease and requires exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
