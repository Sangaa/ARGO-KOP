# P5 — CONTROLLED MUTATION / RECONCILIATION HARNESS MATRIX

Date: 2026-08-17
Status: `EXECUTION-VERIFIED / P5 BUILD CLOSED`
Authority: `GOV-014 v1.0.1`
Scope: Reusable harness for high-risk document mutation and post-commit reconciliation.

## Objective

Convert the proven GOV-014 transaction pattern into a reusable P5 harness that can be applied to any high-risk authoritative document without relying on model memory.

## Control Chain

`CURRENT HEAD → FULL SOURCE → SOURCE SHA → SECTION MATRIX → MUTATION MATRIX → CANDIDATE → PRE-COMMIT VALIDATION → CONTROLLED WRITE → HEAD READ-BACK → RECONCILIATION → CLOSURE`

## Required Gates

| Gate | Requirement | Pass Condition |
|---|---|---|
| H-01 | Current HEAD resolution | Target path and current blob SHA captured |
| H-02 | Complete source capture | Full authoritative file available; no summary/partial source |
| H-03 | Section Matrix | Every section has stable identity, order and source hash |
| H-04 | Mutation Matrix | Every target has explicit action; every non-target unit is KEEP |
| H-05 | Candidate construction | Candidate rebuilt from complete source |
| H-06 | Pre-commit preservation | KEEP mismatches = 0; unexpected changes = 0 |
| H-07 | Identity/authority | Path, identity and authority remain consistent |
| H-08 | Controlled commit | Only validated candidate is written |
| H-09 | Post-commit read-back | Actual repository file is re-read from new HEAD |
| H-10 | Final reconciliation | Applied=Y and Verified=Y for all required changes; KEEP preserved |
| H-11 | Evidence closure | Commit/blob/workflow/read-back evidence recorded |
| H-12 | Abort integrity | Any failed gate blocks commit and remains traceable |

## Execution Evidence

- Workflow: `P5 Controlled Mutation Harness`
- Workflow ID: `336293577`
- Successful run: `32040965964`
- Event: `push`
- Head SHA: `192e9482c4ef7446b53ca195c11af2801f2705ce`
- Job: `p5-harness`
- Job result: `SUCCESS`
- `Run P5 fixture and dispatcher tests`: `SUCCESS`
- `Verify no canonical artifact was modified by tests`: `SUCCESS`

The same workflow also produced a prior successful run `32040934574`. The current run is the authoritative execution evidence for this closure.

## Failure Classes

- `SOURCE-INCOMPLETE`
- `SHA-MISMATCH`
- `MATRIX-MISSING`
- `KEEP-MISMATCH`
- `UNEXPECTED-CHANGE`
- `IDENTITY/AUTHORITY-GAP`
- `WRITE-UNVERIFIED`
- `READBACK-FAILED`
- `RECONCILIATION-OPEN`

## Reuse Rule

The harness is model-independent. A model may select the mutation, but the repository control chain determines whether the mutation is admissible and whether it can be closed.

## Boundary

P5 execution verification validates the harness and its fixture/dispatcher tests. It does not authorize or certify any new mutation of a canonical artifact.

---

End of P5 Harness Matrix
