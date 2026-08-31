# Mutation Matrix — Lease 216

Status: CLOSED / SUCCESSOR-VERIFIED
Baseline: `fc1661ad027954b2d6bc462e8089a777fcbb683c`
Prewrite: `c645f7a616560a0a0110ffedb8bb899cf6841089`
Functional head: `0b67b706de7b7a8d54b7f4decc0fa51820e6add6`
Successor: Lease217 / functional head `f0262431402c953d1138e74f2f4ac6845ca3ef1a`

| Surface | Executed | Constraint/result |
|---|---|---|
| Lease216 + Matrix | yes | authority preceded mutation |
| root EJR-219 source | deleted | one-record identity move |
| root EJR-402 destination | created | H1 identity changed; body otherwise preserved |
| Memory EJR-219 | NO | retained historical allocation |
| Consumers | NO | no operational synchronous obligation established |
| Census/analyzers in Lease216 | NO | expected 34 intentionally preserved |
| REP authority surfaces | NO | no cosmetic sync |

Repair-head Internal-ID failure is preserved: run `33355206134`, sole reason post-repair cohort 34→33. Lease217 separately proves and rebaselines 33, with Internal-ID `33356597214` SUCCESS and 33/33 deterministic census evidence.
