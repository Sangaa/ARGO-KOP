# P5 — CONTROLLED MUTATION / RECONCILIATION HARNESS TEST MATRIX

Date: 2026-08-17
Status: `ACTIVE / TEST DESIGN`
Authority: `GOV-014 v1.0.1`

## Test Matrix

| Test ID | Scenario | Expected Result |
|---|---|---|
| P5-T01 | Complete source read | PASS only when target file is fully captured |
| P5-T02 | Missing/partial source | ABORT / `SOURCE-INCOMPLETE` |
| P5-T03 | Source SHA changed before write | ABORT / `SHA-MISMATCH` |
| P5-T04 | Missing Mutation Matrix | ABORT / `MATRIX-MISSING` |
| P5-T05 | KEEP section changed in candidate | ABORT / `KEEP-MISMATCH` |
| P5-T06 | Unspecified addition/deletion | ABORT / `UNEXPECTED-CHANGE` |
| P5-T07 | Candidate matches matrix | PRE-COMMIT PASS |
| P5-T08 | Controlled write succeeds | Continue to mandatory read-back |
| P5-T09 | Post-write read-back differs | FAIL / `READBACK-FAILED` |
| P5-T10 | Applied/Verified flags incomplete | `RECONCILIATION-OPEN` |
| P5-T11 | Exact expected mutation + zero unexpected changes | Transaction eligible for closure |
| P5-T12 | Historical/retroactive matrix | Must remain explicitly labeled retroactive; never treated as original pre-write compliance |

## Regression Focus

The first regression target is the REP-016 P291 content-preservation failure: a small requested update must never replace the complete large document with a shortened representation.

Required assertion:

`complete source content + explicit KEEP preservation + post-write structural completeness`

## Model-Independence

These tests must evaluate repository artifacts and transaction evidence, not the identity, confidence or memory of the model performing the work.

---

End of P5 Test Matrix
