# Verified Seam Evidence Registry

## Purpose

This registry is the proof layer between repository discovery and a `CONNECTED` canonical-spine seam.

A seam may be promoted to `CONNECTED` only when all three evidence classes exist:

1. **Contract** — defines the source/destination interface or responsibility boundary.
2. **Test** — exercises the seam through an executable or synthetic integration test.
3. **Trace** — demonstrates that the output can be followed into the destination behavior.

```text
Discovery
   ↓
PARTIAL / MISSING
   ↓
Contract + Test + Trace
   ↓
CONNECTED
```

## Safety Rule

No registry entry is valid when one of the three evidence classes is missing.

The registry does not execute code, grant authorization, or modify runtime behavior. It only records proof used by the integration audit.
