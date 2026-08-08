# REP-001

---

# ARGO KOP - MASTER REPOSITORY INDEX

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: REP-001
Version: 1.5.0
Status: Integrity Hold
Category: Root Baseline / Repository Index
Canonical: Yes
Priority: Absolute / Mandatory
Last Audit Date: Aug 08, 2026

---

## 1. Purpose

This document is the canonical index of active, verified repository artifacts. An artifact is active only when its identity, path, version, canonical status, and repository references are consistent with the current repository baseline.

This index MUST NOT declare the repository clean solely because a previous status document declared it clean.

## 2. Root Baseline

- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`
- `README.md`
- `VISION.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`

## 3. Repository Layer

- `Repository/REP-001_MASTER_INDEX.md` — this canonical index.
- `Repository/REP-002_REPOSITORY_MAP.md` — canonical physical map.

## 4. Governance Layer

Verified active Governance artifacts:

- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md` — Document ID `GOV-001`.
- `Governance/GOV-004_DOCUMENT_METADATA.md` — Document ID `GOV-004`.
- `Governance/GOV-005_REVIEW_STANDARD.md` — Document ID `GOV-005`.
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md` — Document ID `GOV-006`.
- `Governance/GOV-009_REPOSITORY_POLICY.md` — active repository policy; metadata validation remains part of the open audit.
- `Governance/GOV-010_GOVERNANCE_MODEL.md` — Document ID `GOV-010`.
- `Governance/_FOLDER_STATUS.md` — evidence record; not an authority to declare completion.

No `GOV-011` document is registered as active. References to an unverified GOV-011 authority must not be treated as canonical.

## 5. Runtime Layer

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

- `Architecture/CORE-000_PLATFORM_ARCHITECTURE.md`
- `Architecture/CORE-002_ARGO_IDENTITY.md`
- `Architecture/CORE-003_CONSTITUTION.md`
- `Architecture/ARC-004_LAYER_MODEL.md`
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Architecture/_FOLDER_STATUS.md`

## 7. Canonicalization Record

On Aug 08, 2026, Governance identity conflicts involving GOV-004, GOV-005, and GOV-006 were reconciled by establishing one active canonical path and preserving superseded evidence under `Archive/Governance-Legacy/`.

GOV-010 was aligned with the verified Governance dependency set. An unverified GOV-011 authority was removed from the active dependency model rather than being invented.

## 8. Integrity State

Current repository state: **INTEGRITY HOLD**.

The index is synchronized with the Governance baseline, but repository-wide integrity is not declared clean until the consolidated identity/path/version/reference audit passes.

## 9. Rule

Repository Reality > Previous Status Claims > Conversation Memory

---

End of Document
