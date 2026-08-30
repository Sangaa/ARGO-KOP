# Mutation Matrix — Lease 202

Transaction: `MUT-2026-08-30-P2-EJR-MEMORY-TO-ROOT-PROVENANCE-CENSUS-202`
State: `FUNCTIONAL CANDIDATE / VERIFICATION PENDING`
Baseline: `main@b3185e877b0977e79fd744bdaa206372c706b474`

| Path | Action | Allowed | Applied | Verified |
|---|---|:---:|:---:|:---:|
| `Quality/Integration/ejr_memory_to_root_provenance_census.py` | ADD evidence-only cohort census | Y | Y | N |
| `Quality/Integration/test_ejr_memory_to_root_provenance_census.py` | ADD regressions | Y | Y | N |
| `.github/workflows/internal-id-audit.yml` | wire test/report/artifact | Y | Y | N |
| this matrix | synchronize transaction evidence | Y | Y | N |

## Functional contract
- target IDs derive from current `ejr_h1_namespace_lineage.py` class `MEMORY_TO_ROOT_EJR`;
- expected cohort count is 36; drift returns `PARTIAL`;
- complete Git history is mandatory;
- H1-only source and lineage cardinality are revalidated;
- content fingerprints/titles, ID-only references, and exact-member-path consumers are emitted separately;
- no owner/canonical/migration disposition exists in the output.

## Forbidden preserved
No EJR mutation/migration/rename/delete/reassignment/normalization/suppression/allocation; no REP-012/016/020 mutation; no scanner weakening; no Priority-2/Phase-1/global closure; no Boot/PASS claim.

## Verification pending
Pre-ref exact-four-path compare; live-parent recheck; force=false fast-forward; read-back; exact-head Internal-ID, Full-Stack, Runtime/Integration, M2, Real Matrix; artifact inspection; closure checkpoint.
