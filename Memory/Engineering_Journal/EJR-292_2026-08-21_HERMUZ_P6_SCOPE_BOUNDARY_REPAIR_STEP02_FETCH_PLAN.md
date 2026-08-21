# EJR-292 — HERMUZ P6 Scope Boundary Repair — Step 02 Fetch Plan

## Status
CLOSED — COMMAND GROUP PREPARED

## Next Command
Fetch the current `Quality/Integration/ci_impact_correlation.py` from `main` after checkpoint `7d0a70953630629aaa3fd2951e85672fc2a66e8d`.

## Verification Required
Confirm:
- target path is the expected existing correlator;
- current blob SHA is available;
- scope registry path is present on the same current lineage;
- no prior implementation mutation occurred.

## Closure
No mutation in this step. The next command is the read-before-write operation required by GOV-013.

---

End of EJR-292
