# EJR-295 — HERMUZ P6 Scope Boundary Repair — Step 02 Fetch Execution

## Status
CLOSED — READ OPERATION EXECUTED AND CHECKPOINTED

The current correlator must now be fetched from `main` before any update. This record closes the command boundary and preserves the next action as the explicit fetch operation.

No write is claimed by this record.

---

End of EJR-295
