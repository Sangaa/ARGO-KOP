# RECOVERY MUTATION MATRIX — P7 CORE-003 ↔ ARC-011 REGISTRY M / FAILURE-01

Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M-R1`
Parent Work Lease: `HERMUZ-P7-M-CORE003-ARC011-20260901`
State: `RECOVERY-CANDIDATE / RECOVERY LEASE ACTIVE / CI-PENDING`
Recovery entry HEAD: `6433e8c6246cbb547b66d54c967019e51f845640`
Recovery pre-write Matrix HEAD: `e35133cca707060b5dee9c9bdfbba21970a26cf1`
Failed candidate: `7ddb174f34019239e1806f8d724be02bc1309ed0`
Failure evidence: `Repository/P7_CORE003_ARC011_REGISTRY_RECONCILIATION_2026-09-01_M_FAILURE_01.md`

## Authorized recovery

1. `Quality/Integrity/test_core003_arc011_authority_boundary.py` — restore Transaction-L exact CORE-003/ARC-011 source assertions while retaining M's exact REL-068/069 registry assertions and anti-overpromotion checks.
2. `Repository/P7_CORE003_ARC011_REGISTRY_RECONCILIATION_2026-09-01_M.md` — bind failed candidate and recovery state without erasing failure.
3. `Repository/MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M_MUTATION_MATRIX.md` — bind failure/recovery state.
4. This recovery Matrix — rebound in the same recovery material commit.

## Forbidden recovery behavior

- no mutation to CORE-003 or ARC-011;
- no mutation to REP-014, manifest or Core status to make the test pass;
- no relationship semantic change;
- no deletion or rewriting of Failure Evidence 01;
- no closure until recovery exact-head required workflows all succeed.

Recovery principle: `FIX THE TEST DEFECT, NOT THE EVIDENCE`.
