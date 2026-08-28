# P408 Mutation Matrix — Authorization ID Boundary

Date: 2026-08-28
Status: `PREWRITE / ISOLATED / NO CANONICAL MUTATION`
Protocol: `GOV-013`

| Mutation | Target | Purpose | Authority boundary | Side effect | Evidence required |
|---|---|---|---|---|---|
| Add negative integration test | `Quality/Integration/test_run010_authorization_id_boundary.py` | Prove prototype authorization cannot satisfy execution handoff without authorization_id | Test-only; no authority creation | None | Test execution + exact-head CI |
| No runtime change | `Runtime/` | Explicit exclusion | Runtime unchanged | None | Diff inspection |
| No service/connector change | `Services/`, connectors | Explicit exclusion | Downstream authority unchanged | None | Diff inspection |
| No canonical change | `main` / canonical docs | Explicit exclusion | Canonical authority unchanged | None | Branch/base comparison |

## Gate

The test is permitted because it observes an already-existing boundary and fails closed. It does not manufacture authorization, provenance, caller reachability, or production execution.

## Promotion

No promotion is justified by this mutation alone.
