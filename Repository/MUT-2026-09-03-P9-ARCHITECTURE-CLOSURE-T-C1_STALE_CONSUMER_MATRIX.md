# P9 Architecture — Closure Exact-Head Stale Consumer Repair — Transaction T-C1

Transaction ID: `MUT-2026-09-03-P9-ARCHITECTURE-CLOSURE-T-C1`
Priority: `9 — Architecture`
Parent Transaction: `MUT-2026-09-03-P9-ARCHITECTURE-BOUNDED-CLOSURE-T`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `ab4515a5e4be4f87b48d32a8bb23c242f666ded4`
Pre-write HEAD: `464e96e9f3e6ba2b31d832cc0345e4263a642e36`
Material HEAD: `4c0f9f823fde49d4774efb6bc6e8efbd8215a999`
Protocol: `PROJECT_BOOTSTRAP / GOV-013 / GOV-014 / GOV-014A`

## Exact-head failure evidence

- Four push workflow families were found for the exact entry HEAD.
- Real Mutation Matrix Regression `33724769998`, Full-Stack Repository Audit `33724770088`, and M2 Multi-Channel Proposal Training `33724769898` are SUCCESS.
- ARGO Runtime Prototype and Integration Tests `33724769967` is FAILURE only because `integration-tests` failed; `prototype-tests` and `integrity-tests` are SUCCESS.
- The integration log reports 2 failures and 583 passes:
  - `test_architecture_p9_repository_reconciliation.py::test_exact_architecture_inventory_and_authority_classification` still requires the superseded pre-closure README literal `Status: Approved / Integrity Hold`.
  - `test_architecture_p9_status_sync.py::test_architecture_status_and_readme_are_synchronized_to_bounded_closure` selects the first numbered inventory line for gate 1 instead of the numbered Validation Gate line, then incorrectly requires `PASS` in the inventory entry.
- Current source proves `Architecture/README.md` and `Architecture/_FOLDER_STATUS.md` carry the intended bounded closure state and preserve all global/downstream non-claims.

## Authorized bounded cohort

Both rows are test consumers of the same T closure state, share the same authority class and verification path, and contain no heterogeneous semantic decision.

| Change ID | Target | Action | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|:---:|:---:|
| P9-T-C1-01 | `Quality/Integration/test_architecture_p9_repository_reconciliation.py` | UPDATE | replace only the obsolete README status literal with the T bounded-closure status literal | exact inventory, canonicality, ARC-011 authority and legacy-foundation guards | PASS | PASS |
| P9-T-C1-02 | `Quality/Integration/test_architecture_p9_status_sync.py` | UPDATE | scope gate-line lookup to the Validation Gates 1–13 block so inventory numbering cannot satisfy the selector | all 13 PASS requirements and every anti-overclaim/closure assertion | PASS | PASS |

## Repair boundary

- Do not change Architecture source or closure semantics.
- Do not weaken or remove an assertion.
- Do not touch `test_core200_architecture_dependency_repair.py`; current tracked evidence does not identify that path as a source of either failure.
- Any new failure leaves this cohort and is isolated.

Validation:
`pre-write matrix → smallest test-consumer repair → local targeted/full integration read-back → exact-head four-family CI → close or preserve HOLD`.

## Material verification and reconciliation

- Direct local execution of every test function in both affected modules: 7/7 PASS; both files also compile successfully.
- Exact compare `464e96e9f3e6ba2b31d832cc0345e4263a642e36 → 4c0f9f823fde49d4774efb6bc6e8efbd8215a999` changes exactly the two authorized test consumers.
- Material exact-head Full-Stack Repository Audit `33741083750` — SUCCESS.
- Material exact-head M2 Multi-Channel Proposal Training `33741083767` — SUCCESS.
- Material exact-head ARGO Runtime Prototype and Integration Tests `33741083854` — SUCCESS; the prior integration failure no longer exists.
- Real Mutation Matrix Regression was not dispatched for the test-only material commit.
- Therefore the T closure semantic source remains valid, the current failure is repaired without assertion weakening, and Priority 9 is `CLOSED_FOR_PHASE_1 / RESUME-SAFE` within its bounded Architecture partition scope.
- Previous T-C1 HOLD classification: `SUPERSEDED BY LATER EXACT-HEAD EVIDENCE`; it is not inherited beyond this transaction.

## Preserved non-claims

Phase 1 remains OPEN; repository-wide graph completeness is not claimed; Global Connected Baseline remains OPEN; downstream Runtime/Interfaces/AI/Knowledge/Memory holds remain independently controlling; Global Integrity PASS is not claimed.
