# MUTATION MATRIX — LEASE 204 — P2 EJR CONTROLLED IDENTITY-REPAIR PLAN

State: `PREWRITE / PLANNING ONLY`
Lease: `R71-20260830-P2-EJR-CONTROLLED-IDENTITY-REPAIR-PLAN-204`
Baseline: `329a7700f9d880674ed7ae317c1464be785ce2f8`

## Authorized prewrite paths
- `Repository/MUT-2026-08-30-P2-EJR-CONTROLLED-IDENTITY-REPAIR-PLAN-204.md`
- `Repository/MUT-2026-08-30-P2-EJR-CONTROLLED-IDENTITY-REPAIR-PLAN-204_MUTATION_MATRIX.md`

## Authorized functional path
- `Repository/P2_EJR_CONTROLLED_IDENTITY_REPAIR_PLAN_204.md`
- this matrix may be updated in the same functional change set.

## Forbidden functional scope
- all `EJR/**` and `Memory/Engineering_Journal/**` record mutations;
- consumer rewrites;
- replacement EJR allocation;
- REP-012 / REP-016 / REP-020 mutation;
- ambiguity suppression;
- authority/canonical promotion;
- Priority 2 or global closure.

## Functional assertions
| Assertion | Required |
|---|---|
| First-valid-allocation retention rule explicitly stated | Y |
| All five collision groups dispositioned | Y |
| EJR-302 triple collision preserved | Y |
| Replacement IDs remain unallocated pending Lease-193 VACANT | Y |
| Consumer/provenance obligations enumerated | Y |
| No EJR content/path mutation | Y |
| No overclaim of P2/Phase1/global closure | Y |

## Verification state
`PENDING FUNCTIONAL PLAN`
