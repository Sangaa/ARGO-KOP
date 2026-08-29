# HORUS — CANDIDATE EXPERIENCE UNITS

Date: 2026-08-29
Role: HORUS / ANALYZE_META_LEARNING_AND_EVIDENCE
Control Room: 71
Status: `HORUS-CANDIDATE / NON-AUTHORITATIVE`
Promotion: NOT AUTHORIZED
Purpose: preserve newly synthesized experience without silently converting analysis into Memory, Governance or default practice.

## Contract

Each unit must preserve:

`OBSERVATIONS → INFERENCE → INVARIANT → BOUNDARY → COUNTERINDICATION → PROVENANCE → TRANSFER TARGET`

These records are analytical candidates. They are not canonical Knowledge Records and are not active Experience Spine inputs unless independently verified and promoted through existing mechanisms.

---

## HXU-2026-08-29-001 — Discovery failure is surface-bounded

**Candidate status:** HORUS-CANDIDATE

**Observed facts**
- P31 repository search returned no expected P30 delta.
- Direct authoritative-path retrieval found the artifact on `main`.
- MEM-009 separately records that bounded/truncated/heuristic search cannot justify exhaustive absence.

**Inference**
A retrieval miss primarily reports failure to discover through that retrieval surface unless the surface is proven complete for the target universe.

**Invariant**
`DISCOVERY FAILURE IS A CLAIM ABOUT THE SEARCH SURFACE, NOT THE RESOURCE UNIVERSE`.

**Applicability boundaries**
- Applies when retrieval completeness is unknown, bounded, heuristic, stale, paginated or otherwise limited.
- Does not weaken an absence result produced by a demonstrably complete authoritative enumeration of the exact bounded universe.

**Counterindications**
- Exact authoritative inventory with proven completeness for the target scope.
- Direct path/identity lookup whose contract itself exhaustively answers the exact existence claim.

**Failure lineage**
`EVIDENCE_GAP / RETRIEVAL_FAILURE` rather than artifact absence.

**Provenance**
- `Memory/MEM-009_MEMORY_EVOLUTION.md` lessons 4 and 6.
- `Memory/Engineering_Journal/EJR-214_2026-08-14_P31_SESSION_CLOSURE.md`.

**Evidence independence note**
MEM-009 promotion and EJR-214 share event lineage for P31; they must not be counted as two independent observations of that incident.

**Current applicability**
High for repository search, connectors, resource discovery and identity audit.

**Suggested consumers**
`SHARED / ARGO / HERMUZ / HORUS`

**Candidate relations**
`DERIVED_FROM MEM-009:L4,L6`; `DERIVED_FROM EJR-214`; `REFINES search-scope lesson`.

---

## HXU-2026-08-29-002 — Independence belongs to lineage, not count

**Candidate status:** HORUS-CANDIDATE

**Observed facts**
- Reusable lessons may have multiple records describing the same originating event.
- Experience Spine explicitly groups records by `evidence_group` and reports same-group items as `CORRELATED_NOT_INDEPENDENT`.
- EJR-211 requires repeated observation and independent re-checking before promotion of broad lessons.

**Inference**
Record multiplicity cannot establish independent corroboration when records derive from one event, one source, one copied payload or one causal chain.

**Invariant**
`INDEPENDENCE IS A PROPERTY OF EVIDENCE LINEAGE, NOT RESULT COUNT`.

**Applicability boundaries**
- Applies to corroboration/confidence claims.
- Multiple correlated records may still improve traceability, explanatory detail or consistency checking; they simply do not multiply independent support.

**Counterindications**
Materially independent observations with separate causal/evidence origins that converge on the same claim may strengthen confidence.

**Failure lineage**
`MODEL_ASSUMPTION_FAILURE / EVIDENCE_GAP` when count is mistaken for independence.

**Provenance**
- `Knowledge/Learning/experience_spine.py` correlation handling.
- `Memory/Engineering_Journal/EJR-211_2026-08-14_P29_VALIDATED_PLATFORM_LESSONS.md` promotion basis.

**Current applicability**
High for multi-agent reports, multiple tools, repeated tests, mirrors and derived documents.

**Suggested consumers**
`SHARED / ARGO / HERMUZ / HORUS`

**Candidate relations**
`DERIVED_FROM Experience-Spine evidence-group semantics`; `SUPPORTS evidence reasoning`; `BOUNDARY_OF corroboration-count claims`.

---

## HXU-2026-08-29-003 — Failed implementation can preserve design learning

**Candidate status:** HORUS-CANDIDATE

**Observed facts**
- GOV-016 requires separation among idea, implementation, test, infrastructure, model-assumption, governance, evidence and schema failures.
- GOV-016 explicitly prohibits automatically invalidating an idea because one implementation failed.
- Repository build history repeatedly uses failures to refine tests, execution channels and architecture while retaining useful concepts.

**Inference**
The reusable residue of failure may be a design principle, boundary, negative pattern or recovery technique even when the failed artifact itself must not be promoted.

**Invariant**
`FAILURE MAY PRODUCE REUSABLE DESIGN KNOWLEDGE WITHOUT VALIDATING THE FAILED IMPLEMENTATION`.

**Applicability boundaries**
- The retained learning must be supported by the failure evidence and preserve the exact failure class.
- A demonstrated `IDEA_FAILURE` cannot be reframed as support for the failed idea.
- Historical preservation does not authorize future execution.

**Counterindications**
Repeated failures across genuinely sound independent implementations can shift evidence against the underlying idea.

**Failure lineage**
All GOV-016 classes; interpretation is class-dependent.

**Provenance**
- `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`.

**Current applicability**
High for experiments, CI repairs, connectors, schemas and cognitive mechanisms.

**Suggested consumers**
`SHARED / HERMUZ / HORUS`

**Candidate relations**
`DERIVED_FROM GOV-016`; `SUPPORTS failure-to-learning`; `BOUNDARY_OF failure-means-rejection assumption`.

---

## HXU-2026-08-29-004 — Currentness is claim-layer specific

**Candidate status:** HORUS-CANDIDATE

**Observed facts**
- Historical PR evidence remains useful provenance but cannot silently establish current-main behavior.
- P36 positive search hits were valid returned artifacts but stale relative to authoritative current main.
- GOV-018 separates historical, state, execution, identity and provenance claim types.

**Inference**
A source can be current enough for one claim layer and stale for another. Staleness must attach to the claim being made rather than globally erasing source value.

**Invariant**
`CURRENTNESS IS CLAIM-LAYER SPECIFIC`.

**Applicability boundaries**
- Current-state and execution claims require temporally fit evidence.
- Historical/provenance claims may correctly rely on older evidence.
- Normative authority is not determined by recency alone.

**Counterindications**
A source proven equivalent to the authoritative current state for the target claim may be reconciled as currently applicable.

**Failure lineage**
`EVIDENCE_GAP / MODEL_ASSUMPTION_FAILURE` when age is ignored or treated as a universal invalidator.

**Provenance**
- `Memory/MEM-009_MEMORY_EVOLUTION.md` lessons 3 and 7.
- `Memory/Engineering_Journal/EJR-219_2026-08-14_P36_SESSION_CLOSURE.md`.
- bounded analytical support from candidate `GOV-018` claim-type semantics.

**Current applicability**
High for branches, cached search, historical records and prior run evidence.

**Suggested consumers**
`SHARED / ARGO / HERMUZ / HORUS`

**Candidate relations**
`DERIVED_FROM MEM-009:L3,L7`; `REFINES historical-evidence and freshness lessons`.

---

## HXU-2026-08-29-005 — Execution visibility must match the claim

**Candidate status:** HORUS-CANDIDATE

**Observed facts**
- MEM-009 distinguishes documentation from execution proof.
- Experience Spine clean extraction discovered that a focused test file existed but was not discovered/executed by the broad workflow until explicitly bound into CI.
- Successful commit persistence is separately insufficient for semantic validation.

**Inference**
Evidence that an artifact exists, is referenced, is persisted, or appears near an execution channel must not be upgraded into proof that the exact target behavior executed.

**Invariant**
`EXECUTION VISIBILITY MUST BE BOUND TO THE CLAIM BEING MADE`.

**Applicability boundaries**
- A file-existence claim can be proven by repository presence.
- A persistence claim can be proven by successful write/read-back.
- An execution claim requires execution evidence bound to the relevant identity/scope.

**Counterindications**
A verified execution record directly bound to the exact target makes additional existence inference unnecessary for the execution claim.

**Failure lineage**
`EVIDENCE_GAP / TEST_FAILURE / MODEL_ASSUMPTION_FAILURE` depending on incident.

**Provenance**
- `Memory/MEM-009_MEMORY_EVOLUTION.md` lessons 2 and 5.
- `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001.md` focused-test discovery incident.

**Current applicability**
High for CI, tests, runtime relationships, generated artifacts and connector calls.

**Suggested consumers**
`SHARED / HERMUZ / ARGO`

**Candidate relations**
`DERIVED_FROM MEM-009:L2,L5`; `DERIVED_FROM Experience-Spine-Clean`; `REFINES execution-proof boundary`.

---

## HXU-2026-08-29-006 — Structural cleanliness can expose semantic risk

**Candidate status:** HORUS-CANDIDATE

**Observed facts**
- Room71 reconciliation increasingly separates physical inventory, identity ownership and branch/workstream hygiene from semantic, relationship, authority and cognitive-effect closure.
- Experience Spine mechanics are execution-verified but its cognitive effect remains inconclusive.
- Semantic audit found compressed reusable lessons depend on recoverable boundaries to avoid over-generalization.

**Inference**
Removing structural ambiguity can reduce integration risk while making the next unresolved layer—semantic quality—more visible. Structural cleanliness is therefore a prerequisite/clarifier, not semantic proof.

**Invariant**
`STRUCTURAL CLEANLINESS CAN EXPOSE, NOT ELIMINATE, SEMANTIC RISK`.

**Applicability boundaries**
- This does not imply every structurally clean system has semantic defects.
- It only prohibits treating structural reconciliation as semantic validation.

**Counterindications**
A separate semantic validation may independently establish correctness after structural closure.

**Failure lineage**
`EVIDENCE_GAP / MODEL_ASSUMPTION_FAILURE` when proof classes are collapsed.

**Provenance**
- Room71 bounded inventory/reconciliation records.
- `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-CLEAN-001.md`.
- `Repository/MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001.md`.
- current HORUS semantic audit.

**Current applicability**
High during repository cleanup, migration and multi-agent integration.

**Suggested consumers**
`SHARED / ARGO / HERMUZ / HORUS / MAAT`

**Candidate relations**
`DERIVED_FROM Room71 reconciliation`; `BOUNDARY_OF structural-pass claims`; `SUPPORTS semantic-audit sequencing`.

---

## HXU-2026-08-29-007 — Negative evidence strength follows enumeration guarantee

**Candidate status:** HORUS-CANDIDATE

**Observed facts**
- MEM-009 distinguishes bounded search from exhaustive claims.
- P31 proved a single search miss could be false absence evidence.
- Room71 later records use `truncated:false` carefully: recursive tree completeness supports exact tree enumeration, while non-recursive `truncated:false` supports only top-level enumeration.

**Inference**
Negative evidence becomes stronger as the evidence producer's completeness guarantee becomes stronger and better aligned with the claim universe.

**Invariant**
`NEGATIVE EVIDENCE STRENGTH IS LIMITED BY THE ENUMERATION GUARANTEE`.

**Applicability boundaries**
- Enumeration guarantee must match target scope, recursion depth, identity semantics and authoritative ref.
- Complete physical enumeration does not prove semantic absence under aliases or equivalent meanings unless identity semantics are also defined.

**Counterindications**
A complete physical inventory can still miss a semantic duplicate represented under a different identifier; semantic identity requires a different validation layer.

**Failure lineage**
`EVIDENCE_GAP / MODEL_ASSUMPTION_FAILURE` when enumeration semantics are widened beyond contract.

**Provenance**
- `Memory/MEM-009_MEMORY_EVOLUTION.md` lessons 4 and 6.
- `Memory/Engineering_Journal/EJR-214_2026-08-14_P31_SESSION_CLOSURE.md`.
- Room71 bounded Knowledge/Memory inventory closure.

**Current applicability**
High for inventory, duplicate-ID searches, tree enumeration and connector/list APIs.

**Suggested consumers**
`SHARED / HERMUZ / HORUS / ARGO`

**Candidate relations**
`REFINES HXU-001`; `DERIVED_FROM MEM-009:L4,L6`; `BOUNDARY_OF absence claims`.

---

## Cross-unit synthesis — candidate meta-invariant

Across HXU-001..007, one repeated structure appears:

`EVIDENCE AT LAYER A → [REQUIRES EXPLICIT BRIDGE] → CLAIM AT LAYER B`.

Examples:

- search miss → resource absence;
- search hit → current state;
- documentation → execution;
- persistence → correctness;
- failed implementation → failed idea;
- multiple records → independent corroboration;
- clean inventory → semantic correctness;
- retrieval mechanics → cognitive improvement.

Candidate meta-invariant:

`DO NOT LET EVIDENCE CROSS A CLAIM-LAYER BOUNDARY WITHOUT AN EXPLICIT BRIDGE`.

This synthesis may overlap candidate GOV-018 evidence-layer reasoning. It must therefore be checked for novelty and non-duplication before any promotion.

## Promotion gate

None of HXU-001..007 may be treated as canonical merely because:

- HORUS derived it;
- multiple documents mention similar ideas;
- it appears logically coherent;
- it improves explanation;
- it fits Experience Spine metadata.

Required next state:

`HORUS-CANDIDATE → HERMUZ-VERIFIED (if supported) → appropriate validation/transfer test → governed promotion decision`.

Until then:

`CANDIDATE EXPERIENCE != REUSABLE PLATFORM MEMORY != GOVERNANCE AUTHORITY`.
