# MUT-2026-08-31-P2 — EJR-247 Disposition and EJR-426 Vacancy Proof — Lease 305

Status: CLOSED / EVIDENCE-VERIFIED
Date: 2026-08-31
Scope: Priority 2 deterministic MEMORY_TO_ROOT_EJR ambiguity cohort.

## Disposition

- Memory `EJR-247` was the earlier first-valid constituted allocation and retains identity `EJR-247`.
- Root `EJR-247` was the later displaced allocation.
- Candidate successor `EJR-426` was tested using complete non-shallow history.

## Vacancy Evidence

Proof head: `feec2779eb800dadd3bf4b45be61c824c25dfa40`
Vacancy workflow: `33413495915` — SUCCESS.
Full-Stack Repository Audit: `33413495838` — SUCCESS.

Artifact decision:
- `candidate = EJR-426`
- `history_complete = true`
- `current_claims = []`
- `historical_claims = []`
- `decision = VACANT`

## Closure

Vacancy gate PASSED. Successor allocation was therefore authorized only through separate Repair306. No Global Integrity promotion.

Next chain: Repair306 → baseline normalization Lease307.
