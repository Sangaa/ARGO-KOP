# RECOVERY MUTATION MATRIX — P7 CORE-003 ↔ ARC-011 REGISTRY M / FAILURE-01

Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M-R1`
Parent Work Lease: `HERMUZ-P7-M-CORE003-ARC011-20260901`
State: `CLOSED / RECOVERY-VERIFIED / CI-VERIFIED / RESUME-SAFE`
Recovery entry HEAD: `6433e8c6246cbb547b66d54c967019e51f845640`
Recovery pre-write Matrix HEAD: `e35133cca707060b5dee9c9bdfbba21970a26cf1`
Failed candidate: `7ddb174f34019239e1806f8d724be02bc1309ed0`
Recovery material HEAD: `ee8d7203f1a22ba6377b079f8f5b78bc018f73c1`
Failure evidence: `Repository/P7_CORE003_ARC011_REGISTRY_RECONCILIATION_2026-09-01_M_FAILURE_01.md`

## Recovery result

R1 changed only the focused integrity test plus transaction/matrix evidence. It restored the already-proven exact source assertions while retaining M's exact REL-068/069 registry checks and anti-overpromotion boundaries. REP-014, manifest, Core status, CORE-003 and ARC-011 were not changed by the recovery.

Exact-head recovery workflows:

- Real Mutation Matrix `33519844866` — SUCCESS.
- M2 `33519844829` — SUCCESS.
- Full-Stack `33519844737` — SUCCESS.
- Runtime/Integration `33519844787` — SUCCESS, including integrity-tests.

Recovery principle satisfied: `FIX THE TEST DEFECT, NOT THE EVIDENCE`.

Recovery Lease: `CLOSED / RESUME-SAFE`.
