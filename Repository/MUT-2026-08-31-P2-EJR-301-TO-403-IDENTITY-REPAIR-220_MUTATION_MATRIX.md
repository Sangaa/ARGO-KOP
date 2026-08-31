# Mutation Matrix — Lease220

Status: CLOSED / SUCCESSOR-VERIFIED / RESUME-SAFE
Lease: `Repository/MUT-2026-08-31-P2-EJR-301-TO-403-IDENTITY-REPAIR-220.md`
Baseline: `a52f3902690e28933de7f61977da6298921b55b6`
Prewrite: `d3c5e7931228d0d4f7c86848843792864424d8bb`
Functional head: `a78bf0dd8760b036656515c39378261a1c0a2a09`
Successor: Lease221

| Surface | Executed | Result |
|---|---|---|
| root EJR-301 GT-040 | yes | removed as displaced later identity |
| root EJR-403 GT-040 | yes | created; semantic body/chronology preserved; H1 identity changed |
| Memory EJR-301 | NO | retained earlier valid allocation |
| REP-021 GT-040 | yes | direct governed learning-record reference moved to EJR-403 in same transaction |
| census/analyzers/tests | NO | expected 33 intentionally preserved in repair lease |
| other REP authority | NO | no cosmetic sync |

Functional-head Full-Stack, Runtime, and M2 passed. Internal-ID failed only on the expected 33→32 drift guard; artifacts proved EJR-301/EJR-403 no longer ambiguous. Lease221 separately restored the proven baseline to 32 and passed exact-head Internal-ID. Real Matrix non-trigger on the functional diff is NOT APPLICABLE.
