# MUT-2026-08-31-CI-EJR429-STALE-VACANCY-GATE-317 — Mutation Matrix

Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE
Date: 2026-08-31

## Problem
At current `main` HEAD `3ac1857c03957c8439008630ddf8c2f891c12476`, workflow run `33420209414` fails because the historical Lease314 vacancy proof still enforces `EJR-429 = VACANT` after Repair315 intentionally and validly allocated EJR-429. The proof itself succeeded at proof head `0b0014744019c19d1272987bdb6f86ca19c8d7a4`; the later failure is stale post-allocation enforcement, not evidence that Repair315 is invalid.

## Prior learning applied
- GOV-013 §9B: a failing required Action is HARD HOLD and must be resolved at the first meaningful failure boundary before continuation.
- GOV-013 §8: use the smallest sufficient mutation.
- GOV-014A: protected mutation requires a pre-write Mutation Matrix.

## Mutation scope

| Change ID | Target | Action | Expected Change | Applied | Verified |
|---|---|---|---|---|---|
| 317-01 | `.github/workflows/ejr-replacement-vacancy-proof-314.yml` | UPDATE | bind the historical vacancy-proof job to its authorized proof SHA so later valid allocation cannot re-run the obsolete VACANT assertion | N | N |
| 317-02 | Lease314/Repair315 evidence | KEEP | preserve proof run, artifact, allocation, and historical records unchanged | Y | Y |
| 317-03 | INTF-006 / production runtime surfaces | KEEP | no interface promotion, runtime wiring, or cosmetic edits in this repair | Y | Y |

## Pre-write validation
- Exact failing run: `33420209414` on HEAD `3ac1857c03957c8439008630ddf8c2f891c12476`.
- Failed job/step: `prove-vacancy` → `Enforce vacancy decision`.
- Observed decision: `OCCUPIED`, with current claim at `EJR/EJR-429_2026-08-17_GOV-015_FIRST_RECONCILIATION_FIELD_VALIDATION.md`.
- Historical authorization evidence: Lease314 records successful vacancy proof at `0b0014744019c19d1272987bdb6f86ca19c8d7a4`; Repair315 then intentionally allocated EJR-429.
- First meaningful failure boundary: lifecycle mismatch — a pre-allocation vacancy assertion remained active after authorized allocation.

## KEEP requirements
Do not change EJR identities, the vacancy gate implementation, Lease314 evidence, Repair315 content, INTF-006 state, production runtime wiring, governance authority, or unrelated workflows.

## Closure gate
`workflow guard applied → target re-read → new run inspected → no stale vacancy failure → matrix updated → session closure recorded`.
