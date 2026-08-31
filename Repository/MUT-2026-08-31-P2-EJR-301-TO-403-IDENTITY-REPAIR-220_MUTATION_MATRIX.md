# Mutation Matrix — Lease220

Status: OPEN / PREWRITE
Lease: `Repository/MUT-2026-08-31-P2-EJR-301-TO-403-IDENTITY-REPAIR-220.md`
Baseline: `a52f3902690e28933de7f61977da6298921b55b6`

| Surface | Before | Authorized after | Boundary |
|---|---|---|---|
| root EJR-301 GT-040 | displaced identity | removed | one-record repair |
| root EJR-403 GT-040 | absent | created with same semantic body/chronology | H1 identity change only |
| Memory EJR-301 | retained earlier allocation | unchanged | protected |
| REP-021 GT-040 | points to root EJR-301 learning record | points to root EJR-403 learning record | direct governed consumer only |
| census/analyzers/tests | current / expected 33 | unchanged | drift must surface honestly |
| other REP authority | current | unchanged | no cosmetic sync |

Exit requires read-back, old-path absence, exact-head Internal-ID plus applicable regressions, and artifact inspection. Any 33→32 cohort rebaseline requires separate successor authority.
