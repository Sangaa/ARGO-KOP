# P5 — CONTROLLED MUTATION / RECONCILIATION HARNESS TEST MATRIX

Date: 2026-08-17
Status: `EXECUTION-VERIFIED`
Authority: `GOV-014 v1.0.1`

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

## Regression Focus

The first regression target is the REP-016 P291 content-preservation failure: a small requested update must never replace the complete large document with a shortened representation.

Required assertion:

`complete source content + explicit KEEP preservation + post-write structural completeness`

## New Learning / Race Protection

The 2026-08-17 traditional replay of `MUT-2026-08-17-REP002-001` reached `PRE_COMMIT_VALIDATED` and passed its candidate test, but the runner's push was rejected because `main` had advanced after the runner's checkout. This proves that source-SHA validation at transaction start is necessary but not sufficient.

The dispatcher therefore requires a second repository-state probe immediately before CREATE/UPDATE. For UPDATE, the live SHA must still equal the SHA used for candidate validation. For CREATE, the path must still be absent. Any change aborts with:

`CURRENT_STATE_CHANGED_BEFORE_WRITE`

No write is permitted after that failure.

## Dual-Path Regression

The fixture path is not a replacement for the traditional path. Both are retained and are now execution-verified. The reusable fixture must:

1. match the traditional candidate and preservation result;
2. survive a second update without losing the first update;
3. preserve all untouched sections;
4. remain non-canonical and disposable.

## Execution Evidence

P5 workflow: `336293577`
Successful regression run: `32041698059`
Job: `95422049526`
Result: `SUCCESS`

Verified steps:

- P5 fixture and dispatcher tests: `SUCCESS`
- Canonical-artifact immutability guard: `SUCCESS`

## Model-Independence

These tests evaluate repository artifacts and transaction evidence, not the identity, confidence or memory of the model performing the work.

---

End of P5 Test Matrix
