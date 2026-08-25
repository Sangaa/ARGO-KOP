# REP-020 — SESSION DELTA — 2026-08-25 — P213 SERVICE_DISPATCH EVIDENCE BOUNDARY

Protocol: GOV-013 HERMUZ Session Build Protocol
Status: CLOSED / VERIFIED-SCOPE / INTEGRITY-HOLD

## Finding

The current integrity regression required an explicit `SERVICE_DISPATCH` evidence marker in REP-020 for the unresolved `RUN-010 → SRV-009` runtime-coupling boundary.

The missing marker was a control-plane evidence-boundary omission, not proof that runtime coupling exists.

## Mutation

REP-020 was updated from `0.2.2` to `0.2.3` using the previously verified blob SHA and a complete-content replacement. The new marker records:

- relationship: `RUN-010 → SRV-009`
- state: `REVALIDATION_REQUIRED`
- runtime coupling: unproven
- no authority/promotion implied

## Verification Boundary

The mutation does not alter runtime code, service authority, or the P4 relationship classification. A fresh CI run is required to establish whether the integrity regression is resolved.

## Closure

`P213 / SERVICE_DISPATCH_EVIDENCE_BOUNDARY / NO_RUNTIME_MUTATION / INTEGRITY-HOLD`
