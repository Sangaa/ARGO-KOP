# P10 Runtime — REL-059 Learning-Promotion Boundary Repair — Transaction D

Transaction ID: `MUT-2026-09-03-P10-RUNTIME-REL059-LEARNING-PROMOTION-D`
Priority: `10 — Runtime`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `1cf7111b5d5b53716f2d73ca412dfb46c2ce4492`
Pre-write HEAD: `335a142afba14efdbb02fe5791d6dd5fbb8e86f5`
Material HEAD: `6d7c3d700c08d4025f141c09be93cb17aba02364`
Corrective pre-write HEAD: `b849379ea2543cc360952c1deb736655f2b07dea`
Corrective HEAD: `864934fc729dfefabce33a0a2035a15446164517`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / REP-011 / REP-014 / REP-016`

## Failure preserved and classified

Current source establishes `RUN-014 → RUN-011 = VALIDATES` as an intended learning-promotion test relationship, but current executable evidence is incomplete:

1. RUN-014 requires proof that the cognitive loop can produce a learning candidate without silent promotion.
2. Existing promotion tests construct a standalone candidate fixture; none consumes a RUN-011 `cognitive_loop_harness` trace.
3. RUN-014 specifies `Conflicting governing rule → HOLD / CONFLICT`, but `learning_promotion_gate.py` has no governing-conflict input or rejection.
4. Required trace identity/pattern fields are checked only for key presence, so null/blank values can pass the current gate.

Classification: `REAL TRACKED RUNTIME CONSUMER + FAIL-CLOSED VALIDATION GAP`. The existing tests are preserved; no assertion is weakened.

## Authorized mutation

| Change ID | Target | Action | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|:---:|:---:|
| P10-D-01 | `Runtime/Prototype/learning_promotion_gate.py` | UPDATE | add explicit side-effect-free RUN-011 trace adapter; keep learning authority separate; hold conflict and incomplete identity/pattern | existing evidence/result/validation/authority/confidence holds | PASS | PASS |
| P10-D-02 | `Runtime/Prototype/test_learning_promotion_gate.py` | UPDATE | exercise a real RUN-011 trace through candidate construction and the promotion gate | existing standalone acceptance coverage | PASS | PASS |
| P10-D-03 | `Runtime/Prototype/test_learning_promotion_edge_cases.py` | UPDATE | cover governing conflict and blank required value failure | existing edge-case coverage | PASS | PASS |
| P10-D-04 | `Quality/Integrity/test_runtime_p10_rel059_learning_boundary.py` | CREATE | enforce separate execution/learning authorities, trace provenance, fail-closed behavior and exact REL-059 scope | non-promotion and non-authority boundary | PASS | PASS |
| P10-D-05 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | retain REL-059 direction/type with accurate executable boundary evidence; increment patch version | every other relationship row and incomplete-graph boundary | PASS | PASS |
| P10-D-06 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | synchronize REP-014 version binding in the same material change set | every other manifest row/status/non-claim | PASS | PASS |
| P10-D-07 | `Repository/REP-011_PRIORITY10_RUNTIME_REL059_LEARNING_ADDENDUM_2026-09-03_D.md` | CREATE | record repaired gap, evidence and semantic limit | historical REP-011 and prior deltas unchanged | PASS | PASS |
| P10-D-08 | this Matrix | UPDATE IN MATERIAL CHANGE SET | bind pre-write and material evidence | scope and non-claims | PASS | PASS |
| P10-D-C1-01 | `Knowledge/Learning/promotion_gate_adapter.py` | UPDATE AFTER CORRECTIVE PRE-WRITE | reconcile the tracked evidence consumer by materializing its bounded no-conflict default into the now fail-closed gate input | existing evidence mapping and separate authority argument | PASS | PASS |
| P10-D-C1-02 | `Knowledge/Learning/test_promotion_gate_adapter.py` | UPDATE AFTER CORRECTIVE PRE-WRITE | prove existing allow/hold behavior and explicit governing-conflict hold through the consumer | current integration contract | PASS | PASS |
| P10-D-C1-03 | this Matrix | UPDATE IN CORRECTIVE CHANGE SET | preserve failure evidence and bind the smallest consumer repair | original material changes and non-claims | PASS | PASS |

## Non-claims

- A cognitive-loop action authorization is not learning-promotion authority.
- `PROMOTION_ELIGIBLE` is not knowledge mutation or canonical promotion.
- RUN-011 and RUN-014 remain `Candidate / Integrity Hold`.
- REL-059 is not promoted to dependency, consumption, implementation, governance or production execution.
- This transaction does not close Runtime Gate 15, Priority 10, Phase 1, the broader graph, Global Connected Baseline or Global Integrity.

Validation:
`pre-write matrix → smallest code/test/registry/manifest/addendum repair → read-back → targeted tests → exact-head four-family CI → close or HOLD`.

## Preserved material-head failure

- Material Real Mutation Matrix `33745593291`, Full-Stack `33745593254`, and M2 `33745593239` — SUCCESS.
- Material Runtime/Integration `33745593285` — FAILURE only in `integration-tests`; `prototype-tests` and `integrity-tests` are SUCCESS.
- Exact failing tracked consumer: `Knowledge/Learning/promotion_gate_adapter.py` builds the promotion-gate candidate but did not materialize the new `governing_conflict` field.
- Exact failures: both cases in `Quality/Integration/test_readiness_to_promotion_gate_boundary.py`; absent field produced `CANDIDATE_INCOMPLETE` before the expected authority decision.
- The Runtime gate and its new tests passed. The assertions remain unchanged. Corrective scope is the real adapter plus its direct tests and this Matrix.

## Corrective verification

- Local deterministic execution: 20 checks passed across Runtime promotion, edge cases, Knowledge adapter, integration consumer and REL-059 integrity guard.
- Corrective Real Mutation Matrix Regression `33745855516` — SUCCESS.
- Corrective Full-Stack Repository Audit `33745855538` — SUCCESS.
- Corrective ARGO Runtime Prototype and Integration Tests `33745855608` — SUCCESS.
- Corrective M2 Multi-Channel Proposal Training `33745855476` — SUCCESS.
- The exact tracked consumer now materializes the gate field and preserves distinct promotion authority/conflict inputs.

Closure:
`P10 TRANSACTION D = CLOSED / VERIFIED / RESUME-SAFE`.
