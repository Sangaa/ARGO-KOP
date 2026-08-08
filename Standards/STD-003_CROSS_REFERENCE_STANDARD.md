# STD-003

---

# CROSS-REFERENCE STANDARD

---

Platform

ARGO KOP (Knowledge Operating Platform)

Document ID

STD-003

Version

1.2.0

Status

Validated / Integrity Hold

Category

Standard / Cross-Reference

Repository Development Baseline

3.2.1

Latest Official Release

1.0.0

Last Audit

2026-08-08

---

# Purpose

Defines how ARGO KOP documents identify, classify and validate relationships to other repository artifacts.

This standard replaces the historical `Standards/ARC-003_CROSS_REFERENCE_SYSTEM.md` identity. The historical file used an `ARC-003` identity that conflicts with the canonical Architecture artifact `Architecture/ARC-003_INFORMATION_FLOW.md`.

# Core Rules

1. Every active canonical document with an assigned Document ID has one unique logical identity.
2. References should prefer stable Document IDs when available, while retaining enough path/section context for practical resolution.
3. A textual reference is not a validated dependency until the target is located, read, identity-checked, authority-checked and relationship-validated.
4. Reference types should distinguish at least:
   - Depends On
   - Related
   - Replaces
   - Supersedes
   - Deprecated By
   - Generated From
   - Referenced By
5. Important decisions and material changes must remain traceable to evidence and applicable authority.
6. Broken or materially ambiguous references remain unresolved until corrected or explicitly bounded.
7. Circular dependencies are findings requiring architectural review; they are not silently accepted or removed without understanding their cause.
8. Reference validation should be bidirectional where practical:
   - Source → Target
   - Target → Authority / Consumers / Indexes
9. Historical references may remain valid as historical evidence even when their targets are no longer active canonical artifacts, provided their historical status is explicit.
10. Reference normalization must not be performed solely from filename similarity or numeric sequence.

# Reference Priority

When multiple identifiers are available, use the strongest stable identity first:

1. Document ID
2. Canonical path
3. Section / heading
4. Paragraph or local anchor

The chosen reference must remain resolvable in the current repository context.

# Validation Model

**Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Validated → Consumer/Dependency Checked → Re-read After Mutation**

# Migration Rule

When a reference target is renamed, moved, archived or reclassified:

1. preserve historical provenance;
2. identify the canonical successor where one exists;
3. update active consumers;
4. update indexes and status records;
5. re-read affected artifacts;
6. record unresolved relationships explicitly.

# Authority Boundary

This standard governs reference mechanics only. It does not create authority over Constitution, Governance, Architecture or Release decisions.

# Related Documents

- `PROJECT_BOOTSTRAP.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`
- `Architecture/ARC-003_INFORMATION_FLOW.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`

---

# Historical Migration Note

Former identity:

`Standards/ARC-003_CROSS_REFERENCE_SYSTEM.md`

Former Document ID:

`ARC-003`

Reason for migration:

The former identity conflicted with the canonical Architecture `ARC-003` identity and the former content was too primitive for the current repository relationship-validation model.

The historical artifact is preserved in Git history; the active standard uses `STD-003`.

---

End of Document
