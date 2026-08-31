# Mutation Matrix — Lease221

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Lease: `Repository/MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-221.md`
Baseline: `a78bf0dd8760b036656515c39378261a1c0a2a09`
Prewrite: `a17f6109283387a29f1eca79babd8d5d5e41eaaa`
Functional head: `bab2d672773a633e404213d02f6ed9bf458d1c78`

| Surface | Executed | Result |
|---|---|---|
| memory→root census baseline | yes | expected 33→32 only |
| classifier-derived membership | NO | 32 groups dynamically selected |
| drift failure semantics | NO | fail-closed behavior preserved |
| EJR-301/EJR-403 + REP-021 | NO | Lease220 post-repair state preserved |
| tests/scanner/workflow logic | NO | unchanged |
| REP authority | NO | no promotion |

Exact-head Internal-ID `33357346467`, Full-Stack `33357346484`, Runtime `33357346422`, and M2 `33357346457` all succeeded. Artifact `9745556033` proves 32/32, CENSUSED, history/classification complete, incomplete=[]. Real Matrix is NOT APPLICABLE to the census-only functional diff; closure Matrix synchronization is its applicable regression point.
