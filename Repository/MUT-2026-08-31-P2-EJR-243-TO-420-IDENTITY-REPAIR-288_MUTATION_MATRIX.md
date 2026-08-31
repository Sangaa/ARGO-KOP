# MUTATION MATRIX — EJR-243 → EJR-420 IDENTITY REPAIR 288

Status: PREWRITE / FUNCTIONAL EXECUTION AUTHORIZED AFTER FRESH HARD GATE
Transaction ID: MUT-2026-08-31-P2-EJR-243-TO-420-IDENTITY-REPAIR-288
Opening main: `e3574912aa3502de7c070d7df084df9b783e8420`
Execution role: HERMUZ

## Authority

Lease287 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE: earlier Memory EJR-243 is RETAINED; later root EJR-243 is DISPLACED legitimate content; EJR-420 is VACANT across complete reachable history and reserved solely for this repair.

Vacancy evidence: run `33394503875`, artifact `9758767482`, digest `sha256:fb3f6e3047c63c0db05f655a201d168157bdb9e10c32c6e30f0d151ddd7cf22c`, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT.

## Fresh hard gate

- live main `e3574912aa3502de7c070d7df084df9b783e8420`;
- source root EJR-243 present, blob `42fefd5ac581c1c908dd089e38b58cbd897b27cb`;
- retained Memory EJR-243 present, blob `288971ce83c7b4e0749754b0952dc2bcd4dc4d7c`;
- target `EJR/EJR-420_2026-08-17_GENERATIVE_KNOWLEDGE_TEST_CONTRACT.md` absent;
- fresh exact old-member-path search returned zero current consumers.

## Authorized mutation

1. retain `Memory/Engineering_Journal/EJR-243_2026-08-15_P61_SESSION_CLOSURE.md` byte-for-byte;
2. remove `EJR/EJR-243_2026-08-17_GENERATIVE_KNOWLEDGE_TEST_CONTRACT.md`;
3. create `EJR/EJR-420_2026-08-17_GENERATIVE_KNOWLEDGE_TEST_CONTRACT.md`;
4. change only first H1 `# EJR-243 — ...` → `# EJR-420 — ...`;
5. preserve all remaining body/date/status/evidence byte-for-byte;
6. zero consumer rewrites.

MEMORY_TO_ROOT baseline remains 17 during Repair288. Expected post-repair observation is 16; any normalization requires a separate successor lease and exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
