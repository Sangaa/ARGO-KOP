# P9 Architecture — Canonical Model Alignment Gate 8 Closure — Transaction I

Transaction ID: `MUT-2026-09-03-P9-ARCHITECTURE-GATE8-CLOSE-I`
Priority: `9 — Architecture`
State: `CLOSED / VERIFIED / REPAIRED AFTER STALE REGRESSION / RESUME-SAFE IFF THIS FINAL CLOSURE HEAD PASSES`
Entry HEAD: `9eb03a67083ea5ea2b35d6709373cd2e9fc077fd`
Pre-write Matrix HEAD: `9295ee7d4760ba54316859de97460cf4a6094456`
Material HEAD: `e7b1313f30dc27c467936e3560d2e5e33d11a4ff`
First Closure HEAD: `8390a05fb9421c7379a647126d3d65daea66289f`
Repair Matrix HEAD: `1c3b33af45b6b34f83283122601606705e2fc316`
Repair Material HEAD: `53f1b057b6860573c6a332a391e1c6945c6d21c2`
Repair Closure HEAD: `5d3443453301e6a6cf17a18f44e9b73f64f6b38e`
Target: `Architecture/_FOLDER_STATUS.md`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Gate | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|---|
| `8. Canonical Architecture Model alignment` | Promote only Gate 8 from OPEN to PASS for the current active primary ARC set and Architecture navigation/handbook surfaces | Gates 4,6,7,9,10,11,12,13 remain OPEN; Architecture remains INTEGRITY HOLD; no repository/global closure | PASS | PASS |

Verification:
- Immutable Gate-8 material read-back: `_FOLDER_STATUS.md` blob `dac074d80d72346cf42dffe680f1eccc8fada122`.
- Exact Gate-8 compare `9295ee7d… → e7b1313f…`: one material commit, one target path, 31 additions / 10 deletions.
- Initial material-head Full-Stack run `33717012048` = SUCCESS; M2 run `33717012078` = SUCCESS.
- First closure HEAD `8390a05f…`: Full-Stack `33717053808` SUCCESS; Real Matrix `33717053833` SUCCESS; M2 `33717053837` SUCCESS; Runtime `33717053853` FAILURE only in integrity-tests.
- Failure was preserved and classified as a stale regression contract requiring Gate 8 to remain OPEN.
- Repair Transaction I-C1 changed only `Quality/Integrity/test_architecture_readme_authority_boundary.py`, preserving Architecture HOLD, no-global-certification, no-registry-promotion and forbidden relationship safeguards.
- Repair material `53f1b057…`: read-back blob `c9b56afac114973ad7c4890e2a3e4746d981d5d2`; exact compare one test target, 4 additions / 3 deletions; Full-Stack `33717235860` SUCCESS; Runtime `33717235869` SUCCESS; M2 `33717235852` SUCCESS.
- No Architecture partition closure, Global Connected Baseline closure, or Global Integrity PASS is claimed.

Disposition:
`GATE 8 CLOSED / STALE REGRESSION REPAIRED / FINAL CLOSURE-HEAD VERIFICATION REQUIRED`.
