# REP-014 — REPOSITORY RELATIONSHIP REGISTRY  

Platform: ARGO KOP  
Document ID: REP-014  
Version: 1.2.6  
Status: Active / Relationship Enumeration In Progress  
Development Baseline: 3.2.1  
Last Audit: 2026-08-17

---

## Purpose

Provide a registry-style representation of relationships among ARGO repository artifacts.

The registry is a navigation/control layer for dependencies, references, implementations, consumption, production, validation, governance, ownership, documentation, supersession, derivation and impact.

## Critical Rule

**A reference is not automatically a relationship.**

Every relationship should eventually be supported by:

`Source Identity → Target Identity → Relationship Type → Evidence → Authority Check → Impact Scope → Consumer Scope → Review State → Checkpoint`

## Relationship Record

Each registry entry should contain:

| Field | Meaning |
|---|---|
| Relationship ID | Stable registry identifier |
| Source | Source document ID/path |
| Target | Target document ID/path |
| Type | Controlled relationship type |
| Direction | Source → Target |
| Evidence | Why the relationship exists |
| Authority | Which document/rule authorizes it |
| State | Proposed / Verified / Revalidation Required / Closed / Rejected |
| Last Review | Review date |
| Checkpoint | Commit/blob evidence where available |
| Impact | Known affected consumers |
| Consumer Scope | Downstream artifacts requiring re-read |

## Controlled Relationship Types

```text
REFERENCES
DEPENDS_ON
IMPLEMENTS
CONSUMES
PRODUCES
VALIDATES
GOVERNS
OWNS
DOCUMENTS
SUPERSEDES
DERIVED_FROM
AFFECTED_BY
```

Relationship sublabels such as `DECISION INPUT`, `ORCHESTRATION`, `SERVICE INPUT` or `CONTROLLED MUTATION` are evidence descriptions, not new uncontrolled relationship types.

## Current Verified / Revalidated Relationships

The following are deliberately limited to relationships established during repository review. This is **not** a complete graph.

| ID | Source | Target | Type | State |
|---|---|---|---|---|
| REL-001 | SPEC-001-KNOWLEDGE-ORGANIZATION | MOD-001 | DEPENDS_ON | Revalidation Required |
| REL-002 | MOD-001 | SRV-004 | CONSUMES | Revalidated within inspected scope |
| REL-003 | SRV-005 | ENG-004 | CONSUMES | Revalidation Required |
| REL-004 | ENG-002 | ENG-006 | DEPENDS_ON | Revalidation Required |
| REL-005 | ENG-006 | SRV-009 | IMPLEMENTS | **BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E** |
| REL-006 | RUN-010 | ENG-002 | CONSUMES | Revalidated within inspected scope |
| REL-007 | RUN-010 | ENG-004 | CONSUMES | Revalidated within inspected scope |
| REL-008 | RUN-010 | ENG-006 | CONSUMES | Revalidated within inspected scope |
| REL-009 | RUN-010 | SRV-009 | CONSUMES | **REVALIDATION REQUIRED** |
| REL-010 | MOD-011 | KNW-002 | DEPENDS_ON | Revalidation Required |
| REL-011 | MOD-011 | KNW-003 | DEPENDS_ON | Revalidation Required |
| REL-012 | MOD-011 | KNW-004 | DEPENDS_ON | Revalidation Required |
| REL-013 | MOD-011 | KNW-008 | DEPENDS_ON | Revalidation Required |
| REL-014 | MOD-011 | KNW-009 | DEPENDS_ON | Revalidation Required |
| REL-015 | REP-011 | REP-012 | DEPENDS_ON | Verified |
| REL-016 | REP-013 | REP-011 | DEPENDS_ON | Verified |
| REL-017 | REP-013 | REP-012 | DEPENDS_ON | Verified |
| REL-018 | REP-015 | REP-011 | DEPENDS_ON | Verified |
| REL-019 | REP-015 | REP-012 | DEPENDS_ON | Verified |
| REL-020 | REP-015 | REP-013 | DEPENDS_ON | Verified |
| REL-021 | REP-015 | REP-014 | DEPENDS_ON | Verified |
| REL-022 | REP-001 | REP-002 | REFERENCES | Verified within control-plane scope |
| REL-023 | REP-002 | REP-001 | REFERENCES | Verified within control-plane scope |
| REL-024 | REP-001 | REP-013 | DEPENDS_ON | Verified within control-plane scope |
| REL-025 | REP-002 | REP-013 | DEPENDS_ON | Verified within control-plane scope |
| REL-026 | REP-013 | REP-014 | DEPENDS_ON | Verified within control-plane scope |
| REL-027 | REP-014 | REP-011 | DEPENDS_ON | Verified within control-plane scope |
| REL-028 | REP-014 | REP-012 | DEPENDS_ON | Verified within control-plane scope |
| REL-029 | REP-016 | REP-012 | DEPENDS_ON | Verified within control-plane scope |
| REL-030 | REP-016 | REP-011 | DEPENDS_ON | Verified within control-plane scope |
| REL-031 | REP-016 | REP-013 | DEPENDS_ON | Verified within control-plane scope |
| REL-032 | REP-016 | REP-014 | DEPENDS_ON | Verified within control-plane scope |
| REL-033 | REP-015 | REP-016 | DEPENDS_ON | Verified within current control-plane scope |
| REL-034 | REP-016 | REP-015 | CONSUMES | Verified within current control-plane scope |
| REL-035 | REP-012 | DIAG-001 | DOCUMENTS | Provenance linked within inspected scope |
| REL-036 | DIAG-001 | REP-012 | DERIVED_FROM | Provenance linked within inspected scope |
| REL-037 | CORE-003 | RUN-001 | GOVERNS | Revalidated within inspected scope |
| REL-038 | RUN-001 | CORE-003 | REFERENCES | Revalidated within inspected scope |
| REL-039 | MEM-008 | MEM-007 | DERIVED_FROM | Verified within current learning-method scope |
| REL-040 | MEM-008 | MEM-006 | DEPENDS_ON | Verified within current learning-method scope |
| REL-041 | MEM-008 | CORE-003 | REFERENCES | Verified within current learning-method scope |
| REL-042 | MEM-008 | REP-014 | REFERENCES | Verified within current learning-method scope |
| REL-043 | EJR-023 | REP-015 | REFERENCES | Verified within current session-checkpoint scope |
| REL-044 | EJR-023 | REP-013 | REFERENCES | Verified within current session-checkpoint scope |
| REL-045 | REP-001 | Memory/Operational_Memory | REFERENCES | Verified within current inventory scope |
| REL-046 | REP-002 | Memory/Operational_Memory | REFERENCES | Verified within current inventory scope |
| REL-047 | Memory/Operational_Memory | MEM-008 | REFERENCES | Verified within current learning-memory scope |
| REL-048 | OPM-001 | MEM-004 | DEPENDS_ON | Verified within current Memory-model scope |
| REL-049 | OPM-002 | OPM-001 | DEPENDS_ON | Verified within current Operational-Memory build scope |
| REL-050 | OPM-003 | OPM-001 | DEPENDS_ON | Verified within current Operational-Memory build scope |
| REL-051 | OPM-004 | OPM-001 | DEPENDS_ON | Verified within current Operational-Memory build scope |
| REL-052 | OPM-002 | MEM-008 | REFERENCES | Verified within current Guided-Discovery scope |
| REL-053 | OPM-003 | OPM-002 | DEPENDS_ON | Verified within current Operational-Memory build scope |
| REL-054 | OPM-004 | OPM-003 | DEPENDS_ON | Verified within current Operational-Memory build scope |
| REL-055 | RUN-011 | ENG-013 | REFERENCES | Revalidated within current Runtime prototype scope |
| REL-056 | RUN-011 | ENG-014 | REFERENCES | Revalidated within current Runtime validation scope |
| REL-057 | RUN-012 | RUN-011 | VALIDATES | Revalidated within current Runtime test scope |
| REL-058 | RUN-013 | RUN-011 | VALIDATES | Revalidated within current controlled-handoff scope |
| REL-059 | RUN-014 | RUN-011 | VALIDATES | Revalidated within current learning-promotion test scope |
| REL-060 | RUN-015 | RUN-011 | VALIDATES | Revalidated within current CI validation scope |
| REL-061 | GOV-013A | GOV-013 | REFERENCES | Revalidated within governance scope |

## Current Review-Cycle Reconciliation — 2026-08-17

### REL-005 executable boundary reconciliation

`REL-005` is now revalidated as a bidirectional relationship using current endpoint authority plus isolated production-runtime evidence.

Current evidence establishes both directions:

```text
ENG-006 → SRV-009 = DOCUMENTED / CONTRACTUAL + EXECUTABLE-VERIFIED IN ISOLATED E2E
SRV-009 → ENG-006 = CONTROLLED MUTATION SERVICE CONSUMED BY ENG-006
```

The Runtime production adapter executed the relationship through the governed write dispatcher and the concrete GitHub repository connector in an isolated non-canonical branch. The successful E2E run created and updated a probe artifact, performed mandatory post-write read-back, emitted governed execution traces, and removed the probe after validation.

Runtime evidence:

- Workflow run: `32021524046`
- Successful HEAD: `702f73b113ce9074ad090ba320867e1dc1eeb3c1`
- Create trace: `TR-6e94cc825acc`
- Update trace: `TR-3d0dd3df6ce3`
- Final persisted SHA before cleanup: `d3287757b644047d6de70a548cf202e34dab1e49`

Therefore the registry may now classify `REL-005` as:

`BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E`

Boundary:

- this promotion applies only to the validated ENG-006 ↔ SRV-009 relationship;
- it does not promote `REL-009` or `REL-061`;
- it does not authorize arbitrary canonical mutation;
- repository-wide graph closure remains open.

Historical P303 evidence is preserved below in repository history; this section supersedes its current-state interpretation for the present review cycle.

### REL-009 executable boundary reconciliation

`REL-009` is retained with its original source, target and `CONSUMES` relationship type, but its state is downgraded to `REVALIDATION REQUIRED`.

Current evidence establishes:

```text
RUN-010 → SRV-009 = DOCUMENTED / CONTRACTUAL
```

`RUN-010_RUNTIME_REFERENCE.md` describes the `RUN-010 → ENG-006 → SRV-009` path as a relationship description and explicitly does not claim that every runtime operation follows the path. The inspected connected execution spine records execution traces through the current entrypoint and remains simulation-only at the adapter boundary; it does not establish a callable `SRV-009` dispatch.

**The executable consumer proof is not established. no executable `VERIFIED` state is added.**

Therefore `REL-009` must not be treated as executable or verified coupling merely because the architectural sequence is documented.

This reconciliation does **not** delete the relationship, alter its direction, create a synthetic consumer, or mutate Runtime implementation. Executable promotion requires independent callable consumer evidence.

### REL-061 governance bootstrap relationship

`GOV-013A` is a canonical addendum that explicitly states it `Supplements GOV-013`. The registry controlled relationship types do not include `SUPPLEMENTS`; therefore the governed registry representation is:

```text
GOV-013A → GOV-013 = REFERENCES
```

The evidence description preserves the stronger semantic fact: `Canonical Addendum / Supplements GOV-013`.

This record does not grant `GOV-013A` higher authority, replace `GOV-013`, or authorize any unrelated mutation.

### Authority boundary

These state corrections are evidence reconciliation only. They do not authorize mutation of `ENG-006`, `SRV-009`, Runtime execution code, or other canonical authority layers.

### Checkpoint

`P303` updated the explicit evidence language requested by the current integration/integrity tests while preserving the unresolved executable boundary. The relationship remains open until executable evidence is independently established.

## Identity Drift Reconciliation — 2026-08-13

`REL-001` was reclassified because the inspected target artifact identifies itself as `SPEC-001-KNOWLEDGE-ORGANIZATION`, not the abbreviated `SPEC-001` identifier previously recorded in this registry.

The target artifact exists at `Specifications/01-Knowledge-Organization.md` and is the artifact referenced by `MOD-001`. The relationship is therefore retained but marked `Revalidation Required` until the canonical identity mapping is independently reconciled across the applicable repository indexes.

This avoids silently treating an abbreviated identifier as an authoritative document identity.

## Operational Memory Build-01 Reconciliation — 2026-08-11

Build-01 constructs the first explicit `Memory/Operational_Memory` subdomain. The relationships above are intentionally scoped to the inspected artifacts and do not imply that the full Memory domain is complete.

```text
REP-001 ──references──> Operational_Memory
REP-002 ──references──> Operational_Memory
Operational_Memory ──references──> MEM-008

OPM-001 ──depends_on──> MEM-004
OPM-002 ──depends_on──> OPM-001
OPM-003 ──depends_on──> OPM-001
OPM-004 ──depends_on──> OPM-001
OPM-002 ──references──> MEM-008
OPM-003 ──depends_on──> OPM-002
OPM-004 ──depends_on──> OPM-003
```

Rationale:

- `REP-001` and `REP-002` were directly updated to enumerate the newly constructed physical subdomain.
- `OPM-001` defines the operational memory item structure and therefore depends on the existing Memory lifecycle authority represented by `MEM-004` within the inspected scope.
- `OPM-002`, `OPM-003`, and `OPM-004` depend on the model defined by `OPM-001`.
- `OPM-002` references `MEM-008` because its capture model explicitly supports the Guided Discovery learning pattern already recorded there.
- Retrieval and lifecycle operate on the capture/model chain rather than becoming independent memory authorities.

These relationships are build-scope relationships. Consolidated Memory validation remains open.

## Learning-Method Reconciliation

The repository now records `MEM-008_GUIDED_DISCOVERY_LEARNING_METHOD.md` as the canonical candidate for the observed Guided Discovery training method.

The relationships are intentionally limited to independently evidenced directions:

```text
MEM-008 ──derived_from──> MEM-007
MEM-008 ──depends_on────> MEM-006
MEM-008 ──references────> CORE-003
MEM-008 ──references────> REP-014
```

Rationale:

- `MEM-007` establishes the authoritative Memory Baseline and the requirement that validated memory becomes baseline through evidence and repository review. MEM-008 operationalizes that learning evidence as a learning-method record.
- `MEM-006` establishes Memory Quality dimensions including accuracy, context, consistency, completeness, traceability, continuity, maintainability, reusability, authority and timeliness. MEM-008 relies on these properties when preserving learning events and their evidence.
- `CORE-003` remains the governing authority for repository changes; MEM-008 explicitly states that learning does not itself grant authority to mutate canonical documents.
- `REP-014` is the relationship registry used to preserve independently evidenced links and therefore is referenced by MEM-008 when recording learning artifacts and their provenance.

No reverse relationships are inferred merely because these documents reference one another conceptually. Reverse entries should be added only after direct source evidence is inspected.

## Session Checkpoint Reconciliation — 2026-08-11

`EJR-023` records the current-session bootstrap inspection and explicitly identifies `REP-015` as the bootstrap/continuation authority and `REP-013` as the content-inventory artifact inspected during the checkpoint.

Therefore the following relationships are registered:

```text
EJR-023 ──references──> REP-015
EJR-023 ──references──> REP-013
```

These are checkpoint/documentation relationships only. They do not make the Engineering Journal authoritative over either control-plane artifact.

## Guided Discovery as a Learning Control

The new learning method introduces a controlled distinction between:

```text
Instruction
Hint
Question
Independent Discovery
```

and records the progression from:

`Taught Rule → Applied Rule → Observed Outcome → Error Diagnosis → Rule Revision → Re-test → Experience`

This is a learning method, not a new authority layer and not an automatic authorization for self-modification.

## Core-to-Runtime Reconciliation

The current review established a material authority relationship between the Constitution and the canonical boot/runtime sequence.

Evidence:

- `Core/CORE-003_CONSTITUTION.md` explicitly states that its rules have higher authority than implementation decisions and that all repository components shall comply within applicable scope.
- `Runtime/RUN-001_BOOT_SEQUENCE.md` explicitly lists `Core/CORE-003_CONSTITUTION.md` under Related Authority and states that Runtime executes approved architecture without redefining Constitution, Governance, Repository authority, Canonical Architecture or Release authority.

Therefore the registry records the two independently evidenced directions:

```text
CORE-003 ──governs──> RUN-001
RUN-001 ──references──> CORE-003
```

The reverse `REFERENCES` relationship is not inferred merely because a `GOVERNS` relationship exists; it is recorded because RUN-001 explicitly names CORE-003 as related authority.

This reconciliation does not certify the complete Core-to-Runtime graph. Other Core, Governance, Architecture and Runtime relationships remain subject to scoped verification.

## Control-Plane Graph

The minimum repository control-plane graph is explicitly represented through the current Phase-1 work queue and bootstrap relationships:

```text
REP-001 ──references──> REP-002
   │                      │
   ├──depends_on────────> REP-013
   │                      │
   └──────────────────────┘

REP-013 ──depends_on──> REP-011
   │
   └──depends_on──────> REP-012

REP-014 ──depends_on──> REP-011
   │
   └──depends_on──> REP-012

REP-015 ──depends_on──> REP-011
         ├────────────> REP-012
         ├────────────> REP-013
         ├────────────> REP-014
         └────────────> REP-016

REP-016 ──depends_on──> REP-011
         ├────────────> REP-012
         ├────────────> REP-013
         ├────────────> REP-014
         └──consumes──> REP-015

REP-012 ──documents──> DIAG-001
DIAG-001 ──derived_from──> REP-012
```

`REP-016` is the execution queue and therefore consumes the control-plane evidence rather than replacing it.

The DIAG-001 edge is provenance/navigation only. It does not make the diagram authoritative over REP-012 or any canonical registry.

This graph describes control-plane dependency only. It does not certify domain semantics.

## P346 Current Control-Plane Evidence Binding — 2026-08-17

Current main evidence through P345 was re-read against the current control-plane manifest and the manifest-driven reconciliation gate.

Evidence bound in this section:

- P345 bound REP-013 after full-content preservation and read-back;
- P340 manifest-driven control-plane gate remained the current consistency gate;
- P345 CI passed Integrity, Integration and Prototype jobs, with the Full-Stack Repository Audit also passing;
- current REP-014 content/blob before this mutation was `6aa9e2d29800659186187203a49db407190327f3`;
- this mutation preserves all prior REP-014 content and appends only this evidence-binding section.

Disposition:

`REP-014 = PRESENT / CURRENT / P346-BINDING-COMPLETE WITHIN CURRENT CONTROL-PLANE EVIDENCE SCOPE`

This is an evidence-binding result only. It does **not** promote any unresolved relationship to `VERIFIED`, does not promote the control plane to `RECONCILED`, does not set `CLOSED_FOR_PHASE_1`, and does not close Priority 1.

The cross-registry state remains open until the corresponding `REP-015/016/020` evidence is reconciled to the same current checkpoint.

---

End of REP-014
