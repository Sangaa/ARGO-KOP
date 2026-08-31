# MUT-2026-08-31-CI-EJR429-STALE-VACANCY-GATE-317 — Mutation Matrix

Protocol: GOV-013 / GOV-014A
Status: CLOSED / VERIFIED / RESUME-SAFE
Date: 2026-08-31

## Problem
At `main` HEAD `3ac1857c03957c8439008630ddf8c2f891c12476`, workflow run `33420209414` failed because the historical Lease314 vacancy proof still enforced `EJR-429 = VACANT` after Repair315 intentionally and validly allocated EJR-429. The proof itself succeeded at proof head `0b0014744019c19d1272987bdb6f86ca19c8d7a4`; the later failure was stale post-allocation enforcement, not evidence that Repair315 was invalid.

## Prior learning applied
- GOV-013 §9B: a failing required Action is HARD HOLD and must be resolved at the first meaningful failure boundary before continuation.
- GOV-013 §8: use the smallest sufficient mutation.
- GOV-014A: protected mutation requires a pre-write Mutation Matrix.

## Mutation scope

| Change ID | Target | Action | Expected Change | Applied | Verified |
|---|---|---|---|---|---|
| 317-01 | `.github/workflows/ejr-replacement-vacancy-proof-314.yml` | UPDATE | bind the historical vacancy-proof job to its authorized proof SHA so later valid allocation cannot re-run the obsolete VACANT assertion | Y | Y |
| 317-02 | Lease314/Repair315 evidence | KEEP | preserve proof run, artifact, allocation, and historical records unchanged | Y | Y |
| 317-03 | INTF-006 / production runtime surfaces | KEEP | no interface promotion, runtime wiring, or cosmetic edits in this repair | Y | Y |

## Failure boundary
- Exact failing run: `33420209414` on HEAD `3ac1857c03957c8439008630ddf8c2f891c12476`.
- Failed job/step: `prove-vacancy` → `Enforce vacancy decision`.
- Observed decision: `OCCUPIED`, with current claim at `EJR/EJR-429_2026-08-17_GOV-015_FIRST_RECONCILIATION_FIELD_VALIDATION.md`.
- Historical authorization evidence: Lease314 records successful vacancy proof at `0b0014744019c19d1272987bdb6f86ca19c8d7a4`; Repair315 then intentionally allocated EJR-429.
- Root cause: lifecycle mismatch — a pre-allocation vacancy assertion remained active after authorized allocation.

## Executed repair
Commit `6fd7a4e65ef3264ed429b6cb6536cff4b4839b7c` added one job-level guard:

`if: github.sha == '0b0014744019c19d1272987bdb6f86ca19c8d7a4'`

No proof artifact, EJR identity, vacancy-gate implementation, interface state, runtime wiring, or authority surface changed.

## Post-change verification
- Historical vacancy workflow run `33420709351` on repair HEAD: `skipped` by the proof-SHA guard; stale post-allocation VACANT enforcement did not execute.
- Full-Stack Repository Audit run `33420711088` on the same repair HEAD: `success`.
- The original Lease314 proof remains attributable to proof head `0b0014744019c19d1272987bdb6f86ca19c8d7a4`.

## Reconciled unresolved boundaries
- `INTF-006_ENVIRONMENT_SENSING.md` remains canonical but `Proposed / Integrity Hold`; no runtime/connector implementation proof is claimed.
- RUN-010 → ENG-006 handoff identity and contract tests are CI-corroborated, but current repository records still explicitly state that complete production reachability through `execute_update()` / ENG-006 → SRV-009 is not proven.
- Therefore the highest-value next runtime action is an execution/evidence closure, not a documentation promotion: exercise an actual authorized RUN-010 result through the existing `build_handoff_candidate(...)` → `ProductionExecutionCandidate` → `execute_update(...)` path using an isolated governed repository target/connector, then prove write/read-back/trace continuity and clean up the isolated artifact.

## Closure
`FAILURE BOUNDARY → PRIOR LEARNING → PRE-WRITE MATRIX → MINIMAL GUARD → RE-READ → WORKFLOW RECONCILIATION → FULL-STACK PASS → UNRESOLVED GAP BOUNDARY → CLOSE`

Final state:
`STALE VACANCY CI HARD HOLD = CLOSED`
`INTF-006 = UNPROVEN / INTEGRITY HOLD`
`PRODUCTION INVOCATION = NOT YET EXECUTION-VERIFIED`
`GLOBAL INTEGRITY = HOLD`
`SESSION = CLOSED / RESUME-SAFE`
