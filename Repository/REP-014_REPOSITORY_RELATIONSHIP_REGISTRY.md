# REP-014 — REPOSITORY RELATIONSHIP REGISTRY

Platform: ARGO KOP  
Document ID: REP-014  
Version: 1.0.8  
Status: Active / Relationship Enumeration In Progress  
Development Baseline: 3.3.0  
Last Audit: 2026-08-10

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

The following are deliberately limited to relationships established during repository review. This is **not a complete graph**.

| ID | Source | Target | Type | State |
|---|---|---|---|---|
| REL-001 | SPEC-001 | MOD-001 | DEPENDS_ON | Revalidated within inspected scope |
| REL-002 | MOD-001 | SRV-004 | CONSUMES | Revalidated within inspected scope |
| REL-003 | ENG-004 | SRV-005 | PRODUCES | Revalidated within inspected scope |
| REL-004 | ENG-002 | ENG-006 | DEPENDS_ON | Revalidation Required |
| REL-005 | ENG-006 | SRV-009 | IMPLEMENTS | Revalidated within inspected scope |
| REL-006 | RUN-010 | ENG-002 | CONSUMES | Revalidated within inspected scope |
| REL-007 | RUN-010 | ENG-004 | CONSUMES | Revalidated within inspected scope |
| REL-008 | RUN-010 | ENG-006 | CONSUMES | Revalidated within inspected scope |
| REL-009 | RUN-010 | SRV-009 | CONSUMES | Revalidated within inspected scope |
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
   └──depends_on──────> REP-012

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

## Registry Does Not Grant Authority

REP-014 is a relationship registry and navigation/control artifact.

It does not become the canonical owner of Governance, Architecture, Models, Knowledge, Runtime, or other domain semantics merely by recording a relationship.

Domain authority remains with the applicable canonical authority document.

## Bidirectional Reconciliation

For every material relationship, the review process should eventually verify both directions:

```text
Source → Target
Target → Source
```

A one-sided reference is insufficient to declare the graph closed.

The control-plane relationships above are considered verified only within the inspected scope; broader repository graph closure remains open.

## Relationship-to-Artifact Control

Every registry relationship must be resolvable through `REP-013` and its artifact state through `REP-012`/`REP-011`.

A relationship must not be marked `Verified` if either endpoint:

- cannot be resolved to a current repository artifact;
- has unresolved identity conflict;
- is marked `QUARANTINED` without explicit relationship review;
- or has a material mutation requiring revalidation.

## Visual Artifact Provenance Rule

Visual or derived artifacts may summarize repository state, but they require an explicit provenance relationship to the source artifacts from which their content was derived.

For `DIAG-001`:

`REP-012 → DOCUMENTS → DIAG-001`

`DIAG-001 → DERIVED_FROM → REP-012`

The paired SVG/metadata files are orientation/provenance artifacts. Their numerical or status claims cannot override current registry evidence.

If the source registry materially changes, DIAG-001 becomes stale and must enter:

`REVALIDATION_REQUIRED`

until regenerated or explicitly superseded.

## Change Impact Rule

A mutation to a source or target artifact may invalidate relationship records.

When a file is renamed, moved, archived, merged, split, or materially changed, affected relationship records enter:

`REVALIDATION_REQUIRED`

until the source, target and known consumers are re-read.

## Control-Plane Synchronization Rule

A control-plane artifact that creates or changes execution state must be represented in the relationship graph before that relationship is treated as closed.

For the current Phase-1 control plane, the minimum synchronized set is:

`REP-011 ↔ REP-012 ↔ REP-013 ↔ REP-014 ↔ REP-015 ↔ REP-016`

The current registry explicitly represents the previously missing `REP-015 ↔ REP-016` execution/bootstrap relationship.

No reverse relationship has been inferred merely because two artifacts participate in the same control plane. Reverse links must be added only when their source, target, type and evidence are independently established.

If a new control-plane artifact is added, moved or materially changed, its relationships must be reconciled before claiming control-plane completeness.

## Reconciliation State

The presence of a relationship record does not by itself mean the entire control plane is reconciled.

Current control-plane relationship status:

`PARTIALLY RECONCILED / INTEGRITY HOLD`

The remaining open work includes broader endpoint identity verification, evidence/checkpoint completion, consumer impact validation, and enumeration beyond the inspected control-plane scope.

## Completion Rule

The registry is not complete until the applicable repository scope has been enumerated and all material relationships are either:

- verified;
- explicitly unresolved;
- rejected with reason;
- or marked for later phase.

Unknown relationships must not be silently inferred.

## Phase 1 Rule

Relationship enumeration remains **OPEN** until Phase-1 completion is explicitly decided.

The existence of this registry does not close any folder or domain.

---

End of Document
