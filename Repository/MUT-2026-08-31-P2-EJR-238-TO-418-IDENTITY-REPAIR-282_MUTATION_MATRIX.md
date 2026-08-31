# MUTATION MATRIX — EJR-238 → EJR-418 IDENTITY REPAIR 282

Status: PREWRITE / FUNCTIONAL EXECUTION AUTHORIZED AFTER FRESH HARD GATE
Transaction ID: MUT-2026-08-31-P2-EJR-238-TO-418-IDENTITY-REPAIR-282
Opening main: `b993e0640453c1a433572a86b8f9fe53005f9e28`
Execution role: HERMUZ

## Authority

Lease281 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE: earlier Memory EJR-238 is RETAINED; later root EJR-238 is DISPLACED legitimate content; EJR-418 is VACANT across complete reachable history and reserved solely for this repair.

Vacancy evidence: run `33388096524`, artifact `9756351209`, digest `sha256:2f5675402cdab0cd6a0dfe7fa7050964f57fbe7b2510291ca5701f5ba3c3119e`, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT.

## Fresh hard gate

Immediately before mutation recheck live main, source blob, retained Memory blob, target absence, and exact old-member-path consumers. Abort if contradictory evidence appears.

## Authorized mutation

1. retain `Memory/Engineering_Journal/EJR-238_2026-08-15_P56_SESSION_CLOSURE.md` byte-for-byte;
2. remove `EJR/EJR-238_2026-08-17_P322_RECONCILIATION_UPDATE.md`;
3. create `EJR/EJR-418_2026-08-17_P322_RECONCILIATION_UPDATE.md`;
4. change only first H1 `# EJR-238 — ...` → `# EJR-418 — ...`;
5. preserve all remaining body/date/status/evidence byte-for-byte;
6. zero consumer rewrites because fresh pre-disposition exact-member-path search found no current consumer.

MEMORY_TO_ROOT baseline remains 19 during Repair282. Expected post-repair observation is 18; normalization requires a separate successor lease and exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
