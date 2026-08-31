# MUT-2026-08-31-P2-EJR-412-REPLACEMENT-VACANCY-PROOF-261

Status: OPEN / EXECUTION-PENDING
Scope: Candidate replacement identity EJR-412 only.
Opening main: `5f0af85e41e439854f6ac78d192e065ca109b01d`
Source disposition: `MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260.md`

## Trigger

Lease260 retained the earlier Memory EJR-232 allocation and classified the later root EJR-232 allocation displaced. It authorized replacement discovery only after a separate complete-history vacancy proof.

## Candidate discovery

- Current `EJR/` directory listing contains no EJR-412 allocation.
- Repository search for `EJR-412` currently returns only the Session259 instruction explicitly warning that EJR-412 must not be assumed vacant.
- These signals establish only that EJR-412 is a reasonable next candidate. They do not prove historical vacancy.

## Required proof

A dedicated workflow must:
1. checkout complete repository history with `fetch-depth: 0`,
2. verify the repository is not shallow,
3. run `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-412`,
4. upload the JSON evidence artifact even if the candidate is occupied,
5. fail unless the decision is exactly `VACANT`.

The execution-verified Lease256 workflow for EJR-411 is the directly applicable precedent.

## Boundaries

No rename, delete, move, EJR-412 allocation, EJR-232 body/H1 rewrite, consumer rewrite, census baseline mutation, Plan204 expansion, or global integrity promotion is permitted in Lease261.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

## Closure condition

Lease261 may close as `VACANT / AUTHORIZED FOR ONE BOUNDED ALLOCATION` only if the dedicated complete-history gate succeeds and the artifact proves:
- `current_claims=[]`,
- `historical_claims=[]`,
- `history_complete=true`,
- `occupied=false`,
- `vacant=true`,
- `decision=VACANT`.

If any condition fails, Lease261 closes BLOCKED and EJR-412 must not be allocated.
