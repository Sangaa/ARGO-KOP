# ARGO KOP - CANONICAL REPOSITORY STORAGE MAP

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: REP-002
Version: 1.7.4
Status: Integrity Hold
Category: Repository
Canonical: Yes
Priority: Critical
Last Audit Date: Aug 16, 2026
Development Baseline: 3.2.1

---

## 1. Purpose

Defines active physical repository paths used by ARGO KOP. It remains synchronized with `REP-001_MASTER_INDEX.md` and current repository evidence.

A path is canonical only when its logical identity is unique and verified.

Review and completion evidence is tracked by `Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md`. REP-002 records physical mapping; REP-011 records whether the mapped content was actually reviewed, re-read and relationship-validated.

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

- `Core/CORE-000_PLATFORM_ARCHITECTURE.md`
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
- `Repository/REP-003_REPOSITORY_STANDARDS.md`
- `Repository/REP-004_REPOSITORY_NAVIGATION.md`
- `Repository/REP-005_REPOSITORY_COMPONENTS.md`
- `Repository/REP-006_REPOSITORY_LIFECYCLE.md`
- `Repository/REP-007_REPOSITORY_GOVERNANCE.md`
- `Repository/REP-008_REPOSITORY_BASELINE.md`
- `Repository/REP-009_REPOSITORY_TRACEABILITY.md`
- `Repository/REP-010_RELEASE_BASELINE.md`
- `Repository/REP-011_REVIEW_TRACEABILITY_LEDGER.md`
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
- `Repository/REP-013_REPOSITORY_CONTENT_TREE.md`
- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
- `Repository/REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md`

The REP-011–015 artifacts form the current repository control plane. They remain subject to cross-registry reconciliation and do not grant domain semantic authority.

## 5. Governance Layer

Path: `Governance/`

- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-004_DOCUMENT_METADATA.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Governance/GOV-010_GOVERNANCE_MODEL.md`
- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md`
- `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`
- `Governance/_FOLDER_STATUS.md`

`Governance/GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md` exists and is verified as `Proposed / Integrity Hold`; it is not active canonical authority until formally ratified.

`Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md` exists as a proposed reconstruction standard. It is not active canonical authority until formally ratified.

`GOV-013` is the approved canonical HERMUZ session operating contract. `GOV-013A` is its approved canonical session-integrity addendum and establishes the mandatory pre-mutation bootstrap gate. Neither document overrides higher ARGO authority.

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
- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Runtime/RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md`
- `Runtime/RUN-013_CONTROLLED_HANDOFF.md`
- `Runtime/RUN-014_LEARNING_PROMOTION_TEST.md`
- `Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md`
- `Runtime/Prototype/PROTOTYPE_INTEGRATION_CONTRACT.md`
- `Runtime/_FOLDER_STATUS.md`

The `RUN-011..015` and `Runtime/Prototype/` paths are directly verified physical inventory from the current Runtime reconciliation. They remain `CROSS-LAYER INTEGRATION HOLD` and are not promoted to executable Runtime authority by mapping alone.

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

## 8. Lifecycle Domain

Path: `Lifecycle/`

The Lifecycle domain is under re-audit and is limited to document-scoped lifecycle authority within the inspected scope:

- `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`
- `Lifecycle/_FOLDER_STATUS.md`

`Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md` previously reused the active `GOV-005` identity owned by `Governance/GOV-005_REVIEW_STANDARD.md`. The lifecycle artifact has been migrated to `LIF-001` and the former active path has been retired; provenance remains in Git history.

`LIF-001` does not establish authority over platform, repository, knowledge, decision, project or memory lifecycles.

## 9. Interfaces Layer

Path: `Interfaces/`

- `Interfaces/INTF-001_INTERFACE_SPEC.md`
- `Interfaces/INTF-004_API.md`
- `Interfaces/INTF-006_ENVIRONMENT_SENSING.md`
- `Interfaces/INTF-010_INTEGRATIONS.md`
- `Interfaces/_FOLDER_STATUS.md`

`INTF-006` remains Proposed / Integrity Hold pending cross-layer validation.

`INTF-010` is Validated / Integrity Hold and is the canonical provider-neutral integration and connector boundary. Its presence in the active map does not certify individual connector implementations.

## 10. Models Layer

Path: `Models/`

- `Models/MOD-001_KNOWLEDGE_MODEL.md`
- `Models/MOD-002_ENTITY_MODEL.md`
- `Models/MOD-003_DOCUMENT_MODEL.md`
- `Models/MOD-004_MEMORY_MODEL.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- `Models/_FOLDER_STATUS.md`

`MOD-001` was reconciled from current-main evidence after independent ID-oriented search and direct authoritative-path verification. It is mapped here because it declares `Canonical: Yes`, is readable on current main, and is directly verified by `Models/_FOLDER_STATUS.md`.

Declared model artifacts not directly located remain unresolved and are not promoted to active authority.

## 11. Plugins Layer

Path: `Plugins/`

- `Plugins/PLG-001_PLUGIN_ARCHITECTURE.md` — Approved / Canonical / Critical
- `Plugins/_FOLDER_STATUS.md`

`PLG-001` explicitly requires active plugin specifications to be registered under `Plugins/` and indexed in `REP-001`. This physical map therefore treats the Plugins domain as an active declared inventory rather than an unqualified additional folder.

The approved plugin architecture does not imply that every plugin is globally integrated; each plugin remains subject to its own manifest, sandbox, interface, security and quality validation.

## 12. Memory — Operational Memory

Path: `Memory/Operational_Memory/`

- `Memory/Operational_Memory/README.md`
- `Memory/Operational_Memory/OPM-001_OPERATIONAL_MEMORY_MODEL.md`
- `Memory/Operational_Memory/OPM-002_OPERATIONAL_EVENT_CAPTURE.md`
- `Memory/Operational_Memory/OPM-003_OPERATIONAL_RETRIEVAL.md`
- `Memory/Operational_Memory/OPM-004_OPERATIONAL_LIFECYCLE.md`

Build-01 is physically constructed and verified. The artifacts remain `Candidate / Integrity Hold` pending consolidated Memory and cross-layer validation.

## 13. Memory — Decision Memory

Path: `Memory/Decision_Memory/`

- `Memory/Decision_Memory/README.md`
- `Memory/Decision_Memory/DM-001_DECISION_RECORD_MODEL.md`
- `Memory/Decision_Memory/DM-002_DECISION_LIFECYCLE_AND_REVIEW.md`
- `Memory/Decision_Memory/DM-003_DECISION_EVIDENCE_AND_REVISION.md`
- `Memory/Decision_Memory/DM-004_DECISION_TRACEABILITY_AND_CONSUMER_LINKS.md`

Build-01 is physically constructed and re-read. The artifacts remain `Candidate / Integrity Hold` pending consolidated Memory and cross-layer validation. They define decision-memory structure and traceability; they do not independently create decision authority.

## 14. Memory — Historical Memory

Path: `Memory/Historical_Memory/`

- `Memory/Historical_Memory/README.md`
- `Memory/Historical_Memory/HM-001_HISTORICAL_RECORD_MODEL.md`
- `Memory/Historical_Memory/HM-002_PROVENANCE_AND_TEMPORAL_CONTEXT.md`
- `Memory/Historical_Memory/HM-003_HISTORICAL_RETRIEVAL_AND_RELEVANCE.md`
- `Memory/Historical_Memory/HM-004_HISTORICAL_TO_CURRENT_TRANSITION.md`

Build-01 is physically constructed and re-read. The artifacts remain `Candidate / Integrity Hold` pending consolidated Memory and cross-layer validation. They preserve historical evidence without silently promoting it to current authority.

## 15. Memory — Project Memory

Path: `Memory/Project_Memory/`

- `Memory/Project_Memory/README.md`
- `Memory/Project_Memory/PM-001_PROJECT_RECORD_MODEL.md`
- `Memory/Project_Memory/PM-002_PROJECT_LIFECYCLE_AND_STATE.md`
- `Memory/Project_Memory/PM-003_PROJECT_TRACEABILITY_AND_CONTINUITY.md`
- `Memory/Project_Memory/PM-004_PROJECT_KNOWLEDGE_AND_LESSONS.md`

Build-01 is physically constructed and re-read. The artifacts remain `Candidate / Integrity Hold` pending consolidated Memory and cross-layer validation. They preserve project-local continuity and controlled promotion of project experience into reusable knowledge.

## 16. Other Repository Domains

Current `SYSTEM_MAP.md` also identifies Knowledge, Memory, Decision, AI, Services, Intelligence, Quality, Projects, Release, Logs, Examples and Future as physical repository domains/groupings.

These domains are not assumed complete or architecturally authoritative from folder names alone. Their active inventories and relationships remain under connected-baseline validation and are tracked through REP-011 review evidence.

## 17. Mapping Rules

1. Every active canonical document has exactly one canonical path.
2. Filename identity must match internal Document ID where one exists.
3. `REP-001` and `REP-002` must agree on active canonical paths.
4. Historical alternatives remain outside active canonical paths and preserve migration traceability.
5. Missing or unverified dependencies remain explicitly unresolved.
6. Any canonical inventory change requires synchronized index/map updates and validation.
7. Archive operations must preserve enough evidence to identify the former active path and its canonical successor.
8. A new interface, model, runtime component, plugin or service must not be considered globally integrated until its consumers and dependencies are validated.
9. Map artifacts and status artifacts must not reuse the identity of canonical content documents.
10. Domain-specific lifecycle artifacts must remain scoped to their declared artifact class and must not silently acquire authority over another domain's lifecycle.
11. An approved canonical domain artifact that explicitly requires repository indexing must appear in both the master index and physical storage map.
12. Proposed artifacts may be mapped as verified physical evidence without becoming canonical authority.
13. A mapped file is not considered reviewed or complete solely because it appears in this map; review state must be taken from REP-011.
14. A folder/domain remains open until its Phase 1 completion is explicitly recorded; reviewed subsets must not imply completion of the remaining contents.
15. If a reviewed file changes, or a dependency/authority/consumer changes materially, its prior review state must be revalidated.
16. Critical Repository Control artifacts (`REP-011` through `REP-015`) must remain mutually discoverable through the active repository map while their cross-registry reconciliation remains open.
17. New Memory subdomains must be mapped when physically constructed and must remain capped by their verified scope until consolidated validation.
18. New Decision Memory, Historical Memory and Project Memory subdomains must be mapped when physically constructed and must remain capped by their verified scope until consolidated validation.
19. Memory mapping establishes physical inventory only; it does not grant Memory authority or certify cross-layer consumers.
20. `REP-001`, `REP-002`, `REP-013` and `REP-014` must be reconciled after material Memory inventory or relationship changes.
21. Directly verified Runtime target/prototype artifacts must be mapped when physically constructed while preserving their declared non-executable authority boundary.
22. Runtime candidate paths in the physical map must match the current `Runtime/` repository paths; historical candidate names are not active inventory.
23. Approved canonical Governance addenda that govern HERMUZ session integrity must appear in both the master index and physical storage map while remaining subordinate to higher ARGO authority.

## 18. Integrity State

Current repository state: **INTEGRITY HOLD**.

The map is synchronized with the current declared Core, Governance, Repository control-plane, Runtime, Architecture, Lifecycle, Interfaces, Models, Plugins and Build-01 Memory inventory within the inspected scope. Runtime ↔ Engine relationship validation remains open.

Completion of individual files or reviewed subsets must not be interpreted as Phase 1 repository completion. REP-011 is the binding review/completion evidence ledger until an explicit Phase 1 closure decision is recorded.

---

## P290 Current Governance Registration Reconciliation — 2026-08-16

`GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` is now physically mapped in the active Governance inventory and is synchronized with REP-001. Its status remains `Approved / Canonical Addendum`, subordinate to higher ARGO authority.

This closes the REP-002 physical-map discoverability gap for `GOV-013A` within the inspected Governance/Repository scope.

## P357 Current Canonical Core Map Reconciliation — 2026-08-17

Current Core folder evidence explicitly identifies `Core/CORE-000_PLATFORM_ARCHITECTURE.md` as a known canonical Core artifact independently revalidated on 2026-08-10. The master index now includes this path as P356.

The physical storage map is synchronized to that same canonical Core path.

This mutation repairs the REP-001 ↔ REP-002 discoverability gap and does not promote the legacy `CORE-000_PLATFORM_IDENTITY.md`, which remains noncanonical historical evidence.

---

End of Document
