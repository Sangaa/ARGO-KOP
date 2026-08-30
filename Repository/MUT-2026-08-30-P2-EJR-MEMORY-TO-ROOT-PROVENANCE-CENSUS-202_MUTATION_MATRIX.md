# Mutation Matrix — Lease 202

Transaction: `MUT-2026-08-30-P2-EJR-MEMORY-TO-ROOT-PROVENANCE-CENSUS-202`
State: `CLOSED / VERIFIED / EXECUTION COMPLETE`
Functional head: `746dbbb111099badc8cf87f1a3e2f747e69a241a`

| Path | Action | Allowed | Applied | Verified |
|---|---|:---:|:---:|:---:|
| `Quality/Integration/ejr_memory_to_root_provenance_census.py` | ADD evidence-only cohort census | Y | Y | Y |
| `Quality/Integration/test_ejr_memory_to_root_provenance_census.py` | ADD regressions | Y | Y | Y |
| `.github/workflows/internal-id-audit.yml` | wire test/report/artifact | Y | Y | Y |
| this matrix | synchronize transaction evidence | Y | Y | Y |

## Verified contract
- target IDs derive from current namespace-lineage class `MEMORY_TO_ROOT_EJR`;
- expected and observed cohort count = 36;
- complete Git history required and observed;
- H1-only source/cardinality contract passed;
- content/title, ID-only refs, and exact-member-path consumers remain separate evidence channels;
- exact-head Internal-ID, Full-Stack, Runtime/Integration, M2 and Real Matrix all passed;
- artifact `9735858989`, digest `sha256:e4f56bde088b1ffd158e415ed807f098b9e0bc711dbd3f171926a64abc6f0aaf`, decision `CENSUSED`.

## Bounded finding
The cohort contains path-bound consumers on both namespace sides: Memory-selected members (`EJR-211/214/219`) and Root-selected members (`EJR-301/302`). Therefore `MEMORY_TO_ROOT_EJR` is not a global ownership or migration rule.

## Forbidden preserved
No EJR mutation/migration/rename/delete/reassignment/normalization/suppression/allocation; no owner/canonical assignment; no REP-012/016/020 mutation; no scanner weakening; no Priority-2/Phase-1/global closure; no Boot/PASS claim.
