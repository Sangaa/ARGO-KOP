# Priority 7 — CORE-003 ↔ ARC-011 Registry Reconciliation — Transaction M

Date: 2026-09-01
State: `FUNCTIONAL-CLOSED / RECOVERY-VERIFIED / CI-VERIFIED / RESUME-SAFE / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-REGISTRY-M`
Work Lease: `HERMUZ-P7-M-CORE003-ARC011-20260901`
Entry HEAD: `59a1762dea1c734ecd5c3ce7e36811f2612dbe23`
Pre-write Matrix HEAD: `9d101de25f8d37060d2b0aa84f6267fd7b882bac`
Failed material candidate: `7ddb174f34019239e1806f8d724be02bc1309ed0`
Failure evidence commit: `6433e8c6246cbb547b66d54c967019e51f845640`
Recovery pre-write Matrix HEAD: `e35133cca707060b5dee9c9bdfbba21970a26cf1`
Recovery material HEAD: `ee8d7203f1a22ba6377b079f8f5b78bc018f73c1`

## Closed result

REP-014 v1.2.12 now registers exactly:

`REL-068 | CORE-003 | ARC-011 | GOVERNS`

`REL-069 | ARC-011 | CORE-003 | REFERENCES`

The current control-plane manifest and Core status are synchronized. CORE-003 and ARC-011 source content remain unchanged. The two directions retain different controlled semantics and are not promoted to dependency.

## Failure preserved and recovered

The first candidate passed M2 (`33519622054`), Real Mutation Matrix (`33519622023`) and Full-Stack (`33519622141`) but Runtime/Integration `33519622061` failed its integrity job while prototype and integration jobs succeeded. Failure Evidence 01 records the root cause as a case-sensitive test-assertion drift introduced while rebinding the focused regression.

R1 restored Transaction-L's already-proven exact source assertions and retained M's exact REL-068/069 plus anti-overpromotion checks. No source or relationship semantics were changed to make the test pass.

## Recovery exact-head CI

On `ee8d7203f1a22ba6377b079f8f5b78bc018f73c1`:

- Real Mutation Matrix Regression — `33519844866` — SUCCESS.
- M2 Multi-Channel Proposal Training — `33519844829` — SUCCESS.
- Full-Stack Repository Audit — `33519844737` — SUCCESS.
- ARGO Runtime Prototype and Integration Tests — `33519844787` — SUCCESS; integrity, prototype and integration jobs all succeeded.

Result: `4/4 REQUIRED WORKFLOWS SUCCESS AFTER GOVERNED RECOVERY`.

## Learning retained

1. Bidirectionality does not imply semantic symmetry: independently evidenced edges may validly be `GOVERNS` one way and `REFERENCES` the other.
2. During registry-only conversion, preserve previously proven exact source assertions unless source evidence changed. Rephrasing an assertion can manufacture test drift unrelated to the material semantics under reconciliation.
3. A failed gate is evidence, not noise: M was not closed until failure was preserved, root cause classified, recovery pre-authorized, and the repaired exact HEAD passed the complete required workflow set.

## Non-claims

No dependency promotion; no source-authority mutation; no Core/Architecture certification; no Phase-1 closure; no Connected Baseline or repository-wide graph closure; no Global PASS.

## Session close / resume-safe checkpoint

Transaction M and recovery R1 are closed/resume-safe. Parent Work Lease CLOSED. Priority 7 remains OPEN.

A future continuation must rediscover live main and recompute the remaining Priority-7 queue from current evidence. No historical NEXT statement grants mutation authority.
