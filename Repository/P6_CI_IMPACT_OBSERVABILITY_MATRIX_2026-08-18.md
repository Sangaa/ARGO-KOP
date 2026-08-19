# P6 — CI ↔ IMPACT-MATRIX OBSERVABILITY MATRIX

Date: `2026-08-18`
Status: `BUILD-02 / LAYERED-VERIFICATION-REBUILD / EXECUTION-VERIFICATION-PENDING`
Authority: `GOV-013 + GOV-014 + REP-020`
Scope: CI invocation evidence correlated with repository impact/relationship scope.

## Purpose

Define and implement the minimum evidence contract required to connect CI execution to affected repository relationships, consumers and impact scope without converting workflow success into semantic closure.

## Core Testing Decision

P6 is a layered control, not a single atomic assertion. Its verification MUST preserve first-failure boundaries instead of collapsing observation, identity, artifact and classification failures into one P6 failure.

Required layered chain:

`P6-A Functional → P6-B Observation → P6-C Identity → P6-D Artifact → P6-E Classification/Reconciliation`

Each layer must have an explicit result and regression coverage.

### Layer contracts

| Layer | Question | Allowed result |
|---|---|---|
| P6-A | Did the functional logic execute correctly? | `PASS / FAIL` |
| P6-B | Is the expected CI run/job observable? | `PRESENT / MISSING / INVALID` |
| P6-C | Does execution bind to the intended baseline/HEAD? | `CURRENT / STALE / MISMATCH` |
| P6-D | Does artifact evidence exist and bind to the run? | `VALID / INVALID / MISSING` |
| P6-E | What state is justified after all available evidence? | explicit classification |

A layer failure MUST NOT be relabeled as another layer's failure.

## Evidence Classification

A successful historical run remains valid execution evidence. If its run/artifact SHA differs from the current baseline it is classified `VALID_EXECUTION_STALE_BASELINE`, not `EXECUTION_FAILED`.

A connector/query returning zero observations is `NO_OBSERVATION`; it is not evidence of `NO_EXECUTION` unless the query surface is proven complete for the trigger type.

## Current Evidence Sources

| Evidence Source | State | Boundary |
|---|---|---|
| `.github/workflows/full-stack-audit.yml` | active | executes P6 correlation + layered regressions |
| `Quality/Integration/ci_impact_correlation.py` | implemented | deterministic path correlation + evidence classification |
| `Quality/Integration/test_ci_impact_correlation.py` | implemented | direct mapping + stale/current/failed classification |
| `Quality/Integration/test_p6_layered_boundaries.py` | implemented | first-boundary isolation across P6-A..P6-E |
| `Quality/Integration/emit_ci_runtime_evidence.py` | active | runtime-produced evidence artifact |
| `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | provisional/current | impact lookup surface |
| `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | canonical/active | relationship identity/state/evidence |

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

| Gate | Requirement | State |
|---|---|---|
| P6-01 | Existing CI workflows inventoried | VERIFIED |
| P6-02 | CI runtime evidence emission inspected | VERIFIED |
| P6-03 | REP-020 impact/consumer matrix inspected | VERIFIED |
| P6-04 | CI result distinguished from semantic relationship verification | VERIFIED |
| P6-05 | Commit/HEAD available as correlation key | VERIFIED |
| P6-06 | Changed-path → impact-matrix correlation | IMPLEMENTED |
| P6-07 | Workflow-run → affected relationship correlation | IMPLEMENTED / execution evidence pending |
| P6-08 | Automated matrix-state update from CI evidence | NOT_IMPLEMENTED |
| P6-09 | Post-CI repository read-back / reconciliation | NOT_IMPLEMENTED |
| P6-10 | Failure first-boundary preservation | IMPLEMENTED as layered regression |
| P6-11 | Model-independent control path | IMPLEMENTED in bounded correlator |

## Layered Regression Requirement

`Quality/Integration/test_p6_layered_boundaries.py` isolates:

1. functional failure;
2. missing CI observation;
3. stale/current SHA identity;
4. artifact missing/mismatch;
5. final execution classification.

The full-stack workflow executes this regression independently from the original P6 correlation regression.

## Safety Rules

1. CI success never upgrades a relationship above the evidence actually exercised by the workflow.
2. A fixture test does not prove canonical artifact behavior unless the canonical path is explicitly exercised.
3. Runtime evidence emission does not prove downstream service dispatch.
4. Changed-path correlation is impact evidence, not relationship proof.
5. Matrix updates remain evidence-bearing and cannot silently create authority.
6. P6 consumes existing evidence before introducing new evidence-generation mechanisms.
7. Ambiguous correlation remains `REVALIDATION_REQUIRED` or `PARTIALLY_VERIFIED`.
8. No observation is not equivalent to no execution.
9. Historical success is never relabeled as execution failure solely because it is stale.
10. Layered tests must preserve the first failing boundary for review and debugging.

## Construction Rule

Any future test combining execution, observation, identity, artifacts or reconciliation MUST be decomposed into independently testable stages before promotion. Compactness is secondary to fault localization.

## Current Verification Boundary

Implementation and layered regression are now committed to `main`. Runtime execution evidence for the newest implementation commit remains pending. No workflow result is inferred from commit existence.

## Current Disposition

`P6 = LAYERED-VERIFICATION-REBUILD / IMPLEMENTED / EXECUTION-VERIFICATION-PENDING / NO-AUTO-PROMOTION`

No P3/P4 relationship is promoted or closed by P6.

---

End of P6 Matrix
