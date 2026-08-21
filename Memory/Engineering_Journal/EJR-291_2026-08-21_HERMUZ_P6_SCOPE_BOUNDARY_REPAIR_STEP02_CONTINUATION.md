# EJR-291 — HERMUZ P6 Scope Boundary Repair — Step 02 Continuation

## Status
CLOSED — PRE-UPDATE CHECKPOINT

## Purpose
Record the corrected operation path after EJR-290. The next command must fetch the existing correlator and obtain its exact blob SHA before mutation.

## Required Operation
Target: `Quality/Integration/ci_impact_correlation.py`
Operation: `fetch_file` on current `main` HEAD.

## Safety Boundary
No write is authorized until the fetched file content and SHA are inspected. The update must be a complete-file replacement using the fetched SHA. No parallel write is permitted.

## Closure
This checkpoint is intentionally limited to the operation boundary. No implementation claim is made.

Next: fetch current correlator.

---

End of EJR-291
