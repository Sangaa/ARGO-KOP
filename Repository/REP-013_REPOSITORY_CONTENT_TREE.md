# REP-013 — REPOSITORY CONTENT TREE

Platform: ARGO KOP  
Document ID: REP-013  
Version: 1.0.1  
Status: Active / Phase 1 Population In Progress  
Development Baseline: 3.2.1  
Last Audit: 2026-08-10  

## Purpose

Provide the second structural tree of the ARGO repository: not only which folders exist, but which known files belong to each folder.

This is a **content inventory**, not a claim that every listed file is reviewed, valid, canonical, or Phase-1 complete.

## State Rule

Each entry must eventually carry:

- Path
- Document ID
- File type
- Current repository state
- Review state from `REP-011`
- Allocation state from `REP-012`
- Canonical authority, where applicable
- Last known checkpoint

A folder is **not CLOSED_FOR_PHASE_1** merely because its contents are listed.

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
├── Templates/
├── Release/
├── Docs/
├── Examples/
├── Assets/
└── Archive/
```

## Domain Content Inventory

The inventory below is populated progressively from repository evidence. It must not be interpreted as exhaustive until the corresponding folder is explicitly reconciled.

### Repository/

```text
Repository/
├── REP-001_MASTER_INDEX.md
├── REP-002_REPOSITORY_MAP.md
├── REP-011_REVIEW_TRACEABILITY_LEDGER.md
├── REP-012_REPOSITORY_ALLOCATION_REGISTRY.md
├── REP-013_REPOSITORY_CONTENT_TREE.md
└── REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md
```

### Models/

```text
Models/
├── README.md
├── MOD-001_KNOWLEDGE_MODEL.md
└── MOD-011_KNOWLEDGE_SOURCE_MODEL.md
```

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
├── SRV-001_*.md
├── SRV-002_*.md
├── SRV-003_*.md
├── SRV-004_*.md
├── SRV-005_*.md
├── SRV-006_*.md
├── SRV-007_*.md
├── SRV-008_*.md
├── SRV-009_UPDATE_SERVICE.md
├── SRV-010_SERVICE_CATALOG.md
└── _FOLDER_STATUS.md
```

The wildcard entries are intentionally unresolved until exact filenames are enumerated from the current repository. They are placeholders, not fabricated file identities.

### Runtime/

```text
Runtime/
├── RUN-001_BOOT_SEQUENCE.md
└── RUN-010_RUNTIME_REFERENCE.md
```

### AI/

Known audited members include:

```text
AI/
├── AI-006_MODEL_ADAPTER.md
├── AI-007_MULTI_MODEL_SUPPORT.md
└── AI-008_EXTERNAL_FEEDBACK_INTEGRATION.md
```

### Memory/Engineering_Journal/

```text
Memory/Engineering_Journal/
├── EJR-002_HERMUZ_BUILD_REVIEW_IDENTITY.md
├── EJR-003_2026-08-09_HERMUZ_SESSION_HANDOFF_FAILURE_ANALYSIS.md
├── EJR-007_2026-08-10_*.md
├── EJR-008_2026-08-10_*.md
├── EJR-009_2026-08-10_*.md
├── EJR-010_2026-08-10_*.md
├── EJR-011_2026-08-10_*.md
├── EJR-012_2026-08-10_*.md
├── EJR-013_2026-08-10_*.md
├── EJR-014_2026-08-10_*.md
├── EJR-015_2026-08-10_PRE_FAILURE_MUTATION_AUDIT.md
├── EJR-016_2026-08-10_REVIEW_TRACEABILITY_AND_PHASE1_COMPLETION_CONTROL.md
├── EJR-017_2026-08-10_REPOSITORY_ALLOCATION_AND_RECOVERY_REGISTRY.md
└── EJR-018_2026-08-10_REPOSITORY_CONTENT_AND_RELATIONSHIP_REGISTRIES.md
```

Wildcard entries here mean exact inventory reconciliation is still required.

### Specifications/

```text
Specifications/
├── README.md
└── SPEC-001-KNOWLEDGE-ORGANIZATION.md
```

### Interfaces/

```text
Interfaces/
└── INTF-010_INTEGRATIONS.md
```

### Governance/, Architecture/, Core/, Templates/, Release/, Docs/, Examples/, Assets/, Archive/

These folders are **STRUCTURE-IDENTIFIED / CONTENT RECONCILIATION PENDING** unless their exact file inventory is separately recorded and linked to `REP-011` and `REP-012`.

No closure is implied.

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

---

End of Document
