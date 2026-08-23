# EJR-315 — Actions Connector Runtime Exposure Checkpoint

**Date:** 2026-08-23
**Status:** CLOSED — BOUNDARY VERIFIED
**Related gap:** ACTIONS_CONNECTOR_EXPOSURE_GAP

## Finding

The GitHub Actions capability is implemented on the repository side, including the `head_sha` execution-discovery parameter, but the current HERMUZ session tool surface does not expose a callable operation for `list_workflow_runs(head_sha=...)`.

## Evidence boundary

1. `Services/GITHUB_ACTIONS_CONNECTOR_INTERFACE.py` defines `list_workflow_runs()` with `head_sha`.
2. `Services/GITHUB_ACTIONS_CONNECTOR.py` implements the method and forwards `head_sha` as a GitHub Actions API query parameter.
3. The current session exposes other Actions operations, but does not expose the dedicated `list_workflow_runs` operation needed for general Run-ID discovery.
4. Generic fetch is not treated as an equivalent capability because its endpoint allowlist rejects the relevant Actions discovery endpoint.
5. `fetch_commit_workflow_runs` is not treated as a general substitute because its observable behavior is limited and cannot establish general execution absence.

## Decision

- Do not modify the Actions connector implementation; repository-side implementation is already verified.
- Do not add another connector.
- Do not use generic fetch for this discovery problem.
- Do not repeat PR-scoped workflow-run probes.
- Do not add repository self-commit evidence as a workaround.
- Do not promote P6.
- Treat runtime/tool exposure as the remaining boundary.

## Reusable learning

**Capability layering rule:**

`Provider capability != repository implementation != interface contract != session-exposed operation`

A capability can be completely correct in the provider API and in ARGO's repository code while remaining unavailable to HERMUZ if the session tool-registration/exposure layer does not surface it.

## Next checkpoint

Review the connector/tool registration or runtime exposure layer only if that layer becomes inspectable or modifiable. Until then, no further GitHub Actions probes are justified.

## P6 state

`IMPLEMENTED / EXECUTION EVIDENCE PENDING`

No execution claim is made from the absence of an exposed discovery operation.
