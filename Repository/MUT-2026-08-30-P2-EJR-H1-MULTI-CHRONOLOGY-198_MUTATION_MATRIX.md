# MUTATION MATRIX — P2 EJR H1 MULTI CHRONOLOGY 198

State: `FUNCTIONAL CANDIDATE`

| Path | Operation | Reason | Verification target |
|---|---|---|---|
| `Quality/Integration/ejr_h1_multi_chronology.py` | ADD | Evidence-only generalized chronology classifier for H1-only EJR ambiguity groups with >2 members | Synthetic tests + exact-head execution |
| `Quality/Integration/test_ejr_h1_multi_chronology.py` | ADD | Total-chain, same-commit, missing-history, shallow-history coverage | Pytest PASS |
| `.github/workflows/internal-id-audit.yml` | MODIFY | Execute and artifact the classifier under complete history | Internal-ID workflow PASS |
| this Matrix | MODIFY | Same-change governance evidence | Exact diff contains only authorized paths |

Protected boundaries: no EJR artifact mutation; no internal Document-ID scanner change; REP-012, REP-016, REP-020 untouched; no ownership inference; no Priority-2/global closure.
