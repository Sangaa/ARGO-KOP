# P389 — B07 Matrix Hardening: Race-Boundary and Preflight Coverage

Date: 2026-08-28
Status: `CLOSED / VERIFIED / EXECUTED / ISOLATED / LEARNING RECORDED / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
Resumed from P388. The live B07 implementation and test inventory were inspected before mutation. P388 established the need for an explicit matrix-to-test reconciliation and warned against inheriting coverage claims from checkpoints without live inspection.

## ANALYSIS
The governed dispatcher source enforces several safety branches that were not represented by explicit tests in the current test file: update-time SHA drift, create-time appearance of a file between probes, and empty-content preflight rejection. The dispatcher contract states that the current repository state must be re-read immediately before mutation and that stale transactions must abort; it also rejects empty write content before repository I/O.

The existing inventory already covered: existing-file update with current SHA, missing-file create, necessity evidence, post-write read-back mismatch, and path traversal rejection. Therefore this mutation targets only genuinely uncovered branches.

## WORK
Added three focused executable tests to `Quality/Integration/test_governed_write_dispatch.py`:

1. `test_update_aborts_when_sha_changes_at_write_boundary`
2. `test_create_aborts_when_file_appears_at_write_boundary`
3. `test_empty_content_is_rejected_before_io`

No production/provider implementation, Governance, Canonical content, or runtime code was modified.

## EXECUTION EVIDENCE
Mutation commit: `0c127656af875172a98611e8fc2839d39a45aacb`

Read-back of the mutated test file: `PASS`.

The commit diff contains only `Quality/Integration/test_governed_write_dispatch.py` and only the three targeted tests.

Exact-head workflow observations for `0c127656...`:
- `ARGO Runtime Prototype and Integration Tests` run `33151516131` — `success`
- `Full-Stack Repository Audit` run `33151516026` — `success`

Runtime workflow jobs all completed successfully: `integration-tests`, `integrity-tests`, and `prototype-tests`. The integration job's `Run integration quality suite` step succeeded; integrity gates and prototype/canonical acceptance steps also succeeded.

## EVIDENCE STATE
- Existing-file update/current SHA: `PROVEN + EXECUTED`.
- Stale SHA rejection: `PROVEN + EXECUTED`.
- Post-write read-back mismatch: `PROVEN + EXECUTED`.
- Connector unavailability propagation: `PROVEN + EXECUTED`.
- Update-time SHA drift at write boundary: `PROVEN + EXECUTED`.
- Create-time file appearance at write boundary: `PROVEN + EXECUTED`.
- Empty-content preflight rejection: `PROVEN + EXECUTED`.
- Runtime prototype suite: `PROVEN / PASS`.
- Integration suite: `PROVEN / PASS`.
- Integrity suite: `PROVEN / PASS`.
- Full-stack audit: `PROVEN / PASS`.
- B07 complete matrix: `SUBSTANTIALLY COVERED / FINAL MATRIX AUDIT STILL REQUIRED`.
- B08 real-provider dispatch: `UNPROVEN`.
- Canonical promotion: `NOT JUSTIFIED`.

## ERROR / LEARNING EXPERIENCE
**EL-004 — Matrix gaps must be derived from live implementation and test inventory.** A checkpoint can identify a suspected gap, but only current source inspection can establish whether the gap is real.

**EL-005 — Safety-critical race boundaries deserve explicit executable coverage.** A contract statement such as "re-read immediately before write" is stronger when both create and update race branches have executable regression tests.

**EL-006 — Preflight invariants should be tested as no-I/O properties.** Rejecting invalid input before repository access protects the boundary and makes the safety rule independently observable.

## KNOWLEDGE DELTA
**KD-081 — Coverage state is a property of the live implementation/test inventory, not of session memory.**

**KD-082 — A governed write contract should map each safety invariant to an explicit test branch where practical: existence routing, evidence requirement, stale-state protection, pre-write race protection, mutation failure propagation, and post-write persistence verification.**

**KD-083 — Passing the full CI workflow proves execution of the selected suite on the exact HEAD, but does not by itself prove that every conceptual matrix cell exists; matrix completeness still requires explicit mapping.**

## CHECKPOINT
`P389 → construct explicit B07 matrix-to-test mapping → reconcile every required safety branch against live tests → execute exact-head suite → close remaining B07 gaps only when mapped and evidenced → then controlled B08 real-provider observation.`

## CLOSE
`CLOSED / VERIFIED / EXECUTED / ISOLATED / LEARNING RECORDED / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
