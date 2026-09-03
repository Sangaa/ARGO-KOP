# REP-014 — REPOSITORY RELATIONSHIP REGISTRY  

Platform: ARGO KOP  
Document ID: REP-014  
Version: 1.2.17
Status: Active / Relationship Enumeration In Progress  
Development Baseline: 3.2.1  
Last Audit: 2026-09-03

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
| REL-001 | SPEC-001-KNOWLEDGE-ORGANIZATION | MOD-001 | DEPENDS_ON | Revalidated within inspected authority scope |
| REL-002 | MOD-001 | SRV-004 | CONSUMES | Revalidated within inspected scope |
| REL-003 | SRV-005 | ENG-004 | CONSUMES | Revalidated within inspected scope |
| REL-004 | ENG-006 | ENG-002 | CONSUMES | Revalidated within inspected scope |
| REL-005 | ENG-006 | SRV-009 | IMPLEMENTS | **BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E** |
| REL-006 | RUN-010 | ENG-002 | CONSUMES | Revalidated within inspected scope |
| REL-007 | RUN-010 | ENG-004 | CONSUMES | Revalidated within inspected scope |
| REL-008 | RUN-010 | ENG-006 | CONSUMES | Revalidated within inspected scope |
| REL-009 | RUN-010 | SRV-009 | CONSUMES | **INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL** |
| REL-010 | KNW-002 | MOD-011 | CONSUMES | Revalidated within inspected scope |
| REL-011 | MOD-011 | KNW-003 | REFERENCES | Revalidation Required |
| REL-012 | MOD-011 | KNW-004 | DEPENDS_ON | Revalidated within inspected scope |
| REL-013 | MOD-011 | KNW-008 | REFERENCES | Revalidated within inspected scope |
| REL-014 | KNW-009 | MOD-011 | CONSUMES | Revalidated within inspected scope |
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
| REL-056 | ENG-014 | RUN-011 | REFERENCES | **RUNTIME VALIDATION CONTRACT / DIRECT-SOURCE-VALIDATED / NON-DEPENDENCY** |
| REL-057 | RUN-012 | RUN-011 | VALIDATES | Revalidated within current Runtime test scope |
| REL-058 | RUN-013 | RUN-011 | VALIDATES | **CONTROLLED-HANDOFF TRACE GATE / EXECUTABLE-TESTED / SIDE-EFFECT-FREE / NON-AUTHORITY** |
| REL-059 | RUN-014 | RUN-011 | VALIDATES | **TRACE-TO-LEARNING-CANDIDATE / EXECUTABLE-TESTED / SEPARATE-PROMOTION-AUTHORITY** |
| REL-060 | RUN-015 | RUN-011 | VALIDATES | Revalidated within current CI validation scope |
| REL-061 | GOV-013A | GOV-013 | REFERENCES | **INTENTIONAL ONE-WAY / GOVERNANCE-REVALIDATED** |
| REL-062 | CORE-KERNEL | RUN-001 | REFERENCES | **INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY** |
| REL-063 | CORE-009 | LIF-001 | REFERENCES | **DOCUMENT-LIFECYCLE-BOUNDARY / BIDIRECTIONAL-DOCUMENTARY / NON-DEPENDENCY** |
| REL-064 | LIF-001 | CORE-009 | REFERENCES | **PLATFORM-LIFECYCLE-BOUNDARY / BIDIRECTIONAL-DOCUMENTARY / NON-DEPENDENCY** |
| REL-065 | CORE-012 | GOV-016 | REFERENCES | **INTENTIONAL ONE-WAY / FAILURE-LEARNING-ALIGNED / NON-DEPENDENCY** |
| REL-066 | ARC-005 | CORE-011 | REFERENCES | **INTENTIONAL ONE-WAY / CHARTER-BOUNDARY-ALIGNED / NON-DEPENDENCY** |
| REL-067 | ARC-006 | CORE-003 | REFERENCES | **INTENTIONAL ONE-WAY / CONSTITUTION-AUTHORITY-ALIGNED / NON-DEPENDENCY** |
| REL-068 | CORE-003 | ARC-011 | GOVERNS | **CONSTITUTION-AUTHORITY / DIRECT-SOURCE-VALIDATED / NON-DEPENDENCY** |
| REL-069 | ARC-011 | CORE-003 | REFERENCES | **SUBORDINATE-ARCHITECTURE / DIRECT-SOURCE-VALIDATED / NON-DEPENDENCY** |
| REL-070 | CORE-KERNEL | RUN-009 | REFERENCES | **INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY** |
| REL-071 | CORE-003 | RUN-003 | GOVERNS | **CONSTITUTION-AUTHORITY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY** |
| REL-072 | RUN-003 | CORE-003 | REFERENCES | **CRITICAL-RUNTIME-CONFIGURATION / DIRECT-SOURCE-VALIDATED / NON-DEPENDENCY** |

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

`REL-009` retains its canonical identity and controlled relationship type:

```text
RUN-010 → SRV-009 = CONSUMES
```

Current evidence now supports a bounded intentional-directional disposition:

`INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`

Evidence basis:

- `Runtime/RUN-010_RUNTIME_REFERENCE.md` describes the governed execution relationship ending in `SRV-009 Controlled Mutation` while explicitly stating that the sequence is not a claim that every runtime operation follows that exact path.
- current main contains a pure RUN-010 handoff contract plus an integration-only observation harness that composes the existing governed ENG-006/SRV-009 production adapter;
- the observation preserves execution/task/session/source-trace identity and authorization identity and records an attributable SRV-009-targeted dispatch with post-read verification;
- exact-main Full-Stack and Runtime/Integration CI verify the positive isolated observation and the negative normal connected-spine boundary together;
- the normal connected spine remains simulation-oriented and contains no direct `SRV-009` dispatch;
- provider-backed ENG-006/SRV-009 E2E evidence remains a separate evidence class from the isolated RUN-010 observation.

Directionality boundary:

- no `SRV-009 → RUN-010` dependency is created;
- no reverse dependency is required merely to manufacture graph symmetry;
- this state does not mean every RUN-010 operation invokes SRV-009;
- this state does not convert the normal connected spine to production dispatch;
- repository-wide graph closure is not implied.

Current evidence checkpoints include:

- P3 clean proof merged to main: `a538325bcde36d3a45f19583ca20d72d8f591e0a`;
- P3 exact-main Full-Stack: `33196013636` — SUCCESS;
- P3 exact-main Runtime/Integration: `33196013609` — SUCCESS;
- P4 semantic reconciliation merged to main: `94a9bbb43432f3e098854571130778a498f76299`;
- P4 exact-main Full-Stack: `33196750118` — SUCCESS;
- P4 exact-main Runtime/Integration: `33196750113` — SUCCESS.

Historical records that state executable consumer evidence was absent remain valid for their original checkpoint and are superseded only for current operational interpretation within this bounded relationship scope.

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

The target artifact exists at `Specifications/01-Knowledge-Organization.md` and is the artifact referenced by `MOD-001`.

Current direct source re-read establishes the bounded authority relationship without changing its controlled type:

- `Specifications/01-Knowledge-Organization.md` identifies itself as `SPEC-001-KNOWLEDGE-ORGANIZATION`, places canonical Models above the Specification in its authority boundary, and requires dependency authority checks;
- `Models/MOD-001_KNOWLEDGE_MODEL.md` is canonical and explicitly names the Specification as an active operational specification while stating that it does not override the canonical knowledge model.

Therefore `REL-001` remains `DEPENDS_ON` and is now `Revalidated within inspected authority scope`.

This disposition is intentionally bounded: it does not certify the complete Specifications or Models layers, does not create a reverse edge, and does not promote repository-wide graph integrity.

This avoids silently treating identity correction or authority evidence as broader certification.

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

## P7 Core-Kernel → RUN-001 Relationship Reconciliation — 2026-09-01

Current Priority-7 review validates one additional bounded Core-to-Runtime contract seam:

```text
CORE-KERNEL ──references──> RUN-001
```

Evidence basis:

- `Core/ARGO_KERNEL.md` is canonical, identifies itself as `Core / Runtime Contract`, and explicitly states that the current canonical runtime lifecycle is defined by `Runtime/RUN-001_BOOT_SEQUENCE.md`;
- the Kernel states that it does not duplicate or supersede the Runtime lifecycle definition and lists `RUN-001` under Related Authority;
- direct inspection of `RUN-001` confirms the canonical boot/runtime contract but does not identify `CORE-KERNEL` as a specific required dependency or consumer;
- current reverse searches do not establish a `RUN-001 → CORE-KERNEL` dependency/consumer edge;
- `Architecture/ARC-006_DEPENDENCY_MODEL.md` states that Core has no architectural-layer dependency on lower layers, so the forward edge must not be promoted to `DEPENDS_ON` merely because the Kernel aligns to the Runtime contract.

Disposition:

`REL-062 = INTENTIONAL ONE-WAY / RUNTIME-CONTRACT-ALIGNED / NON-DEPENDENCY`

Boundary:

- this is documentary/contract alignment, not executable proof;
- no `CORE-KERNEL → RUN-001 = DEPENDS_ON` edge is created;
- no `RUN-001 → CORE-KERNEL` edge is manufactured for symmetry;
- existing `REL-037/038` remain unchanged;
- broader Core cross-layer validation and certification remain open.

## P7 CORE-009 ↔ LIF-001 Lifecycle Authority Reconciliation — 2026-09-01

Current Priority-7 review validates a bounded bidirectional documentary seam between platform lifecycle and document lifecycle authority:

```text
CORE-009 ──references──> LIF-001
LIF-001  ──references──> CORE-009
```

Evidence basis:

- `Core/CORE-009_PLATFORM_LIFECYCLE.md` defines platform evolution while explicitly preserving separate lifecycle authority for individual document artifacts;
- current `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md` is canonical for document lifecycle and explicitly describes its interaction with `CORE-009` without inheriting platform-lifecycle authority;
- the former `Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md` identity/path is retired provenance after collision with active `Governance/GOV-005_REVIEW_STANDARD.md`;
- Priority-7 correction changes only the stale document-lifecycle identity/path inside CORE-009; it does not merge the two lifecycle authorities;
- neither inspected source establishes a `DEPENDS_ON`, `GOVERNS`, `IMPLEMENTS`, or `CONSUMES` relationship between these two lifecycle artifacts.

Disposition:

- `REL-063 = DOCUMENT-LIFECYCLE-BOUNDARY / BIDIRECTIONAL-DOCUMENTARY / NON-DEPENDENCY`.
- `REL-064 = PLATFORM-LIFECYCLE-BOUNDARY / BIDIRECTIONAL-DOCUMENTARY / NON-DEPENDENCY`.

Boundary:

- these are documentary reference relationships, not executable proof;
- no stronger relationship type is inferred from related lifecycle semantics;
- `CORE-009` remains platform-lifecycle authority only;
- `LIF-001` remains document-lifecycle authority only;
- broader Core and Lifecycle cross-domain validation and certification remain open.

## P7 CORE-012 → GOV-016 Failure/Learning Reconciliation — 2026-09-01

Current Priority-7 review validates one bounded Core-to-Governance learning-control seam:

```text
CORE-012 ──references──> GOV-016
```

Evidence basis:

- `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md` explicitly states that its Failure-as-Generative-Training rule works together with `GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`;
- current `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md` is ACTIVE / MANDATORY and defines failure classification, root-cause analysis, regression, reuse and knowledge transfer;
- direct target inspection does not name `CORE-012` as a dependency or required source, so no reverse registry edge is established;
- historical EJR-251 provenance shows CORE-012 and GOV-016 were introduced together in governed inventory reconciliation, but co-introduction and later co-authority usage do not independently create a reverse relationship;
- historical GOV-016 path reconciliation preserved its semantics and did not change Core authority or relationships.

Disposition:

`REL-065 = INTENTIONAL ONE-WAY / FAILURE-LEARNING-ALIGNED / NON-DEPENDENCY`.

Boundary:

- CORE-012 and GOV-016 source content remain unchanged;
- no `GOV-016 → CORE-012` edge is manufactured for symmetry;
- no `CORE-012 → GOV-016 = DEPENDS_ON` edge is inferred from the phrase “works together”;
- no authority promotion is implied;
- broader Core cross-layer validation and certification remain open.

## P7 ARC-005 → CORE-011 Charter/Rules Reconciliation — 2026-09-01

Current Priority-7 review validates one bounded Architecture-to-Core documentary seam:

```text
ARC-005 ──references──> CORE-011
```

Evidence basis:

- `Architecture/ARC-005_ARCHITECTURE_RULES.md` explicitly lists `Core/CORE-011_PLATFORM_CHARTER.md` under Related Documents;
- `Core/CORE-011_PLATFORM_CHARTER.md` defines platform scope, responsibilities and authority boundaries but does not directly name ARC-005;
- `Architecture/ARC-006_DEPENDENCY_MODEL.md` preserves the architectural rule that Core depends on none while Architecture may depend on Core/Governance; the documentary reference therefore must not be inverted or promoted merely for symmetry;
- independent repository search found no direct current evidence for a reverse `CORE-011 → ARC-005` registry edge or for stronger `DEPENDS_ON`, `GOVERNS`, `IMPLEMENTS`, or `CONSUMES` semantics.

Disposition:

`REL-066 = INTENTIONAL ONE-WAY / CHARTER-BOUNDARY-ALIGNED / NON-DEPENDENCY`.

Boundary:

- CORE-011 and ARC-005 source content remain unchanged;
- no reverse edge is manufactured for symmetry;
- no architectural dependency is inferred from the Related Documents reference;
- no Core or Architecture authority promotion is implied;
- broader Core cross-layer validation and certification remain open.

## P7 ARC-006 → CORE-003 Constitution/Dependency Reconciliation — 2026-09-01

Current Priority-7 review validates one bounded Architecture-to-Core documentary authority seam:

```text
ARC-006 ──references──> CORE-003
```

Evidence basis:

- `Architecture/ARC-006_DEPENDENCY_MODEL.md` explicitly lists `Core/CORE-003_CONSTITUTION.md` under Related Documents;
- ARC-006 states Architecture may depend on Core/Governance, but also explicitly states that a textual reference to a file path does not by itself establish an architectural dependency;
- `Core/CORE-003_CONSTITUTION.md` is the highest current constitutional authority and does not directly name ARC-006;
- Transaction J validated the direct source direction, preserved the absence of reverse/stronger registry semantics, and passed all required exact-head CI before this registration;
- current reverse/search checks do not establish a direct `CORE-003 → ARC-006` registry edge or stronger `DEPENDS_ON`, `GOVERNS`, `IMPLEMENTS`, or `CONSUMES` semantics.

Disposition:

`REL-067 = INTENTIONAL ONE-WAY / CONSTITUTION-AUTHORITY-ALIGNED / NON-DEPENDENCY`.

Boundary:

- ARC-006 and CORE-003 source content remain unchanged;
- no reverse edge is manufactured for symmetry;
- no architectural dependency is inferred from the Related Documents reference;
- no constitutional or architectural authority promotion is implied;
- broader Core cross-layer validation and certification remain open.

## P7 CORE-003 ↔ ARC-011 Constitutional Authority Reconciliation — 2026-09-01

Current Priority-7 review validates and registers the bounded constitutional authority/reference pair:

```text
CORE-003 ──governs──> ARC-011
ARC-011  ──references──> CORE-003
```

Evidence basis:

- `Core/CORE-003_CONSTITUTION.md` defines the highest governing rules for ARGO KOP and requires repository components to comply within applicable scope;
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` declares itself subordinate to the Constitution and applicable Governance and explicitly places `Constitution / applicable Governance authority` above the Canonical Architecture Model;
- ARC-011 directly lists `Core/CORE-003_CONSTITUTION.md` under Related Documents;
- Transaction L validated both directions against current source text and preserved the semantic distinction between authority subordination and dependency;
- the existing REL-037/038 Core-to-Runtime pair provides a controlled-type precedent, but does not itself establish this pair.

Disposition:

- `REL-068 = CONSTITUTION-AUTHORITY / DIRECT-SOURCE-VALIDATED / NON-DEPENDENCY`.
- `REL-069 = SUBORDINATE-ARCHITECTURE / DIRECT-SOURCE-VALIDATED / NON-DEPENDENCY`.

Boundary:

- CORE-003 and ARC-011 source content remain unchanged;
- no `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES` or runtime/executable edge is inferred;
- no reverse `ARC-011 → CORE-003 = GOVERNS` edge is manufactured;
- this bounded reconciliation does not certify Core, Architecture or the repository-wide graph.

## P7 CORE-KERNEL → RUN-009 Recovery Handoff Reconciliation — 2026-09-01

Current Priority-7 review validates and registers one additional bounded Core-to-Runtime documentary seam:

```text
CORE-KERNEL ──references──> RUN-009
```

Evidence basis:

- `Core/ARGO_KERNEL.md` explicitly states that recovery follows the applicable governed recovery flow;
- the same canonical Kernel artifact directly lists `Runtime/RUN-009_RECOVERY.md` under Related Authority;
- the Kernel explicitly warns that a name appearing in the document does not establish dependency merely by being listed;
- `Runtime/RUN-009_RECOVERY.md` defines the canonical governed Runtime recovery mechanism and safe-resume conditions but does not directly identify CORE-KERNEL as a reverse dependency, consumer, implementation or governing source;
- Transaction N validation-first evidence passed all required exact-head candidate and closure workflows before this registry synchronization.

Disposition:

`REL-070 = INTENTIONAL ONE-WAY / RECOVERY-HANDOFF-ALIGNED / NON-DEPENDENCY`.

Boundary:

- CORE-KERNEL and RUN-009 source content remain unchanged;
- no reverse `RUN-009 → CORE-KERNEL` edge is manufactured;
- no `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES`, `GOVERNS` or executable-reachability relationship is inferred;
- broader Core cross-layer validation and certification remain open;
- this reconciliation does not certify Runtime or the repository-wide graph.

## P7 CORE-003 ↔ RUN-003 Runtime Configuration Authority Reconciliation — 2026-09-01

Current Priority-7 review validates and registers the bounded constitutional authority/reference pair:

```text
CORE-003 ──governs──> RUN-003
RUN-003  ──references──> CORE-003
```

Evidence basis:

- `Core/CORE-003_CONSTITUTION.md` defines the highest governing rules for ARGO KOP and requires repository components to comply within applicable scope;
- `Runtime/RUN-003_CONFIGURATION.md` is canonical and critical, controls runtime behavior without modifying repository architecture or authority, and explicitly states that Runtime configuration does not override `Core/CORE-003_CONSTITUTION.md`;
- RUN-003 directly lists CORE-003 under Related Documents and states that repository authority remains above runtime assumptions;
- Transaction P validated both directions against current source text, enforced absence of premature registry rows, prohibited stronger dependency/consumer/implementation semantics, and passed all required exact-head candidate and closure workflows;
- REL-037/038 CORE-003↔RUN-001 is an existing controlled-type precedent but does not itself establish the RUN-003 pair.

Disposition:

- `REL-071 = CONSTITUTION-AUTHORITY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY`.
- `REL-072 = CRITICAL-RUNTIME-CONFIGURATION / DIRECT-SOURCE-VALIDATED / NON-DEPENDENCY`.

Boundary:

- CORE-003 and RUN-003 source content remain unchanged;
- no `DEPENDS_ON`, `IMPLEMENTS`, `CONSUMES` or executable-reachability edge is inferred;
- no reverse `RUN-003 → CORE-003 = GOVERNS` edge is manufactured;
- Runtime configuration remains subordinate to constitutional/repository authority without becoming an architectural dependency;
- broader Core cross-layer validation and certification remain open;
- this bounded reconciliation does not certify Runtime or the repository-wide graph.

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

## P10 REL-056 Runtime Validation Direction Reconciliation — 2026-09-03

Current-source revalidation corrects the stable REL-056 row from the historical `RUN-011 → ENG-014` direction to `ENG-014 → RUN-011`.

Evidence basis:

- `Engine/ENG-014_COGNITIVE_LOOP_INTEGRATION_VALIDATION.md` directly lists `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md` under Related Contracts;
- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md` does not list ENG-014;
- the pair remains documentary/contractual and establishes no dependency, consumption, implementation, validation execution or authority transfer;
- REL-056 retains its stable registry ID and controlled `REFERENCES` type; REL-055 and REL-057..060 remain unchanged.

The earlier P75 direction remains historical evidence and is superseded only for current REL-056 interpretation. This bounded repair does not certify Runtime Gate 15, Priority 10 or the repository-wide graph.

## P10 REL-058 Controlled-Handoff Validation Reconciliation — 2026-09-03

Current-source and executable revalidation retains the stable relationship:

```text
RUN-013 → RUN-011 = VALIDATES
```

Evidence basis:

- RUN-013 directly names RUN-011 and defines the controlled-handoff safety checkpoint for a validated cognitive trace;
- `Runtime/Prototype/CONTROLLED_HANDOFF.md` binds that checkpoint to `controlled_execution_gate.py`;
- the gate evaluates the trace emitted by `cognitive_loop_harness.run` and holds incomplete, unvalidated, unauthorized or side-effecting proposals;
- the paired prototype tests exercise authorized, unauthorized and incomplete trace outcomes;
- the gate returns only handoff readiness or hold and never executes an action.

Disposition:

`REL-058 = CONTROLLED-HANDOFF TRACE VALIDATION / EXECUTABLE-TESTED / SIDE-EFFECT-FREE / NON-AUTHORITY`.

The validation claim is limited to the RUN-011 trace at the RUN-013 controlled-handoff boundary. It establishes no production executor, dependency, implementation, consumption, governance or Runtime closure. RUN-013 remains `Candidate / Integrity Hold`; Runtime Gate 15, Priority 10 and the broader graph remain open.

## P10 REL-059 Learning-Promotion Boundary Repair — 2026-09-03

The current RUN-014 test contract directly names RUN-011, but prior executable tests created isolated candidate fixtures and did not consume a RUN-011 trace. The repair adds an explicit side-effect-free trace adapter and preserves the authority boundary:

```text
RUN-011 trace → explicit observed learning candidate → RUN-014 promotion gate
action authorization ≠ learning-promotion authority
```

The adapter carries task/session identity, evidence and validation from the trace while requiring observed result, pattern, confidence, governing-conflict disposition and promotion authority explicitly. The gate now fails closed for blank identity/pattern values and governing conflict. Tests prove that an action-authorized trace remains held until distinct learning-promotion authority is supplied.

Disposition:

`REL-059 = TRACE-TO-LEARNING-CANDIDATE VALIDATION / EXECUTABLE-TESTED / SEPARATE-PROMOTION-AUTHORITY`.

`PROMOTION_ELIGIBLE` remains a candidate state, not knowledge mutation. No automatic promotion, canonical learning, dependency, implementation, consumption or governance edge is claimed. RUN-011 and RUN-014 remain `Candidate / Integrity Hold`; Runtime Gate 15, Priority 10 and the broader graph remain open.

---

End of REP-014
