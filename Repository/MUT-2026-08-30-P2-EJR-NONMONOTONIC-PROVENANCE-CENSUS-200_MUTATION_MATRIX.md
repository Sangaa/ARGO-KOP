# MUTATION MATRIX — P2 EJR NON-MONOTONIC PROVENANCE CENSUS 200

State: `FUNCTIONAL CANDIDATE / VERIFICATION PENDING`
Transaction: `MUT-2026-08-30-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Lease: `R71-20260830-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Prewrite head: `b8dbeaf0a350be8404d7cd15329b83492705a853`

| Path | Operation | Functional intent |
|---|---|---|
| `Quality/Integration/ejr_nonmonotonic_provenance_census.py` | ADD | Evidence-only content/reference census for EJR-195..198; fail closed on incomplete history/current membership drift |
| `Quality/Integration/test_ejr_nonmonotonic_provenance_census.py` | ADD | Distinct-content/reference, membership-drift, and shallow-history coverage |
| `.github/workflows/internal-id-audit.yml` | MODIFY | Run test + emit/upload deterministic provenance artifact |
| this Matrix | MODIFY | Same-change governance synchronization |

Hard boundaries:
- no EJR owner/canonical/migration/rename/suppression decision emitted;
- internal Document-ID scanner semantics unchanged;
- REP-012/016/020 untouched;
- Priority 2 and global holds remain open.

Verification: `PENDING exact-head Actions + artifact read-back`.
