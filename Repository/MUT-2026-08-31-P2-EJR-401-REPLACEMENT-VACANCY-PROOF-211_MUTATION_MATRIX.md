# MUT-2026-08-31-P2-EJR-401-REPLACEMENT-VACANCY-PROOF-211 — MUTATION MATRIX

Status: FUNCTIONAL / VACANCY PROOF
Lease: `R71-20260831-P2-EJR-401-REPLACEMENT-VACANCY-PROOF-211`
Baseline: `71b3137f2dc7f98617cca069fafbf81345911c1c`

## Authorized functional paths
- `.github/workflows/ejr-replacement-vacancy-proof-211.yml`
- this Matrix

## Exact functional change
Added one dedicated workflow that:
- checks out complete history (`fetch-depth: 0`);
- asserts repository is not shallow;
- runs existing `ejr_allocation_vacancy_gate.py EJR-401` unchanged;
- uploads `ejr-401-vacancy.json` as `ejr-401-vacancy-proof`;
- fails closed unless decision is `VACANT`.

## Preserved semantics
- vacancy gate implementation and tests unchanged;
- Internal Document-ID analyzer unchanged;
- no EJR content/path/H1 changed;
- no candidate allocated by this workflow itself.

## Required postwrite validation
- compare limited to workflow + Matrix;
- exact-head EJR Replacement Vacancy Proof 211 SUCCESS;
- artifact candidate=EJR-401, history_complete=true, current_claims=[], historical_claims=[], decision=VACANT;
- applicable Full-Stack / Runtime / M2 / Real Mutation Matrix workflows PASS.
