# EJR-296 — HERMUZ Blind Repository Phenomena and Connector Laws

Date: 2026-08-22
Status: CLOSED / DIAGNOSTIC LEARNING CAPTURED
Classification: Architectural Learning / Connector Capability Boundary
Production impact: NONE

## Purpose

Test the hypothesis that observable GitHub phenomena may leave evidence outside the initially assumed Actions observation surface, and identify the governing relationships before declaring a resource absent.

## Prior-learning gate

Prior evidence reviewed before new reasoning:
- EJR-432: mandatory prior-learning retrieval gate.
- EJR-294: blind Actions boundary expansion and ID-dependent observation.
- EJR-295: controlled PR state experiment and run-identity boundary.
- Issue #11: historical connector boundary and Actions evidence constraint.
- Issue #21: repository-access vs CI-execution capability separation.

## Blind search observations

A repository-wide search was performed without restricting the investigation to `.github/workflows` or the Actions surface.

The search found workflow/execution phenomena represented in multiple repository layers:
- `.github/workflows/full-stack-audit.yml` — authoritative workflow definition.
- `Runtime/RUN-005_RUNTIME_WORKFLOW.md`, `Runtime/RUN-009_RECOVERY.md`, `Runtime/RUN-010_RUNTIME_REFERENCE.md`, and `Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md` — runtime-side workflow/evidence descriptions.
- `Quality/Integration/VERIFIED_SEAM_EVIDENCE_REGISTRY.md` — integration evidence surface.
- `Memory/Engineering_Journal/EJR-225...` — prior CI-channel installation/evidence boundary.
- EJR records and Repository session-closure records — historical state/evidence traces.
- PR history — execution-probe and P6 validation events.
- Issue #11 — explicit connector/action evidence boundary.

This demonstrates a concrete phenomenon: repository state and execution knowledge are distributed across multiple evidence surfaces. Searching only the Actions surface cannot exhaust the repository's observable evidence.

## Workflow law discovered

The current `full-stack-audit.yml` explicitly declares all three trigger classes:
- `push` to `main`;
- `pull_request` to `main`;
- `workflow_dispatch`.

The workflow also writes `github.run_id`, `github.event_name`, `github.ref`, `github.sha`, and checkout SHA into `ci-execution-identity.json`, then uploads that file as a workflow artifact.

Therefore, if an authoritative run occurs, the repository-defined execution law provides an exact run identity inside the execution evidence itself.

## Connector law discovered

Issue #11 records that the connected GitHub surface cannot dispatch `workflow_dispatch`, despite the repository workflow declaring it. The same issue records that repository read/write works and that the commit-run helper exposes only PR-triggered runs. The connector application metadata shown in the issue includes Actions write, Checks read, Contents write, Statuses read, and Workflows write permissions.

This establishes a crucial distinction:

`GitHub/App Permission != Exposed Connector Operation != Observed World State`

A permission existing at the application level does not prove that the conversational connector exposes the corresponding operation to HERMUZ.

## Blind-search law

The investigation produced the following reusable rule:

`Phenomenon exists -> search all evidence surfaces -> identify repeated relationships -> infer candidate law -> test the law -> only then classify absence`

A search constrained to the initially assumed environment can produce a false absence even when the phenomenon leaves traces elsewhere.

## Revised model

The repository environment must be modeled as a distributed evidence system:

`Repository files + commits + branches + PRs + issues + workflow definitions + runtime evidence + artifacts`

The connector must separately be modeled as:

`Tool capability -> connector exposure -> invocation -> discovery -> exact-ID observation`

No layer may be silently substituted for another.

## Result

The blind search did not yet recover an authoritative current-HEAD ARGO Actions run ID. It did, however, recover the workflow's own run-identity mechanism and the historical connector boundary from a different repository surface.

Therefore the unresolved problem is narrower than "GitHub Actions unavailable":

`CURRENT-HEAD RUN ID DISCOVERY / AUTHORIZED INVOCATION = UNRESOLVED`

while:

`WORKFLOW DEFINITION = VERIFIED`
`RUN-ID EMISSION CONTRACT = VERIFIED`
`EXACT-ID DOWNSTREAM OBSERVATION = PROVEN AVAILABLE`

## P6 impact

No P6 logic, relationship, Runtime evidence, or governance state was promoted.
P6 remains execution-verification-pending.

## Reusable diagnostic pattern

`Prior Learning -> Blind Multi-Surface Search -> Phenomenon Confirmation -> Law Candidate -> Controlled Test -> Failure/Success Learning -> Boundary Classification -> Cleanup/Closure`

## Closure

The experiment is closed as a learning checkpoint. No production logic was modified. The finding is reusable for future ARGO self-diagnostics: when an expected phenomenon is not visible in the normal observation channel, search for its traces across the wider evidence environment before concluding that the phenomenon is absent.

End of EJR-296