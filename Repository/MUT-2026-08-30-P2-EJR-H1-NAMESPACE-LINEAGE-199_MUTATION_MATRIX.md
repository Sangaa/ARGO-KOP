# MUTATION MATRIX — P2 EJR H1 NAMESPACE LINEAGE 199

State: `PREWRITE / OPEN`
Baseline: `main@6b011215286aae70d78d0ad86d6d8acc75ee7fa2`

| Path | Planned operation | Authority / constraint |
|---|---|---|
| `Quality/Integration/ejr_h1_namespace_lineage.py` | ADD | Evidence-only namespace-lineage classifier |
| `Quality/Integration/test_ejr_h1_namespace_lineage.py` | ADD | Synthetic total-order/direction/fail-closed coverage |
| `.github/workflows/internal-id-audit.yml` | MODIFY | Execute tests + emit/upload deterministic report only |
| this Matrix | MODIFY | Same-change-set governance evidence |

Forbidden: all EJR identity/content mutations; scanner semantic changes; REP-012/016/020 changes; ownership assignment; ambiguity suppression; P2/Phase1/global closure.

Verification: compare before ref update, live-parent recheck, `force=false`, read-back, exact-head Actions, report artifact inspection, closure checkpoint.
