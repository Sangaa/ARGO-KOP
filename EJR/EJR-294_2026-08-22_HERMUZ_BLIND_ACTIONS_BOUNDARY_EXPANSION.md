# EJR-294 — HERMUZ Blind Actions Boundary Expansion

Date: 2026-08-22
Status: CLOSED / DIAGNOSTIC LEARNING CAPTURED
Classification: Architectural Learning / Connector Capability Boundary
Production impact: NONE

## Trigger

Following EJR-432, HERMUZ was instructed to search beyond the previously assumed GitHub connector boundary rather than treating the exercised surface as the full environment.

## Prior-learning check

Relevant prior evidence was retrieved before new reasoning:
- EJR-279: Actions evidence boundary was previously identified.
- EJR-432: GOV-013 now requires Prior-Learning Retrieval before new solution work.
- Issue #11: dispatch is not exposed through the connected surface; historical retry returned 403; commit-run helper was limited to PR-triggered discovery.
- Issue #21: repository access and CI evidence were classified as distinct surfaces.

## Blind-search experiment

The investigation intentionally widened the search domain:

1. Search ARGO for Actions/run identifiers and references.
2. Search PRs/issues for historical Actions evidence.
3. Test generic GitHub fetch against Actions collection endpoints.
4. Test generic fetch against an exact known public workflow-run resource from another accessible repository.
5. Test specialized workflow-run job and job-log readers using the exact known public run/job IDs.
6. Compare the result with the ARGO-specific evidence boundary.

## Observations

### Generic collection boundary

Generic fetch of an Actions collection such as `/actions/runs` is rejected by the connector surface.

### Exact-resource observation

When a valid workflow `run_id` is already known, the generic fetch surface can read that exact public workflow-run resource.

### Specialized downstream observation

When a valid run/job identifier is known, the specialized Actions surfaces can read:
- workflow-run jobs;
- job steps;
- decoded job logs.

A public control experiment against `KAFKA2306/agent-resources` run `32426146718` and job `96608388051` demonstrated this end-to-end.

### ARGO-specific boundary

No valid ARGO workflow `run_id` was recovered through the available discovery paths. Searches for `actions/runs/`, `workflow_runs`, `run_id`, and `github-actions` commit references did not yield an ARGO run identity. PR #10 head `1e93713cfc7fd05e28d6cec23aa072046378d64a` returned combined statuses as an empty set.

## Revised model

The earlier model "Actions are unavailable" is too broad.

The supported evidence is:

`Actions Observation = ID-Dependent`

`Run/Job/Log readers = AVAILABLE when identifiers are known`

`Run discovery for ARGO = NOT ESTABLISHED`

`Workflow dispatch surface = NOT EXPOSED`

Therefore:

`NO OBSERVED RUN != NO RUN EXISTS`

and:

`NO RUN ID != NO EXECUTION`

## Architectural learning

The environment is larger than the initially exercised observation frame. HERMUZ must distinguish:

1. capability exists;
2. capability is exposed through the current connector;
3. capability can be invoked;
4. resulting state can be discovered;
5. resulting state can be read downstream;
6. absence of state is actually proven.

A tool boundary must never be promoted into a world-state claim without a discovery proof.

## Reusable diagnostic rule

For future connector investigations:

`Prior Learning → Capability Inventory → Discovery Surface → Exact-ID Probe → Downstream Evidence Probe → World-State Conclusion`

If discovery is unavailable but exact-ID observation works, classify the boundary as `OBSERVATION_ID_DEPENDENT`, not `RESOURCE_ABSENT`.

## P6 impact

No P6 logic, relationship, Runtime evidence, or governance state was promoted.
P6 remains execution-verification-pending until an authoritative current-HEAD run identity and its evidence are established.

## Closure

This experiment materially refined the GitHub capability model and was recorded as reusable architectural learning. No production logic was changed.

End of EJR-294