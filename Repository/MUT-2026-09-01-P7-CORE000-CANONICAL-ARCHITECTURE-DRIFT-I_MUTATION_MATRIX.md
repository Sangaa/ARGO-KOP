# MUTATION MATRIX — P7 CORE-000 CANONICAL ARCHITECTURE DRIFT — I

Transaction: `MUT-2026-09-01-P7-CORE000-CANONICAL-ARCHITECTURE-DRIFT-I`
Priority: 7 — Core cross-layer validation
State: `PREWRITE-REVALIDATED / SCOPE-MINIMIZED / OPEN`
Original Entry HEAD: `c9b7488732aef02fd53aa45d1fb608a24dbd019f`
Post-H rebind commit: `3443681aab4463c61ef99e5994053f1041515f8f`
Date: 2026-09-01

## Problem Definition

`Core/CORE-000_PLATFORM_ARCHITECTURE.md` still declares a platform component/layer model that conflicts materially with current canonical Architecture authority.

Observed live CORE-000 state:
- Version `3.1.0`;
- eight primary components: CORE, ENGINE, MEMORY, KNOWLEDGE, PROJECTS, RUNTIME, INTERFACES, ARCHIVE;
- layer order begins `Governance → Core → Engine → Memory → Knowledge → Projects → Runtime → Interfaces → Archive`;
- Archive is represented as active Layer 8.

Current canonical architecture evidence independently converges on:
`Identity/Core → Governance → Architecture → Repository → Knowledge/Specifications/Standards → Memory → Cognition/Engine → Runtime/Services/AI → Projects/Applied Artifacts`.

Evidence sources:
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` — authoritative structural/dependency reference under Constitution/Governance;
- `Architecture/ARC-004_LAYER_MODEL.md` — same nine-layer model;
- `Architecture/ARC_MAP.md` — same model and explicit `Archive = preservation domain / not active dependency layer`;
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md` — same dependency direction.

This is substantive canonical-content drift inside an active Core authority artifact.

## Constitutional Classification

Per `CORE-003` Laws 1, 2, 3, 5, 9 and the Cross-Layer Consistency Rule, the discrepancy is a **Core architectural-content defect / superseded architectural model**. Architecture does not silently override Core; the conflict is explicitly classified and the Core artifact is governedly reconciled while Constitution/Governance remain higher authority.

## Prior-Learning Retrieval

- `CORE-003` authoritative-source and controlled-evolution laws: `DIRECTLY APPLICABLE`.
- `ARC-011` canonical authority boundary: `DIRECTLY APPLICABLE`.
- `ARC-004`, `ARC_MAP`, `ARC-001`: `DIRECTLY APPLICABLE` independent corroboration.
- Transaction F content-drift method: `TRANSFERABLE`.
- EJR-179 semantic-boundary regression principle: `TRANSFERABLE`.
- Transaction E same-change-set recovery: `DIRECTLY APPLICABLE`.

## Independent Evidence Gate

1. Direct CORE-000 inspection confirms the old model.
2. Direct ARC-011 inspection confirms the authoritative current model.
3. ARC-004, ARC_MAP and ARC-001 independently corroborate the ARC-011 model.
4. No inspected current authority grants the older CORE-000 model precedence over ARC-011 in structural-boundary/dependency scope.

Result: `CONTENT DRIFT CONFIRMED / HIGH CONFIDENCE`.

## Intervening Transaction H Revalidation

H closed after the original I prewrite and changed `REP-014`, Core status and the current control-plane manifest. H did not change CORE-000 and its final closure HEAD `dca9829c...` is green on all four required workflows.

The I baseline was therefore rebound after H before protected mutation.

## Scope-Minimization Decision

The first rebound I design considered combining two material concerns:
1. repair CORE-000 substantive architecture drift;
2. register a new `CORE-000 → ARC-011` relationship in REP-014.

That combination is unnecessary for proving the content correction and would widen the protected mutation surface. Under the one-material-change discipline, Transaction I is narrowed to the **CORE-000 content correction and its direct evidence surfaces only**.

Relationship registration is explicitly deferred to the next Priority-7 relationship seam after I succeeds. This is not an absence claim and not a rejection of the relationship; it is controlled sequencing.

Because REP-014 is not mutated in I, `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` also requires no I mutation.

## Current Target Baseline

- `CORE-000`: v`3.1.0`, blob `22c03130cc74a4ac619fa177168ae3b6fcf3bd45`.
- Core status: v`1.3.6`.
- REP-014 remains v`1.2.10` and is outside I mutation scope.
- Current manifest keeps REP-014 v`1.2.10` and is outside I mutation scope.

## Authorized Mutation Surface

| ID | Path | Planned Change | Boundary |
|---|---|---|---|
| I-01 | `Core/CORE-000_PLATFORM_ARCHITECTURE.md` | Reconcile component/layer description to current ARC-011 model; advance this document's version/audit metadata because this document itself is materially revalidated | Preserve Integrity Hold |
| I-02 | `Core/_FOLDER_STATUS.md` | Record bounded CORE-000 canonical-architecture content reconciliation | P7 remains OPEN |
| I-03 | `Quality/Integrity/test_core000_canonical_architecture_boundary.py` | Add durable semantic regression for layer order, Archive boundary and rejection of the old competing model | No prose-format freezing |
| I-04 | `Repository/P7_CORE000_CANONICAL_ARCHITECTURE_DRIFT_2026-09-01_I.md` | Record evidence, decision, candidate CI and deferred relationship follow-up | No certification |
| I-05 | this matrix | Bind exact atomic change set and candidate/closure evidence | Same-change-set required |

Explicitly **not mutated in I**:
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`;
- `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`;
- Architecture source artifacts.

## Candidate Design Boundary

CORE-000 remains the active canonical `CORE-000` owner, but shall not compete with the Architecture layer on structural boundary authority. The repaired document will:
- preserve Core-level platform identity/foundational architecture intent;
- explicitly align structural boundaries and dependency direction to `ARC-011` under Constitution/Governance;
- use the current nine-boundary model;
- classify Archive as a preservation domain, not an active dependency layer;
- state that physical repository domains do not automatically create architectural layers;
- keep implementation/completeness claims evidence-dependent.

## Mutation Method

Protected I mutation MUST be committed atomically with this matrix using Git-object multi-file commit (`create_blob → create_tree → create_commit → update_ref force=false`). Separate Contents-API commits for protected I targets are prohibited.

Before candidate ref update:
1. rediscover live `main`;
2. require `main` to equal this matrix-only scope-minimization commit or inspect/rebind any divergence;
3. construct one atomic candidate containing Matrix + CORE-000 + Core status + regression + progress record;
4. re-read exact candidate files;
5. run exact-head Runtime/Integration, Full-Stack, M2 and Real Mutation Matrix Regression;
6. any required failure triggers GOV-013 §9B HARD HOLD.

## Explicit Non-Claims

- No Core certification.
- No Architecture certification.
- No Phase-1 closure.
- No repository-wide graph closure.
- No Global Connected Baseline PASS.
- No relationship registration completed by I.

## Post-I Legal Follow-Up

If I succeeds, recompute live Priority-7 ordering. The directly evidenced `CORE-000 → ARC-011` documentary/alignment relationship becomes a candidate relationship-registration seam, but it must still be revalidated from the then-current repository before REP-014 mutation.