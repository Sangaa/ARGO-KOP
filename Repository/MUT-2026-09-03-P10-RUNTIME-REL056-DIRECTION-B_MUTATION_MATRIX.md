# P10 Runtime — REL-056 Direction Reconciliation — Transaction B

Transaction ID: `MUT-2026-09-03-P10-RUNTIME-REL056-DIRECTION-B`
Priority: `10 — Runtime`
State: `PRE-WRITE / HARD HOLD / RESUME-SAFE`
Entry HEAD: `a720b8fa531c94fcbad01ab41e9321606d569f74`
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
| P10-B-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | correct REL-056 to `ENG-014 → RUN-011 = REFERENCES`; increment registry patch version/audit date; add bounded evidence note | every other relationship row; REL-056 stable ID; controlled type; incomplete-graph boundary | PASS | PENDING |
| P10-B-02 | `Repository/REP-011_PRIORITY10_RUNTIME_REL056_DIRECTION_ADDENDUM_2026-09-03_B.md` | CREATE | record current review evidence and supersede only the old P75 direction | historical P75 ledger content unchanged | PASS | PENDING |
| P10-B-03 | `Quality/Integrity/test_runtime_p10_rel056_direction.py` | CREATE | enforce direct-source direction and prohibit old/stronger REL-056 forms | no executable or bidirectional promotion | PASS | PENDING |
| P10-B-04 | this Matrix | UPDATE IN MATERIAL CHANGE SET | satisfy same-change-set enforcement and bind material evidence | all pre-write evidence and non-claims | PASS | PENDING |

## Non-claims

- No Runtime or Engine source contract is modified.
- `REFERENCES` is not promoted to `DEPENDS_ON`, `CONSUMES`, `IMPLEMENTS`, `VALIDATES` or execution proof.
- REL-055 and REL-057..060 remain unchanged.
- This row repair does not close Runtime Gate 15, Priority 10, Phase 1, the repository-wide graph, Global Connected Baseline or Global Integrity.

Validation:
`pre-write matrix → atomic registry/addendum/guard/matrix change set → read-back → targeted tests → exact-head four-family CI → close or HOLD`.
