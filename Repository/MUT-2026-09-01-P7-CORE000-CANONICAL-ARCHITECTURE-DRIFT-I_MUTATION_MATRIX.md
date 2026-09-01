# MUTATION MATRIX — P7 CORE-000 CANONICAL ARCHITECTURE DRIFT — I

Transaction: `MUT-2026-09-01-P7-CORE000-CANONICAL-ARCHITECTURE-DRIFT-I`
Priority: 7 — Core cross-layer validation
State: `PREWRITE-REVALIDATED / REBOUND-AFTER-H / OPEN`
Original Entry HEAD: `c9b7488732aef02fd53aa45d1fb608a24dbd019f`
Revalidated live HEAD before this matrix-only rebind: `dca9829c451a7cedd4607bb9ecd8b82c7a8dc055`
Date: 2026-09-01

## Problem Definition

`Core/CORE-000_PLATFORM_ARCHITECTURE.md` still declares a platform component/layer model that conflicts materially with the current canonical Architecture authority.

Observed live CORE-000 state at `dca9829c...`:
- Version `3.1.0`;
- eight primary components: CORE, ENGINE, MEMORY, KNOWLEDGE, PROJECTS, RUNTIME, INTERFACES, ARCHIVE;
- layer order begins `Governance → Core → Engine → Memory → Knowledge → Projects → Runtime → Interfaces → Archive`;
- Archive is represented as active Layer 8.

Current canonical architecture evidence independently converges on a different model:
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` is the authoritative architectural reference for structural boundaries and dependency direction, subordinate only to Constitution/applicable Governance;
- `ARC-011` defines `Identity/Core → Governance → Architecture → Repository → Knowledge/Specifications/Standards → Memory → Cognition/Engine → Runtime/Services/AI → Projects/Applied Artifacts`;
- `Architecture/ARC-004_LAYER_MODEL.md` defines the same nine-layer model;
- `Architecture/ARC_MAP.md` repeats the same canonical layers and explicitly classifies Archive as a repository preservation domain, not an active dependency layer;
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md` independently repeats the same nine-layer dependency direction.

This is substantive canonical-content drift inside an active Core authority artifact, not a filename/folder discrepancy.

## Constitutional Classification

Per `CORE-003` Laws 1, 2, 3, 5, 9 and the Cross-Layer Consistency Rule, the discrepancy is classified as a **Core architectural-content defect / superseded architectural model**. Architecture does not silently override Core; the conflict is explicitly classified and CORE-000 is reconciled through governed mutation to the already-established canonical architecture boundary while Constitution/Governance remain higher authority.

## Prior-Learning Retrieval

- `CORE-003` authoritative-source and controlled-evolution laws: `DIRECTLY APPLICABLE`.
- `ARC-011` canonical authority boundary: `DIRECTLY APPLICABLE`.
- `ARC-004`, `ARC_MAP`, `ARC-001`: `DIRECTLY APPLICABLE` independent corroboration.
- Transaction F content-drift method: `TRANSFERABLE` — inspect substantive authority text, not only provenance/reference chain.
- EJR-179 semantic-boundary regression principle: `TRANSFERABLE` — test durable authority semantics, not incidental prose.
- Transaction E same-change-set recovery: `DIRECTLY APPLICABLE` — protected mutation + Matrix must be atomically bound in the candidate commit.

## Search / Independent Evidence Gate

1. Direct live source inspection: CORE-000 retains the conflicting eight-component / Governance-first / Archive-layer model.
2. Canonical authority inspection: ARC-011 retains the current authoritative nine-boundary model and explicit authority ordering.
3. Independent corroboration: ARC-004, ARC_MAP and ARC-001 converge on the same nine-layer model.
4. No current inspected authority grants the older CORE-000 model precedence over ARC-011 within structural-boundary/dependency scope.

Result: conflict remains established at live `main` with high confidence.

## Intervening Transaction H Revalidation

Transaction H closed after the original I prewrite and modified three I-adjacent protected surfaces:
- `REP-014` advanced to `1.2.10` and added `REL-066`;
- `Core/_FOLDER_STATUS.md` advanced to `1.3.6` and recorded the fourth bounded seam;
- `REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` refreshed its REP-014 row to `1.2.10`.

H did **not** modify `CORE-000`. H closure HEAD `dca9829c...` has all four exact-head required workflows green.

Therefore the original I prewrite is not executed against its stale baseline. This matrix-only commit rebinds I to current post-H reality before any protected I target mutation.

## Current Target Baseline

- `CORE-000`: v`3.1.0`, blob `22c03130cc74a4ac619fa177168ae3b6fcf3bd45`.
- `REP-014`: v`1.2.10`.
- Core status: v`1.3.6`.
- Current control-plane manifest: REP-014 row = `1.2.10`; CORE-000 is **not** a listed manifest row.

## Authorized Mutation Surface

| ID | Path | Planned Change | Boundary |
|---|---|---|---|
| I-01 | `Core/CORE-000_PLATFORM_ARCHITECTURE.md` | Reconcile component/layer description to ARC-011 canonical boundary model; version/audit metadata advance only because this document itself is materially revalidated | Preserve Integrity Hold / no folder certification |
| I-02 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | Add one evidence-backed `CORE-000 → ARC-011 = REFERENCES` relationship after CORE-000 explicitly names ARC-011 as canonical architecture authority; no reverse edge | REFERENCES only / non-dependency |
| I-03 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | Refresh **REP-014 only** if REP-014 version changes; CORE-000 is outside this manifest's row scope | Preserve Phase-1 OPEN / global hold |
| I-04 | `Core/_FOLDER_STATUS.md` | Record bounded CORE-000 canonical-architecture content reconciliation as the fifth P7 seam/content correction | P7 remains OPEN |
| I-05 | `Quality/Integrity/test_core000_canonical_architecture_boundary.py` | Add durable semantic regression for canonical layer order, Archive preservation-domain boundary, ARC-011 alignment and rejection of the old competing model | No prose-format freezing |
| I-06 | `Repository/P7_CORE000_CANONICAL_ARCHITECTURE_DRIFT_2026-09-01_I.md` | Record evidence, decision, exact candidate CI and closure state | No authority promotion |
| I-07 | this matrix | Bind exact atomic protected change set and candidate/closure evidence | Same-change-set required |

## Candidate Design Boundary

CORE-000 remains the active canonical `CORE-000` owner, but it shall no longer compete with the Architecture layer on structural boundary authority. The repaired text will state that:
- Core preserves platform identity/foundational architecture intent;
- structural layer boundaries and dependency direction are controlled by `ARC-011` under Constitution/Governance;
- the canonical layer model is the nine-boundary model used by ARC-011/004/001/ARC_MAP;
- Archive is a preservation domain, not an active dependency layer;
- physical repository domains do not automatically create architectural layers;
- implementation status remains evidence-dependent.

## Mutation Method

Protected mutation MUST be committed atomically with this matrix using Git-object multi-file commit (`create_blob → create_tree → create_commit → update_ref force=false`). Separate Contents-API commits for protected I targets are prohibited.

Before candidate ref update:
1. rediscover live `main`;
2. require `main` to equal this matrix-only rebind commit or explicitly inspect/rebase any intervening changes;
3. construct one atomic candidate containing Matrix + all changed protected targets + regression + progress record;
4. re-read candidate files from exact candidate HEAD;
5. run exact-head Runtime/Integration, Full-Stack, M2 and Real Mutation Matrix Regression;
6. any required failure triggers GOV-013 §9B HARD HOLD and no next transaction.

## Explicit Non-Claims

- No Core certification.
- No Architecture-layer certification.
- No Phase-1 closure.
- No repository-wide graph closure.
- No Global Connected Baseline PASS.
- No reverse relationship manufactured for symmetry.
- No claim that every physical repository folder is an architectural layer.

## Next Legal Action

After this matrix-only rebind persists, re-read live `main`. If unchanged and no competing mutation touches I targets, build the smallest atomic I candidate from the rebound baseline.