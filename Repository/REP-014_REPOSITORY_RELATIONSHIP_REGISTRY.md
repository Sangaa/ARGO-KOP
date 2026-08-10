# REP-014 — REPOSITORY RELATIONSHIP REGISTRY

Platform: ARGO KOP  
Document ID: REP-014  
Version: 1.0.1  
Status: Active / Relationship Enumeration In Progress  
Development Baseline: 3.2.1  
Last Audit: 2026-08-10  

## Purpose

Provide a registry-style representation of relationships among ARGO repository artifacts.

The registry is a navigation/control layer for dependencies, references, implementations, consumption, production, validation, governance, ownership, documentation, supersession, derivation and impact.

## Critical Rule

**A reference is not automatically a relationship.**

Every relationship should eventually be supported by:

`Source Identity → Target Identity → Relationship Type → Evidence → Authority Check → Impact Scope → Review State`

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
| State | Proposed / Verified / Revalidation Required / Closed |
| Last Review | Review date |
| Checkpoint | Commit/blob evidence where available |
| Impact | Known affected consumers |

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

## Current Verified / Revalidated Relationships

The following are deliberately limited to relationships established during repository review. This is **not a complete graph**.

| ID | Source | Target | Type | State |
|---|---|---|---|---|
| REL-001 | SPEC-001 | MOD-001 | DEPENDS_ON | Revalidated within inspected scope |
| REL-002 | MOD-001 | SRV-004 | CONSUMES / IMPLEMENTATION CONTEXT | Revalidated within inspected scope |
| REL-003 | ENG-004 | SRV-005 | PRODUCES / SERVICE INPUT | Revalidated within inspected scope |
| REL-004 | ENG-002 | ENG-006 | DECISION INPUT | Revalidation scope required |
| REL-005 | ENG-006 | SRV-009 | IMPLEMENTS / CONTROLLED MUTATION | Revalidated within inspected scope |
| REL-006 | RUN-010 | ENG-002 | CONSUMES / ORCHESTRATION | Revalidated within inspected scope |
| REL-007 | RUN-010 | ENG-004 | CONSUMES / ORCHESTRATION | Revalidated within inspected scope |
| REL-008 | RUN-010 | ENG-006 | CONSUMES / ORCHESTRATION | Revalidated within inspected scope |
| REL-009 | RUN-010 | SRV-009 | CONSUMES / MUTATION PATH | Revalidated within inspected scope |
| REL-010 | MOD-011 | KNW-002 | SEMANTIC DEPENDENCY | Revalidation Required |
| REL-011 | MOD-011 | KNW-003 | SEMANTIC DEPENDENCY | Revalidation Required |
| REL-012 | MOD-011 | KNW-004 | SEMANTIC DEPENDENCY | Revalidation Required |
| REL-013 | MOD-011 | KNW-008 | TRACEABILITY DEPENDENCY | Revalidation Required |
| REL-014 | MOD-011 | KNW-009 | EVOLUTION DEPENDENCY | Revalidation Required |
| REL-015 | REP-011 | REP-012 | REVIEW / ALLOCATION CONTROL | Verified |
| REL-016 | REP-013 | REP-011 | CONTENT → REVIEW STATE | Verified |
| REL-017 | REP-013 | REP-012 | CONTENT → ALLOCATION STATE | Verified |

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

## Relationship-to-Artifact Control

Every registry relationship must be resolvable through `REP-013` and its artifact state through `REP-012`/`REP-011`.

A relationship must not be marked `Verified` if either endpoint:

- cannot be resolved to a current repository artifact;
- has unresolved identity conflict;
- is marked `QUARANTINED` without explicit relationship review;
- or has a material mutation requiring revalidation.

## Change Impact Rule

A mutation to a source or target artifact may invalidate relationship records.

When a file is renamed, moved, archived, merged, split, or materially changed, affected relationship records enter:

`REVALIDATION_REQUIRED`

until the source, target and known consumers are re-read.

## Relationship Completion Rule

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
