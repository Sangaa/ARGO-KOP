# ENG-004

---

# VALIDATION ENGINE SPECIFICATION

---

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: ENG-004
Version: 3.2.0
Status: Integrity Hold / Revalidated
Category: Engine
Canonical: Yes
Priority: Critical
Last Audit Date: 2026-08-08

---

# Purpose

The Validation Engine (`ENG-004`) is the integrity gate for ARGO KOP engineering and execution flows.

It validates artifacts, metadata, references, dependencies and applicable governance constraints before an authorized state mutation is accepted.

# Validation Framework

| Validation Scope | Required Evidence | Action on Violation |
| :--- | :--- | :--- |
| Metadata | Current applicable document metadata standard | Reject or hold; issue `METADATA_ERROR`. |
| Naming | Current applicable naming authority | Reject or hold; issue `NAMING_ERROR`. |
| Quality | Current applicable quality gate | Block or hold mutation. |
| Cross-References | Verified current target artifacts | Flag unresolved reference and hold affected decision. |
| Canonical Identity | Governance / Repository evidence | Do not certify canonical status when authority is ambiguous. |
| Evidence Coverage | Required repository content for the decision | Stop or constrain execution. |

# Repository-First Rules

1. Current repository evidence overrides historical references, ZIP snapshots and model assumptions.
2. A referenced path is not valid merely because a document names it.
3. If a target artifact cannot be located and verified, the dependency remains `UNRESOLVED`.
4. Archived material is not treated as active authority without explicit evidence.
5. Folder names do not establish architecture or authority.
6. A successful mutation does not itself prove validation success.

# Validation Sequence

Repository Synchronization

↓

Required Artifact Enumeration

↓

Content Inspection

↓

Cross-Reference Resolution

↓

Authority / Canonical Check

↓

Constraint Validation

↓

Mutation Gate

↓

Post-Mutation Re-read

↓

Validation Result

# Evidence States

- `VERIFIED`
- `PARTIALLY_VERIFIED`
- `UNAVAILABLE`
- `INFERRED`
- `ASSUMED`
- `UNRESOLVED`

`UNAVAILABLE`, `ASSUMED` or materially `UNRESOLVED` evidence cannot be silently promoted to verified state.

# Hold Conditions

The Validation Engine shall return `HOLD` when:

- required evidence is unavailable;
- a canonical target is ambiguous;
- a dependency points only to historical/archived material without active authority;
- cross-layer contracts conflict;
- evidence coverage is insufficient for the requested decision.

# Related Documents

- `PROJECT_BOOTSTRAP.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

---

# Guiding Statement

Validation is not a status label; it is an evidence-backed determination made against the current repository state.

---

End of Document
