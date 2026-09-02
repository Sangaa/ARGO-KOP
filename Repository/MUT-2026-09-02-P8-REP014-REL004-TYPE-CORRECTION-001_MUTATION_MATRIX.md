# P8 REL-004 Bounded Type/Direction Correction — Pre-Write Mutation Matrix

Transaction ID: `MUT-2026-09-02-P8-REP014-REL004-TYPE-CORRECTION-001`
Priority: `8 — Governance`
State: `PRE-WRITE / READY`
Entry HEAD: `727bceb502462cb1f651eadf58f4d5ebe4118cac`
Pre-write Matrix HEAD: `PENDING`
Targets: `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` + `Quality/Integration/test_engine_validation_decision_reciprocity.py`
REP-014 source blob: `4f4c2dd8ba068a5ee19df1406e98fc3d6349347c`
Protocols: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / REP-003 / REP-014 / ENG-002 / ENG-006`

## Legal entry and disposition

The REL-010..REL-014 MOD-011/Knowledge seam is closed within its inspected bounds with closure-head four-workflow success. Priority 8 remains OPEN. REL-004 is the next explicit `Revalidation Required` relationship row.

Current row: `ENG-002 → ENG-006 = DEPENDS_ON / Revalidation Required`.

Evidence gates:

- ENDPOINT AUTHORITY: ENG-002 and ENG-006 are Canonical / Integrity Hold / Revalidated. ENG-002 owns decision recommendations within its authority boundary; ENG-006 owns downstream execution subject to validation and authorization.
- SEMANTIC DIRECTION: ENG-006 explicitly states that it consumes decisions/execution candidates from ENG-002. ENG-002 sends candidates toward Validation/Execution but does not depend on ENG-006 to define decision semantics.
- DEPENDENCY NECESSITY: PASS for the corrected edge only within the documentary contract; ENG-006's decision-input path requires an authorized ENG-002 output where that path applies. This does not establish runtime reachability or universal execution.
- CONSUMER / IMPACT: `Quality/Integration/test_engine_validation_decision_reciprocity.py` is the only executable guard found for the exact row and currently asserts the reversed registry tuple. Its endpoint assertions are valid, but the tuple is stale and must be synchronized without weakening the boundary.
- TYPE FIT: `CONSUMES` exactly matches ENG-006 wording and is more precise than `DEPENDS_ON`; `REFERENCES` is too weak for the explicit input relationship; no `IMPLEMENTS/GOVERNS/VALIDATES` relation is supported.

Disposition: `TYPE CORRECTION REQUIRED / STALE GUARD SYNCHRONIZATION REQUIRED`.

Authorized row: `REL-004 | ENG-006 | ENG-002 | CONSUMES | Revalidated within inspected scope`.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---:|---:|
| P8-REL004-01 | REP-014 REL-004 row | UPDATE | reverse direction, change `DEPENDS_ON → CONSUMES`, set bounded revalidated state | N | N |
| P8-REL004-02 | reciprocity guard | UPDATE | assert corrected exact tuple and retain decision/execution authority checks | N | N |
| P8-REL004-03 | all other content | KEEP | no unrelated semantic or test change | N | N |
| P8-REL004-04 | ENG-002 / ENG-006 | KEEP | no endpoint mutation or promotion | N | N |
| P8-REL004-05 | this Matrix | UPDATE | bind material compare, read-back and verification | N | N |

Atomicity: exactly one material commit after the pre-write Matrix HEAD, exactly REP-014 + the targeted guard + this Matrix, unexpected paths `0`.

Forbidden: no executable-connectivity claim, no endpoint/folder promotion, no P8/Phase-1/global closure, no repository-wide graph claim and no guard weakening.

Closure requires exact authorized diffs, immutable read-back, exact-head four-workflow success with Runtime job split reviewed, Matrix reconciliation and closure-head verification.
