# ARCHITECTURE_README

---

# ARGO KOP — ARCHITECTURE LAYER SPECIFICATION & DIRECTORY HANDBOOK

---

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: ARCHITECTURE_README
Version: 3.2.1
Status: Approved / Integrity Hold
Category: Architecture / Directory Handbook
Canonical: Yes
Priority: Absolute / Critical
Development Baseline: 3.2.1
Last Audit Date: 2026-09-01
Review Type: Priority-7 Cross-Layer Consumer Authority Reconciliation

---

## 1. Purpose & Authority Scope

The Architecture layer defines stable structural boundaries, dependency direction, component responsibilities and integration constraints for ARGO KOP.

Architecture interpretation remains subject to the current authority boundary:

Constitution / applicable Governance authority

↓

`Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`

↓

Other applicable Architecture documents

↓

Repository and implementation artifacts

`ARC-011` is the current authoritative architectural reference for structural boundaries and dependency direction, subordinate to the Constitution and applicable Governance authority.

`Core/CORE-000_PLATFORM_ARCHITECTURE.md` preserves Core-level platform architecture intent and must remain aligned with that governed Architecture-control boundary. CORE-000 does not establish a competing Architecture model merely because it is a Core artifact or because another document references it.

Implementation must remain compatible with the applicable Architecture authority; implementation evidence does not silently redefine Architecture.

This README is a canonical directory handbook and navigation/control surface. It does not outrank ARC-011, create relationships merely by listing artifacts, or certify the Architecture domain by itself.

---

## 2. Current Primary Architecture Review Set

The current primary Architecture review set is the active ARC series identified by the current Architecture folder status:

1. [`Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`](ARC-001_PLATFORM_ARCHITECTURE.md)
2. [`Architecture/ARC-002_COMPONENT_ARCHITECTURE.md`](ARC-002_COMPONENT_ARCHITECTURE.md)
3. [`Architecture/ARC-003_INFORMATION_FLOW.md`](ARC-003_INFORMATION_FLOW.md)
4. [`Architecture/ARC-004_LAYER_MODEL.md`](ARC-004_LAYER_MODEL.md)
5. [`Architecture/ARC-005_ARCHITECTURE_RULES.md`](ARC-005_ARCHITECTURE_RULES.md)
6. [`Architecture/ARC-006_DEPENDENCY_MODEL.md`](ARC-006_DEPENDENCY_MODEL.md)
7. [`Architecture/ARC-007_INTEGRATION_MODEL.md`](ARC-007_INTEGRATION_MODEL.md)
8. [`Architecture/ARC-008_REPOSITORY_LAYOUT.md`](ARC-008_REPOSITORY_LAYOUT.md)
9. [`Architecture/ARC-009_ARCHITECTURE_DECISIONS.md`](ARC-009_ARCHITECTURE_DECISIONS.md)
10. [`Architecture/ARC-010_EVOLUTION_MODEL.md`](ARC-010_EVOLUTION_MODEL.md)
11. [`Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`](ARC-011_CANONICAL_ARCHITECTURE_MODEL.md)

The list above identifies the current primary ARC review set; it does not mean that every member is globally certified or that numeric membership alone establishes authority.

### Supporting navigation / control surfaces

The Architecture folder also contains non-ARC navigation/control artifacts with distinct roles:

- [`Architecture/ARC_MAP.md`](ARC_MAP.md) — canonical Architecture map/navigation artifact; it intentionally has no `ARC-NNN` Document ID and does not create authority merely by listing a node.
- [`Architecture/README.md`](README.md) — this directory handbook and navigation/control surface.
- [`Architecture/_FOLDER_STATUS.md`](_FOLDER_STATUS.md) — living evidence/status record; status evidence is not itself proof of semantic certification.

### Preserved foundation / legacy material

`Architecture/01-System-Overview.md` remains physically present as earlier foundation material. Its physical presence does not make its historical four-layer/five-component model current Architecture authority. Any useful content from that artifact must be independently revalidated before promotion or reuse.

Physical inventory, canonical authority, relationship semantics and certification are separate questions.

---

## 3. Core-Level Architecture Alignment

`Core/CORE-000_PLATFORM_ARCHITECTURE.md` expresses Core-level platform architecture intent.

For current structural boundaries and dependency direction, CORE-000 is aligned with the current canonical Architecture authority rather than replacing it:

Constitution / applicable Governance authority

↓

`Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`

↓

Other applicable Architecture controls

↓

Repository / implementation artifacts

CORE-000 may provide foundational intent, purpose and Core-level constraints, but current structural interpretation must not use an older or lower-fidelity CORE-000 model to override ARC-011.

A textual link between this README, CORE-000, CORE-003 or ARC-011 does not by itself establish a `REFERENCES`, `DEPENDS_ON`, `GOVERNS` or other REP-014 relationship. Relationship registration requires its own evidence and authority review.

---

## 4. Structural Integration Rules

1. **Authority boundary:** Constitution and applicable Governance remain above Architecture; ARC-011 controls current Architecture interpretation for structural boundaries and dependency direction within that governed scope.
2. **Dependency direction:** dependency claims must remain compatible with ARC-011 and `ARC-006_DEPENDENCY_MODEL.md`; reverse dependency requires explicit governed architectural authorization.
3. **Single ownership / identity:** every active canonical artifact must preserve one applicable identity/ownership boundary and one active canonical path where the repository model requires it.
4. **Repository reality first:** physical folder placement, filenames, numbering, status files and textual references do not create architectural authority by themselves.
5. **Evidence-backed relationships:** references, dependencies, integrations and ownership claims require direct evidence and classification; a directory list is navigation, not relationship proof.
6. **Controlled mutation:** material Architecture changes follow applicable Governance, including `GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md` and `GOV-014A_HERMUZ_PREWRITE_MUTATION_MATRIX_GATE.md` where applicable. Technical write capability does not replace authorization.
7. **Preserve unrelated content:** correction of one bounded Architecture consumer or authority statement does not authorize broad refactoring, certification or silent promotion of adjacent artifacts.

---

## 5. Integrity / Certification Boundary

The Architecture folder remains under `INTEGRITY HOLD` while its active semantics, layer/dependency consistency, cross-layer references and consumer alignment are re-audited.

This README's current review establishes only its own bounded alignment with current CORE-000 / CORE-003 / ARC-011 authority semantics and the current Architecture folder inventory model.

It does **not** establish:

- Architecture folder certification;
- Core folder certification;
- all Architecture relationships as reconciled;
- all downstream consumers as aligned;
- repository-wide graph completion;
- Phase-1 closure;
- Connected Baseline closure;
- Global PASS.

The authoritative current domain state remains the evidence-backed `Architecture/_FOLDER_STATUS.md`, interpreted together with the applicable higher authority and current repository evidence.

---

## 6. Related Authority / Evidence

- `PROJECT_BOOTSTRAP.md`
- `Core/CORE-003_CONSTITUTION.md`
- `Core/CORE-000_PLATFORM_ARCHITECTURE.md`
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`
- `Architecture/ARC_MAP.md`
- `Architecture/_FOLDER_STATUS.md`
- `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`
- `Governance/GOV-014A_HERMUZ_PREWRITE_MUTATION_MATRIX_GATE.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

---

## 7. Guiding Statement

A stable Architecture layer requires current authority boundaries, explicit evidence, controlled mutation and honest separation between navigation, canonical interpretation, implementation and certification.

---

End of Document
