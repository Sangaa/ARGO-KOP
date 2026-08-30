# MUTATION MATRIX — P2 EJR H1 PAIR CHRONOLOGY — 197

Status: `FUNCTIONAL CANDIDATE / APPLIED PENDING EXACT-HEAD VERIFICATION`
Transaction: `MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197`
Lease: `R71-20260830-P2-EJR-H1-PAIR-CHRONOLOGY-197`

| Path | Prewrite | Functional authorization | Applied effect |
|---|---|---|---|
| `Repository/MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197.md` | CREATE | documentation only | unchanged after prewrite |
| `Repository/MUT-2026-08-30-P2-EJR-H1-PAIR-CHRONOLOGY-197_MUTATION_MATRIX.md` | CREATE | UPDATE | functional accounting state |
| `Quality/Integration/ejr_h1_pair_chronology.py` | — | CREATE | exact-path chronology evidence classifier |
| `Quality/Integration/test_ejr_h1_pair_chronology.py` | — | CREATE | ancestor/same-commit/missing/shallow regression coverage |
| `.github/workflows/internal-id-audit.yml` | — | UPDATE | execute chronology tests/report and upload artifact |

## Preserved boundaries

No EJR file changed. No `REP-012`, `REP-016`, or `REP-020` changed. Internal Document-ID scanner is untouched. No identity migration, rename, deletion, reassignment, normalization, suppression, or allocation is authorized or performed.

Chronology is explicitly scoped to exact current path names across all locally reachable refs. It is not rename-lineage proof and is not canonical ownership authority.

## Verification requirements

- exact changed-path set = analyzer + tests + workflow + this Matrix;
- shallow history returns `HISTORY_INCOMPLETE` and no groups;
- missing path history returns `PARTIAL` rather than inferred precedence;
- exact-head Internal Document-ID Audit succeeds and uploads `ejr-h1-pair-chronology`;
- exact-head Full-Stack, Runtime, M2, and Real Mutation Matrix runs are observed;
- artifact content is inspected before lease closure.
