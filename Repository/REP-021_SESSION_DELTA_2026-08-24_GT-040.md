# REP-021 Session Delta — GT-040

Date: 2026-08-24
Checkpoint: GT-040
State: BUILD CONTINUATION / CONTROLLED REGRESSION RECORDED / CI EXECUTION PENDING

## Protocol

Session operating sequence:

`Execute → Document in repository → Read-back/verify → Close → Brief report`

## Current Build Point

GT-040 — Multilevel Explicit Provenance Root Agreement.

## Evidence

Test artifact:
`Quality/Integration/test_evidence_reasoning_classification.py`

Test mutation commit:
`94f683bbe6816260131832a597eaa57aee143c59`

Learning record:
`EJR/EJR-301_2026-08-24_GT-040_MULTILEVEL_EXPLICIT_ROOT_AGREEMENT.md`

Documentation commit:
`cc90f7822460ccbfb60e3e083c3189b04a3ed4eb`

## Result

The controlled multilevel chain:

`ROOT-A → PARENT → CHILD`

with explicit `provenance_root = ROOT-A` on all three nodes is classified as:

`VALID PROVENANCE`

and the parent/child evidence comparison remains:

`CONSISTENT / CORRELATED`

The regression confirms that explicit root repetition across multiple parent levels does not create a provenance conflict or falsely promote independence.

## Verification Boundary

The modified test file was re-read after mutation and the GT-040 assertion was present.

The learning record was created and persisted in the repository.

No CI/runtime PASS is claimed because no workflow execution was exposed for the mutation during verification.

## Closure

GT-040 is recorded as a controlled regression boundary only. No broader canonical rule or promotion is made beyond the tested case.

Next continuation must begin from the committed GT-040 state and test the next distinct provenance boundary without weakening prior GT-037/GT-038/GT-039 constraints.
