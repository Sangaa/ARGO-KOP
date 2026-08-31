# MUTATION MATRIX — EJR-244 → EJR-421 IDENTITY REPAIR 291

Status: PREWRITE / FUNCTIONAL EXECUTION AUTHORIZED AFTER FRESH HARD GATE
Transaction ID: MUT-2026-08-31-P2-EJR-244-TO-421-IDENTITY-REPAIR-291
Opening main: `eff63514babc30c3d0805bac18f31316601676c6`
Execution role: HERMUZ

## Authority

Lease290 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE: earlier Memory EJR-244 is RETAINED; later root EJR-244 is DISPLACED legitimate content; EJR-421 is VACANT across complete reachable history and reserved solely for this repair.

Vacancy evidence: run `33396768282`, artifact `9759617449`, digest `sha256:28a790a1c1bf3a3a4425602426ea3351be2f09c4c469add1e21723970a55d96c`, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT.

## Fresh hard gate

- live main `eff63514babc30c3d0805bac18f31316601676c6`;
- source root EJR-244 present, blob `4c62b2f8b9151255a87d83c87829f3bafe1c0f54`;
- retained Memory EJR-244 present, blob `2fe0ad5eabfb708f7fd1c931156f96c250d425cf`;
- target `EJR/EJR-421_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md` absent;
- verified census reports zero exact-member-path consumers for both EJR-244 members.

## Authorized mutation

1. retain `Memory/Engineering_Journal/EJR-244_2026-08-15_P62_SESSION_CLOSURE.md` byte-for-byte;
2. remove `EJR/EJR-244_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md`;
3. create `EJR/EJR-421_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md`;
4. change only first H1 `# EJR-244 — ...` → `# EJR-421 — ...`;
5. preserve all remaining body/date/status/evidence byte-for-byte;
6. zero consumer rewrites;
7. perform source deletion and successor creation in one Git tree/commit mutation to avoid an intermediate duplicate identity state.

MEMORY_TO_ROOT baseline remains 16 during Repair291. Expected post-repair observation is 15; any normalization requires a separate successor lease and exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
