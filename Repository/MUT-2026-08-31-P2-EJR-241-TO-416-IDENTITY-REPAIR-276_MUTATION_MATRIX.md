# MUTATION MATRIX — EJR-241 → EJR-416 IDENTITY REPAIR 276

Status: PREWRITE / FUNCTIONAL EXECUTION AUTHORIZED AFTER FRESH HARD GATE
Transaction ID: MUT-2026-08-31-P2-EJR-241-TO-416-IDENTITY-REPAIR-276
Opening main: `9e6322ea9e204b004d49df36f62ba8fc32f51576`
Execution role: HERMUZ

## Authority

Lease275 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE: earlier Memory EJR-241 is RETAINED; later root EJR-241 is DISPLACED legitimate content; EJR-416 is VACANT across complete reachable history and reserved solely for this repair.

Vacancy evidence: run `33384024659`, artifact `9754849239`, digest `sha256:5eb4c19afb1976fbce08fdeabce50a1baaaa9d7eb0ffc4b00db54a4affed30d2`, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT.

## Fresh hard gate

At opening main the target root EJR-416 path is absent and fresh exact old-member-path search returns zero consumers. Immediately before mutation, live main, source blob, retained Memory blob, target absence and consumer evidence must be rechecked.

## Authorized mutation

1. retain `Memory/Engineering_Journal/EJR-241_2026-08-15_P59_SESSION_CLOSURE.md` byte-for-byte;
2. remove `EJR/EJR-241_2026-08-17_MATRIX_VARIANT_REPEAT_VALIDATION.md`;
3. create `EJR/EJR-416_2026-08-17_MATRIX_VARIANT_REPEAT_VALIDATION.md`;
4. change only first H1 `# EJR-241 — ...` → `# EJR-416 — ...`;
5. preserve all remaining body/date/status/evidence byte-for-byte;
6. zero consumer rewrites unless a fresh executable/governed exact-path consumer appears.

## Boundary

MEMORY_TO_ROOT baseline remains 21 during Repair276. Expected post-repair observation is 20; any baseline normalization must occur only in a separate successor lease if the sole Internal-ID incompleteness is deterministic cohort-count drift.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
