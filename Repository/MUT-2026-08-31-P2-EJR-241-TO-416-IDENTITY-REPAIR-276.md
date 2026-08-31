# MUT-2026-08-31-P2-EJR-241-TO-416-IDENTITY-REPAIR-276

Status: OPEN / FUNCTIONAL MUTATION PENDING
Scope: one-record Priority-2 identity repair: displaced root EJR-241 → EJR-416.
Opening main: `9e6322ea9e204b004d49df36f62ba8fc32f51576`
Pre-write Matrix276: `362e530c3031da067f7da8a96e370ba1474341de`

## Authority

Lease275 retained the earlier Memory EJR-241, displaced the later root EJR-241, and proved EJR-416 VACANT across complete reachable history. EJR-416 is reserved solely for this repair.

## Authorized mutation

Retain Memory EJR-241 unchanged; rename only the displaced root record to EJR-416; replace only its first H1 identity; preserve all other bytes; zero consumer rewrites absent fresh executable/governed consumers.

MEMORY_TO_ROOT baseline remains 21 in this repair. Any 21→20 normalization is a separate successor lease and requires exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
