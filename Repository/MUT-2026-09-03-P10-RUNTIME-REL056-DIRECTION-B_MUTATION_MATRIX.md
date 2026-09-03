# P10 Runtime — REL-056 Direction Reconciliation — Transaction B

Transaction ID: `MUT-2026-09-03-P10-RUNTIME-REL056-DIRECTION-B`
Priority: `10 — Runtime`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `a720b8fa531c94fcbad01ab41e9321606d569f74`
Pre-write HEAD: `6a9bea903268b65a5b284fbb4d9af71cb968263f`
Material HEAD: `ec9de34505bd96d46e8b9a48e344ced41e34e0c6`
Corrective HEAD: `95558851199302eec14384661d5a49368c13be06`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / REP-011 / REP-014 / REP-016`

## Prior-learning and evidence retrieval

Three materially different checks establish the current boundary:

1. Exact registry/ledger search finds `REL-056` and the old P75 review statement as `RUN-011 → ENG-014 = REFERENCES`.
2. Direct current-source read finds no ENG-014 reference in `RUN-011`, while `ENG-014` directly lists `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md` under Related Contracts.
3. Reverse/consumer search finds the same ENG-014 → RUN-011 reference and no executable, dependency, implementation or governing evidence for this pair.

The P75 record is `HISTORICAL / SUPERSEDED` for direction. The controlled `REFERENCES` type remains valid but must follow the source that actually contains the reference.

## Authorized mutation

| Change ID | Target | Action | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|:---:|:---:|
| P10-B-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | correct REL-056 to `ENG-014 → RUN-011 = REFERENCES`; increment registry patch version/audit date; add bounded evidence note | every other relationship row; REL-056 stable ID; controlled type; incomplete-graph boundary | PASS | PASS |
| P10-B-02 | `Repository/REP-011_PRIORITY10_RUNTIME_REL056_DIRECTION_ADDENDUM_2026-09-03_B.md` | CREATE | record current review evidence and supersede only the old P75 direction | historical P75 ledger content unchanged | PASS | PASS |
| P10-B-03 | `Quality/Integrity/test_runtime_p10_rel056_direction.py` | CREATE | enforce direct-source direction and prohibit old/stronger REL-056 forms | no executable or bidirectional promotion | PASS | PASS |
| P10-B-04 | this Matrix | UPDATE IN MATERIAL CHANGE SET | satisfy same-change-set enforcement and bind material evidence | all pre-write evidence and non-claims | PASS | PASS |
| P10-B-C1-01 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | synchronize REP-014 binding from v1.2.14 to v1.2.15 | every other manifest row/status/non-claim | PASS | PASS |
| P10-B-C1-02 | `Repository/REP-011_PRIORITY10_RUNTIME_REL056_DIRECTION_ADDENDUM_2026-09-03_B.md` | UPDATE | preserve first failure and corrective scope | direction evidence and boundaries | PASS | PASS |
| P10-B-C1-03 | this Matrix | UPDATE IN CORRECTIVE CHANGE SET | preserve failure evidence and satisfy protected-manifest same-change-set enforcement | all original evidence and scope | PASS | PASS |

## Non-claims

- No Runtime or Engine source contract is modified.
- `REFERENCES` is not promoted to `DEPENDS_ON`, `CONSUMES`, `IMPLEMENTS`, `VALIDATES` or execution proof.
- REL-055 and REL-057..060 remain unchanged.
- This row repair does not close Runtime Gate 15, Priority 10, Phase 1, the repository-wide graph, Global Connected Baseline or Global Integrity.

Validation:
`pre-write matrix → atomic registry/addendum/guard/matrix change set → read-back → targeted tests → exact-head four-family CI → close or HOLD`.

## Preserved material-head failure

- Material Full-Stack `33742492409`, Real Mutation Matrix `33742492497`, and M2 `33742492386` — SUCCESS.
- Material Runtime/Integration `33742492247` — FAILURE only in `integration-tests`; `integrity-tests` and `prototype-tests` are SUCCESS.
- Exact failures: the current control-plane manifest binds REP-014 v1.2.14 while material source is v1.2.15 in `test_control_plane_current_manifest.py` and `test_control_plane_reconciliation_gate.py`.
- Registry direction, direct-source guard and all unrelated Runtime behavior passed. The failure is a stale current-manifest consumer, not a reason to revert REL-056 or weaken either test.
- Corrective scope is limited to the manifest version binding plus this evidence/addendum update, packaged with this Matrix.

## Corrective verification

- Corrective exact-head Real Mutation Matrix Regression `33742702226` — SUCCESS.
- Corrective exact-head Full-Stack Repository Audit `33742702133` — SUCCESS.
- Corrective exact-head ARGO Runtime Prototype and Integration Tests `33742702182` — SUCCESS.
- Corrective exact-head M2 Multi-Channel Proposal Training `33742702178` — SUCCESS.
- Current REL-056 and the manifest-bound REP-014 version now agree; no stale consumer remains in the inspected transaction scope.

Closure:
`P10 TRANSACTION B = CLOSED / VERIFIED / RESUME-SAFE`.
