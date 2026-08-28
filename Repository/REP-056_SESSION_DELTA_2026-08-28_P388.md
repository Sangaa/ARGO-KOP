# P388 — B07 Coverage Reconciliation: Error Learning and Exception Path

Date: 2026-08-28
Status: `CLOSED / VERIFIED / EXECUTED / ISOLATED / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
Resumed from P387. P387 classified B07 as substantially covered and listed read-back mismatch and connector-exception behavior as remaining explicit coverage targets.

## ANALYSIS
A fresh repository inspection found that the governed dispatcher already contains an explicit hard-failure test for post-write read-back mismatch: `test_readback_mismatch_is_a_hard_failure` in `Quality/Integration/test_governed_write_dispatch.py`. The dispatcher contract itself requires exact post-mutation content equality and raises `POST_WRITE_READBACK_MISMATCH` on mismatch.

Therefore no duplicate read-back mismatch test was added. This corrects the prior P387 characterization from `explicit case not yet present` to `existing explicit coverage present`.

This is recorded as an error-learning event: the earlier checkpoint relied on an incomplete inspection of the current test inventory. The corrective behavior is to reconcile the live repository before adding tests and to distinguish `missing coverage` from `coverage not yet inspected/reconciled`.

## WORK
Added one targeted connector integration test:
`test_update_propagates_connector_unavailability`

The test forces the initial GET/read-current observation to succeed, then forces the PUT transport to raise `urllib.error.URLError`. It verifies that the connector exposes the governed `ConnectorError` with `GITHUB_CONNECTOR_UNAVAILABLE` and that the call sequence is exactly `GET → PUT`.

No production/provider implementation, Governance, or Canonical content was modified.

## EXECUTION EVIDENCE
Target commit: `88c3df00b989d2692e1db63ca20823795c766e41`

Commit inspection confirms the mutation is limited to `Quality/Integration/test_github_repository_connector.py` and adds only the exception-propagation test.

Observed workflow runs for the exact target commit:
- `ARGO Runtime Prototype and Integration Tests` run `33148883399` — `success`
- `Full-Stack Repository Audit` run `33148883388` — `success`

The runtime test workflow completed `prototype-tests`, `integration-tests`, and `integrity-tests` successfully; the integration job completed `Run integration quality suite` successfully.

## EVIDENCE STATE
- Read-back mismatch test: `PROVEN BY SOURCE + EXISTING EXPLICIT EXECUTABLE COVERAGE`
- Connector exception test source: `PROVEN`
- Connector exception path exact-head execution: `PROVEN / PASS`
- Runtime prototype suite: `PROVEN / PASS`
- Integration suite: `PROVEN / PASS`
- Integrity suite: `PROVEN / PASS`
- Full-stack audit: `PROVEN / PASS`
- B07 observed-SHA update path: `PROVEN + EXECUTED` (from P387)
- B07 stale-SHA rejection: `PROVEN + EXECUTED` (from P387)
- B07 complete matrix: `NOT YET CLOSED` — explicit full matrix-to-test mapping remains required
- B08 real-provider dispatch: `UNPROVEN`
- Canonical promotion: `NOT JUSTIFIED`

## ERROR LEARNING
**EL-001 — Incomplete inventory inspection can create a false coverage gap.** Before adding a test, inspect the current repository test inventory and reconcile prior claims against live source.

**EL-002 — A corrected classification is itself valuable evidence.** When a prior statement is shown to be outdated or incomplete, preserve the correction rather than silently replacing history.

**EL-003 — Test additions should target genuinely uncovered behavior.** Once read-back mismatch coverage was found to exist, the mutation was narrowed to the genuinely missing connector-exception path.

## KNOWLEDGE DELTA
**KD-078 — Coverage claims require live inventory reconciliation, not checkpoint inheritance alone.**

**KD-079 — Existing executable coverage can satisfy a matrix branch even when the latest session did not create it; evidence ownership must remain tied to the test and exact execution that established it.**

**KD-080 — Error learning includes correcting the model of repository state and preventing duplicate or unnecessary mutations.**

## CHECKPOINT
`P388 → build explicit B07 matrix-to-test mapping from live repository tests → identify only genuinely uncovered branches → execute targeted cases on exact HEADs → close B07 only when all required branches have evidence → then controlled B08 real-provider observation.`

## CLOSE
`CLOSED / VERIFIED / EXECUTED / ISOLATED / ERROR-LEARNING RECORDED / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
