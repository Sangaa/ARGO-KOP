# MUTATION MATRIX — P7 CORE-000 CANONICAL ARCHITECTURE DRIFT — I

Transaction: `MUT-2026-09-01-P7-CORE000-CANONICAL-ARCHITECTURE-DRIFT-I`
Priority: 7 — Core cross-layer validation
State: `ATOMIC-CANDIDATE-PREPARED / CI-PENDING / OPEN`
Original Entry HEAD: `c9b7488732aef02fd53aa45d1fb608a24dbd019f`
Post-H rebind commit: `3443681aab4463c61ef99e5994053f1041515f8f`
Scope-minimization HEAD: `f8fc6d4e26518ed09e0227ff458337bbbd68712d`
Date: 2026-09-01

## Problem Definition

`Core/CORE-000_PLATFORM_ARCHITECTURE.md` still declares a platform component/layer model that conflicts materially with current canonical Architecture authority.

Observed live CORE-000 state at scope-minimization HEAD:
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

Result: `CONTENT DRIFT CONFIRMED / HIGH CONFIDENCE`.

## Constitutional Classification

Per `CORE-003` and current Architecture authority, the discrepancy is classified as a Core architectural-content defect / superseded structural model. Architecture does not silently override Core; the conflict is explicitly classified and CORE-000 is governedly reconciled while Constitution/Governance remain higher authority.

## Prior-Learning Retrieval

- `CORE-003` authoritative-source and controlled-evolution laws: `DIRECTLY APPLICABLE`.
- `ARC-011` canonical authority boundary: `DIRECTLY APPLICABLE`.
- `ARC-004`, `ARC_MAP`, `ARC-001`: `DIRECTLY APPLICABLE` independent corroboration.
- Transaction F content-drift method: `TRANSFERABLE`.
- EJR-179 semantic-boundary regression principle: `TRANSFERABLE`.
- Transaction E same-change-set recovery: `DIRECTLY APPLICABLE`.

## Scope-Minimization Decision

Transaction I contains one material concern only: repair CORE-000 substantive architecture drift and bind direct evidence surfaces.

Relationship registration is deferred and is not an absence claim. REP-014 and the current control-plane manifest are explicitly outside I mutation scope.

## Authorized Mutation Surface

| ID | Path | Planned Change | Candidate State |
|---|---|---|---|
| I-01 | `Core/CORE-000_PLATFORM_ARCHITECTURE.md` | Reconcile structural-boundary content to current ARC-011 model; v3.1.0 → v3.2.0; audit 2026-09-01 | APPLIED / READ-BACK PENDING |
| I-02 | `Core/_FOLDER_STATUS.md` | Record bounded CORE-000 content reconciliation; v1.3.6 → v1.3.7 | APPLIED / READ-BACK PENDING |
| I-03 | `Quality/Integrity/test_core000_canonical_architecture_boundary.py` | Add durable semantic regression for nine-boundary order and Archive boundary | APPLIED / READ-BACK PENDING |
| I-04 | `Repository/P7_CORE000_CANONICAL_ARCHITECTURE_DRIFT_2026-09-01_I.md` | Record candidate scope, evidence and closure gate | APPLIED / READ-BACK PENDING |
| I-05 | this matrix | Bind exact atomic change set and candidate/closure evidence | APPLIED / READ-BACK PENDING |

Explicitly not mutated in I:
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`;
- `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md`;
- Architecture source artifacts.

## Preservation Requirements

- Keep `CORE-000` as the active canonical CORE-000 owner.
- Preserve Core Integrity Hold and Priority 7 OPEN state.
- Preserve legacy `CORE-000_PLATFORM_IDENTITY.md` as noncanonical provenance; do not promote it.
- Preserve implementation/completeness claims as evidence-dependent.
- Do not create a new relationship edge in I.
- Do not claim Core, Architecture, Phase-1 or Global Connected Baseline certification.

## Candidate Design Boundary

The repaired CORE-000:
- preserves Core-level platform architecture intent;
- explicitly aligns current structural boundaries and dependency direction to `ARC-011` under Constitution/Governance;
- uses the current nine-boundary model;
- classifies Archive as a preservation domain, not an active dependency layer;
- states that physical repository domains do not automatically create architectural layers;
- keeps implementation/completeness claims evidence-dependent.

## Atomic Mutation Method

The protected candidate MUST use one Git-object commit containing exactly the five authorized I paths:

`create_blob → create_tree(base live-main tree) → create_commit(parent live main) → recheck main → update_ref(force=false)`.

Separate Contents-API commits are prohibited for the candidate.

## Candidate Pre-Write Validation

- Live main rediscovered: `f8fc6d4e26518ed09e0227ff458337bbbd68712d`.
- Live main message: `P7: minimize Transaction I to CORE-000 content drift`.
- CORE-000 source blob: `22c03130cc74a4ac619fa177168ae3b6fcf3bd45`.
- Core status source blob: `a48959e7e66b3698c5d344b1c490cb332216c537`.
- Candidate CORE-000 blob: `fdb2313fdeabc6b506258815d39e8ed99c17ca27`.
- Candidate Core status blob: `805e026b3e298a709a0cd0e99709abcbc21782da`.
- Candidate regression blob: `5d5191b0ef3b5c96d37c002dee82d52930cbfbe1`.
- Candidate progress-record blob: `798cc23448adc472a8f16fefe43ed128f0941642`.
- Candidate matrix blob: self / bound by resulting atomic tree.
- Unexpected authorized-path expansion: `0`.

Pre-write result: `PASS / READY FOR ATOMIC TREE`.

## Required Post-Write Validation

1. Re-read all five candidate files from exact candidate HEAD.
2. Confirm REP-014 and current manifest are unchanged from parent.
3. Run exact-head Runtime/Integration, Full-Stack, M2 and Real Mutation Matrix Regression.
4. Any required failure triggers GOV-013 §9B HARD HOLD.
5. Only after all required checks succeed may I be closed resume-safe.

## Explicit Non-Claims

- No Core certification.
- No Architecture certification.
- No Phase-1 closure.
- No repository-wide graph closure.
- No Global Connected Baseline PASS.
- No relationship registration completed by I.

## Closure Gate

`ATOMIC COMMIT → EXACT READ-BACK → REQUIRED EXACT-HEAD CI SUCCESS → CLOSURE RECORD/MATRIX UPDATE → FINAL CLOSURE-HEAD REVALIDATION`.

No new Priority-7 transaction may be opened before this gate is complete.
