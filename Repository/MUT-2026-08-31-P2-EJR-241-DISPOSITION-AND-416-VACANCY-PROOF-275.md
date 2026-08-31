# MUT-2026-08-31-P2-EJR-241-DISPOSITION-AND-416-VACANCY-PROOF-275

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: EJR-241 retained/displaced classification plus complete-history vacancy proof for candidate EJR-416; no identity mutation.
Opening main: `c421044c3e8c9782a3344f0b465f041411bf15f8`
Pre-write Matrix275: `3127fa2e2bc86e2444bc0d566cd606e994ad3d22`
Proof-workflow head: `92d637c88e3dfc266db8e62894241cbdb341fdd7`

## EJR-241 disposition

- `Memory/Engineering_Journal/EJR-241_2026-08-15_P59_SESSION_CLOSURE.md` is the earlier valid allocation and RETAINS EJR-241.
- `EJR/EJR-241_2026-08-17_MATRIX_VARIANT_REPEAT_VALIDATION.md` is the later legitimate allocation and is DISPLACED / LEGITIMATE CONTENT / FUTURE ONE-RECORD REPAIR.
- Direct reads prove distinct semantic records.
- Current deterministic census reports zero exact member-path consumers and only two baseline exact-ID references.
- Fresh exact root member-path search returned zero consumers.

## EJR-416 complete-history vacancy proof

Dedicated workflow `.github/workflows/ejr-replacement-vacancy-proof-275.yml` used fetch-depth:0, verified a non-shallow repository, and executed the existing fail-closed vacancy gate.

Execution evidence:
- EJR Replacement Vacancy Proof 275 run `33384024659`: SUCCESS.
- Artifact `9754849239`, digest `sha256:5eb4c19afb1976fbce08fdeabce50a1baaaa9d7eb0ffc4b00db54a4affed30d2`.
- Artifact: candidate=EJR-416, current_claims=[], historical_claims=[], history_complete=true, history_scope=all locally reachable refs, occupied=false, vacant=true, decision=VACANT.
- Full-Stack Repository Audit #2415 / run `33384024639`: SUCCESS on proof head.
- M2 #1072 / run `33384024636`: SUCCESS on proof head.

## Reservation and resume

EJR-416 is reserved solely for a bounded replacement allocation of the displaced root EJR-241 record. No identity mutation occurred in Lease275.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Next safe entry: separate pre-write repair for root EJR-241 → EJR-416 with fresh source/blob, target absence, consumer and live-main hard gates.
