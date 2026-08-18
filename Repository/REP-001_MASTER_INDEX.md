# REP-001

---

# ARGO KOP - MASTER REPOSITORY INDEX

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: REP-001
Version: 1.11.3
Status: Integrity Hold
Category: Repository
Canonical: Yes
Priority: Critical
Last Audit Date: Aug 16, 2026
Development Baseline: 3.2.1

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
- `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md`
- `Core/_FOLDER_STATUS.md`

## 4. Repository Layer

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

`REP-011` through `REP-015` form the current repository control plane. They are mutually discoverable here and through REP-002. They remain subject to cross-registry reconciliation and do not grant domain semantic authority.

## 5. Governance Layer

- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-004_DOCUMENT_METADATA.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Governance/GOV-010_GOVERNANCE_MODEL.md`
- `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md`
- `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`
- `GOVERNANCE/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`
- `Governance/_FOLDER_STATUS.md`

`Governance/GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md` exists as a proposed intake standard but is not active canonical authority until formally ratified.

`Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md` exists as a proposed reconstruction standard. It governs rebuilding legacy or immature domains but is not active canonical authority until formally ratified.

`GOV-013` is the approved canonical HERMUZ session operating contract. `GOV-013A` is its approved canonical session-integrity addendum and establishes the mandatory pre-mutation bootstrap gate. Neither document overrides higher ARGO authority.

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
- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Runtime/RUN-012_COGNITIVE_LOOP_TEST_MATRIX.md`
- `Runtime/RUN-013_CONTROLLED_HANDOFF.md`
- `Runtime/RUN-014_LEARNING_PROMOTION_TEST.md`
- `Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md`
- `Runtime/Prototype/PROTOTYPE_INTEGRATION_CONTRACT.md`
- `Runtime/_FOLDER_STATUS.md`

`RUN-011..015` and `Runtime/Prototype/` are directly verified current Runtime inventory, but remain bounded by `CROSS-LAYER INTEGRATION HOLD`. Their presence does not establish executable Runtime authority.

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

## 8. Lifecycle Domain

The Lifecycle domain is **under re-audit** and is limited to document-scoped lifecycle authority within the inspected scope:

- `Lifecycle/LIF-001_DOCUMENT_LIFECYCLE.md`
- `Lifecycle/_FOLDER_STATUS.md`

`Lifecycle/GOV-005_DOCUMENT_LIFECYCLE.md` previously reused the active `GOV-005` identity owned by `Governance/GOV-005_REVIEW_STANDARD.md`. The lifecycle artifact has been migrated to `LIF-001`; the former active path is retired and its provenance remains in Git history.

The presence of `LIF-001` does not establish authority over platform, repository, knowledge, decision, project or memory lifecycles.

## 9. Interfaces Layer

The following interface artifacts were directly verified during the current audit:

- `Interfaces/INTF-001_INTERFACE_SPEC.md`
- `Interfaces/INTF-004_API.md`
- `Interfaces/INTF-006_ENVIRONMENT_SENSING.md`
- `Interfaces/INTF-010_INTEGRATIONS.md`
- `Interfaces/_FOLDER_STATUS.md`

`INTF-006` remains `Proposed / Integrity Hold` pending cross-layer validation.

`INTF-010` is `Validated / Integrity Hold` and establishes the provider-neutral connector/integration boundary. It is indexed here because it is a canonical domain artifact and its architecture explicitly requires active integration artifacts to be represented in repository inventories. Its validation does not certify every external connector implementation.

## 10. Models Layer

The following model artifacts were directly verified during the current audit:

- `Models/MOD-001_KNOWLEDGE_MODEL.md`
- `Models/MOD-002_ENTITY_MODEL.md`
- `Models/MOD-003_DOCUMENT_MODEL.md`
- `Models/MOD-004_MEMORY_MODEL.md`
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`
- `Models/_FOLDER_STATUS.md`

`MOD-001` was reconciled from current-main evidence after independent ID-oriented search and direct authoritative-path verification. It is indexed here because it declares `Canonical: Yes`, is readable on current main, and is directly verified by `Models/_FOLDER_STATUS.md`.

Declared model artifacts not directly located remain unresolved and are not promoted to active authority.

The Models domain is subject to the reconstruction process defined by proposed `GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md`; existing model files are not assumed to represent the final canonical model until relationship and consumer validation is complete.

## 11. Plugins Layer

The current repository contains a directly verified canonical plugin architecture artifact:

- `Plugins/PLG-001_PLUGIN_ARCHITECTURE.md` — Approved / Canonical / Critical
- `Plugins/_FOLDER_STATUS.md`

`PLG-001` establishes the plugin extension boundary and explicitly requires active plugin specifications to be registered under `Plugins/` and indexed in this master repository index. It therefore cannot remain only under the generic "other physical domains" description.

The existence and approval of `PLG-001` do not certify that every future plugin is integrated; each plugin remains subject to manifest, sandbox, interface, security and quality validation.

## 12. Memory — Operational Memory

The current build adds a directly verified Operational Memory subdomain:

- `Memory/Operational_Memory/README.md`
- `Memory/Operational_Memory/OPM-001_OPERATIONAL_MEMORY_MODEL.md`
- `Memory/Operational_Memory/OPM-002_OPERATIONAL_EVENT_CAPTURE.md`
- `Memory/Operational_Memory/OPM-003_OPERATIONAL_RETRIEVAL.md`
- `Memory/Operational_Memory/OPM-004_OPERATIONAL_LIFECYCLE.md`

Build-01 is physically constructed and re-read. These artifacts remain `Candidate / Integrity Hold` pending consolidated Memory and cross-layer validation. They do not independently create Memory authority.

## 13. Memory — Decision Memory

The current build adds a directly verified Decision Memory subdomain:

- `Memory/Decision_Memory/README.md`
- `Memory/Decision_Memory/DM-001_DECISION_RECORD_MODEL.md`
- `Memory/Decision_Memory/DM-002_DECISION_LIFECYCLE_AND_REVIEW.md`
- `Memory/Decision_Memory/DM-003_DECISION_EVIDENCE_AND_REVISION.md`
- `Memory/Decision_Memory/DM-004_DECISION_TRACEABILITY_AND_CONSUMER_LINKS.md`

Build-01 is physically constructed and re-read. These artifacts remain `Candidate / Integrity Hold` pending consolidated Memory and cross-layer validation. They define decision-memory structure and traceability; they do not independently create decision authority.

## 14. Memory — Historical Memory

The current build adds a directly verified Historical Memory subdomain:

- `Memory/Historical_Memory/README.md`
- `Memory/Historical_Memory/HM-001_HISTORICAL_RECORD_MODEL.md`
- `Memory/Historical_Memory/HM-002_PROVENANCE_AND_TEMPORAL_CONTEXT.md`
- `Memory/Historical_Memory/HM-003_HISTORICAL_RETRIEVAL_AND_RELEVANCE.md`
- `Memory/Historical_Memory/HM-004_HISTORICAL_TO_CURRENT_TRANSITION.md`

Build-01 is physically constructed and re-read. These artifacts remain `Candidate / Integrity Hold` pending consolidated Memory and cross-layer validation. They preserve historical evidence without silently promoting it to current authority.

## 15. Memory — Project Memory

The current build adds a directly verified Project Memory subdomain:

- `Memory/Project_Memory/README.md`
- `Memory/Project_Memory/PM-001_PROJECT_RECORD_MODEL.md`
- `Memory/Project_Memory/PM-002_PROJECT_LIFECYCLE_AND_STATE.md`
- `Memory/Project_Memory/PM-003_PROJECT_TRACEABILITY_AND_CONTINUITY.md`
- `Memory/Project_Memory/PM-004_PROJECT_KNOWLEDGE_AND_LESSONS.md`

Build-01 is physically constructed and re-read. These artifacts remain `Candidate / Integrity Hold` pending consolidated Memory and cross-layer validation. They preserve project-local continuity and controlled promotion of project experience into reusable knowledge.

## 16. Other Active Repository Domains

The repository contains additional physical domains shown by the current `SYSTEM_MAP.md`, including Knowledge, Memory, Decision, AI, Services, Intelligence, Quality, Projects, Release, Logs, Examples and Future.

The following Intelligence artifacts are directly verified as Approved and Canonical by `Intelligence/_FOLDER_STATUS.md`:

- `Intelligence/INT-001_INTELLIGENCE_LAYER.md`
- `Intelligence/INT-002_PATTERN_EXTRACTION.md`
- `Intelligence/INT-003_ANOMALY_DETECTOR.md`

The current audit also identifies physical domains requiring staged reconstruction or re-audit, including:

- `Templates/`
- `Standards/`
- `Specifications/`
- `Release/`
- `Plugins/`
- `Models/`
- `Assets/`
- `Blueprints/`

Their presence in the physical repository does not by itself certify their architectural role or completeness. Their inventories are being validated through the connected-baseline audit and staged reconstruction process and will be promoted into this index only with sufficient evidence.

### Legacy / Reconstruction Policy

Some domains contain early drafts, primitive sketches, incomplete structures or documents produced before the current ARGO architectural model and governance discipline were mature.

These artifacts are **source material, not automatic authority**.

For a domain that is rebuilt, the preferred method is:

**Read existing material → extract useful evidence → classify facts / assumptions / draft ideas → identify obsolete structure → rebuild from the current foundation → validate identity / authority / relationships → index the rebuilt domain**.

The detailed reconstruction control is defined by proposed `Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md`.

Where the old structure is fundamentally immature or misleading, ARGO may rewrite the domain from first principles rather than preserve its old organization.

Old material must remain recoverable when it has provenance or migration value, normally through governed Archive/history. It must not be reintroduced into the active index merely because it existed previously.

A domain is not considered complete merely because its folder exists or because draft files have been populated.

## 17. Canonicalization Rules

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
11. Map and status artifacts must not reuse the identity of canonical content documents.
12. A domain-specific lifecycle artifact must not silently claim authority over another domain's lifecycle.
13. Any approved canonical domain artifact that imposes an explicit indexing requirement must be represented in the applicable active inventory rather than hidden under an unqualified physical-domain summary.
14. Legacy draft content must not be promoted solely because it is old, populated or previously referenced.
15. Rebuilt domains must be revalidated as connected relationship graphs before active canonical promotion.
16. Domains under reconstruction remain outside active canonical authority unless explicitly promoted after validation.
17. Critical Repository Control artifacts (`REP-011` through `REP-015`) must remain mutually discoverable through both the master index and physical storage map while their cross-registry reconciliation remains open.
18. Registry membership is evidence of inventory only; review, allocation and relationship states are controlled by the respective registries.
19. New Memory subdomains must be indexed when physically constructed and must remain capped by their verified scope until consolidated validation.
20. New Decision Memory subdomains must be indexed when physically constructed and must remain capped by their verified scope until consolidated validation.
21. New Historical Memory subdomains must be indexed when physically constructed and must remain capped by their verified scope until consolidated validation.
22. New Project Memory subdomains must be indexed when physically constructed and must remain capped by their verified scope until consolidated validation.
23. Directly verified Runtime target/prototype artifacts must be indexed when physically constructed while preserving their declared non-executable authority boundary.
24. Master Index Runtime paths must match the current physical Runtime candidate paths; historical candidate names are not active inventory.
25. Approved canonical Governance addenda that govern HERMUZ session integrity must be represented in the active Governance inventory and remain subordinate to higher ARGO authority.

## 18. Integrity State

Current repository state: **INTEGRITY HOLD**.

The index is synchronized with the currently verified inventory within the inspected scope. Architecture, Lifecycle inventory, Plugin inventory, Memory cross-layer relationships, Runtime ↔ Engine integration and other staged reconstruction work remain open.

## 19. Verification Model

Current audit model:

**Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Validated → Consumer/Dependency Checked → Mutation Impact Checked → Re-read After Mutation**

Local validation results remain bounded to their inspected scope. `100%` repository integrity requires aggregated evidence across the affected repository graph and absence of unresolved blocking relationships.

## 20. Governing Rule

Repository Reality > Previous Status Claims > Conversation Memory

---

## P290 Current Governance Registration Reconciliation — 2026-08-16

`GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` is now registered in the active Governance inventory. The addendum remains subordinate to higher ARGO authority and does not create independent semantic or architectural authority.

This registration closes the REP-001 discoverability gap for `GOV-013A` within the inspected Governance/Repository index scope.

## P356 Current Canonical Core Inventory Reconciliation — 2026-08-17

Current Core folder evidence (`Core/_FOLDER_STATUS.md`) explicitly identifies `Core/CORE-000_PLATFORM_ARCHITECTURE.md` as a known canonical Core artifact independently revalidated on 2026-08-10. The artifact declares `Document ID: CORE-000` and `Canonical: Yes`.

The active Core inventory therefore now explicitly includes:

`Core/CORE-000_PLATFORM_ARCHITECTURE.md`

This mutation repairs an index-scope discrepancy; it does not promote `CORE-000_PLATFORM_IDENTITY.md`, whose own document states `Canonical: No / Legacy / Superseded`.

P356 is an inventory/identity reconciliation only. Core remains under Integrity Hold and cross-layer validation.

---

End of Document
