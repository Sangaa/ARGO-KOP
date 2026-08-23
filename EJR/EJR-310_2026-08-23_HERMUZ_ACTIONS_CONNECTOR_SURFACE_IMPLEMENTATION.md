# EJR-310 — HERMUZ GitHub Actions Connector Surface Implementation

Date: 2026-08-23
Status: CLOSED / IMPLEMENTATION CAPTURED / EXECUTION VERIFICATION PENDING
Classification: Connector Capability Extension / P6 Evidence Boundary
Production impact: Connector surface only; no P6 promotion

## Prior-learning gate

The session resumed from the established P6 boundary:
- Workflow definition is verified.
- Run identity is emitted by the workflow.
- The existing commit-to-workflow-run observation helper is PR-trigger limited.
- Jobs/logs/artifacts require an already known Run ID.
- Connector application permission cannot be equated with an exposed connector operation.
- Repeating PR probes was therefore rejected as redundant.

## Gap confirmed

The missing capability was the connector-level Actions surface needed to bridge:

`Invocation / Discovery -> Run ID -> Jobs -> Logs`

The existing repository Contents connector did not expose Actions control/observation operations.

## Implementation

A provider-neutral interface was added:
- `Services/GITHUB_ACTIONS_CONNECTOR_INTERFACE.py`

A concrete GitHub REST implementation was added:
- `Services/GITHUB_ACTIONS_CONNECTOR.py`

The implementation exposes:
- `list_workflow_runs()` with branch/event/head_sha/status filters;
- `get_workflow_run()` with explicit Run ID validation;
- `dispatch_workflow()` using `POST /actions/workflows/{workflow_id}/dispatches`;
- `list_workflow_run_jobs()`;
- `get_workflow_job_logs()`.

Explicit connector failures are preserved through `ConnectorError`. A successful workflow dispatch is represented only after the GitHub request is accepted; GitHub's 204 response is handled without attempting JSON decoding.

## Test coverage added

`Quality/Integration/test_github_actions_connector.py` covers:
- execution filter preservation for Run discovery;
- invalid Run ID rejection;
- workflow dispatch and 204 handling;
- invalid ref rejection;
- explicit HTTP failure classification.

## Commits

- `755b9637b986eeede851974189ff4927cb5f15a9` — interface
- `3a9839e12ef04ccdbcf9c04379bbc9fa8ab4d432` — concrete implementation
- `3b935cc7dda22326590448307365144f74039ada` — tests

## Verification boundary

Repository write/read-back is available for the created artifacts.
No claim is made that the new Actions calls have executed successfully against GitHub from ARGO runtime in this session. The connector token's effective Actions permission and the conversational connector's ability to invoke the new class remain runtime/E2E verification targets.

Therefore:

`Connector surface implemented = VERIFIED`
`Unit-test intent = CAPTURED`
`Live Actions invocation = NOT YET VERIFIED`
`Current-HEAD Run discovery through new surface = NOT YET VERIFIED`
`P6 promotion = FORBIDDEN`

## Reusable learning

The architectural fix is deliberately a separate Actions capability surface rather than silently expanding repository Contents semantics. This preserves the law:

`Repository access != Actions invocation != Execution observation`

The next safe step is a controlled runtime/E2E execution of the new surface, followed by exact Run-ID observation and downstream job/log evidence.

## Closure

This implementation cycle is closed. No P6 status was promoted and no execution claim was inferred from code existence.

End of EJR-310
