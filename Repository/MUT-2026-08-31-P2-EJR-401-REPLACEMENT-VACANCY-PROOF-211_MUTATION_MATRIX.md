# MUT-2026-08-31-P2-EJR-401-REPLACEMENT-VACANCY-PROOF-211 — MUTATION MATRIX

Status: PREWRITE / VACANCY PROOF
Lease: `R71-20260831-P2-EJR-401-REPLACEMENT-VACANCY-PROOF-211`
Baseline: `f2c2c106dcb8fac38a8b8d41ec2d1523ea593214`

## Authorized functional paths
- `.github/workflows/ejr-replacement-vacancy-proof-211.yml`
- this Matrix

## Exact permitted change
Add one dedicated workflow that:
- checks out complete history;
- asserts repository is not shallow;
- runs existing `ejr_allocation_vacancy_gate.py EJR-401` unchanged;
- uploads `ejr-401-vacancy.json` as `ejr-401-vacancy-proof`;
- fails closed unless decision is `VACANT`.

## Forbidden
- no changes to vacancy-gate Python semantics/tests;
- no EJR allocation or mutation;
- no consumer rewrite;
- no authority promotion or Priority2 closure.

## Validation
- compare limited to workflow + Matrix;
- exact-head vacancy proof SUCCESS;
- inspect deterministic artifact rather than trusting workflow color alone;
- supporting standard workflow regressions PASS.
