# Priority 12 — Models Transaction-A Exact-Head Control-Plane Corrective Matrix

Transaction ID: `MUT-2026-09-05-P12-MODELS-EXACT-HEAD-CONTROL-PLANE-CORRECTIVE`

Priority: `12 — Models`

State: `CORRECTIVE MATERIAL APPLIED / EXACT-HEAD CI PENDING`

Failure entry HEAD: `3fefe4fcb8db810b8ab15518deb81323ffb8d396`
Corrective material HEAD: `d70fd6d72139e4a5c2cbbd109480e4a6063bcb0d`

## Failure classification

Transaction-A material was complete, but exact-head closure validation failed closed in `ARGO Runtime Prototype and Integration Tests` while the other three required workflow families succeeded.

The failure is a stale control-plane consumer/binding defect, not contradictory Models material evidence:

- `REP-012` current version is `1.0.13`, while REP-020 recorded `1.0.12`.
- `REP-013` current version is `1.1.6`, while REP-020 recorded `1.1.5`.
- `REP-016` current version is `1.3.1`, while REP-020 recorded `1.3.0`.
- `REP-002` was intentionally advanced to `1.7.8` by P12 exact physical-map synchronization, while the bounded reconciliation regression still pinned `1.7.7`.

`CURRENT ARTIFACT TRUTH > STALE MANIFEST/EXPECTED VERSION`, while preserving all semantic, status and integrity boundaries.

## Authorized corrective set

| Change ID | Target | Action | Purpose |
|---|---|---|---|
| P12-CA-01 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | refresh current version bindings to REP-012 1.0.13, REP-013 1.1.6, REP-016 1.3.1; preserve non-authority/Integrity-Hold semantics |
| P12-CA-02 | `Quality/Integration/test_core_rep002_control_plane_reconciliation.py` | UPDATE | synchronize stale REP-002 expected version from 1.7.7 to intentional current 1.7.8 while retaining bounded-state assertions |
| P12-CA-03 | this corrective Matrix | CREATE / trigger-family normalization | classify failure, bind corrective scope, and ensure Real Mutation Matrix workflow trigger coverage |

No Transaction-A material artifact is downgraded or semantically promoted. No relationship authority is manufactured. No Priority-12 closure is claimed.

## Verification gate

The corrective HEAD must pass the same four exact-head workflow families required by Transaction A. Only then may the original Transaction-A Matrix be changed in a separate Matrix-only closure commit. That closure HEAD must itself pass all four families before Transaction A is declared `CLOSED / VERIFIED / RESUME-SAFE`.
