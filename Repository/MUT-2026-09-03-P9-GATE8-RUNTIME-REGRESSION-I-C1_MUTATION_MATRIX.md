# P9 Architecture — Gate-8 Runtime Regression Contract Repair — Transaction I-C1

Transaction ID: `MUT-2026-09-03-P9-GATE8-RUNTIME-REGRESSION-I-C1`
Priority: `9 — Architecture`
Parent Transaction: `MUT-2026-09-03-P9-ARCHITECTURE-GATE8-CLOSE-I`
State: `CLOSED / VERIFIED / TARGET EXACT-HEAD GREEN / RESUME-SAFE IFF THIS CLOSURE HEAD PASSES`
Entry HEAD: `a30fc0780dadda98fbaff299bb2a66f7674fd083`
Pre-write Matrix HEAD: `1c3b33af45b6b34f83283122601606705e2fc316`
Material HEAD: `53f1b057b6860573c6a332a391e1c6945c6d21c2`
Target: `Quality/Integrity/test_architecture_readme_authority_boundary.py`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Repair | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|---|
| stale Gate-8 regression expectation | Replace obsolete requirement that Gate 8 remain OPEN with the new bounded PASS marker; replace obsolete exact consumer-marker strings with current bounded evidence markers | Continue asserting Architecture INTEGRITY HOLD, no registry promotion, no global Architecture certification, Core closure separation, and unchanged forbidden REP-014 relationships | PASS | PASS |

Verification:
- Immutable material read-back blob: `c9b56afac114973ad7c4890e2a3e4746d981d5d2`.
- Exact compare `1c3b33af… → 53f1b057…`: one commit, one test target, 4 additions / 3 deletions.
- Material-head Full-Stack run `33717235860` = SUCCESS.
- Material-head Runtime/Integration run `33717235869` = SUCCESS, proving the previously failing integrity suite now passes without weakening Architecture HOLD/global-certification/registry safeguards.
- Material-head M2 run `33717235852` = SUCCESS.
- Real Mutation Matrix did not dispatch for the test-only material change; no non-triggered success is claimed.

Disposition:
`STALE REGRESSION CONTRACT REPAIRED / VERIFIED / PARENT MAY RESUME`.
