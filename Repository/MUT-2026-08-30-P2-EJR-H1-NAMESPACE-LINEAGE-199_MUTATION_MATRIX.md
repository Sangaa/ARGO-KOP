# MUTATION MATRIX — P2 EJR H1 NAMESPACE LINEAGE 199

State: `FUNCTIONAL CANDIDATE / VERIFICATION PENDING`
Baseline prewrite head: `f28d19d48f5b33ccd642af54b46360a79868b0ee`

| Path | Operation | Expected result |
|---|---|---|
| `Quality/Integration/ejr_h1_namespace_lineage.py` | ADD | Evidence-only namespace lineage classifier |
| `Quality/Integration/test_ejr_h1_namespace_lineage.py` | ADD | Synthetic direction/same-surface/multi-transition/shallow-history coverage |
| `.github/workflows/internal-id-audit.yml` | MODIFY | Run test + emit/upload deterministic namespace-lineage artifact |
| this Matrix | MODIFY | Same-change-set governance evidence synchronized |

Semantic boundaries:
- H1-only groups only; explicit-ID MIXED groups excluded.
- complete locally reachable Git history required.
- exact-path first-seen ancestry + namespace surface are provenance signals, not ownership authority.
- non-total ancestry, same-first-seen, missing history, or shallow history fail closed / remain unresolved.

Forbidden: no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, allocation, scanner-semantic change, REP-012/016/020 mutation, authority promotion, P2/Phase1/global closure.

Functional verification pending exact-head compare, read-back, Actions, and report artifact inspection.
