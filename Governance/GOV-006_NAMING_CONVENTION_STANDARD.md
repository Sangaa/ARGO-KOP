# GOV-006

---

# NAMING CONVENTION STANDARD

---

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: GOV-006  
Version: 1.3.0  
Status: Proposed / Audit-Derived Update  
Category: Governance / Standards  
Canonical: Yes  
Priority: Critical  
Last Audit Date: Aug 08, 2026  

---

# Purpose

This document establishes the mandatory naming, identity, path, and reference conventions for all canonical ARGO KOP repository artifacts.

The repository is the operational source of truth for active paths. Historical or superseded artifacts may be preserved in `Archive/`, but archived artifacts are not active canonical references.

---

# Directory & Prefix Matrix

| Prefix | Domain Layer | Canonical Parent Directory | Example Path |
| :--- | :--- | :--- | :--- |
| **`CORE`** | Platform Identity & Constitution | `Architecture/` | `Architecture/CORE-003_CONSTITUTION.md` |
| **`GOV`** | Governance Framework & Standards | `Governance/` | `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md` |
| **`REP`** | Repository Index & Mapping | `Repository/` | `Repository/REP-001_MASTER_INDEX.md` |
| **`RUN`** | Runtime Pipeline & Life-cycle | `Runtime/` | `Runtime/RUN-001_BOOT_SEQUENCE.md` |
| **`ENG`** | Cognitive Engines | `Engine/` | `Engine/ENG-004_VALIDATION_ENGINE.md` |
| **`SRV`** | Service Operations | `Services/` | `Services/SRV-005_VALIDATION_SERVICE.md` |
| **`MOD`** | Data & Knowledge Models | `Models/` | `Models/MOD-002_ENTITY_MODEL.md` |
| **`EJR`** | Engineering Journal Records | `Memory/Engineering_Journal/` | `Memory/Engineering_Journal/EJR-001_SELF_ASSESSMENT_AND_MARKET_FEEDBACK.md` |

---

# Legacy Namespace Boundary

The Engineering Journal historically used `ENG-001` through `ENG-010` before the current canonical prefix matrix was formalized. Those records are retained as **legacy journal identities** during the Connected-Baseline Stabilization Phase.

They MUST NOT be treated as evidence that `ENG` is valid for new Engineering Journal artifacts.

New Engineering Journal records MUST use the `EJR-*` namespace after this standard is formally approved.

Historical journal records are not silently renamed during the current audit because renaming them would create broad path, index, and historical-reference mutations that require a separate migration decision.

---

# Canonical Identity Rules

1. **One ID, one active canonical path.** An active Document ID MUST resolve to exactly one canonical repository path.
2. **Filename identity must match Document ID.** The identifier in the filename MUST match the internal `Document ID`.
3. **Canonical path determines active ownership.** Active governance artifacts belong under `Governance/`; `Standards/` is not an active canonical Governance location.
4. **No duplicate logical identities.** A second artifact with the same Document ID is permitted only in `Archive/` and must be clearly marked historical/superseded.
5. **Cross-references MUST resolve.** Related-document references MUST point to current active paths. References to archived paths are prohibited unless explicitly documenting historical evidence.
6. **Path changes require synchronized index updates.** Any canonical path change MUST be reflected in `REP-001` and `REP-002` before the repository can pass Integrity.
7. **Case sensitivity is mandatory.** Document IDs and canonical filenames MUST preserve the uppercase identifier format.
8. **No silent deletion.** Superseded artifacts must be preserved in `Archive/` before removal from an active path.
9. **Namespace ownership is global unless explicitly bounded.** A prefix cannot be reused for a different active domain without an explicit governance decision.
10. **Legacy identifiers must be classified, not silently normalized.** Historical numbering conflicts are resolved through an explicit migration decision, not by renaming files during unrelated audits.

---

# Canonicalization Decision — GOV-006

`Governance/GOV-006_NAMING_CONVENTION_STANDARD.md` is the sole active canonical GOV-006 artifact.

The previous `Standards/GOV-006_NAMING_CONVENTION_STANDARD.md` Version `1.0.0` has been preserved under `Archive/Governance-Legacy/` as historical evidence and is no longer canonical.

---

# Related Documents

* `Repository/REP-001_MASTER_INDEX.md`
* `Repository/REP-002_REPOSITORY_MAP.md`
* `Governance/GOV-004_DOCUMENT_METADATA.md`
* `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
* `Services/SRV-005_VALIDATION_SERVICE.md`
* `Memory/Engineering_Journal/README.md`

---

# Guiding Statement

A canonical identity must have one active path, one authoritative definition, and resolvable references. Historical identity conflicts must be preserved as evidence and resolved through explicit migration decisions.

---

End of Document
