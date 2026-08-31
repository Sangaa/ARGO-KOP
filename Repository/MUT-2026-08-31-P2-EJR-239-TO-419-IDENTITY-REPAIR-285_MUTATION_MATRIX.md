# MUTATION MATRIX — EJR-239 → EJR-419 IDENTITY REPAIR 285

Status: PREWRITE / FUNCTIONAL EXECUTION AUTHORIZED AFTER FRESH HARD GATE
Transaction ID: MUT-2026-08-31-P2-EJR-239-TO-419-IDENTITY-REPAIR-285
Opening main: `c5165a375a3cd72671ee7d0062fb3c17dd43e133`
Execution role: HERMUZ

## Authority

Lease284 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE: earlier Memory EJR-239 is RETAINED; later root EJR-239 is DISPLACED legitimate content; EJR-419 is VACANT across complete reachable history and reserved solely for this repair.

Vacancy evidence: run `33390427316`, artifact `9757215042`, digest `sha256:66ef8d95b28ceab9d491b70d87a3b071ceb93cb4c3903a38c6c5db848c2138b9`, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT.

## Fresh hard gate

- live main `c5165a375a3cd72671ee7d0062fb3c17dd43e133`;
- source root EJR-239 present, blob `4d707cad5da6e9d6de4a7b4b02f32580c37f459a`;
- retained Memory EJR-239 present, blob `e2ff8422e5d3abf1dae5d59a8aa0052f27ec1e96`;
- target `EJR/EJR-419_2026-08-17_P1_MUTATION_MATRIX_PREFLIGHT.md` absent;
- fresh exact old-member-path search returned zero current consumers.

## Authorized mutation

1. retain `Memory/Engineering_Journal/EJR-239_2026-08-15_P57_SESSION_CLOSURE.md` byte-for-byte;
2. remove `EJR/EJR-239_2026-08-17_P1_MUTATION_MATRIX_PREFLIGHT.md`;
3. create `EJR/EJR-419_2026-08-17_P1_MUTATION_MATRIX_PREFLIGHT.md`;
4. change only first H1 `# EJR-239 — ...` → `# EJR-419 — ...`;
5. preserve all remaining body/date/status/evidence byte-for-byte;
6. zero consumer rewrites.

MEMORY_TO_ROOT baseline remains 18 during Repair285. Expected post-repair observation is 17; any normalization requires a separate successor lease and exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
