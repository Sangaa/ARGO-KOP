# MUTATION MATRIX — P7 CORE-000 CANONICAL ARCHITECTURE DRIFT — I

Transaction: `MUT-2026-09-01-P7-CORE000-CANONICAL-ARCHITECTURE-DRIFT-I`
Priority: 7 — Core cross-layer validation
State: PREWRITE-AUTHORIZED / OPEN
Entry HEAD: `c9b7488732aef02fd53aa45d1fb608a24dbd019f`
Date: 2026-09-01

## Problem Definition

`Core/CORE-000_PLATFORM_ARCHITECTURE.md` declares a platform component/layer model that conflicts materially with the current canonical Architecture authority.

Observed CORE-000 model:
- eight primary components: CORE, ENGINE, MEMORY, KNOWLEDGE, PROJECTS, RUNTIME, INTERFACES, ARCHIVE;
- layer order begins `Governance → Core → Engine → Memory → Knowledge → Projects → Runtime → Interfaces → Archive`.

Current canonical architecture evidence independently converges on a different model:
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` explicitly identifies itself as the authoritative architectural reference for structural boundaries and dependency direction, subordinate only to Constitution/applicable Governance;
- `ARC-011` defines `Identity/Core → Governance → Architecture → Repository → Knowledge/Specifications/Standards → Memory → Cognition/Engine → Runtime/Services/AI → Projects/Applied Artifacts`;
- `Architecture/ARC-004_LAYER_MODEL.md` defines the same nine-layer model;
- `Architecture/ARC_MAP.md` independently repeats the same canonical layers and explicitly classifies Archive as a repository preservation domain, not an active dependency layer;
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md` also repeats the same nine-layer dependency direction.

This is therefore not a folder-name discrepancy or relationship inference. It is substantive canonical-content drift inside a Core architectural authority artifact.

## Constitutional Classification

Per `CORE-003` Cross-Layer Consistency Rule, the discrepancy is classified as a **Core architectural-content defect / superseded architectural model**, not as permission for Architecture to silently override Core. The applicable governed change must reconcile CORE-000 to the already-established canonical Architecture Model while preserving constitutional authority.

## Prior-Learning Retrieval

- `CORE-003` Law 2 (Authoritative Source): DIRECTLY APPLICABLE — avoid competing architectural source-of-truth models.
- `CORE-003` Law 3 (Architecture Before Implementation): DIRECTLY APPLICABLE.
- `CORE-003` Law 9 (Controlled Evolution): DIRECTLY APPLICABLE — old approved text is reviewable.
- `ARC-011` Canonical Authority Boundary: DIRECTLY APPLICABLE.
- `ARC-004` + `ARC_MAP`: DIRECTLY APPLICABLE independent convergence.
- Transaction F content-drift method: TRANSFERABLE — inspect substantive authority text, not only provenance/reference chain.
- EJR-179 semantic-boundary regression principle: TRANSFERABLE — test durable authority semantics, not incidental prose.

## Three-Search / Independent Evidence Gate

1. Direct source inspection: CORE-000 declares the conflicting eight-component / Governance-first layer model.
2. Canonical authority inspection: ARC-011 declares the current authoritative nine-boundary model and authority ordering.
3. Independent architecture corroboration: ARC-004, ARC_MAP, and ARC-001 independently converge on the ARC-011 model.
4. Repository search for `CORE-000` + `ARC-011` found index/map references but no evidence authorizing CORE-000's older model over ARC-011.

Result: conflict is established with high confidence; negative claim is limited to the inspected authority scope.

## Authorized Mutation Surface

| ID | Path | Planned Change | Boundary |
|---|---|---|---|
| I-01 | `Core/CORE-000_PLATFORM_ARCHITECTURE.md` | Reconcile platform component/layer description to ARC-011 canonical boundary model; preserve Core/constitutional authority and integrity hold | No global certification |
| I-02 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | Record only evidence-backed CORE-000 → ARC-011 architectural alignment/reference relationship if current text after reconciliation explicitly supports it | No inferred reverse edge |
| I-03 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | Refresh CORE-000 / REP-014 versions if changed | Preserve Phase-1 OPEN / global hold |
| I-04 | `Core/_FOLDER_STATUS.md` | Record bounded CORE-000 canonical-architecture reconciliation | P7 remains OPEN |
| I-05 | `Quality/Integrity/test_core000_canonical_architecture_boundary.py` | Add durable regression for canonical layer order, Archive boundary, and non-competing architecture model | Semantic assertions only |
| I-06 | `Repository/P7_CORE000_CANONICAL_ARCHITECTURE_DRIFT_2026-09-01_I.md` | Record evidence, decision, CI and closure state | No authority promotion |
| I-07 | this matrix | Bind exact atomic change set and closure evidence | Same-change-set required |

## Mutation Method

Protected mutation MUST be committed atomically with this matrix using Git-object multi-file commit (`create_blob → create_tree → create_commit → update_ref force=false`). Separate Contents-API commits for protected targets are prohibited for this transaction.

Before ref update:
1. rediscover `main`;
2. if `main != authorization parent`, inspect intervening changes and rebase/recompute;
3. create one atomic candidate containing matrix + all protected targets;
4. run exact-head required CI;
5. any required failure triggers GOV-013 §9B HARD HOLD.

## Explicit Non-Claims

- No Core certification.
- No Architecture-layer certification.
- No Phase-1 closure.
- No repository-wide graph closure.
- No Global Connected Baseline PASS.
- No reverse relationship manufactured for symmetry.
- No claim that every physical repository folder is an architectural layer.

## Next Legal Action

Re-read live `main`; if unchanged and no competing transaction touches the same target, construct the smallest atomic candidate reconciling CORE-000 to ARC-011 and the independently corroborated canonical layer model.
