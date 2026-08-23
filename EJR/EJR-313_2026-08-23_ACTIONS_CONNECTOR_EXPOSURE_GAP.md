# EJR-313 — ACTIONS CONNECTOR EXPOSURE GAP

Date: 2026-08-23
Status: CLOSED — DOCUMENTED BOUNDARY
Checkpoint: ACTIONS_CONNECTOR_EXPOSURE_GAP

## Finding

`list_workflow_runs(head_sha=...)` exists in the ARGO KOP repository implementation of the GitHub Actions connector, but it is not exposed as a callable operation in the current HERMUZ session tool surface.

## Evidence Boundary

- GitHub REST API capability: the Actions runs endpoint supports `head_sha` filtering.
- Repository implementation: the dedicated Actions connector contains the intended `list_workflow_runs(...)` capability.
- Current session exposure: no callable session operation was available for `list_workflow_runs(head_sha=...)`.
- Generic GitHub fetch is not a substitute: the tested generic surface rejects the Actions runs/check-runs endpoints as not allowed.
- Existing PR-scoped workflow-run observation must not be interpreted as general Run-ID discovery.

## Gap Classification

**Gap Name:** ACTIONS_CONNECTOR_EXPOSURE_GAP

**Method:** `list_workflow_runs`

**Required parameter:** `head_sha`

**Repository status:** IMPLEMENTED

**Session-exposed status:** NOT EXPOSED

**Impact:** Current HERMUZ session cannot perform general commit/SHA → Run-ID discovery through the dedicated Actions connector surface.

## Decision

1. Do not run additional probes against generic fetch.
2. Do not reuse the PR-triggered `fetch_commit_workflow_runs` operation as general Run-ID discovery.
3. Do not add another connector or duplicate the existing implementation.
4. Do not modify the canonical workflow merely to work around the exposure gap.
5. Do not promote P6 to execution-verified status.
6. Treat the current session operation registry/tool exposure as a separate capability boundary from repository implementation.

## Next Safe Investigation

Review the connector manifest/tool-registration layer and determine whether the current session can extend its exposed operation surface. If that registry is fixed outside the session, the gap is outside the authority of the current session and must remain documented rather than worked around.

## Reusable Learning

**Provider capability ≠ repository implementation ≠ session-exposed capability.**

A method being implemented in repository code does not establish that HERMUZ can invoke it. Conversely, a generic connector operation being available does not establish that it exposes the provider endpoint needed for the task.

This checkpoint closes the current probe loop and converts the remaining uncertainty into a precisely bounded connector-exposure question.

## P6 State

`IMPLEMENTED / EXECUTION EVIDENCE PENDING`

Run-ID discovery: NOT DISCOVERED
Connector implementation: PRESENT
Session exposure: NOT EXPOSED
Mutation in this checkpoint: DOCUMENTATION ONLY
