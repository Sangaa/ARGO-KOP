# MUTATION MATRIX — Lease 311 EJR-248 Disposition / EJR-428 Vacancy Proof

Transaction ID: MUT-2026-08-31-P2-EJR-248-311
Protocol: GOV-014
Status: OPEN

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 311-A | Lease 311 record | CREATE | Evidence-only disposition and proof requirement | Y | Y |
| 311-B | Vacancy workflow | CREATE | Complete-history EJR-428 vacancy proof | N | N |

## KEEP REQUIREMENT
Keep both current EJR-248 members unchanged until the vacancy gate returns VACANT. Preserve all unrelated repository content byte-for-byte.

## Execution Evidence
Current main was re-read before mutation. Current code search returned no EJR-428 allocation, but this is explicitly treated as discovery only.

## Closure
Close only after the complete-history workflow and artifact are inspected. If EJR-428 is not VACANT, stop without identity mutation.
