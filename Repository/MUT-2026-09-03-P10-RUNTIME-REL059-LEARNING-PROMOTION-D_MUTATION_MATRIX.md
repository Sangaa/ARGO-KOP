# P10 Runtime — REL-059 Learning-Promotion Boundary Repair — Transaction D

Transaction ID: `MUT-2026-09-03-P10-RUNTIME-REL059-LEARNING-PROMOTION-D`
Priority: `10 — Runtime`
State: `MATERIAL CHANGE SET / CI PENDING`
Entry HEAD: `1cf7111b5d5b53716f2d73ca412dfb46c2ce4492`
Pre-write HEAD: `335a142afba14efdbb02fe5791d6dd5fbb8e86f5`
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

## Non-claims

- A cognitive-loop action authorization is not learning-promotion authority.
- `PROMOTION_ELIGIBLE` is not knowledge mutation or canonical promotion.
- RUN-011 and RUN-014 remain `Candidate / Integrity Hold`.
- REL-059 is not promoted to dependency, consumption, implementation, governance or production execution.
- This transaction does not close Runtime Gate 15, Priority 10, Phase 1, the broader graph, Global Connected Baseline or Global Integrity.

Validation:
`pre-write matrix → smallest code/test/registry/manifest/addendum repair → read-back → targeted tests → exact-head four-family CI → close or HOLD`.
