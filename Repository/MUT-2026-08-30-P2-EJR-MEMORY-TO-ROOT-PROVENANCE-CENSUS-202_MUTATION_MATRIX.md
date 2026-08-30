# Mutation Matrix — Lease 202

Transaction: `MUT-2026-08-30-P2-EJR-MEMORY-TO-ROOT-PROVENANCE-CENSUS-202`
State: `PREWRITE / OPEN`
Baseline: `main@ed0642f9d1fd579f7cf7b39a3c1e5406596a8d8d`

| Path | Action | Allowed | Applied | Verified |
|---|---|:---:|:---:|:---:|
| `Quality/Integration/ejr_memory_to_root_provenance_census.py` | ADD evidence-only cohort census | Y | N | N |
| `Quality/Integration/test_ejr_memory_to_root_provenance_census.py` | ADD regressions | Y | N | N |
| `.github/workflows/internal-id-audit.yml` | wire test/report/artifact | Y | N | N |
| this matrix | synchronize transaction evidence | Y | Y | N |

## Forbidden
- EJR identity/content mutation or migration;
- owner/canonical assignment;
- REP-012/016/020 mutation;
- scanner semantic weakening;
- suppression of ambiguity groups;
- Priority-2 / Phase-1 / global closure or Boot/PASS claim.

## Required gates
1. cohort is derived from namespace-lineage class `MEMORY_TO_ROOT_EJR`;
2. expected group count 36, otherwise `PARTIAL`;
3. complete history required;
4. exact-path consumer evidence remains distinct from ID-only references;
5. functional compare must contain exactly the four authorized paths;
6. exact-head workflows and artifact must pass before closure.
