# REP-013 — REPOSITORY CONTENT TREE  

Platform: ARGO KOP  
Document ID: REP-013  
Version: 1.1.2  
Status: Active / Phase 1 Population In Progress  
Development Baseline: 3.2.1  
Last Audit: 2026-08-16

## Purpose

Provide the second structural tree of the ARGO repository: not only which folders exist, but which known files belong to each folder.

This is a **content inventory**, not a claim that every listed file is reviewed, valid, canonical, or Phase-1 complete.

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

A folder is **not CLOSED_FOR_PHASE_1** merely because its contents are listed.

## P293 Regression Repair — 2026-08-16

The first P293 write used an abbreviated replacement and unintentionally removed previously recorded inventory detail. This was detected by immediate post-mutation read-back and is classified as a **content-preservation regression**.

Repair action:

- restored the full pre-P293 inventory from the verified current repository state;
- retained all previously recorded domain evidence;
- added only the required `GOV-013A` Governance inventory entry;
- preserved the existing inventory semantics and unresolved scope.

The repaired file is the current `REP-013` state.

## Root

```text
ARGO-KOP/
├── README.md
├── START_HERE.md
├── PROJECT_BOOTSTRAP.md
├── PROJECT_STATUS.md
├── VISION.md
├── ROADMAP.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
│
├── Core/
├── Governance/
├── Architecture/
├── Models/
├── Knowledge/
├── Engine/
├── Services/
├── Runtime/
├── AI/
├── Memory/
├── Repository/
├── Specifications/
├── Interfaces/
├── Lifecycle/
├── Plugins/
├── Templates/
├── Release/
├── Projects/
├── Docs/
├── Examples/
├── Assets/
└── Archive/
```

## Domain Content Inventory

The inventory below is populated progressively from current repository evidence. It must not be interpreted as exhaustive until the corresponding folder is explicitly reconciled.

### Repository/

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

The control-plane set `REP-011` through `REP-016` is now explicitly present in the content inventory. Their own allocation, review and relationship records remain subject to cross-registry reconciliation.

### Models/

```text
Models/
├── README.md
├── MOD-001_KNOWLEDGE_MODEL.md
└── MOD-011_KNOWLEDGE_SOURCE_MODEL.md
```

This is a **partial evidence inventory**, not a claim that these are the only files in `Models/`.

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

The exact current-main Services directory enumeration establishes the physical filenames for `SRV-001` through `SRV-010`. `SRV-010_SERVICE_REFERENCE.md` remains the canonical current physical identity established by direct current-main read-back. This mutation replaces earlier wildcard placeholders with observed physical identities; it does not assert implementation, runtime execution, or Services partition closure.

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

This remains a partial inventory until the folder is physically reconciled.

### Memory/

Known recorded members include:

```text
Memory/
├── MEM-008_GUIDED_DISCOVERY_LEARNING_METHOD.md
├── Engineering_Journal/
│   ├── EJR-002_HERMUZ_BUILD_REVIEW_IDENTITY.md
│   ├── EJR-003_2026-08-09_HERMUZ_SESSION_HANDOFF_FAILURE_ANALYSIS.md
│   ├── EJR-015_2026-08-10_PRE_FAILURE_MUTATION_AUDIT.md
│   ├── EJR-016_2026-08-10_REVIEW_TRACEABILITY_AND_PHASE1_COMPLETION_CONTROL.md
│   ├── EJR-017_2026-08-10_REPOSITORY_ALLOCATION_AND_RECOVERY_REGISTRY.md
│   ├── EJR-018_2026-08-10_REPOSITORY_CONTENT_AND_RELATIONSHIP_REGISTRIES.md
│   ├── EJR-020_2026-08-10_CONTROL_PLANE_BOOTSTRAP_AND_ALLOCATION_BINDING.md
│   ├── EJR-021_2026-08-10_CONTROL_PLANE_OPERATIONALIZATION.md
│   ├── EJR-022_2026-08-10_HERMUZ_BUILD_METHOD_LESSONS.md
│   ├── EJR-023_2026-08-11_SESSION_RESUME_AND_PHASE1_CONTINUATION.md
│   └── EJR-025_2026-08-11_REP015_REVALIDATION_AND_SESSION_CLOSURE.md
├── Operational_Memory/
│   ├── README.md
│   ├── OPM-001_OPERATIONAL_MEMORY_MODEL.md
│   ├── OPM-002_OPERATIONAL_EVENT_CAPTURE.md
│   ├── OPM-003_OPERATIONAL_RETRIEVAL.md
│   └── OPM-004_OPERATIONAL_LIFECYCLE.md
├── Decision_Memory/
│   └── README.md
├── Historical_Memory/
│   └── Engineering_Journal/
└── Project_Memory/
    ├── README.md
    ├── PM-001_PROJECT_MEMORY_MODEL.md
    └── PM-003_PROJECT_MEMORY_LIFECYCLE.md
```

`Operational_Memory/`, `Decision_Memory/`, `Historical_Memory/`, and `Project_Memory/` are now explicitly represented in the content inventory because current repository evidence establishes their physical presence. Their review/allocation/relationship states remain governed by `REP-011`, `REP-012`, and `REP-014`; physical presence does not imply Phase-1 closure or canonical authority.

The `Historical_Memory/Engineering_Journal/` entry is intentionally represented as a directory-level evidence path because the current evidence confirms historical engineering-journal artifacts, while the exhaustive physical enumeration of that subdomain remains open.

This remains a known-evidence inventory and is not yet an exhaustive physical enumeration of `Memory/`.

### Specifications/

```text
Specifications/
├── README.md
└── 01-Knowledge-Organization.md
```

Canonical Path: `Specifications/01-Knowledge-Organization.md`

The current specification artifact declares the internal identity `SPEC-001-KNOWLEDGE-ORGANIZATION`; the physical path above is canonical within the inspected scope. The registry relationship `REL-001` remains `Revalidation Required` until cross-index identity reconciliation is complete.

### Interfaces/

```text
Interfaces/
├── INTF-001_INTERFACE_SPEC.md
├── INTF-004_API.md
├── INTF-006_ENVIRONMENT_SENSING.md
├── INTF-010_INTEGRATIONS.md
└── _FOLDER_STATUS.md
```

### Governance/

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

`GOV-011` and `GOV-012` are mapped as proposed artifacts and are not active canonical authority until ratified.

`GOV-013A` is `Approved / Canonical Addendum` to `GOV-013`. It establishes a mandatory pre-mutation bootstrap integrity gate and does not override higher ARGO authority.

### Architecture/

Known mapped members include:

```text
Architecture/
├── ARC_MAP.md
├── ARC-001_PLATFORM_ARCHITECTURE.md
├── ARC-002_COMPONENT_ARCHITECTURE.md
├── ARC-003_INFORMATION_FLOW.md
├── ARC-004_LAYER_MODEL.md
├── ARC-005_ARCHITECTURE_RULES.md
├── ARC-006_DEPENDENCY_MODEL.md
├── ARC-007_INTEGRATION_MODEL.md
├── ARC-008_REPOSITORY_LAYOUT.md
├── ARC-009_ARCHITECTURE_DECISIONS.md
├── ARC-010_EVOLUTION_MODEL.md
├── ARC-011_CANONICAL_ARCHITECTURE_MODEL.md
└── _FOLDER_STATUS.md
```

`ARC_MAP.md` is a map/navigation artifact and must not reuse the `ARC-001` identity.

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
├── CORE-007_DESIGN_PRINCIPLES.md
├── CORE-008_ARCHITECTURAL_LAWS.md
├── CORE-009_PLATFORM_LIFECYCLE.md
├── CORE-010_PLATFORM_ROADMAP.md
├── CORE-011_PLATFORM_CHARTER.md
└── _FOLDER_STATUS.md
```

### Assets/Diagrams/

The first explicitly registered visual artifact pair is now included in the content inventory:

```text
Assets/
└── Diagrams/
    ├── DIAG-001_REPOSITORY_PHASE1_STATUS_2026-08-10.svg
    └── DIAG-001_REPOSITORY_PHASE1_STATUS_2026-08-10.md
```

### Templates/, Release/, Projects/, Docs/, Examples/, Archive/

These folders are **STRUCTURE-IDENTIFIED / CONTENT RECONCILIATION PENDING** unless their exact file inventory is separately recorded and linked to `REP-011` and `REP-012`.

No closure is implied.

## Inventory Confidence States

Each folder should eventually be assigned one of:

`UNKNOWN → STRUCTURE_IDENTIFIED → PARTIAL_INVENTORY → RECONCILED → REVIEWED → RELATIONSHIP_VALIDATED → CLOSED_FOR_PHASE_1`

These states are controlled by evidence and explicit decisions. Listing content in this document cannot advance a folder directly to `CLOSED_FOR_PHASE_1`.

## Repository Progress Measurement

Progress percentages are **indicators, not canonical truth**. A percentage must never be presented as repository completion unless its denominator, scope, evidence source and calculation date are recorded.

For Phase 1, progress should be measured against explicit work units rather than raw file count.

## Relationship to Other Repository Control Files

`REP-013` answers:

> **What files are physically present in each folder?**

`REP-002` answers:

> **What is the repository's structural/domain map?**

`REP-014` answers:

> **How do the known artifacts relate, and which relationships remain unresolved?**

`REP-011` answers:

> **What has actually been reviewed, with what evidence?**

`REP-012` answers:

> **What is the allocation/state/checkpoint/recovery status of each artifact?**

A complete Phase-1 view requires all five perspectives.

## Completion Rule

A folder can only be marked `CLOSED_FOR_PHASE_1` when:

1. Its physical content inventory is reconciled;
2. Every known file has an allocation record;
3. Every required file has a review state;
4. Dependencies and consumers have been assessed where applicable;
5. material relationships are represented or explicitly unresolved;
6. unresolved items are explicitly recorded;
7. an explicit closure decision is recorded.

Until then the folder remains **OPEN**.

## Integrity State

Current repository state: **INTEGRITY HOLD**.

The content tree is synchronized with the current inspected repository baseline and records the canonical physical path for the Knowledge Organization specification and `SRV-010_SERVICE_REFERENCE.md`. `GOV-013A` is now represented in the Governance inventory. Runtime `RUN-011..015` and `Runtime/Prototype/` are explicitly represented from current repository evidence; exhaustive Runtime and broader cross-layer relationship validation remain open.

## Verification Model

Current audit model:

**Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Validated → Consumer/Dependency Checked → Mutation Impact Checked → Re-read After Mutation**

## P310 Cross-Control-Plane Binding Reconciliation — 2026-08-17

P310 established closure-readiness evidence after `REP-011` and `REP-012` were bound to the P309 control-plane cycle.

Current identity evidence:

- `REP-011` bound within current cycle; current reconciliation remains `PARTIALLY_RECONCILED / INTEGRITY HOLD`.
- `REP-012` bound within current cycle; current reconciliation remains `PARTIALLY_RECONCILED / INTEGRITY HOLD`.
- `REP-013` remains the canonical content inventory and is revalidated as physically current within the inspected scope.
- P309 Runtime/Integration and Full-Stack CI evidence passed on the resulting control-plane HEAD.

This section does not mark `REP-013` or Ring 0 closed. It records that its inventory identity was re-read as part of the P310 closure-readiness pass.

Next required transition:

`REP-013/014/015/016/020 CURRENT CROSS-READ → EXPLICIT PRIORITY-1 CLOSURE REVIEW`

## P345 Current Control-Plane Evidence Binding — 2026-08-17

Current main evidence through P344 was re-read against the current control-plane manifest, REP-011/REP-012 binding sections and the manifest-driven reconciliation gate.

Evidence bound in this section:

- P344 synchronized REP-011 and REP-012 evidence checkpoints;
- P340 manifest-driven control-plane gate passed on current main;
- P343 CI passed Integrity, Prototype and Integration jobs, with Full-Stack Repository Audit also PASS;
- current REP-013 content/blob before this mutation was `a6653b6d6665e92a14fa6b9a21e3ce1569cf49b5`;
- this mutation preserves all prior REP-013 content and appends only this evidence-binding section.

Disposition:

`REP-013 = PRESENT / CURRENT / P345-BINDING-COMPLETE WITHIN CURRENT CONTROL-PLANE EVIDENCE SCOPE`

This is an evidence-binding result only. It does **not** promote the control plane to `RECONCILED`, does not set `CLOSED_FOR_PHASE_1`, and does not close Priority 1.

The cross-registry state remains open until the corresponding `REP-014/015/016/020` evidence is reconciled to the same current checkpoint.

## Governing Rule

Repository Reality > Previous Status Claims > Conversation Memory

---

End of Document
