# MUTATION MATRIX — P7 CORE-003 ↔ ARC-011 REGISTRY RECONCILIATION — M

Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M`
Work Lease: `HERMUZ-P7-M-CORE003-ARC011-20260901`
Priority: `7 — Core cross-layer validation`
State: `CLOSED / RECOVERY-VERIFIED / CI-VERIFIED / RESUME-SAFE`
Entry HEAD: `59a1762dea1c734ecd5c3ce7e36811f2612dbe23`
Pre-write Matrix HEAD: `9d101de25f8d37060d2b0aa84f6267fd7b882bac`
Failed candidate: `7ddb174f34019239e1806f8d724be02bc1309ed0`
Failure evidence: `Repository/P7_CORE003_ARC011_REGISTRY_RECONCILIATION_2026-09-01_M_FAILURE_01.md`
Recovery pre-write Matrix HEAD: `e35133cca707060b5dee9c9bdfbba21970a26cf1`
Recovery material HEAD: `ee8d7203f1a22ba6377b079f8f5b78bc018f73c1`
Protocol: `GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Closed material result

REP-014 v1.2.12 contains REL-068 `CORE-003 → ARC-011 = GOVERNS` and REL-069 `ARC-011 → CORE-003 = REFERENCES`; current manifest and Core status are synchronized. No source-authority document was changed.

The initial material candidate failed one required integrity job due a focused-test case-sensitive assertion drift. Failure was preserved and governed recovery R1 repaired only the test/evidence bindings.

Recovery exact-head `ee8d720...` passed all four required workflows: Real Mutation Matrix `33519844866`, M2 `33519844829`, Full-Stack `33519844737`, Runtime/Integration `33519844787`.

## KEEP / non-authority

- No mutation to CORE-003 or ARC-011.
- No dependency/runtime/executable promotion.
- No reversal of governing direction.
- No Core/Architecture certification or Phase-1/Connected-Baseline/Global closure.
- Failure Evidence 01 remains preserved.

Work Lease disposition: `CLOSED / RESUME-SAFE`.
