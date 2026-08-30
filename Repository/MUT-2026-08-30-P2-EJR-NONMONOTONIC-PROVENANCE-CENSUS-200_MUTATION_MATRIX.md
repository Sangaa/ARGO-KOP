# MUTATION MATRIX — P2 EJR NON-MONOTONIC PROVENANCE CENSUS 200

State: `OPEN / PREWRITE`
Transaction: `MUT-2026-08-30-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Lease: `R71-20260830-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Baseline: `9762b1dbc0240dc9a8cfc4c409ed39982018d1d9`

| Path | Operation | Authorized purpose |
|---|---|---|
| `Quality/Integration/ejr_nonmonotonic_provenance_census.py` | ADD | Evidence-only content/reference/consumer census for EJR-195..198 |
| `Quality/Integration/test_ejr_nonmonotonic_provenance_census.py` | ADD | Synthetic bounded/fail-closed coverage |
| `.github/workflows/internal-id-audit.yml` | MODIFY | Execute and upload deterministic census |
| this Matrix | MODIFY | Same-change governance evidence |

Forbidden: EJR identity mutation; scanner semantic change; REP-012/016/020 changes; ambiguity suppression; ownership assignment; P2/global closure.

Verification: `PENDING`.
