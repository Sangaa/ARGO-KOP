# MUTATION MATRIX — EJR-236 → EJR-417 IDENTITY REPAIR 279

Status: PREWRITE / FUNCTIONAL EXECUTION AUTHORIZED AFTER FRESH HARD GATE
Transaction ID: MUT-2026-08-31-P2-EJR-236-TO-417-IDENTITY-REPAIR-279
Opening main: `b6a7050d5290e059580287c971671d6a84c33562`
Execution role: HERMUZ

## Authority

Lease278 is CLOSED / EXECUTION-VERIFIED / RESUME-SAFE: earlier Memory EJR-236 is RETAINED; later root EJR-236 is DISPLACED legitimate content; EJR-417 is VACANT across complete reachable history and reserved solely for this repair.

Vacancy evidence: run `33386421955`, artifact `9755737419`, digest `sha256:253af9f9654868e2908a1f2f9beb5e3f456c0aaa87b623b4d79e74770107dcdf`, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT.

## Fresh hard gate

Immediately before mutation recheck live main, source blob, retained Memory blob, target absence, and exact old-member-path consumers. Abort if any contradictory evidence appears.

## Authorized mutation

1. retain `Memory/Engineering_Journal/EJR-236_2026-08-14_P54_SESSION_CLOSURE.md` byte-for-byte;
2. remove `EJR/EJR-236_2026-08-17_P4_REL009_CONSUMER_BOUNDARY_GATE.md`;
3. create `EJR/EJR-417_2026-08-17_P4_REL009_CONSUMER_BOUNDARY_GATE.md`;
4. change only first H1 `# EJR-236 — ...` → `# EJR-417 — ...`;
5. preserve all remaining body/date/status/evidence byte-for-byte;
6. zero consumer rewrites unless a fresh executable/governed exact-path consumer appears.

MEMORY_TO_ROOT baseline remains 20 during Repair279. Expected post-repair observation is 19; normalization requires a separate successor lease and exact artifact proof that cohort-count drift is the sole incompleteness.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
