# MUT-2026-08-31-P2 — EJR-247 Disposition and EJR-426 Vacancy Proof — Lease 305

Status: OPEN / EVIDENCE-GATED / NO IDENTITY MUTATION YET
Date: 2026-08-31
Scope: Priority 2 deterministic MEMORY_TO_ROOT_EJR ambiguity cohort.

## Current Evidence

- Current cohort baseline: 11.
- `EJR-247` current namespace sequence: `MEMORY_EJR → ROOT_EJR`.
- Memory allocation: `Memory/Engineering_Journal/EJR-247_2026-08-15_P66_SESSION_CLOSURE.md`.
- Root allocation: `EJR/EJR-247_2026-08-17_MULTI_CHANNEL_TRAINING_COMPLETION.md`.
- Memory allocation is historically earlier and is a constituted closed journal identity.
- Root allocation is a distinct later record.
- Current evidence therefore selects Memory as the retained first-valid allocation and root as the displaced allocation, subject to successor vacancy proof.

## Successor Candidate

`EJR-426`

Search absence is discovery evidence only and is NOT sufficient vacancy proof.

## Hard Gate

The dedicated complete-history workflow must prove:

- repository checkout is non-shallow;
- current claim count for `EJR-426` = 0;
- historical allocation claim count for `EJR-426` = 0;
- decision = `VACANT`.

No rename, delete, reassignment, or successor allocation is authorized until this gate passes.

## Non-Claims

- No claim that all remaining cohort members share the same disposition.
- No Global Integrity promotion.
- No authority promotion of either journal content.

## Next Safe Action

Run and inspect the complete-history `EJR-426` vacancy proof. If and only if it returns `VACANT`, close this lease and open a separate governed identity-repair lease.
