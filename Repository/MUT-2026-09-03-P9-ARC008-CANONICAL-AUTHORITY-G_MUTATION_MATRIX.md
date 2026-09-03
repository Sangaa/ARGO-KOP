# P9 Architecture — ARC-008 Canonical Authority Correction — Transaction G

Transaction ID: `MUT-2026-09-03-P9-ARC008-CANONICAL-AUTHORITY-G`
Priority: `9 — Architecture`
State: `FUNCTIONAL CLOSED / TARGET EXACT-HEAD GREEN / RESUME-SAFE IFF THIS CLOSURE HEAD PASSES`
Entry HEAD: `15c924a3384ca5bc111f0e5fe47986394ca4acd3`
Pre-write Matrix HEAD: `d3ec1dc1e00a4cf248e3a0ff4e60833c0546d47e`
Material HEAD: `2daf75a1f15328db7330b50df67ba410e3c303f1`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Target | Action | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|---|
| `Architecture/ARC-008_REPOSITORY_LAYOUT.md` | bounded stale-authority correction | Replace stale statement that active architecture is represented by ARC-001 with current canonical ARC-011 authority; retain ARC-001 as platform architecture surface; add ARC-011 Related Document; refresh audit/version minimally | Repository-layout principles, physical-vs-logical distinction, nine-layer model, Repository authority, connected-baseline hold | PASS | PASS |

Verification:
- Immutable target read-back at material HEAD: blob `fd5817ebfa785c7f0d991698c98ef544ccae31f2`.
- Exact compare `d3ec1dc1… → 2daf75a1…`: one commit, one target path, 8 additions / 5 deletions.
- Material-head CI: Full-Stack Repository Audit run `33716648969` = SUCCESS; M2 run `33716648967` = SUCCESS.
- Runtime / Real Mutation Matrix were not dispatched for the Architecture-only material change and no non-triggered success is claimed.
- ARC-001 remains active; only the competing canonical interpretation was removed.
- No Architecture partition closure, Global Connected Baseline closure, or Global Integrity PASS claimed.

Disposition:
`CLOSED / VERIFIED / RESUME-SAFE SUBJECT TO CLOSURE-HEAD CI`.
