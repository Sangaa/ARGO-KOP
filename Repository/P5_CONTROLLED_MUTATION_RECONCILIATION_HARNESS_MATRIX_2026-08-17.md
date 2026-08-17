# P5 — CONTROLLED MUTATION / RECONCILIATION HARNESS MATRIX

Date: 2026-08-17
Status: `EXECUTION-VERIFIED / P5 BUILD CLOSED`
Authority: `GOV-014 v1.0.1`
Scope: Reusable harness for high-risk document mutation and post-commit reconciliation.

## Default Validation Strategy

`FIXTURE = DEFAULT ROUTINE VALIDATION PATH`

The reusable non-canonical fixture path is the default validation path for routine harness execution because it is faster, isolated and deterministic.

`TRADITIONAL = INTEGRATION / PERIODIC REGRESSION PATH`

The traditional repository-document path remains mandatory when validating real repository integration or when the actual artifact semantics are material. Fixture success never authorizes a canonical write by itself.

Default sequence:

`FIXTURE DEFAULT → REQUIRED GATES PASS → TRADITIONAL/INTEGRATION WHEN APPLICABLE → GOVERNED CANONICAL MUTATION ONLY`

## Objective

Convert the proven GOV-014 transaction pattern into a reusable P5 harness that can be applied to any high-risk authoritative document without relying on model memory.

## Control Chain

`CURRENT HEAD → FULL SOURCE → SOURCE SHA → SECTION MATRIX → MUTATION MATRIX → CANDIDATE → PRE-COMMIT VALIDATION → PRE-WRITE CURRENT-STATE RECHECK → CONTROLLED WRITE → HEAD READ-BACK → RECONCILIATION → CLOSURE`

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
| H-08 | Pre-write current-state recheck | Live repository state still matches the transaction state immediately before write |
| H-09 | Controlled commit | Only validated candidate is written |
| H-10 | Post-commit read-back | Actual repository file is re-read from new HEAD |
| H-11 | Final reconciliation | Applied=Y and Verified=Y for all required changes; KEEP preserved |
| H-12 | Evidence closure | Commit/blob/workflow/read-back evidence recorded |
| H-13 | Abort integrity | Any failed gate blocks commit and remains traceable |

## Execution Evidence

- Workflow: `P5 Controlled Mutation Harness`
- Workflow ID: `336293577`
- Successful regression run: `32041698059`
- Latest successful regression run: `32041738841`
- Event: `push`
- Job: `p5-harness`
- Job result: `SUCCESS`
- Fixture/default validation path: `SUCCESS`
- Traditional-vs-fixture equivalence: `VERIFIED`
- Stale-state update race: `VERIFIED`
- Create race: `VERIFIED`
- Successive fixture update preservation: `VERIFIED`
- Canonical-artifact immutability guard: `SUCCESS`

## Failure Classes

- `SOURCE-INCOMPLETE`
- `SHA-MISMATCH`
- `MATRIX-MISSING`
- `KEEP-MISMATCH`
- `UNEXPECTED-CHANGE`
- `IDENTITY/AUTHORITY-GAP`
- `CURRENT_STATE_CHANGED_BEFORE_WRITE`
- `WRITE-UNVERIFIED`
- `READBACK-FAILED`
- `RECONCILIATION-OPEN`

## Dual-Path / Fixture Fidelity Rule

The fixture path is the default for routine validation, but it must remain representative of the traditional path.

The fixture must:

1. produce an equivalent validated candidate for the supported mutation scenario;
2. preserve all untouched sections;
3. survive successive updates without losing prior mutations;
4. remain non-canonical and disposable;
5. be periodically compared against the traditional path so fixture drift cannot silently weaken validation coverage.

The traditional path is therefore retained as an integration and periodic regression control, not as the routine default.

## Reuse Rule

The harness is model-independent. A model may select the mutation, but the repository control chain determines whether the mutation is admissible and whether it can be closed.

## Boundary

P5 execution verification validates the harness, its fixture/default path, the traditional compatibility path, dispatcher races, and canonical-artifact immutability. It does not authorize or certify any new mutation of a canonical artifact.

---

End of P5 Harness Matrix
