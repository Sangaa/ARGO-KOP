# MUT-2026-08-31-P2-EJR-212-TO-415-IDENTITY-REPAIR-273

Status: OPEN / FUNCTIONAL MUTATION PENDING
Scope: one-record Priority-2 identity repair: displaced root EJR-212 → EJR-415.
Opening main: `a23c7cf7702125978a7991b8db5dbe642e12e311`
Pre-write Matrix273: `a7c3128fddf77e14d69dcc36aa7312e80e4ae033`

## Authority

Lease272 retained the earlier Memory EJR-212, displaced the later root EJR-212, and proved EJR-415 VACANT across complete reachable history. EJR-415 is reserved solely for this repair.

## Authorized mutation

- retain `Memory/Engineering_Journal/EJR-212_2026-08-14_P29_SESSION_CLOSURE.md` unchanged;
- rename root `EJR/EJR-212_P2_CURRENT_RELATIONSHIP_GRAPH_RECONCILIATION_2026-08-17.md` to `EJR/EJR-415_P2_CURRENT_RELATIONSHIP_GRAPH_RECONCILIATION_2026-08-17.md`;
- change only the first H1 identity from EJR-212 to EJR-415;
- preserve all remaining body/date/status/relationship evidence exactly;
- zero consumer rewrites unless a fresh executable/governed exact-path consumer appears before mutation.

Prewrite Full-Stack #2402 / run `33381857813` passed all repository-audit steps.

## Boundary

MEMORY_TO_ROOT baseline remains 22 during Repair273. Expected post-repair cohort observation is 21; baseline normalization is forbidden here and may occur only in a separate successor lease if the sole Internal-ID incompleteness is deterministic cohort-count drift.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
