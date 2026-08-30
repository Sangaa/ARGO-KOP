# MUTATION MATRIX — P2 EJR H1 MULTI CHRONOLOGY 198

State: `OPEN / PREWRITE`

| Path | Operation | Reason | Content preservation |
|---|---|---|---|
| `Quality/Integration/ejr_h1_multi_chronology.py` | ADD | Evidence-only generalized chronology classifier for H1-only EJR ambiguity groups with >2 members | New companion analyzer only |
| `Quality/Integration/test_ejr_h1_multi_chronology.py` | ADD | Synthetic ancestry/partial-order/fail-closed verification | New tests only |
| `.github/workflows/internal-id-audit.yml` | MODIFY | Execute and artifact the new classifier under complete history | Existing workflow semantics preserved; append coverage only |
| this Matrix | MODIFY | Same-change governance evidence | Preserve lease boundaries |

Forbidden paths: all EJR artifacts, REP-012, REP-016, REP-020, and the internal Document-ID scanner.

Prewrite verification: N/A until functional commit exists.
