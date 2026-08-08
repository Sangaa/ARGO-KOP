# REP-001

---

# MASTER INDEX

---

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: REP-001  
Version: 1.2.0  
Status: Approved  
Category: Repository  
Canonical: Yes  
Priority: Critical  

---

# Purpose

This document is the canonical navigation entry point for the entire ARGO KOP repository.

Every folder, specification, engine, service, model, and runtime artifact inside the repository shall be reachable directly or indirectly through this Master Index. It guarantees strict repository integrity, deterministic traceability, and continuous knowledge continuity across all operational components.

---

# Core Repository Structure

ARGO-KOP/
├── Root Baseline
│   ├── PROJECT_BOOTSTRAP.md
│   ├── START_HERE.md
│   ├── README.md
│   ├── VISION.md
│   ├── ROADMAP.md
│   ├── SECURITY.md
│   ├── PROJECT_STATUS.md
│   ├── CONTRIBUTE.md
│   ├── CODE_OF_CONDUCT.md
│   ├── LICENSE.md
│   └── NOTICE.md
├── Governance & Standards
│   ├── Governance/
│   ├── Standards/
│   └── Lifecycle/
├── System Core & Specifications
│   ├── Specs/
│   ├── Docs/
│   ├── Models/
│   └── Architecture/
├── Intelligence & Processing
│   ├── Engine/
│   ├── Intelligence/
│   ├── Cognition/
│   └── Memory/
├── Execution & Operational Services
│   ├── Services/
│   ├── Runtime/
│   ├── Interfaces/
│   └── Plugins/
└── Quality, Integration & Maintenance
├── Quality/
├── Repository/
├── Templates/
├── Projects/
├── Release/
└── Future/


---

# Complete Directory Map & Status Index

| Directory | Primary Domain & Responsibility | Status | Primary Canonical Spec |
| :--- | :--- | :--- | :--- |
| **`Root`** | Root initialization, bootstrap rules, core status & security baseline | ACTIVE | `PROJECT_BOOTSTRAP.md` |
| **`Governance/`** | Repository governance rules, approval flows, and authority policies | ACTIVE | `GOV-001_GOVERNANCE_FRAMEWORK.md` |
| **`Standards/`** | Standards for naming, metadata, lifecycle, and document classification | ACTIVE | `GOV-004_DOCUMENT_METADATA.md` |
| **`Lifecycle/`** | Lifecycle definitions for documents, repository artifacts, and knowledge | ACTIVE | `GOV-005_DOCUMENT_LIFECYCLE.md` |
| **`Specs/`** | Functional, structural, and technical definitions and specifications | ACTIVE | `01-Knowledge-Organization.md` |
| **`Docs/`** | High-level system descriptions, architecture overviews, and glossaries | ACTIVE | `DOC-001_PROJECT_OVERVIEW.md` |
| **`Models/`** | Conceptual, logical, and structural knowledge domain models | ACTIVE | `MOD-001_KNOWLEDGE_MODEL.md` |
| **`Engine/`** | Core cognitive execution engines (Reasoning, Analysis, Learning) | ACTIVE | `ENG-001_REASONING_ENGINE.md` |
| **`Intelligence/`** | Specialized intelligence modules, pattern extraction, and synthesis | ACTIVE | `INT-001_INTELLIGENCE_LAYER.md` |
| **`Cognition/`** | Contextual awareness, cognitive navigation, and semantic routing | ACTIVE | `COG-001_COGNITIVE_NAVIGATION.md` |
| **`Memory/`** | Context retention, engineering journal, and historical continuity | ACTIVE | `MEM-004_MEMORY_LIFECYCLE.md` |
| **`Services/`** | Operational capabilities, orchestration, update services, and APIs | ACTIVE | `SRV-001_SERVICE_ARCHITECTURE.md` |
| **`Runtime/`** | Execution flows, state management, and real-time process execution | ACTIVE | `RNT-001_RUNTIME_ENVIRONMENT.md` |
| **`Interfaces/`** | External and internal communication contracts, protocols, and APIs | ACTIVE | `INTF-001_INTERFACE_SPEC.md` |
| **`Plugins/`** | Modular extensions, external integrations, and tool adapters | ACTIVE | `PLG-001_PLUGIN_ARCHITECTURE.md` |
| **`Quality/`** | Quality assurance, verification standards, and validation suites | ACTIVE | `QLT-001_QUALITY_ASSURANCE.md` |
| **`Repository/`** | Repository structure, master indexes, maps, and integrity checks | ACTIVE | `REP-001_MASTER_INDEX.md` |
| **`Templates/`** | Standardized markdown templates for document creation and updates | ACTIVE | `TEMPLATE-001_DOCUMENT.md` |
| **`Projects/`** | Active engineering project plans, work packages, and sprints | ACTIVE | `PRJ-001_PROJECT_INDEX.md` |
| **`Release/`** | Release notes, deployment instructions, and quick start guides | ACTIVE | `REL-004_QUICK_START.md` |
| **`Future/`** | Strategic roadmap expansion, future research, and architectural vision | ACTIVE | `FUT-001_FUTURE_ARCHITECTURE.md` |

---

# Verification & Compliance Rules

1. **Mandatory Indexing:** Every newly added directory or canonical file MUST be registered inside `REP-001_MASTER_INDEX.md` and linked in `REP-002_REPOSITORY_MAP.md`.
2. **Metadata Standard:** Every document in any directory MUST contain the metadata header as defined in `GOV-004`.
3. **Immutability of Canonical Baseline:** Canonical specifications registered here cannot be altered or removed without triggering the formal update workflow defined in `SRV-009_UPDATE_SERVICE.md`.

---

# Revision History

| Version | Date | Description | Author / Authority |
| :--- | :--- | :--- | :--- |
| 1.0.0 | 2026-08-01 | Initial Master Index Baseline | ARGO Foundation |
| 1.1.0 | 2026-08-04 | Added Engine, Services, and Memory cross-references | ARGO Foundation |
| 1.2.0 | 2026-08-06 | Full repository synchronization incorporating Runtime, Intelligence, Models, Plugins, Interfaces, and Quality domains | ARGO Engineering |
| `Intelligence/INT-001_INTELLIGENCE_LAYER.md` | `INT-001` | Approved | Pattern extraction & synthesis architecture |
| `Intelligence/INT-002_PATTERN_EXTRACTION.md` | `INT-002` | Approved | Specialized pattern extraction pipeline |
| `Intelligence/INT-003_ANOMALY_DETECTOR.md` | `INT-003` | Approved | Structural drift & anomaly detection |

### Engine Layer (`Engine/`)

| Path / File Name | Document ID | Status | Description |
| :--- | :--- | :--- | :--- |
| `Engine/ENG-001_REASONING_ENGINE.md` | `ENG-001` | Approved | Primary Cognitive & Deduction Engine (v3.1.0) |
| `Engine/ENG-002_DECISION_ENGINE.md` | `ENG-002` | Approved | Deterministic & Risk-Evaluated Decision Engine |
| `Engine/ENG-003_ANALYSIS_ENGINE.md` | `ENG-003` | Approved | Structural & Pattern Decomposition Engine |
| `Engine/ENG-004_VALIDATION_ENGINE.md` | `ENG-004` | Approved | Real-Time Schema & Integrity Gatekeeper |
| `Engine/ENG-005_PLANNING_ENGINE.md` | `ENG-005` | Approved | Sequential Execution Plan & Task Graph Engine |
| `Engine/ENG-006_EXECUTION_ENGINE.md` | `ENG-006` | Approved | Transactional Task & Runtime Execution Engine |
| `Engine/ENG-007_LEARNING_ENGINE.md` | `ENG-007` | Approved | Continuous Lesson Capture & Evolution Engine |
| `Engine/ENG-008_MEMORY_ENGINE.md` | `ENG-008` | Approved | Session, Working & Canonical Memory Manager |
| `Engine/ENG-009_CONTEXT_ENGINE.md` | `ENG-009` | Approved | Context Hydration & Isolation Fence Engine |
| `Engine/ENG-010_ENGINE_COORDINATION.md` | `ENG-010` | Approved | Central Neural Dispatcher & Multi-Engine Router |
| `Engine/ENG-011_MARITIME_GAME_ENGINE.md` | `ENG-011` | Approved | ARGO GEM Gamified Experiential Mentor Engine |
| `Engine/_FOLDER_STATUS.md` | N/A | Approved | Directory Audit & Inventory Log (v2.0.0) |