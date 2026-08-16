# REP-013 — REPOSITORY CONTENT TREE

Platform: ARGO KOP
Document ID: REP-013
Version: 1.1.2
Status: Active / Phase 1 Population In Progress
Development Baseline: 3.2.1
Last Audit: 2026-08-16

## Purpose

Provide the second structural tree of the ARGO repository: not only which folders exist, but which known files belong to each folder.

This is a content inventory, not a claim that every listed file is reviewed, valid, canonical, or Phase-1 complete.

## State Rule

Each inventory entry must eventually carry:

- Path
- Document ID, where applicable
- File type
- Current repository state
- Review state from `REP-011`
- Allocation state from `REP-012`
- Canonical authority, where applicable
- Last known checkpoint

A folder is not `CLOSED_FOR_PHASE_1` merely because its contents are listed.

## Current Reconciliation Update — P293

`Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` is now explicitly represented in the Governance content inventory as a canonical addendum to `GOV-013`.

This entry establishes physical inventory/discoverability only. It does not grant the addendum authority beyond its declared governance scope, and it does not close Governance or Ring 0.

## Known Control-Plane Inventory

```text
Repository/
├── REP-001_MASTER_INDEX.md
├── REP-002_REPOSITORY_MAP.md
├── REP-003_REPOSITORY_STANDARDS.md
├── REP-006_REPOSITORY_LIFECYCLE.md
├── REP-009_REPOSITORY_TRACEABILITY.md
├── REP-010_RELEASE_BASELINE.md
├── REP-011_REVIEW_TRACEABILITY_LEDGER.md
├── REP-012_REPOSITORY_ALLOCATION_REGISTRY.md
├── REP-013_REPOSITORY_CONTENT_TREE.md
├── REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md
├── REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md
└── REP-016_PHASE1_PARTITION_WORK_QUEUE.md
```

## Governance/

Known mapped members include:

```text
Governance/
├── GOV-001_GOVERNANCE_FRAMEWORK.md
├── GOV-004_DOCUMENT_METADATA.md
├── GOV-005_REVIEW_STANDARD.md
├── GOV-006_NAMING_CONVENTION_STANDARD.md
├── GOV-009_REPOSITORY_POLICY.md
├── GOV-010_GOVERNANCE_MODEL.md
├── GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md
├── GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md
├── GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md
├── GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md
└── _FOLDER_STATUS.md
```

`GOV-011` and `GOV-012` remain proposed artifacts and are not active canonical authority until ratified.

`GOV-013A` is an `Approved / Canonical Addendum` to `GOV-013`. It controls HERMUZ bootstrap discipline and does not override Constitution, Architecture, Release authority, or domain-specific authority.

## Other Domain Evidence

The inventory remains progressively populated from current repository evidence and must not be interpreted as exhaustive until each corresponding folder is explicitly reconciled.

### Models/

```text
Models/
├── README.md
├── MOD-001_KNOWLEDGE_MODEL.md
└── MOD-011_KNOWLEDGE_SOURCE_MODEL.md
```

This is a partial evidence inventory, not a claim that these are the only files in `Models/`.

### Knowledge/

```text
Knowledge/
├── KNW-002_KNOWLEDGE_CLASSIFICATION.md
├── KNW-003_KNOWLEDGE_RELATIONSHIPS.md
├── KNW-004_KNOWLEDGE_LIFECYCLE.md
├── KNW-008_KNOWLEDGE_TRACEABILITY.md
└── KNW-009_KNOWLEDGE_EVOLUTION.md
```

### Engine/

```text
Engine/
├── ENG-002_DECISION_ENGINE.md
├── ENG-004_VALIDATION_ENGINE.md
├── ENG-006_EXECUTION_ENGINE.md
└── ENG-007_LEARNING_ENGINE.md
```

### Services/

```text
Services/
├── SRV-001_SERVICE_ARCHITECTURE.md
├── SRV-002_REPOSITORY_SERVICE.md
├── SRV-003_MEMORY_SERVICE.md
├── SRV-004_KNOWLEDGE_SERVICE.md
├── SRV-005_VALIDATION_SERVICE.md
├── SRV-006_SEARCH_SERVICE.md
├── SRV-007_LOGGING_SERVICE.md
├── SRV-008_INDEX_SERVICE.md
├── SRV-009_UPDATE_SERVICE.md
├── SRV-010_SERVICE_REFERENCE.md
├── README.md
└── _FOLDER_STATUS.md
```

The exact current-main Services directory enumeration establishes the physical filenames for `SRV-001` through `SRV-010`. This does not assert implementation, runtime execution, or Services partition closure.

### Runtime/

Known audited members include:

```text
Runtime/
├── README.md
├── RUN-001_BOOT_SEQUENCE.md
├── RUN-002_INITIALIZATION.md
├── RUN-003_CONFIGURATION.md
├── RUN-004_CONTEXT_LOADING.md
├── RUN-005_RUNTIME_WORKFLOW.md
├── RUN-006_AI_PROTOCOL.md
├── RUN-007_RUNTIME_SECURITY.md
├── RUN-008_RUNTIME_STATE.md
├── RUN-009_RECOVERY.md
├── RUN-010_RUNTIME_REFERENCE.md
├── RUN-011_COGNITIVE_EXECUTION_TARGET.md
├── RUN-012_COGNITIVE_CONTEXT_HANDOFF.md
├── RUN-013_COGNITIVE_DECISION_GATE.md
├── RUN-014_COGNITIVE_TRACE_TARGET.md
├── RUN-015_COGNITIVE_ACCEPTANCE_TARGET.md
├── Prototype/
│   └── PROTOTYPE_INTEGRATION_CONTRACT.md
└── _FOLDER_STATUS.md
```

`RUN-011..015` and `Runtime/Prototype/` are directly verified current Runtime inventory. Their presence does not establish executable Runtime authority; cross-layer integration remains under `INTEGRITY HOLD`.

### AI/

Known audited members include:

```text
AI/
├── AI-006_MODEL_ADAPTER.md
├── AI-007_MULTI_MODEL_SUPPORT.md
└── AI-008_EXTERNAL_FEEDBACK_INTEGRATION.md
```

### Memory/

Known recorded members include the Engineering Journal and current memory subdomains already represented in the existing inventory. Their review/allocation/relationship states remain governed by `REP-011`, `REP-012`, and `REP-014`.

### Specifications/

```text
Specifications/
├── README.md
└── 01-Knowledge-Organization.md
```

### Interfaces/

```text
Interfaces/
├── INTF-001_INTERFACE_SPEC.md
├── INTF-004_API.md
├── INTF-006_ENVIRONMENT_SENSING.md
├── INTF-010_INTEGRATIONS.md
└── _FOLDER_STATUS.md
```

### Architecture/

Known mapped members include `ARC_MAP.md`, `ARC-001..ARC-011`, and `_FOLDER_STATUS.md`. `ARC_MAP.md` remains a map/navigation artifact and must not reuse the `ARC-001` identity.

### Lifecycle/

```text
Lifecycle/
├── LIF-001_DOCUMENT_LIFECYCLE.md
└── _FOLDER_STATUS.md
```

### Plugins/

```text
Plugins/
├── PLG-001_PLUGIN_ARCHITECTURE.md
└── _FOLDER_STATUS.md
```

### Core/

```text
Core/
├── CORE-003_CONSTITUTION.md
├── CORE-004_CORE_PRINCIPLES.md
├── CORE-005_COGNITIVE_MODEL.md
├── CORE-006_SYSTEM_PHILOSOPHY.md
├── CORE-007_ARCHITECTURAL_LAWS.md
├── CORE-008_ARCHITECTURAL_LAWS.md
├── CORE-009_PLATFORM_LIFECYCLE.md
├── CORE-010_PLATFORM_ROADMAP.md
├── CORE-011_PLATFORM_CHARTER.md
└── _FOLDER_STATUS.md
```

## Inventory Confidence States

Each folder should eventually be assigned one of:

`UNKNOWN → STRUCTURE_IDENTIFIED → PARTIAL_INVENTORY → RECONCILED → REVIEWED → RELATIONSHIP_VALIDATED → CLOSED_FOR_PHASE_1`

These states are controlled by evidence and explicit decisions. Listing content cannot advance a folder directly to `CLOSED_FOR_PHASE_1`.

## Completion Rule

A folder can only be marked `CLOSED_FOR_PHASE_1` when:

1. Its physical content inventory is reconciled;
2. Every known file has an allocation record;
3. Every required file has a review state;
4. Dependencies and consumers have been assessed where applicable;
5. material relationships are represented or explicitly unresolved;
6. unresolved items are explicitly recorded;
7. an explicit closure decision is recorded.

Until then the folder remains OPEN.

## Integrity State

Current repository state: **INTEGRITY HOLD**.

This content tree is a progressively reconciled physical inventory. `GOV-013A` is now explicitly represented, but broader folder enumeration, allocation, relationship validation and Phase-1 closure remain open.

## Governing Rule

**Repository Reality > Previous Status Claims > Conversation Memory**

---

End of Document
