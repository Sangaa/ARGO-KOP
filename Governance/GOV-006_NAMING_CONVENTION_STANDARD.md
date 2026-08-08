# GOV-006

---

# NAMING CONVENTION STANDARD

---

Platform: ARGO KOP (Knowledge Operating Platform) 
Document ID: GOV-006 
Version: 1.1.0 
Status: Approved 
Category: Governance / Standards 
Canonical: Yes 
Priority: Critical 
Last Audit Date: Aug 08, 2026 

---

# Purpose

This document establishes the mandatory alphanumeric naming conventions and file routing prefixes for all directories, files, and logical entities inside the ARGO KOP repository.

---

# Directory & Prefix Matrix

All artifacts MUST use uppercase alphanumeric prefixes followed by sequential numbering and explicit snake_case labeling:

| Prefix | Domain Layer | Example Path / Filename |
| :--- | :--- | :--- |
| **`CORE`** | Platform Identity & Constitution | `Architecture/CORE-003_CONSTITUTION.md` |
| **`GOV`** | Governance Framework & Standards | `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md` |
| **`RUN`** | Runtime Pipeline & Life-cycle | `Runtime/RUN-001_BOOT_SEQUENCE.md` |
| **`ENG`** | Core Engines & Engineering Logs | `Engine/ENG-004_VALIDATION_ENGINE.md` |
| **`SRV`** | Service Operations Layer | `Services/SRV-005_VALIDATION_SERVICE.md` |
| **`MOD`** | Data & Knowledge Models | `Models/MOD-002_ENTITY_MODEL.md` |

---

# Naming Integrity Rules

1. **Anti-Rename Rule:** Never rename or shift an active file path without comprehensively updating all cross-references across the repository matrix.
2. **Case Sensitivity:** All codes (`RUN-001`, `GOV-006`) MUST remain entirely capitalized.
3. **No Duplication:** Internal classification numbering cannot overlap across different domains.

---

# Related Documents

* `Repository/REP-001_MASTER_INDEX.md`
* `Governance/GOV-007_DOCUMENT_CLASSIFICATION.md`
* `Services/SRV-005_VALIDATION_SERVICE.md`

---

# Guiding Statement

Absolute predictability in structure eliminates execution latency.

---

End of Document
