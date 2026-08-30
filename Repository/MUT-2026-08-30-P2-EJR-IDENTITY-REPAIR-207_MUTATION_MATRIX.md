# MUT-2026-08-30-P2-EJR-IDENTITY-REPAIR-207 — MUTATION MATRIX

Status: PREWRITE
Lease: `R71-20260830-P2-EJR-IDENTITY-REPAIR-207`
Baseline: `c03b05ab21859adbe6e18518f60385e376cc798b`

## Authorized functional paths
- delete `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md`
- add `EJR/EJR-400_P2_SESSION_CLOSURE_2026-08-17.md`
- this matrix

## Proven replacement vacancy
Lease206 / run `33329388744` / artifact `9737186617` proves `EJR-400 = VACANT`, history_complete=true, no current or historical claims in all locally reachable refs.

## Consumer disposition
Three materially different current searches were used around exact path, semantic ID, and control-plane surfaces. No current operational consumer was established. References in Leases/Rooms/census/repair-plan surfaces remain provenance describing the pre-repair state and are not rewritten to falsify history.

## Preservation rule
The target record body is preserved exactly except:
`# EJR-214 — P2 Session Closure`
becomes
`# EJR-400 — P2 Session Closure`.

Date, Status, Scope, baseline, integrity state, work-completed evidence, P2 disposition, learning/error correction, and next safe action remain unchanged.

## Required checks
- no unauthorized path in functional diff;
- current old path absent; new path readable;
- Internal Document-ID Audit must trigger and pass;
- EJR-214 ambiguity must lose the displaced root member;
- EJR-400 must not appear ambiguous;
- Full-Stack / Runtime / M2 / Real Matrix applicable exact-head checks pass;
- no broad P2 closure claim.
