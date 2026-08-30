# MUTATION MATRIX — P2 EJR NON-MONOTONIC PROVENANCE CENSUS 200

State: `CLOSED / VERIFIED / EXECUTION COMPLETE`
Transaction: `MUT-2026-08-30-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Lease: `R71-20260830-P2-EJR-NONMONOTONIC-PROVENANCE-CENSUS-200`
Prewrite head: `b8dbeaf0a350be8404d7cd15329b83492705a853`
Functional head: `2bce04b83567736415ac2fa91217da585922cb1e`

| Path | Operation | Verified result |
|---|---|---|
| `Quality/Integration/ejr_nonmonotonic_provenance_census.py` | ADD | Evidence-only content/reference census active; fail-closed history/membership behavior verified |
| `Quality/Integration/test_ejr_nonmonotonic_provenance_census.py` | ADD | Synthetic distinct-content/reference, membership-drift, shallow-history coverage PASS |
| `.github/workflows/internal-id-audit.yml` | MODIFY | Test + deterministic report + artifact upload PASS |
| this Matrix | MODIFY | Same-change governance synchronized |

Exact-head workflows at `2bce04b83567736415ac2fa91217da585922cb1e`:
- Internal-ID `33319971746` — SUCCESS
- Full-Stack `33319971759` — SUCCESS
- Runtime/Integration `33319971731` — SUCCESS
- M2 `33319971699` — SUCCESS
- Real Matrix `33319971704` — SUCCESS

Artifact `9734601892`, digest `sha256:d5bdc6792235c9adc5ea0974bb33a05692866f280d9e9113562abffa3be5b948`.

Observed result:
- 4/4 target groups `CENSUSED` under complete history;
- each group has exactly three H1-fallback members;
- all 12 member contents are SHA-256 distinct;
- zero external exact sibling-path references for all 12 member paths;
- ID-only references remain insufficient to select one member as canonical.

Bounded disposition: `DISTINCT RECORDS / EJR-ID REUSE EVIDENCE / PATH-LEVEL OWNERSHIP UNRESOLVED`.

Hard boundaries preserved: no EJR identity mutation; no scanner semantic change; REP-012/016/020 untouched; no ambiguity suppression; no ownership assignment; Priority 2 and global holds remain open.
