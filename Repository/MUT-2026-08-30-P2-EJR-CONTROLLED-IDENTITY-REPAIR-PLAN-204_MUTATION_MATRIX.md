# MUTATION MATRIX — LEASE 204 — P2 EJR CONTROLLED IDENTITY-REPAIR PLAN

State: `FUNCTIONAL PLAN / NO IDENTITY EXECUTION`
Lease: `R71-20260830-P2-EJR-CONTROLLED-IDENTITY-REPAIR-PLAN-204`
Prewrite head: `89c46c600550fb1d70054c6a2089c0507fb51681`

## Functional paths
- `Repository/P2_EJR_CONTROLLED_IDENTITY_REPAIR_PLAN_204.md`
- `Repository/MUT-2026-08-30-P2-EJR-CONTROLLED-IDENTITY-REPAIR-PLAN-204_MUTATION_MATRIX.md`

## Disposition assertions
| ID | Retained record | Displaced records | Replacement allocation |
|---|---|---:|---|
| EJR-211 | Memory P29 | 1 | BLOCKED pending VACANT proof |
| EJR-214 | Memory P31 | 1 | BLOCKED pending VACANT proof |
| EJR-219 | Memory P36 | 1 | BLOCKED pending VACANT proof |
| EJR-301 | Memory P6 CI recheck | 1 | BLOCKED pending VACANT proof |
| EJR-302 | Memory current-head recheck | 2 | BLOCKED pending two independent VACANT proofs |

## Consumer obligations captured
- EJR-211 retained Memory provenance: MEM-009 + REP-020 P29 delta.
- EJR-214 retained Memory provenance: MEM-009 + P31 chain.
- EJR-219 retained Memory provenance: MEM-009.
- displaced GT-040 record: REP-021 exact-path consumer rewrite required.
- displaced GT-041 record: REP-022 exact-path consumer rewrite required.
- displaced P221 CI-decision record: GOV-013B semantic provenance rewrite required if identity is repaired/retained in that context.

## Functional assertions
| Assertion | Result |
|---|---|
| First-valid-allocation retention rule explicit | Y |
| Five groups dispositioned | Y |
| Six displaced legitimate records preserved | Y |
| EJR-302 triple collision preserved | Y |
| No concrete replacement ID allocated | Y |
| Lease-193 VACANT proof mandatory | Y |
| One displaced record per future execution lease default | Y |
| Consumer rewrite obligations explicit | Y |
| No EJR mutation/path change | Y |
| No REP-012/016/020 mutation | Y |
| No P2/Phase1/global closure claim | Y |

## Forbidden scope confirmed
No `EJR/**`, `Memory/Engineering_Journal/**`, Governance consumer, REP control-plane artifact, scanner, gate or workflow is modified by this functional plan.

## Verification
`PENDING EXACT-HEAD WORKFLOWS`
