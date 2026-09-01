# Priority 7 — Architecture README Authority Alignment — Transaction S

Date: 2026-09-01
State: `MATERIAL-CANDIDATE / CI-PENDING / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-ARCHITECTURE-README-AUTHORITY-DRIFT-S`
Work Lease: `HERMUZ-P7-S-ARCHITECTURE-README-20260901`
Entry HEAD: `cb45d5fd9b6dbba1727e52060b9e181a54db3239`
Pre-write Matrix HEAD: `cbba871330e9cb82486b7cbda73a20edd65f114e`
Rejected unpublished object candidate: `c81500caacbd385b9706a09de57b0fce55c2dae3`

## Why S was selected

Post-R Priority-7 recomputation did not treat the validated `RUN-002 → CORE-003 = REFERENCES` seam as an automatic REP-014 registration obligation. REP-014 is explicitly not a complete graph and Core status requires registry reconciliation only where evidence requires.

A broader three-form search for current Core consumers instead exposed a higher-value semantic problem: canonical `Architecture/README.md` retained pre-reconciliation authority and inventory language after Transaction I repaired CORE-000 on 2026-09-01.

The README is itself Canonical and Absolute/Critical, so stale authority text in that consumer is material to Core cross-layer validation.

## Direct evidence

### Architecture README before S

The live README at S entry stated:

- `Status: Approved`;
- `Canonical: Yes`;
- `Priority: Absolute / Critical`;
- architecture operates `In accordance with CORE-003 Constitutional Laws`;
- `Core/CORE-000_PLATFORM_ARCHITECTURE.md` is the `ultimate guiding text` and overrides project details;
- the directory is `globally locked`;
- every valid artifact must be cataloged by its partial listed component set;
- an `Anti-Patch Policy` controlled modification.

Its listed architecture components omitted multiple artifacts now present in the current primary Architecture review set, including ARC-001, ARC-003, ARC-005, ARC-007, ARC-010 and ARC-011.

### Current CORE-000 authority after Transaction I

Current `Core/CORE-000_PLATFORM_ARCHITECTURE.md` says:

- it defines **Core-level canonical platform architecture intent**;
- current structural boundaries/dependency direction are aligned with `ARC-011`;
- it is subordinate to the Constitution and applicable Governance;
- its authority hierarchy places `ARC-011` above other Architecture controls and repository/implementation artifacts;
- it must not establish a competing lower-fidelity structural model.

### Current ARC-011 authority

Current `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` says:

- it is the current canonical Architecture Model;
- it is the authoritative architectural reference for structural boundaries and dependency direction;
- it is subordinate only to the Constitution and applicable Governance authority;
- if Architecture documents conflict, the order is Constitution/Governance → ARC-011 → other Architecture documents → Repository/Project artifacts.

### Current Architecture status

`Architecture/_FOLDER_STATUS.md` remains `INTEGRITY HOLD` and explicitly keeps:

- layer-boundary consistency OPEN;
- dependency-direction consistency OPEN;
- Canonical Architecture Model alignment OPEN;
- stale-reference review OPEN;
- cross-layer boundaries OPEN.

Its current primary review set includes ARC_MAP plus ARC-001 through ARC-011.

### Foundation artifact boundary

`Architecture/01-System-Overview.md` is still physically present and contains an earlier four-layer/five-component Foundation Build model from July 2026. Current folder status does not place it in the primary Architecture review set. Therefore S preserves it as legacy/foundation evidence without allowing physical presence to create current authority.

## Search-triple result

Three materially different repository searches were used before selecting S:

1. exact current Constitution path: `Core/CORE-003_CONSTITUTION.md`;
2. identity term: `CORE-003`;
3. broad Core-path family: `Core/CORE-`.

Code-search indexing lag was observed: discovery URLs initially pointed to an earlier recent HEAD. Search was therefore used only for candidate discovery; every material S finding was re-read from exact live `cb45d5fd...` source files before mutation.

Additional targeted searches showed:

- the phrase `ultimate guiding text` was localized to `Architecture/README.md`;
- the conflict/override wording was likewise localized there;
- current CORE-000/ARC-011 alignment language is present in current canonical evidence and Transaction-I records/tests.

## Prior learning

Transaction I is `DIRECTLY APPLICABLE`: it repaired stale canonical-architecture content without manufacturing a REP-014 edge or claiming certification.

Transactions L/M and ARC-006 are `DIRECTLY APPLICABLE` to authority/dependency separation and the rule that textual references do not create dependency or relationship authority.

Transaction R's incident chain is `DIRECTLY APPLICABLE` only to execution discipline: before every write-capable operation S checks action type, path, Matrix authorization, required atomicity and whether `main` moves.

## Repair applied in S candidate

S performs one bounded canonical-consumer reconciliation:

1. `Architecture/README.md` v3.2.0 → v3.2.1;
2. README status clarified to `Approved / Integrity Hold`;
3. README authority hierarchy aligned to Constitution/Governance → ARC-011 → other Architecture → repository/implementation;
4. CORE-000 reclassified in the README as Core-level platform architecture intent aligned with ARC-011 rather than an `ultimate` competing Architecture authority;
5. current ARC-001..ARC-011 primary review set represented explicitly;
6. ARC_MAP / README / `_FOLDER_STATUS.md` distinguished as navigation/control surfaces rather than ARC-NNN documents;
7. `01-System-Overview.md` explicitly retained as foundation/legacy material without authority promotion;
8. stale `globally locked` / `Anti-Patch Policy` language replaced by current governed controlled-mutation boundaries;
9. Architecture status v1.5.1 → v1.5.2 records this bounded consumer repair while retaining all broader OPEN/HOLD gates;
10. focused regression protects the repaired authority/inventory/non-certification boundaries.

## Pre-publish validation-design defect caught before `main`

The first unpublished Git-object candidate `c81500caacbd385b9706a09de57b0fce55c2dae3` passed the one-commit/five-path structural compare but was rejected during exact candidate read-back before `main` moved.

The initial focused test attempted to verify ARC-001..ARC-011 ordering using `readme.index()` across the entire README. That assertion was semantically wrong because ARC-011 is intentionally named earlier in the authority section before the primary-review-set inventory. The test could therefore report a false ordering failure even when the inventory section itself was correct.

Classification: `PRE-PUBLISH VALIDATION_DESIGN_DEFECT / NO REPOSITORY MUTATION / NO CI FAILURE`.

Correction: scope the ordering check to the `Current Primary Architecture Review Set` section only, preserving the stronger authority section rather than removing the valid earlier ARC-011 reference.

No authority language was weakened to satisfy the test. The rejected object commit was never fast-forwarded to `main` and is not treated as repository history/closure evidence.

Reusable lesson retained at session level: when a validation assertion tests ordering or uniqueness inside a bounded semantic section, scope the assertion to that semantic boundary rather than using first occurrence across a document that may intentionally reference the same identity elsewhere.

This is a test-design refinement, not a new Governance rule.

## Relationship-registry decision

S does **not** add a REP-014 relationship.

The repair concerns stale consumer content and authority interpretation. A path/reference in the README is not sufficient to create `REFERENCES`, `DEPENDS_ON`, `GOVERNS` or another controlled relationship type. No new edge is required to make the content internally correct.

`RUN-002 → CORE-003 = REFERENCES` also remains a validated R seam outside REP-014 unless a later fresh review proves registration materially required.

## Forbidden promotion

S does not claim or establish:

- CORE-000 as subordinate via a new dependency edge;
- any README ↔ CORE-000 / CORE-003 / ARC-011 REP-014 row;
- complete Architecture semantic revalidation;
- Architecture folder certification;
- Core folder certification;
- Priority-7 closure;
- Phase-1 closure;
- Connected Baseline closure;
- repository-wide graph completion;
- Global PASS.

## Material verification contract

The publishable candidate is valid only if:

- it is exactly one commit after `cbba8713...`;
- exactly five Matrix-authorized paths change;
- unexpected path expansion is zero;
- exact-head read-back confirms all material surfaces;
- required CI/integration workflows succeed;
- Full-Stack exact-SHA/Matrix/audit steps succeed;
- Runtime integrity/prototype/integration jobs succeed.

Failure remains evidence and must not be resolved by weakening the repaired authority boundary.

## Continuation boundary

Even if S closes successfully, Priority 7 remains OPEN until a fresh recomputation determines whether another higher-value material Core consumer gap remains or whether evidence is sufficient to enter explicit Core Certification Readiness review.

This record is not future mutation authority.
