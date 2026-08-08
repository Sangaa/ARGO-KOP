# REP-001

---

# ARGO KOP - MASTER REPOSITORY INDEX

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: REP-001
Version: 1.7.3
Status: Integrity Hold
Category: Repository
Canonical: Yes
Priority: Critical
Last Audit Date: Aug 08, 2026

---

## 1. Purpose

Canonical index of active, verified repository artifacts within the inspected scope. An artifact is active only when identity, path, authority, version and references are consistent with the current repository baseline.

This index does not certify repository-wide cleanliness merely because a previous status record did.

The repository is currently being validated as a **relationship graph**. Index membership therefore records inventory; it does not by itself certify the relationships between inventory nodes.

## 2. Root Baseline

- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`
- `README.md`
- `VISION.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`

Historical root naming-convention material is not active canonical inventory and is preserved under `Archive/Governance-Legacy/` for migration traceability.

## 3. Core Layer

- `Core/CORE-003_CONSTITUTION.md`
- `Core/CORE-004_CORE_PRINCIPLES.md`
- `Core/CORE-005_COGNITIVE_MODEL.md`
- `Core/CORE-006_SYSTEM_PHILOSOPHY.md`
- `Core/CORE-007_DESIGN_PRINCIPLES.md`
- `Core/CORE-008_ARCHITECTURAL_LAWS.md`
- `Core/CORE-009_PLATFORM_LIFECYCLE.md`
- `Core/CORE-010_PLATFORM_ROADMAP.md`
- `Core/CORE-011_PLATFORM_CHARTER.md`
- `Core/_FOLDER_STATUS.md`

## 4. Repository Layer

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

## 5. Governance Layer

- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-004_DOCUMENT_METADATA.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Governance/GOV-010_GOVERNANCE_MODEL.md`
- `Governance/_FOLDER_STATUS.md`

No GOV-011 artifact is treated as active canonical authority without verified repository evidence.

## 6. Runtime Layer

- `Runtime/README.md`
- `Runtime/RUN-001_BOOT_SEQUENCE.md`
- `Runtime/RUN-002_INITIALIZATION.md`
- `Runtime/RUN-003_CONFIGURATION.md`
- `Runtime/RUN-004_CONTEXT_LOADING.md`
- `Runtime/RUN-005_RUNTIME_WORKFLOW.md`
- `Runtime/RUN-006_AI_PROTOCOL.md`
- `Runtime/RUN-007_RUNTIME_SECURITY.md`
- `Runtime/RUN-008_RUNTIME_STATE.md`
- `Runtime/RUN-009_RECOVERY.md`
- `Runtime/RUN-010_RUNTIME_REFERENCE.md`
- `Runtime/_FOLDER_STATUS.md`

## 7. Architecture Domain

The Architecture domain is **under re-audit**. Current repository evidence establishes the following candidate active artifacts, but their consolidated canonical status and cross-layer relationships remain subject to verification:

- `Architecture/ARC_MAP.md` — map/navigation artifact; no numeric `ARC-NNN` identity
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`
- `Architecture/ARC-002_COMPONENT_ARCHITECTURE.md`
- `Architecture/ARC-003_INFORMATION_FLOW.md`
- `Architecture/ARC-004_LAYER_MODEL.md`
- `Architecture/ARC-005_ARCHITECTURE_RULES.md`
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Architecture/ARC-007_INTEGRATION_MODEL.md`
- `Architecture/ARC-008_REPOSITORY_LAYOUT.md`
- `Architecture/ARC-009_ARCHITECTURE_DECISIONS.md`
- `Architecture/ARC-010_EVOLUTION_MODEL.md`
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`
- `Architecture/_FOLDER_STATUS.md`

`ARC_MAP.md` previously declared `ARC-001` internally, conflicting with `ARC-001_PLATFORM_ARCHITECTURE.md`. That identity collision has been corrected; the map is now explicitly a non-numeric map artifact.

## 8. Interfaces Layer

The following interface artifacts were directly verified during the current audit:

- `Interfaces/INTF-001_INTERFACE_SPEC.md`
- `Interfaces/INTF-004_API.md`
- `Interfaces/INTF-006_ENVIRONMENT_SENSING.md`
- `Interfaces/_FOLDER_STATUS.md`

`INTF-006` remains `Proposed / Integrity Hold` pending cross-layer validation.

## 9. Models Layer

The following model artifacts were directly verified during the current audit:

- `Models/MOD-002_ENTITY_MODEL.md`
- `Models/MOD-003_DOCUMENT_MODEL.md`
- `Models/MOD-004_MEMORY_MODEL.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- `Models/_FOLDER_STATUS.md`

Declared model artifacts not directly located remain unresolved and are not promoted to active authority.

## 10. Other Active Repository Domains

The repository contains additional physical domains shown by the current `SYSTEM_MAP.md`, including Knowledge, Memory, Decision, AI, Services, Intelligence, Quality, Projects, Release, Logs, Examples and Future.

Their presence in the physical repository does not by itself certify their architectural role or completeness. Their inventories are being validated through the connected-baseline audit and will be promoted into this index only with sufficient evidence.

## 11. Canonicalization Rules

1. One active canonical artifact per logical identity.
2. Filename identity and internal Document ID must agree where a Document ID exists.
3. Canonical paths are established by repository evidence and applicable governance, not historical references.
4. Historical alternatives remain archived and are not active authority.
5. Missing or unverified dependencies remain unresolved; they are not invented.
6. Repository indexes must be updated when canonical paths or active inventories change.
7. A reference is not an accepted dependency until its target is located, read, identity-checked, authority-checked and relationship-validated.
8. Critical relationships should be validated in both directions where practical.
9. A material conflict must be traced through affected consumers, indexes, status files and release/version declarations before local resolution is considered complete.
10. An archive operation must preserve enough migration evidence to identify the former active path and canonical successor.

## 12. Integrity State

Current repository state: **INTEGRITY HOLD**.

The index is synchronized with the currently verified inventory within the inspected scope. Architecture inventory and cross-layer relationship validation remain open.

## 13. Verification Model

Current audit model:

**Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Validated → Consumer/Dependency Checked → Mutation Impact Checked → Re-read After Mutation**

Local validation results remain bounded to their inspected scope. `100%` repository integrity requires aggregated evidence across the affected repository graph and absence of unresolved blocking relationships.

## 14. Governing Rule

Repository Reality > Previous Status Claims > Conversation Memory

---

End of Document
