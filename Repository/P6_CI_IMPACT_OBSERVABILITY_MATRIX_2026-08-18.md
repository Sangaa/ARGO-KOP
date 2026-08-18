# P6 — CI ↔ IMPACT-MATRIX OBSERVABILITY MATRIX

Date: `2026-08-18`
Status: `BUILD-02 / IMPLEMENTED / EXECUTION-VERIFICATION-PENDING`
Authority: `GOV-013 + GOV-014 + REP-020`
Scope: CI invocation evidence correlated with repository impact/relationship scope.

## Purpose

Define and implement the minimum evidence contract required to connect CI execution to the affected repository relationships, consumers and impact scope without converting workflow success into semantic closure.

P6 addresses an observability gap already identified by the current repository evidence: workflows can emit successful execution evidence, while the current impact matrix does not yet automatically bind that evidence to the specific relationship or affected scope.

## Current Evidence Sources

| Evidence Source | Current State | What It Proves | What It Does Not Prove |
|---|---|---|---|
| `.github/workflows/full-stack-audit.yml` | Modified / active | Full-stack workflow now includes P6 regression + impact-correlation steps | Successful execution of the new steps until CI run evidence exists |
| `.github/workflows/real-matrix-regression.yml` | Present / active | Real mutation-matrix corpus regression executes on relevant changes | Automatic impact-to-CI closure |
| `Quality/Integration/ci_impact_correlation.py` | Implemented / current main | Deterministic changed-path → direct matrix/registry evidence correlation with `UNMAPPED` fail-safe behavior | Semantic relationship proof or automatic promotion |
| `Quality/Integration/test_ci_impact_correlation.py` | Implemented / current main | Regression coverage for mapped and unmapped behavior | CI execution success until workflow evidence is available |
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
| P6-05 | Commit/HEAD is available as correlation key | VERIFIED / used by implementation |
| P6-06 | Changed-path → impact-matrix correlation | IMPLEMENTED / execution evidence pending |
| P6-07 | Workflow-run → affected relationship correlation | IMPLEMENTED / execution evidence pending |
| P6-08 | Automated matrix-state update from CI evidence | NOT_IMPLEMENTED |
| P6-09 | Post-CI repository read-back / reconciliation | NOT_IMPLEMENTED |
| P6-10 | Failure first-boundary preservation | SPECIFIED / implementation pending |
| P6-11 | Model-independent control path | IMPLEMENTED in bounded correlator; CI execution pending |

## Implementation Boundary

`Quality/Integration/ci_impact_correlation.py` reads the actual Git commit range, extracts changed paths, and searches the current `REP-020` and `REP-014` text for direct evidence. A path is classified as:

- `MAPPED` when direct matrix or relationship evidence is found;
- `UNMAPPED` when no direct evidence is found;
- `NO_CHANGES` when the range contains no changed files.

The tool always emits `NO_AUTO_PROMOTION`. It does not infer relationships from folder names, neighboring artifacts or semantic similarity.

`Quality/Integration/test_ci_impact_correlation.py` covers the direct-match and explicit-unmapped cases.

`.github/workflows/full-stack-audit.yml` now executes the regression test and correlation command and uploads `ci-impact-correlation.json` as workflow evidence.

## Current Verification Boundary

The implementation is committed on current `main`, but the GitHub Actions status surface has not yet returned a workflow run/status for the implementation commit. Therefore the implementation is **not yet classified as execution-verified**.

Current state:

`IMPLEMENTED / EXECUTION-VERIFICATION-PENDING`

This is not a failure. It is an evidence boundary.

## Safety Rules

1. CI success never upgrades a relationship above the evidence actually exercised by the workflow.
2. A workflow that tests a fixture does not prove canonical artifact behavior unless the canonical path is explicitly exercised.
3. Runtime evidence emission does not prove downstream service dispatch.
4. A changed-path correlation is impact evidence, not relationship proof.
5. Matrix updates must remain evidence-bearing and must not silently create authority.
6. P6 must consume existing evidence before introducing a new evidence-generation mechanism.
7. If correlation is ambiguous, the affected matrix state remains `REVALIDATION_REQUIRED` or `PARTIALLY_VERIFIED` rather than being auto-promoted.

## Existing CI Boundary

The current Full-Stack workflow executes P4 relationship safety gates, Mutation Matrix regressions, candidate reuse checks, negative executable-consumer regression, the P6 regression/correlation steps, repository-wide audit and real runtime evidence emission. The Real Mutation Matrix workflow separately executes the real matrix corpus regression.

The observability gap is therefore now split into two stages:

1. **Correlation implementation — present.**
2. **Execution/read-back evidence — pending.**

## Build-02 Decision

P6 Build-02 implementation is complete at the code/workflow level but remains open for execution verification.

The next required evidence is:

`CI Run → Job Result → ci-impact-correlation.json → Read-back → Classification → REP-022/Checkpoint Reconciliation`

No workflow result may be inferred from commit existence.

## Current Disposition

`P6 = IMPLEMENTED / EXECUTION-VERIFICATION-PENDING / NO AUTO-PROMOTION`

P3 and P4 remain independent open priorities. P6 does not promote or close any P3/P4 relationship.

---

End of P6 Matrix
