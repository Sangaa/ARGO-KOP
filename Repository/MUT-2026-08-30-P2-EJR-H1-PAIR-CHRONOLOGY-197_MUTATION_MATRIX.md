# MUTATION MATRIX — P2 EJR H1 PAIR CHRONOLOGY — 197

Status: `PREWRITE / OPEN`
Transaction: `MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197`
Lease: `R71-20260830-P2-EJR-H1-PAIR-CHRONOLOGY-197`

| Path | Prewrite | Functional authorization | Intended effect |
|---|---|---|---|
| `Repository/MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197.md` | CREATE | documentation only | lease contract |
| `Repository/MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197_MUTATION_MATRIX.md` | CREATE | UPDATE | mutation accounting |
| `Quality/Integration/ejr_h1_pair_chronology.py` | — | CREATE | evidence-only chronology analyzer |
| `Quality/Integration/test_ejr_h1_pair_chronology.py` | — | CREATE | deterministic regression tests |
| `.github/workflows/internal-id-audit.yml` | — | UPDATE | execute tests/report and upload evidence artifact |

## Forbidden in this transaction

Any EJR file; `REP-012`; `REP-016`; `REP-020`; internal Document-ID scanner semantics; identity migration/renaming/deletion/reassignment/suppression; closure of Priority 2 or broader holds.

## Verification requirements

- exact changed-path set must match authorization;
- complete-history condition must be verified;
- analyzer tests must include fail-closed shallow-history behavior;
- exact-head Internal Document-ID Audit must succeed and emit chronology artifact;
- exact-head Full-Stack, Runtime, M2, and Real Mutation Matrix workflows must be observed;
- evidence artifact must be inspected before closure.
