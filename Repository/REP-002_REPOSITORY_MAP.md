# REP-002

---

# ARGO KOP - CANONICAL REPOSITORY STORAGE MAP

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: REP-002
Version: 1.5.0
Status: Integrity Hold
Category: Root Baseline / Repository Map
Canonical: Yes
Priority: Absolute / Mandatory
Last Audit Date: Aug 08, 2026

---

## 1. Purpose

This document defines the active physical repository paths used by ARGO KOP. It must remain synchronized with `REP-001_MASTER_INDEX.md` and the actual repository state.

A path is canonical only when its logical document identity is unique and verified.

## 2. Root Baseline

Path: `ARGO-KOP/`

Active root artifacts:

- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`
- `README.md`
- `VISION.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`

## 3. Repository Layer

Path: `Repository/`

Active canonical artifacts:

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

## 4. Governance Layer

Path: `Governance/`

Active canonical artifacts currently verified:

- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-004_DOCUMENT_METADATA.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Governance/GOV-010_GOVERNANCE_MODEL.md`
- `Governance/_FOLDER_STATUS.md`

`GOV-011` is not mapped as an active canonical artifact because no verified canonical document currently exists for that identity.

Superseded Governance artifacts are historical evidence under `Archive/Governance-Legacy/` and are not active canonical paths.

## 5. Runtime Layer

Path: `Runtime/`

Active mapped artifacts:

- `Runtime/README.md`
- `Runtime/RUN-001_BOOT_SEQUENCE.md`
- `Runtime/RUN-002_INITIALIZATION.md`
- `Runtime/RUN-003_CONFIGURATION.md`
- `Runtime/RUN-004_CONTEXT_LOADING.md`
- `Runtime/RUN-005_RUNTIME_WORKFLOW.md`
- `Runtime/RUN-006_AI_PROTOCOL.md`
- `Runtime/RUN-009_RECOVERY.md`
- `Runtime/_FOLDER_STATUS.md`

## 6. Architecture Layer

Path: `Architecture/`

Active mapped artifacts:

- `Architecture/CORE-000_PLATFORM_ARCHITECTURE.md`
- `Architecture/CORE-002_ARGO_IDENTITY.md`
- `Architecture/CORE-003_CONSTITUTION.md`
- `Architecture/ARC-004_LAYER_MODEL.md`
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Architecture/_FOLDER_STATUS.md`

## 7. Mapping Rules

1. Every active canonical document MUST have exactly one canonical path.
2. Filename identity MUST match internal Document ID where an ID is assigned.
3. `REP-001` and `REP-002` MUST agree on active canonical Governance paths.
4. Historical alternatives MUST remain outside active canonical paths.
5. A missing or unverified dependency MUST remain explicitly unresolved; it MUST NOT be represented as an active canonical artifact.
6. Architecture changes require synchronized updates to repository status and integrity records before a clean validation can pass.

## 8. Canonicalization Record

On Aug 08, 2026, Governance identity conflicts involving GOV-004, GOV-005, and GOV-006 were reconciled. Superseded evidence is preserved under `Archive/Governance-Legacy/`.

GOV-010 was aligned with the verified dependency set. No active GOV-011 artifact is mapped.

## 9. Integrity State

Current repository state: **INTEGRITY HOLD**.

This map is synchronized with the current Governance baseline but does not declare the entire repository clean until the consolidated repository audit passes.

---

End of Document
