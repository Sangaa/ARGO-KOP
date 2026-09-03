# P9 Architecture — Canonical Model Alignment Gate 8 Closure — Transaction I

Transaction ID: `MUT-2026-09-03-P9-ARCHITECTURE-GATE8-CLOSE-I`
Priority: `9 — Architecture`
State: `HARD HOLD / CLOSURE-HEAD RUNTIME FAILURE / REPAIR REQUIRED`
Entry HEAD: `9eb03a67083ea5ea2b35d6709373cd2e9fc077fd`
Pre-write Matrix HEAD: `9295ee7d4760ba54316859de97460cf4a6094456`
Material HEAD: `e7b1313f30dc27c467936e3560d2e5e33d11a4ff`
First Closure HEAD: `8390a05fb9421c7379a647126d3d65daea66289f`
Target: `Architecture/_FOLDER_STATUS.md`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Gate | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|---|
| `8. Canonical Architecture Model alignment` | Promote only Gate 8 from OPEN to PASS for the current active primary ARC set and Architecture navigation/handbook surfaces | Gates 4,6,7,9,10,11,12,13 remain OPEN; Architecture remains INTEGRITY HOLD; no repository/global closure | PASS | PASS |

Verification before closure-head failure:
- Immutable material read-back: `_FOLDER_STATUS.md` blob `dac074d80d72346cf42dffe680f1eccc8fada122`.
- Exact compare `9295ee7d… → e7b1313f…`: one material commit, one target path, 31 additions / 10 deletions.
- Material-head CI: Full-Stack Repository Audit run `33717012048` = SUCCESS; M2 run `33717012078` = SUCCESS.
- Architecture remains INTEGRITY HOLD; Gates 4,6,7,9,10,11,12,13 remain explicitly OPEN; no Architecture partition/global closure claimed.

Closure-head failure classification:
- First closure HEAD `8390a05f…` dispatched all four workflow families.
- Full-Stack run `33717053808` = SUCCESS.
- Real Mutation Matrix run `33717053833` = SUCCESS.
- M2 run `33717053837` = SUCCESS.
- Runtime/Integration run `33717053853` = FAILURE; only `integrity-tests` failed while integration/prototype jobs passed.
- Direct test evidence in `Quality/Integrity/test_architecture_readme_authority_boundary.py` shows a stale regression assertion requiring `Canonical Architecture Model alignment — OPEN` even after this transaction legitimately changed Gate 8 to PASS. The same test also hard-codes older bounded-consumer marker wording.
- The gate closure itself is therefore preserved pending a bounded regression-contract repair; the test is not weakened to ignore Architecture hold/global-certification constraints.

Disposition:
`FAIL → PRESERVE GATE-8 MATERIAL → CLASSIFY STALE REGRESSION CONTRACT → REPAIR SMALLEST TEST BOUNDARY → READ-BACK → VERIFY`.
