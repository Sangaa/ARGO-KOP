# P9 Architecture — Gate-8 Runtime Regression Contract Repair — Transaction I-C1

Transaction ID: `MUT-2026-09-03-P9-GATE8-RUNTIME-REGRESSION-I-C1`
Priority: `9 — Architecture`
Parent Transaction: `MUT-2026-09-03-P9-ARCHITECTURE-GATE8-CLOSE-I`
State: `PRE-WRITE / REPAIR TARGET NOT YET APPLIED`
Entry HEAD: `a30fc0780dadda98fbaff299bb2a66f7674fd083`
Target: `Quality/Integrity/test_architecture_readme_authority_boundary.py`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Repair | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|---|
| stale Gate-8 regression expectation | Replace obsolete requirement that Gate 8 remain OPEN with the new bounded PASS marker; replace obsolete exact consumer-marker strings with current bounded evidence markers | Continue asserting Architecture INTEGRITY HOLD, no registry promotion, no global Architecture certification, Core closure separation, and unchanged forbidden REP-014 relationships | PASS | PENDING |

Failure evidence:
- Parent first closure HEAD `8390a05f…`: Runtime run `33717053853` failed only the integrity test job; prototype and integration jobs passed.
- Direct current test content requires `Canonical Architecture Model alignment — OPEN`, which contradicts the evidence-backed Gate-8 status transition performed by the parent transaction.
- The test's purpose is to prevent Core closure or README alignment from silently certifying Architecture or inventing relationships; Gate-8 bounded closure does neither.

Repair boundary:
- Do not alter production Architecture semantics.
- Do not remove Architecture HOLD/global-certification safeguards.
- Do not change forbidden relationship assertions.
- Do not broadly refactor the test suite.

Validation plan:
`immutable test read-back → exact compare → exact-head Runtime + required CI → parent transaction close or preserve failure`.
