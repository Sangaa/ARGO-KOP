# REP-002

---

# ARGO KOP - CANONICAL REPOSITORY STORAGE MAP

---

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: REP-002
Version: 1.4.0
Status: Approved
Category: Root Baseline / Repository Index
Canonical: Yes
Priority: Absolute / Mandatory
Last Audit Date: Aug 08, 2026

---

## 1. System Framework Boundary & Mapping Spec

This document establishes the physical directory boundary maps and mandatory routing paths for the ARGO KOP platform storage environment. It serves as the structural guide for aligning physical paths with the definitions registered in the Master Index (`REP-001`).

All active canonical paths listed below are subject to repository integrity validation.

---

## 2. Canonical Directory Tree & Allocation Mapping

### 2.1 Root Baseline Allocation
* **Path Target:** `ARGO-KOP/` (Global Isolated Storage Root Fence)
* **Primary Manifest Files:**
  * `PROJECT_BOOTSTRAP.md`
  * `PROJECT_STATUS.md`
  * `README.md`
  * `VISION.md`
  * `CONTRIBUTING.md`
  * `CODE_OF_CONDUCT.md`

### 2.2 Repository Index Layer Location
* **Path Target:** `Repository/`
* **Mandatory Prefix Rule:** `REP-`
* **Active Canonical Artifacts:**
  * `Repository/REP-001_MASTER_INDEX.md`
  * `Repository/REP-002_REPOSITORY_MAP.md`

### 2.3 Governance & Standards Layer Location
* **Path Target:** `Governance/`
* **Mandatory Prefix Rule:** `GOV-`
* **Active Canonical Artifacts:**
  * `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
  * `Governance/GOV-004_DOCUMENT_METADATA.md`
  * `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
  * `Governance/GOV-010_GOVERNANCE_MODEL.md`
  * `Governance/_FOLDER_STATUS.md`

Legacy Governance artifacts are preserved under `Archive/Governance-Legacy/` and are not active canonical paths.

### 2.4 Runtime & State Life-cycle Layer Location
* **Path Target:** `Runtime/`
* **Mandatory Prefix Rule:** `RUN-`
* **Active Canonical Artifacts:**
  * `Runtime/README.md`
  * `Runtime/RUN-001_BOOT_SEQUENCE.md`
  * `Runtime/RUN-002_INITIALIZATION.md`
  * `Runtime/RUN-003_CONFIGURATION.md`
  * `Runtime/RUN-004_CONTEXT_LOADING.md`
  * `Runtime/RUN-005_RUNTIME_WORKFLOW.md`
  * `Runtime/RUN-006_AI_PROTOCOL.md`
  * `Runtime/RUN-009_RECOVERY.md`
  * `Runtime/_FOLDER_STATUS.md`

### 2.5 Cognitive Core Layer Location
* **Path Target:** `Architecture/`
* **Mandatory Prefix Rule:** `CORE-` / `ARC-`
* **Active Canonical Artifacts:**
  * `Architecture/CORE-000_PLATFORM_ARCHITECTURE.md`
  * `Architecture/CORE-002_ARGO_IDENTITY.md`
  * `Architecture/CORE-003_CONSTITUTION.md`
  * `Architecture/ARC-004_LAYER_MODEL.md`
  * `Architecture/ARC-006_DEPENDENCY_MODEL.md`
  * `Architecture/_FOLDER_STATUS.md`

---

## 3. Physical Boundary Enforcement Rules

1. **Isolation Fence Rule:** Any directory structure outside designated ARGO-KOP canonical storage targets shall be rejected from active memory context loops.
2. **Strict Extension Lock:** Canonical platform artifacts MUST use lowercase `.md` extensions.
3. **Audit Parity Sync:** Modification of directory architecture requires synchronized updates across `PROJECT_STATUS.md`, `REP-001`, and `REP-002` before validation can pass.
4. **Canonical Uniqueness:** Each logical document ID MUST have one active canonical path. Historical alternatives belong under `Archive/` and are not active.

---

## 4. Canonicalization Record

On Aug 08, 2026, `GOV-004` was canonicalized to `Governance/GOV-004_DOCUMENT_METADATA.md`. The previous conflicting artifacts were preserved under `Archive/Governance-Legacy/`.

---

## 5. Related Documents

* `PROJECT_BOOTSTRAP.md`
* `Repository/REP-001_MASTER_INDEX.md`
* `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
* `Governance/GOV-004_DOCUMENT_METADATA.md`
* `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`

---

## 6. Guiding Statement

Absolute physical mapping layout clarity guarantees deterministic file tracking and blocks execution latency.

---

End of Document
