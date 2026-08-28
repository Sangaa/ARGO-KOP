# P387 — B07 Observed-SHA Behavioral Coverage

Date: 2026-08-28
Status: `CLOSED / VERIFIED / EXECUTED / ISOLATED / NO CANONICAL MUTATION / NO PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
Resumed from P386. P386 established an observable CI channel on exact HEADs and required mapping successful CI coverage to the B07 matrix before declaring behavioral closure.

## WORK
Added one targeted B07 integration test: `test_update_uses_observed_sha_and_returns_commit`.

The test uses a provider-neutral fake transport and verifies that update behavior:
- reads the current artifact identity first;
- uses the observed SHA in the PUT payload;
- returns the resulting commit identity.

Existing stale-SHA rejection coverage remains intact. No production/provider behavior, Governance, or Canonical content was modified.

## EXECUTION EVIDENCE
Target commit: `d5b836d325057f0c09ef7f9d09f63779d7ba7930`

Observed workflow runs:
- `ARGO Runtime Prototype and Integration Tests` run `33148697030` — completed successfully.
- `Full-Stack Repository Audit` run `33148697040` — completed successfully.

Runtime/integration jobs:
- `integrity-tests` = success
- `prototype-tests` = success
- `integration-tests` = success

The integration job reached and completed `Run integration quality suite` successfully. The full-stack audit also completed current-checkout SHA binding and all listed repository/runtime boundary gates successfully.

## ANALYSIS
This is stronger than source-only evidence for the newly added observed-SHA path because the exact commit produced observable successful CI execution through the integration suite. It still does not prove every B07 semantic branch, because the complete matrix includes additional cases such as read-back content mismatch and connector exception behavior.

Therefore B07 is classified as `SUBSTANTIALLY COVERED / NOT FULLY CLOSED`, pending explicit coverage mapping for remaining matrix cases.

## EVIDENCE STATE
- Targeted observed-SHA update test source: `PROVEN`
- Exact-head CI execution: `PROVEN`
- Integration suite: `PROVEN / PASS`
- Integrity suite: `PROVEN / PASS`
- Prototype suite: `PROVEN / PASS`
- Full-stack audit: `PROVEN / PASS`
- Stale-SHA rejection: `PROVEN BY SOURCE + EXECUTED SUITE`
- Successful observed-SHA update path: `PROVEN BY SOURCE + EXECUTED SUITE`
- Read-back mismatch semantics: `PARTIALLY COVERED / EXPLICIT CASE NOT YET PRESENT`
- Connector exception propagation: `PARTIALLY COVERED / EXPLICIT CASE NOT YET PRESENT`
- B07 complete behavioral matrix: `NOT YET CLOSED`
- B08 real-provider dispatch: `UNPROVEN`
- Canonical promotion: `NOT JUSTIFIED`

## KNOWLEDGE DELTA
**KD-076 — Exact-head CI execution can convert a targeted provider-neutral B07 case from source evidence to executed behavioral evidence, provided the relevant suite is actually reached and completed.**

**KD-077 — Successful suite execution does not automatically imply complete matrix coverage; closure requires explicit mapping from test cases to behavioral branches.**

## CHECKPOINT
`P387 → add/execute explicit read-back mismatch case → add/execute explicit connector-exception case → map all B07 cases to observed tests → close B07 only when coverage is complete → then controlled B08 real-provider observation.`

## CLOSE
`CLOSED / VERIFIED / EXECUTED / ISOLATED / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
