# EJR-316 — Runtime Exposure Boundary Review

Date: 2026-08-23
Status: CLOSED / VERIFIED BOUNDARY
Related: ACTIONS_CONNECTOR_EXPOSURE_GAP, EJR-315

## Finding

A targeted repository-side inspection was performed to determine whether the missing HERMUZ session exposure can be resolved from the existing Runtime/Services implementation.

## Evidence

1. `Services/README.md` defines Services as reusable operational capabilities and explicitly states that the Services layer supports Runtime, but services do not become the source of truth.
2. `Services/SRV-001_SERVICE_ARCHITECTURE.md` defines the canonical service lifecycle and says service-to-runtime relationships require direct verification; its implementation and cross-layer integration are not globally certified.
3. `Runtime/README.md` defines Runtime as the governed execution layer and its lifecycle, but does not identify a session tool registry or dynamic tool-registration mechanism.
4. `Runtime/Execution/connected_spine_runner.py` demonstrates a repository-side execution runner, but its imports and execution path do not expose a generic connector/tool registry.
5. `.github/workflows/` contains repository workflows, but no repository evidence was found that these workflows constitute the HERMUZ session tool-registration layer.

## Decision

Do not invent or add a session tool registry inside ARGO KOP solely to close the current P6 evidence gap.

The repository currently provides:

- GitHub Actions connector contract: VERIFIED
- GitHub Actions connector implementation: VERIFIED
- `head_sha` propagation: VERIFIED
- Runtime execution architecture: PRESENT
- Concrete HERMUZ session tool-registration mechanism: NOT VERIFIED

## Boundary

`Provider capability != repository implementation != interface contract != runtime implementation != session-exposed operation`.

The missing session exposure therefore remains an external/undetermined boundary from the repository evidence currently available.

## P6 State

`P6 = IMPLEMENTED / EXECUTION EVIDENCE PENDING`

No promotion to PASS/FAIL is authorized.

## Prohibited Next Actions

- No repeated GitHub Actions probes through blocked generic fetch.
- No repeated PR-scoped discovery probe as a substitute for general Run-ID discovery.
- No duplicate connector implementation.
- No speculative runtime registry creation.

## Future Next Step

Only when the actual tool/runtime registration surface becomes observable or explicitly exposed should the `list_workflow_runs(head_sha=...)` operation be tested as a session-callable capability.

## Learning

A repository can contain a complete connector contract and implementation while the active AI session still lacks the operation. Capability exposure is an independent evidence boundary and must be verified separately.

## Session Closure

Execution: completed.
Mutation: documentation only.
Verification: required read-back after write.
P6 promotion: none.
Session: CLOSED.
