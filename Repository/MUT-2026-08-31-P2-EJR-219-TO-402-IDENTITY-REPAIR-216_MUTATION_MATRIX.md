# Mutation Matrix — Lease 216

Status: FUNCTIONAL MUTATION APPLIED / VERIFICATION PENDING
Baseline: `fc1661ad027954b2d6bc462e8089a777fcbb683c`
Prewrite: `c645f7a616560a0a0110ffedb8bb899cf6841089`

| Surface | Executed | Constraint/result |
|---|---|---|
| Lease216 + Matrix | yes | authority precedes mutation |
| root EJR-219 source | deleted | identity move only |
| root EJR-402 destination | created | H1 identity changed; body otherwise preserved |
| Memory EJR-219 | NO | retained historical allocation |
| Consumers | NO | no operational synchronous obligation established |
| Census/analyzers | NO | expected 34 preserved intentionally |
| REP authority surfaces | NO | no cosmetic sync |

Verification must determine whether the preserved drift guard reports 34→33. Any rebaseline requires separate successor authority.
