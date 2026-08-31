# MUT-2026-08-31-P2-EJR-413-REPLACEMENT-VACANCY-PROOF-265

Status: OPEN / PROOF-PENDING
Scope: Candidate replacement identity EJR-413 only; no identity mutation.
Opening main: `9abec7dff2799bb28dcf0708bbb59079bbb2758e`.
Pre-write Matrix265: `f2038d02c2776c477818aa79aad1bb1159b4a6fd`.
Source disposition: `MUT-2026-08-31-P2-EJR-233-DISPOSITION-AUTHORIZATION-264.md`.

## Trigger

Lease264 retained the earlier Memory EJR-233 allocation and classified the later root EJR-233 allocation displaced. It authorizes replacement discovery only through a separate complete-history vacancy proof.

## Candidate discovery

A current repository search for `EJR-413` returned no result. This is screening evidence only; it is explicitly insufficient to prove vacancy.

## Pre-write validation

Matrix265 passed before this lease opened:
- Full-Stack Repository Audit #2365 / run `33373910461`: SUCCESS
- ARGO Runtime Prototype and Integration #2140 / run `33373910383`: SUCCESS
- Real Mutation Matrix Regression #203 / run `33373910446`: SUCCESS
- M2 #1022 / run `33373910426`: SUCCESS

## Authorized proof

Create one dedicated workflow bound to this Matrix and candidate EJR-413. It must:
1. checkout complete history using `fetch-depth: 0`;
2. verify the checkout is not shallow;
3. run `python Quality/Integration/ejr_allocation_vacancy_gate.py EJR-413`;
4. upload the resulting JSON artifact even when the gate itself reports non-vacancy;
5. enforce `decision == VACANT` as a hard success condition.

## Acceptance

Only a dedicated execution proving `current_claims=[]`, `historical_claims=[]`, `history_complete=true`, `occupied=false`, `vacant=true`, and `decision=VACANT` can reserve EJR-413 for one bounded future replacement allocation.

No rename, delete, move, EJR-413 allocation, EJR-233 rewrite, consumer rewrite, cohort-baseline mutation, or Global Integrity promotion is authorized in Lease265.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.