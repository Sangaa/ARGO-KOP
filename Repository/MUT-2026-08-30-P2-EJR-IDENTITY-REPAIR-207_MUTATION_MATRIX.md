# MUT-2026-08-30-P2-EJR-IDENTITY-REPAIR-207 — MUTATION MATRIX

Status: FUNCTIONAL / ONE-RECORD REPAIR
Lease: `R71-20260830-P2-EJR-IDENTITY-REPAIR-207`
Baseline: `42c3233a0424417447e873e368f5357b9f7d9989`

## Authorized functional paths
- delete `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md`
- add `EJR/EJR-400_P2_SESSION_CLOSURE_2026-08-17.md`
- this matrix

## Proven replacement vacancy
Lease206 / run `33329388744` / artifact `9737186617` proves `EJR-400 = VACANT`, history_complete=true, no current or historical claims in all locally reachable refs.

## Consumer disposition
Current exact-path, semantic-ID, and control-plane-targeted searches established no current operational consumer requiring synchronous rewrite. References in Leases/Rooms/census/repair-plan surfaces remain provenance describing the pre-repair state and are intentionally preserved.

## Preservation rule
The target record body is byte-for-byte semantically preserved except the first H1 identity:
`# EJR-214 — P2 Session Closure`
becomes
`# EJR-400 — P2 Session Closure`.

All date/status/scope/baseline/integrity/work-completed/P2-disposition/learning/next-action content remains unchanged.

## Required checks
- functional diff contains only old path deletion, new path addition, and this Matrix;
- old path absent and new path readable at exact head;
- Internal Document-ID Audit exact-head SUCCESS;
- EJR-214 ambiguity loses the displaced root member;
- EJR-400 remains unique;
- Full-Stack / Runtime / M2 / Real Matrix applicable exact-head checks pass;
- Priority 2 remains OPEN.
