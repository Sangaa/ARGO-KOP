# P6 — CI ↔ IMPACT-MATRIX OBSERVABILITY MATRIX

Date: `2026-08-18`
Status: `BUILD-01 / SPECIFICATION-ESTABLISHED / IMPLEMENTATION-PENDING`
Authority: `GOV-013 + GOV-014 + REP-020`
Scope: CI invocation evidence correlated with repository impact/relationship scope.

## Purpose

Define the minimum evidence contract required to connect CI execution to the affected repository relationships, consumers and impact scope without converting workflow success into semantic closure.

P6 addresses an observability gap already identified by the current repository evidence: workflows can emit successful execution evidence, while the current impact matrix does not yet automatically bind that evidence to the specific relationship or affected scope.

## Current Evidence Sources

| Evidence Source | Current State | What It Proves | What It Does Not Prove |
|---|---|---|---|
| `.github/workflows/full-stack-audit.yml` | Present / active | Full-stack workflow executed configured audit and evidence-emission steps | Repository-wide semantic integrity |
| `.github/workflows/real-matrix-regression.yml` | Present / active | Real mutation-matrix corpus regression executes on relevant changes | Automatic impact-to-CI closure |
| `Quality/Integration/emit_ci_runtime_evidence.py` | Present / active | CI can emit a runtime-produced evidence artifact without canonical promotion | Relationship verification or semantic correctness |
| `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | Provisional / current | Artifact → relationship → consumer/dependency lookup surface | CI correlation by itself |
| `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | Canonical / active | Relationship identity, evidence and state registry | CI execution semantics by itself |

## Required P6 Control Chain

`CI Invocation → Commit/HEAD → Changed Scope → Affected Matrix Entries → Relationship/Consumer Scope → Workflow/Job Evidence → Test Result → Evidence Classification → Matrix Update → Checkpoint`

## Minimum Evidence Record

Every CI-to-impact observation should capture, where available:

- workflow name;
- workflow run identifier;
- triggering commit SHA;
- base commit SHA where applicable;
- changed paths;
- affected matrix/relationship IDs;
- impacted consumers/dependencies;
- job/check identifier;
- result: `PASS / FAIL / NOT_TESTED / NOT_APPLICABLE`;
- evidence artifact or log reference;
- classification: `STRUCTURAL / CONTRACT / IMPLEMENTED / INTEGRATION-TESTED / RUNTIME-VERIFIED`;
- reconciliation state;
- checkpoint.

## P6 Gates

| Gate | Requirement | Current State |
|---|---|---|
| P6-01 | Existing CI workflows inventoried | VERIFIED within inspected workflow scope |
| P6-02 | Existing CI runtime evidence emission inspected | VERIFIED |
| P6-03 | Existing REP-020 impact/consumer matrix inspected | VERIFIED |
| P6-04 | CI result is distinguishable from semantic relationship verification | VERIFIED |
| P6-05 | Commit/HEAD is available as correlation key | AVAILABLE / not yet automatically bound |
| P6-06 | Changed-path → impact-matrix correlation | NOT_IMPLEMENTED |
| P6-07 | Workflow-run → affected relationship correlation | NOT_IMPLEMENTED |
| P6-08 | Automated matrix-state update from CI evidence | NOT_IMPLEMENTED |
| P6-09 | Post-CI repository read-back / reconciliation | NOT_IMPLEMENTED |
| P6-10 | Failure first-boundary preservation | SPECIFIED / implementation pending |
| P6-11 | Model-independent control path | REQUIRED / implementation pending |

## Safety Rules

1. CI success never upgrades a relationship above the evidence actually exercised by the workflow.
2. A workflow that tests a fixture does not prove canonical artifact behavior unless the canonical path is explicitly exercised.
3. Runtime evidence emission does not prove downstream service dispatch.
4. A changed-path correlation is impact evidence, not relationship proof.
5. Matrix updates must remain evidence-bearing and must not silently create authority.
6. P6 must consume existing evidence before introducing a new evidence-generation mechanism.
7. If correlation is ambiguous, the affected matrix state remains `REVALIDATION_REQUIRED` or `PARTIALLY_VERIFIED` rather than being auto-promoted.

## Existing CI Boundary

The current Full-Stack workflow already executes P4 relationship safety gates, Mutation Matrix regressions, candidate reuse checks, negative executable-consumer regression, a repository-wide audit and real runtime evidence emission. The Real Mutation Matrix workflow separately executes the real matrix corpus regression.

The observability gap is therefore **correlation**, not absence of CI execution.

## Build-01 Decision

P6 Build-01 establishes the specification and evidence contract only.

No workflow mutation is authorized by this matrix alone.

Implementation requires a separate controlled change with:

`Existing Workflow Read → Impact Correlation Design → Test Fixture → Failure Boundary → Controlled Workflow Change → CI Run → Evidence Read-back → REP-020 Reconciliation → Checkpoint`

## Current Disposition

`P6 = SPECIFICATION-ESTABLISHED / IMPLEMENTATION-PENDING`

P3 and P4 remain independent open priorities. P6 does not promote or close any P3/P4 relationship.

---

End of P6 Matrix
