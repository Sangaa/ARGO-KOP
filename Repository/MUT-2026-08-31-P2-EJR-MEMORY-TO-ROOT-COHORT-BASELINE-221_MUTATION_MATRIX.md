# Mutation Matrix — Lease221

Status: OPEN / PREWRITE
Lease: `Repository/MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-221.md`
Baseline: `a78bf0dd8760b036656515c39378261a1c0a2a09`

| Surface | Before | Authorized after | Boundary |
|---|---|---|---|
| memory→root census baseline | expected 33 / observed 32 | expected 32 / observed 32 | one-line rebaseline only |
| classifier-derived membership | 32 observed groups | unchanged | dynamic selection preserved |
| drift failure semantics | fail when observed != expected | unchanged | must remain fail-closed |
| EJR-301/EJR-403 + REP-021 | Lease220 post-repair state | unchanged | no identity/consumer mutation |
| tests / scanner / workflow logic | current | unchanged | no weakening |
| REP authority surfaces | current | unchanged | no promotion |

Exit requires exact-head Internal-ID SUCCESS and deterministic 32/32 CENSUSED artifact plus applicable regressions. Real Matrix path-filter non-trigger on census-only diff is NOT APPLICABLE, not PASS/FAIL.
