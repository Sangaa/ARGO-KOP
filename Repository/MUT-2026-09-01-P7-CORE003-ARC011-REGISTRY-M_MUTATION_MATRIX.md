# MUTATION MATRIX — P7 CORE-003 ↔ ARC-011 REGISTRY RECONCILIATION — M

Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M`
Work Lease: `HERMUZ-P7-M-CORE003-ARC011-20260901`
Priority: `7 — Core cross-layer validation`
State: `RECOVERY-CANDIDATE / LEASE ACTIVE / CI-PENDING`
Entry HEAD: `59a1762dea1c734ecd5c3ce7e36811f2612dbe23`
Pre-write Matrix HEAD: `9d101de25f8d37060d2b0aa84f6267fd7b882bac`
Failed candidate: `7ddb174f34019239e1806f8d724be02bc1309ed0`
Failure evidence: `Repository/P7_CORE003_ARC011_REGISTRY_RECONCILIATION_2026-09-01_M_FAILURE_01.md`
Recovery pre-write Matrix HEAD: `e35133cca707060b5dee9c9bdfbba21970a26cf1`
Protocol: `GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Reconstructed legal action

REP-016 places Core as the first open Phase-1 partition. Transaction L directly validated `CORE-003 → ARC-011 = GOVERNS` and `ARC-011 → CORE-003 = REFERENCES`. M reconciles exactly those edges into REP-014.

## Material result already applied

The first candidate atomically updated REP-014 to v1.2.12 with REL-068/069, synchronized the current control-plane manifest, Core status and focused regression, and added transaction evidence. Its diff was limited to the six authorized paths. Three required workflows succeeded, but Runtime/Integration failed its integrity job because the newly rebound focused test changed a previously proven exact source assertion into a case-sensitive paraphrase.

The failed candidate is retained and not promoted.

## Recovery authorization

R1 is governed by `Repository/MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M_RECOVERY_MATRIX.md` and may change only the focused test plus transaction/matrix evidence. It must fix the test assertion, not alter source evidence or relationship semantics.

## KEEP / non-authority

- No mutation to CORE-003 or ARC-011.
- No dependency/runtime/executable promotion.
- No reversal of governing direction.
- No Core/Architecture certification or Phase-1/Connected-Baseline/Global closure.
- Failure Evidence 01 remains immutable evidence.

## Verification contract

`FAILURE PRESERVED → RECOVERY PRE-WRITE MATRIX → ONE ATOMIC RECOVERY COMMIT → EXACT-HEAD READ-BACK → DIFF SCOPE CHECK → REQUIRED CI/RUNTIME/INTEGRITY → LEARNING CAPTURE → LEASE CLOSE → CLOSURE-HEAD CI`
