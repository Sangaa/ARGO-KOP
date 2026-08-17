# P5 — CONTROLLED MUTATION / RECONCILIATION HARNESS TEST MATRIX

Date: 2026-08-17
Status: `EXECUTION-VERIFIED`
Authority: `GOV-014 v1.0.1`

## Default Test Policy

`FIXTURE = DEFAULT VALIDATION PATH`

The reusable non-canonical fixture path is the default execution path for routine mutation-harness validation because it is faster, isolated and deterministic.

`TRADITIONAL = INTEGRATION / PERIODIC REGRESSION PATH`

The traditional repository-document path remains mandatory whenever real repository integration is being validated and must be retained as a compatibility/regression control. Fixture success never authorizes a canonical write by itself.

Canonical mutation remains governed by the full mutation sequence:

`FIXTURE DEFAULT → REQUIRED GATES PASS → TRADITIONAL/INTEGRATION WHEN APPLICABLE → CANONICAL WRITE ONLY UNDER GOVERNED MUTATION MATRIX`

## Test Matrix

| Test ID | Scenario | Expected Result | Latest Verification |
|---|---|---|---|
| P5-T01 | Complete source read | PASS only when target file is fully captured | VERIFIED |
| P5-T02 | Missing/partial source | ABORT / `SOURCE-INCOMPLETE` | VERIFIED |
| P5-T03 | Source SHA changed before write | ABORT / `SHA-MISMATCH` | VERIFIED |
| P5-T04 | Missing Mutation Matrix | ABORT / `MATRIX-MISSING` | VERIFIED |
| P5-T05 | KEEP section changed in candidate | ABORT / `KEEP-MISMATCH` | VERIFIED |
| P5-T06 | Unspecified addition/deletion | ABORT / `UNEXPECTED-CHANGE` | VERIFIED |
| P5-T07 | Candidate matches matrix | PRE-COMMIT PASS | VERIFIED |
| P5-T08 | Controlled write succeeds | Continue to mandatory read-back | VERIFIED |
| P5-T09 | Post-write read-back differs | FAIL / `READBACK-FAILED` | VERIFIED |
| P5-T10 | Applied/Verified flags incomplete | `RECONCILIATION-OPEN` | VERIFIED |
| P5-T11 | Exact expected mutation + zero unexpected changes | Transaction eligible for closure | VERIFIED |
| P5-T12 | Historical/retroactive matrix | Must remain explicitly labeled retroactive; never treated as original pre-write compliance | VERIFIED |
| P5-T13 | Repository state changes after initial read but before write | ABORT / `CURRENT_STATE_CHANGED_BEFORE_WRITE`; zero write allowed | VERIFIED |
| P5-T14 | Traditional source path vs fixture path | Both paths must produce equivalent validated candidates and preservation results | VERIFIED |
| P5-T15 | Second update after a prior fixture update | Prior mutation must remain preserved while the new mutation is applied | VERIFIED |
| P5-T16 | Create race: file appears after initial absence check | ABORT / `CURRENT_STATE_CHANGED_BEFORE_WRITE`; zero write allowed | VERIFIED |
| P5-T17 | Fixture is default routine validation path | CI executes fixture tests first; traditional path remains available for compatibility/regression | VERIFIED |
| P5-T18 | Fixture fidelity regression | Fixture and traditional path must remain semantically equivalent for the supported mutation scenario | VERIFIED |
| P5-T19 | GOV-015 execution-record template applied to fixture/test session | Required execution identity, evidence boundary, learning classification, transfer decision and closure gates are capturable without implying canonical write authority | VERIFIED |

## Regression Focus

The first regression target is the REP-016 P291 content-preservation failure: a small requested update must never replace the complete large document with a shortened representation.

Required assertion:

`complete source content + explicit KEEP preservation + post-write structural completeness`

## New Learning / Race Protection

The 2026-08-17 traditional replay of `MUT-2026-08-17-REP002-001` reached `PRE_COMMIT_VALIDATED` and passed its candidate test, but the runner's push was rejected because `main` had advanced after the runner's checkout. This proves that source-SHA validation at transaction start is necessary but not sufficient.

The dispatcher therefore requires a second repository-state probe immediately before CREATE/UPDATE. For UPDATE, the live SHA must still equal the SHA used for candidate validation. For CREATE, the path must still be absent. Any change aborts with:

`CURRENT_STATE_CHANGED_BEFORE_WRITE`

No write is permitted after that failure.

## Dual-Path Regression and Default Strategy

The fixture path is now the **default routine validation path**. It is not a replacement for the traditional repository-document path.

The fixture path must:

1. match the traditional candidate and preservation result;
2. survive a second update without losing the first update;
3. preserve all untouched sections;
4. remain non-canonical and disposable;
5. be periodically compared against the traditional path so fixture drift cannot silently weaken validation coverage.

The traditional path is reserved for integration/compatibility/regression verification or whenever the actual repository artifact semantics are material to the decision.

## Execution Evidence

P5 workflow: `336293577`
Successful regression run: `32041698059`
Latest successful regression run: `32041738841`
Current GOV-015 fixture/test verification run: `32045549749`
Job: `p5-harness` / `95432507754`
Result: `SUCCESS`

Verified steps:

- P5 fixture/default tests: `SUCCESS`
- Canonical-artifact immutability guard: `SUCCESS`
- Stale-state update race: `VERIFIED`
- Create race: `VERIFIED`
- Traditional vs fixture equivalence: `VERIFIED`
- Successive fixture update preservation: `VERIFIED`
- P5-T19 GOV-015 fixture/test execution-record capture: `VERIFIED`

## Model-Independence

These tests evaluate repository artifacts and transaction evidence, not the identity, confidence or memory of the model performing the work.

---

End of P5 Test Matrix
