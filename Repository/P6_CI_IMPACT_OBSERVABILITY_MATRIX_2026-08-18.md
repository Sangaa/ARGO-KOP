# P6 — CI ↔ IMPACT-MATRIX OBSERVABILITY MATRIX

Date: `2026-09-01`
Status: `BUILD-03 / P6-08+P6-09 IMPLEMENTED / EXECUTION-VERIFICATION-PENDING`
Authority: `GOV-013 + GOV-014 + REP-020`
Scope: CI invocation evidence correlated with repository impact/relationship scope.

## Purpose

Define and implement the minimum evidence contract required to connect CI execution to affected repository relationships, consumers and impact scope without converting workflow success into semantic closure or repository mutation authority.

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
| `.github/workflows/full-stack-audit.yml` | active | executes P6 correlation + layered regressions and uploads CI-impact evidence |
| `Quality/Integration/ci_impact_correlation.py` | implemented Build-03 | deterministic path correlation + bounded reconciliation candidate + read-back result |
| `Quality/Integration/p6_matrix_reconciliation_candidate.py` | implemented Build-03 | non-authoritative candidate construction + source-hash read-back verification |
| `Quality/Integration/test_ci_impact_correlation.py` | implemented | mapping/classification + Build-03 candidate/read-back regression |
| `Quality/Integration/test_p6_matrix_reconciliation_candidate.py` | implemented | fail-closed identity, drift and no-auto-promotion regressions |
| `Quality/Integration/test_p6_layered_boundaries.py` | implemented | first-boundary isolation across P6-A..P6-E |
| `Quality/Integration/p6_reconciliation.py` | implemented | deterministic observation/identity/artifact reconciliation engine |
| `Quality/Integration/test_p6_runtime_lineage_adapter.py` | implemented / CI-bound | controlled runtime-lineage compatibility boundary |
| `Quality/Integration/emit_ci_runtime_evidence.py` | active | runtime-produced evidence artifact |
| `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | provisional/current | impact lookup surface; never auto-mutated by P6 |
| `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | canonical/active | relationship identity/state/evidence; never auto-mutated by P6 |

## Required P6 Control Chain

`CI Invocation → Commit/HEAD → Changed Scope → Affected Matrix Entries → Relationship/Consumer Scope → Workflow/Job Evidence → Test Result → Evidence Classification → Non-Authoritative Reconciliation Candidate → Repository Source Read-Back → Checkpoint`

## P6-08 / P6-09 Safety Architecture

P6 Build-03 deliberately does **not** allow CI to write REP-020, REP-014 or another canonical authority.

Instead:

1. the existing CI-impact report builds a deterministic `P6-MATRIX-RECONCILIATION-CANDIDATE/v1` candidate;
2. every candidate record is derived from an already-classified correlation record;
3. `MAPPED` becomes candidate `OBSERVED_IMPACT`, never `VERIFIED`;
4. `UNMAPPED` becomes `REVALIDATION_REQUIRED`;
5. policy-unresolved and not-applicable states remain unchanged in meaning;
6. candidate authority is always `NON_AUTHORITATIVE_EVIDENCE_CANDIDATE`;
7. promotion is always `NO_AUTO_PROMOTION`;
8. REP-020 and REP-014 source hashes are captured before candidate creation and re-read from the checked-out repository after candidate construction;
9. any HEAD mismatch, source drift or attempted auto-promotion fails closed.

Canonical mutation remains a separate governed action under applicable GOV-014/GOV-014A controls.

## Minimum Evidence Record

Every CI-to-impact observation should capture, where available:

- workflow name and run identifier;
- triggering and checkout commit SHA;
- base commit SHA where applicable;
- changed paths and scope eligibility;
- matrix/relationship correlation evidence;
- result and evidence classification;
- bounded candidate state;
- candidate authority / no-auto-promotion marker;
- REP-020 and REP-014 source hashes;
- post-CI repository read-back result;
- checkpoint.

## P6 Gates

| Gate | Requirement | State |
|---|---|---|
| P6-01 | Existing CI workflows inventoried | VERIFIED |
| P6-02 | CI runtime evidence emission inspected | VERIFIED |
| P6-03 | REP-020 impact/consumer matrix inspected | VERIFIED |
| P6-04 | CI result distinguished from semantic relationship verification | VERIFIED |
| P6-05 | Commit/HEAD available as correlation key | VERIFIED |
| P6-06 | Changed-path → impact-matrix correlation | IMPLEMENTED / REGRESSION-VERIFIED |
| P6-07 | Workflow-run / exact CI HEAD → affected relationship correlation | IMPLEMENTED / EXECUTION-OBSERVED via Full-Stack path; exact Build-03 verification pending |
| P6-08 | Automated matrix-state update from CI evidence | IMPLEMENTED as bounded non-authoritative reconciliation candidate; exact Build-03 verification pending |
| P6-09 | Post-CI repository read-back / reconciliation | IMPLEMENTED as exact-HEAD + REP-020/REP-014 source-hash read-back; exact Build-03 verification pending |
| P6-10 | Failure first-boundary preservation | IMPLEMENTED / CI-REGRESSION |
| P6-11 | Model-independent control path | IMPLEMENTED in correlator + candidate/read-back component |

## Safety Rules

1. CI success never upgrades a relationship above evidence actually exercised by the workflow.
2. Runtime evidence emission does not prove downstream service dispatch.
3. Changed-path correlation is impact evidence, not relationship proof.
4. Candidate output is evidence, not repository authority.
5. P6 MUST NOT write REP-020 or REP-014 automatically.
6. Ambiguous correlation remains `REVALIDATION_REQUIRED` or `POLICY_UNRESOLVED` as applicable.
7. No observation is not equivalent to no execution.
8. Historical success is never relabeled as execution failure solely because it is stale.
9. Source read-back mismatch is a hard verification failure, never an invitation to overwrite the source.
10. Layered tests preserve the first failing boundary for review and debugging.

## Current Verification Boundary

Build-03 implementation is prepared under P335 with pre-write Mutation Matrix control. Promotion of P6 to closed/execution-verified requires exact functional diff plus exact-head Full-Stack, Runtime/Integration, Real Mutation Matrix and M2 success. Until that evidence is recorded, this document remains execution-verification-pending.

## Current Disposition

`P6 = BUILD-03 / BOUNDED OBSERVABILITY + RECONCILIATION CANDIDATE / EXECUTION-VERIFICATION-PENDING / NO-AUTO-PROMOTION`.

No P3/P4 relationship is promoted or closed by P6, and Global Connected Baseline remains separately open.

---

End of P6 Matrix
