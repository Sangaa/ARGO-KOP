# REP-002

---

# ARGO KOP - CANONICAL REPOSITORY STORAGE MAP

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: REP-002
Version: 1.6.3
Status: Integrity Hold
Category: Repository
Canonical: Yes
Priority: Critical
Last Audit Date: Aug 08, 2026

---

## 1. Purpose

Defines active physical repository paths used by ARGO KOP. It remains synchronized with `REP-001_MASTER_INDEX.md` and current repository evidence.

A path is canonical only when its logical identity is unique and verified.

## 2. Root Baseline

Path: `ARGO-KOP/`

- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`
- `README.md`
- `VISION.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`

Historical root naming-convention material is excluded from active inventory and preserved under `Archive/Governance-Legacy/`.

## 3. Core Layer

Path: `Core/`

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

Path: `Repository/`

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

## 5. Governance Layer

Path: `Governance/`

- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-004_DOCUMENT_METADATA.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Governance/GOV-010_GOVERNANCE_MODEL.md`
- `Governance/_FOLDER_STATUS.md`

`GOV-011` is not mapped as active canonical authority because no verified artifact establishes it.

## 6. Runtime Layer

Path: `Runtime/`

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

Path: `Architecture/`

The Architecture domain is under re-audit. Current repository evidence identifies:

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

`ARC_MAP.md` previously declared `ARC-001`, conflicting with `ARC-001_PLATFORM_ARCHITECTURE.md`; the map identity collision has been corrected.

## 8. Interfaces Layer

Path: `Interfaces/`

- `Interfaces/INTF-001_INTERFACE_SPEC.md`
- `Interfaces/INTF-004_API.md`
- `Interfaces/INTF-006_ENVIRONMENT_SENSING.md`
- `Interfaces/_FOLDER_STATUS.md`

`INTF-006` remains Proposed / Integrity Hold pending cross-layer validation.

## 9. Models Layer

Path: `Models/`

- `Models/MOD-002_ENTITY_MODEL.md`
- `Models/MOD-003_DOCUMENT_MODEL.md`
- `Models/MOD-004_MEMORY_MODEL.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- `Models/_FOLDER_STATUS.md`

Declared model artifacts not directly located remain unresolved and are not promoted to active authority.

## 10. Other Repository Domains

Current `SYSTEM_MAP.md` also identifies Knowledge, Memory, Decision, AI, Services, Intelligence, Quality, Projects, Release, Logs, Examples and Future as physical repository domains/groupings.

These domains are not assumed complete or architecturally authoritative from folder names alone. Their active inventories and relationships remain under connected-baseline validation.

## 11. Mapping Rules

1. Every active canonical document has exactly one canonical path.
2. Filename identity must match internal Document ID where one exists.
3. `REP-001` and `REP-002` must agree on active canonical paths.
4. Historical alternatives remain outside active canonical paths and preserve migration traceability.
5. Missing or unverified dependencies remain explicitly unresolved.
6. Any canonical inventory change requires synchronized index/map updates and validation.
7. Archive operations must preserve enough evidence to identify the former active path and its canonical successor.
8. A new interface, model, runtime component or service must not be considered globally integrated until its consumers and dependencies are validated.
9. Map artifacts and status artifacts must not reuse the identity of canonical content documents.

## 12. Integrity State

Current repository state: **INTEGRITY HOLD**.

The map is synchronized with the current declared Core, Governance, Repository, Runtime, Architecture, Interfaces and Models inventory within the inspected scope. Cross-layer relationship validation remains open.

---

End of Document
