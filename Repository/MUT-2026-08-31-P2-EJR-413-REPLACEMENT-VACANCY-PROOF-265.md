# MUT-2026-08-31-P2-EJR-413-REPLACEMENT-VACANCY-PROOF-265

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Candidate replacement identity EJR-413 only; no identity mutation.

## Chain

- Opening main: `9abec7dff2799bb28dcf0708bbb59079bbb2758e`.
- Pre-write Matrix265: `f2038d02c2776c477818aa79aad1bb1159b4a6fd`.
- Lease265 open: `e37ee1a3508a7ed538e838063bdd5a51e8adac99`.
- Vacancy workflow: `2e657a7458f0f835ddb1c27b73d46ef96a9dc0c9`.
- Matrix265 closure: `150b9a5230c6c8c3bd43932b5deff4da59b0d1d4`.

## Trigger and proof

Lease264 retained the earlier Memory EJR-233 allocation and classified the later root EJR-233 allocation displaced. A current search found no EJR-413, but that signal was used only for candidate discovery.

Dedicated workflow `EJR Replacement Vacancy Proof 265`, run `33374040160`, executed with `fetch-depth: 0`, verified the checkout was non-shallow, executed the repository vacancy gate for EJR-413, uploaded evidence, and enforced `decision == VACANT`.

Artifact `9751158049`, digest `sha256:f127a8d668f2eb1fa2b24081f0c04be22251855109765d21c3ac448fb7b5b48d`, proves:
- candidate=`EJR-413`
- current_claims=[]
- historical_claims=[]
- history_complete=true
- history_scope=`all locally reachable refs`
- occupied=false
- vacant=true
- decision=`VACANT`

## Validation

Pre-write Matrix265 passed:
- Full-Stack #2365 / `33373910461`: SUCCESS
- Runtime #2140 / `33373910383`: SUCCESS
- Real Mutation Matrix #203 / `33373910446`: SUCCESS
- M2 #1022 / `33373910426`: SUCCESS

Lease opening commit passed:
- Full-Stack #2366 / `33373975043`: SUCCESS
- Runtime #2141 / `33373975079`: SUCCESS
- M2 #1023 / `33373975075`: SUCCESS

Workflow commit passed:
- dedicated vacancy run `33374040160`: SUCCESS
- Full-Stack #2367 / `33374040106`: SUCCESS
- M2 #1024 / `33374040153`: SUCCESS

## Decision

EJR-413 is authorized and reserved for exactly one bounded replacement allocation for the displaced root EJR-233 record in the next separate identity-repair lease.

Lease265 performed no rename, delete, move, EJR-413 allocation, EJR-233 content/H1 rewrite, consumer rewrite, cohort-baseline mutation, or Global Integrity promotion.

## Learning / transfer disposition

No new permanent rule is required. This is another execution-confirmed use of the existing rule that current-tree absence is only candidate discovery; historical vacancy requires complete-history execution evidence.

## Resume

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Next safe entry: re-discover live main and open a separate EJR-233 → EJR-413 identity-repair lease with its own pre-write Mutation Matrix. Re-read the displaced source and enumerate current consumer obligations before atomic path/H1 mutation.