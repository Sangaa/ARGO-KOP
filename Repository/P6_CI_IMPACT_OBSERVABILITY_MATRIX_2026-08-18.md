# P6 — CI ↔ IMPACT-MATRIX OBSERVABILITY MATRIX

Date: `2026-09-01`
Status: `CLOSED_FOR_PHASE_1 / EXECUTION-VERIFIED / BOUNDED OBSERVABILITY + NON-AUTHORITATIVE RECONCILIATION`
Authority: `GOV-013 + GOV-014 + REP-020`
Scope: CI invocation evidence correlated with repository impact/relationship scope.

## Purpose

Define and implement the minimum evidence contract required to connect CI execution to affected repository relationships, consumers and impact scope without converting workflow success into semantic closure or repository mutation authority.

## Core Testing Decision

P6 is a layered control, not a single atomic assertion. Its verification preserves first-failure boundaries instead of collapsing observation, identity, artifact and classification failures into one P6 failure.

Required layered chain:

`P6-A Functional → P6-B Observation → P6-C Identity → P6-D Artifact → P6-E Classification/Reconciliation`

## Evidence Classification

A successful historical run remains valid execution evidence. If its run/artifact SHA differs from the current baseline it is classified `VALID_EXECUTION_STALE_BASELINE`, not `EXECUTION_FAILED`.

A connector/query returning zero observations is `NO_OBSERVATION`; it is not evidence of `NO_EXECUTION` unless the query surface is proven complete for the trigger type.

## Current Evidence Sources

| Evidence Source | State | Boundary |
|---|---|---|
| `.github/workflows/full-stack-audit.yml` | active / exact-head verified | executes P6 correlation + layered regressions and uploads CI-impact evidence |
| `Quality/Integration/ci_impact_correlation.py` | Build-03 execution-verified | deterministic path correlation + bounded reconciliation candidate + read-back result |
| `Quality/Integration/p6_matrix_reconciliation_candidate.py` | Build-03 execution-verified | non-authoritative candidate construction + source-hash read-back verification |
| `Quality/Integration/test_ci_impact_correlation.py` | exact-head regression verified | mapping/classification + candidate/read-back regression |
| `Quality/Integration/test_p6_matrix_reconciliation_candidate.py` | integration-suite verified | fail-closed identity, drift and no-auto-promotion regressions |
| `Quality/Integration/test_p6_layered_boundaries.py` | exact-head CI verified | first-boundary isolation across P6-A..P6-E |
| `Quality/Integration/p6_reconciliation.py` | exact-head CI verified | deterministic observation/identity/artifact reconciliation engine |
| `Quality/Integration/test_p6_runtime_lineage_adapter.py` | exact-head CI verified | controlled runtime-lineage compatibility boundary |
| `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | provisional/current | impact lookup surface; never auto-mutated by P6 |
| `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | canonical/active | relationship identity/state/evidence; never auto-mutated by P6 |

## Required P6 Control Chain

`CI Invocation → Commit/HEAD → Changed Scope → Affected Matrix Entries → Relationship/Consumer Scope → Workflow/Job Evidence → Test Result → Evidence Classification → Non-Authoritative Reconciliation Candidate → Repository Source Read-Back → Checkpoint`

## P6-08 / P6-09 Safety Architecture

P6 does **not** allow CI to write REP-020, REP-014 or another canonical authority.

Instead:
1. the existing CI-impact report builds a deterministic `P6-MATRIX-RECONCILIATION-CANDIDATE/v1` candidate;
2. every candidate record is derived from an already-classified correlation record;
3. `MAPPED` becomes candidate `OBSERVED_IMPACT`, never `VERIFIED`;
4. `UNMAPPED` becomes `REVALIDATION_REQUIRED`;
5. policy-unresolved and not-applicable states remain unchanged in meaning;
6. candidate authority is always `NON_AUTHORITATIVE_EVIDENCE_CANDIDATE`;
7. promotion is always `NO_AUTO_PROMOTION`;
8. REP-020 and REP-014 source hashes are captured and re-read from the checked-out repository after candidate construction;
9. any HEAD mismatch, source drift or attempted auto-promotion fails closed.

Canonical mutation remains a separate governed action under applicable GOV-014/GOV-014A controls.

## P6 Gates

| Gate | Requirement | State |
|---|---|---|
| P6-01 | Existing CI workflows inventoried | VERIFIED |
| P6-02 | CI runtime evidence emission inspected | VERIFIED |
| P6-03 | REP-020 impact/consumer matrix inspected | VERIFIED |
| P6-04 | CI result distinguished from semantic relationship verification | VERIFIED |
| P6-05 | Commit/HEAD available as correlation key | VERIFIED |
| P6-06 | Changed-path → impact-matrix correlation | EXECUTION-VERIFIED |
| P6-07 | Workflow-run / exact CI HEAD → affected relationship correlation | EXECUTION-VERIFIED at functional HEAD `9e6a5c25f0a18985e2163080059985cbd95addbc` |
| P6-08 | Automated matrix-state update from CI evidence | EXECUTION-VERIFIED as bounded non-authoritative reconciliation candidate |
| P6-09 | Post-CI repository read-back / reconciliation | EXECUTION-VERIFIED; REP-020 and REP-014 read-back `VERIFIED_UNCHANGED` |
| P6-10 | Failure first-boundary preservation | EXECUTION-VERIFIED / CI-REGRESSION |
| P6-11 | Model-independent control path | EXECUTION-VERIFIED in correlator + candidate/read-back component |

## Exact-head P335 Evidence

Functional HEAD: `9e6a5c25f0a18985e2163080059985cbd95addbc`.

- Full-Stack Repository Audit `33464500515` — SUCCESS, including P6 correlation, canonical repository boundary, layered boundaries, reconciliation boundaries, runtime-lineage adapter, Mutation Matrix enforcement, repository-wide audit and CI-impact artifact upload.
- Runtime Prototype and Integration Tests `33464500542` — SUCCESS across prototype, integrity and integration jobs.
- Real Mutation Matrix Regression `33464500603` — SUCCESS.
- M2 Multi-Channel Proposal Training `33464500521` — SUCCESS.
- CI-impact artifact ID `9784359327`, digest `sha256:2ebda6c2c285a8590ea76b8f6704f690124c6c5c57025e676361dfb4895ca35e`, bound to the same functional HEAD.

Artifact read-back proved:
- schema `P6-CI-IMPACT-CORRELATION/v5`;
- candidate schema `P6-MATRIX-RECONCILIATION-CANDIDATE/v1`;
- candidate authority `NON_AUTHORITATIVE_EVIDENCE_CANDIDATE`;
- promotion `NO_AUTO_PROMOTION`;
- post-CI read-back status `VERIFIED`;
- REP-020 read-back `VERIFIED_UNCHANGED`;
- REP-014 read-back `VERIFIED_UNCHANGED`.

The artifact also correctly surfaced `REVALIDATION_REQUIRED` for in-scope unmapped paths and `POLICY_UNRESOLVED` for paths without an explicit P6 scope decision. Those states are valid fail-closed observations, not CI failures and not grounds for invented mappings.

## Safety Rules

1. CI success never upgrades a relationship above evidence actually exercised by the workflow.
2. Changed-path correlation is impact evidence, not relationship proof.
3. Candidate output is evidence, not repository authority.
4. P6 MUST NOT write REP-020 or REP-014 automatically.
5. Ambiguous correlation remains `REVALIDATION_REQUIRED` or `POLICY_UNRESOLVED` as applicable.
6. Source read-back mismatch is a hard verification failure, never an invitation to overwrite the source.
7. Layered tests preserve the first failing boundary for review and debugging.

## Current Disposition

`PRIORITY 6 = CLOSED_FOR_PHASE_1 / EXECUTION-VERIFIED / BOUNDED OBSERVABILITY + NON-AUTHORITATIVE RECONCILIATION`.

This closes the bounded Priority-6 build workstream. Ongoing CI evidence collection, impact mapping maintenance and future scope decisions continue as operational work and do not reopen Priority 6 unless they expose a defect in the P6 method or invalidate its declared control boundary.

No P3/P4 relationship is promoted by P6. Phase 1 overall remains OPEN. Repository-wide graph validation and Global Connected Baseline remain OPEN / NOT CERTIFIED. Global `BOOTED / INTEGRITY PASS` is not claimed.

---

End of P6 Matrix
