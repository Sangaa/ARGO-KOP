# STD-003

---

# CROSS-REFERENCE STANDARD

Platform: ARGO KOP
Knowledge Operating Platform

Document ID: STD-003
Version: 1.3.1
Status: Validated / Integrity Hold
Category: Standard / Cross-Reference
Repository Development Baseline: 3.2.1
Latest Official Release: 1.0.0
Last Audit: 2026-08-10

---

# Purpose

Defines how ARGO KOP identifies, classifies, validates, migrates and revalidates relationships between repository artifacts.

A reference is evidence of an intended relationship until validation establishes what that relationship actually is.

# Core Rules

1. Every active canonical document with an assigned Document ID has one unique logical identity.
2. References should prefer stable Document IDs when available, while retaining enough path/section context for practical resolution.
3. A textual reference is NOT a validated dependency until the target is located, read, identity-checked, authority-checked and relationship-validated.
4. Reference types MUST distinguish at least:
   - Depends On
   - Related
   - Replaces
   - Supersedes
   - Deprecated By
   - Generated From
   - Referenced By
   - Implements
   - Consumes
   - Produces
5. Material relationships must remain traceable to evidence and applicable authority.
6. Broken, stale or materially ambiguous references remain unresolved until corrected or explicitly bounded.
7. Circular dependencies are findings requiring architectural review; they must not be silently removed merely to make the graph appear clean.
8. Reference validation should be bidirectional where practical:
   - Source → Target
   - Target → Authority / Consumers / Dependencies / Indexes
9. Historical references may remain valid as historical evidence when their targets are no longer active canonical artifacts, provided their historical status is explicit.
10. Reference normalization MUST NOT be performed solely from filename similarity or numeric sequence.
11. Legacy references are evidence to investigate, not authority to preserve automatically.
12. A reference cannot promote a draft, proposal or external model claim into canonical authority.

# Reference Priority

When multiple identifiers are available, use the strongest stable identity first:

1. Document ID
2. Canonical path
3. Section / heading
4. Local anchor or bounded content context

The chosen reference must remain resolvable in the current repository context.

# Validation Model

Referenced → Located → Read → Identity Verified → Authority Verified → Relationship Classified → Consumer/Dependency Checked → Impact Reviewed → Re-read After Mutation

A reference is considered validated only when the applicable steps have evidence.

# Relationship Evidence

For material relationships, validation should record:

- Source artifact
- Target artifact
- Relationship type
- Evidence location
- Authority basis
- Validation status
- Consumer / dependency impact
- Last validation date
- Unresolved constraints

# Mutation Rule

Any rename, move, archive, merge, split, identity correction or material content change affecting a referenced artifact triggers revalidation of affected relationships.

The mutation process is:

Detect → Scope → Update → Re-read Source → Re-read Target → Validate Consumers / Dependencies → Update Index / Map → Record unresolved relationships.

# Migration Rule

When a reference target is renamed, moved, archived or reclassified:

1. Preserve historical provenance.
2. Identify the canonical successor where one exists.
3. Update active consumers.
4. Update indexes and status records.
5. Re-read affected artifacts.
6. Revalidate upstream and downstream relationships.
7. Record unresolved relationships explicitly.

# External Feedback Rule

References originating from external model reports, reviewer comments or external tools are treated as external evidence.

They MUST be validated against repository evidence before they can influence canonical artifacts.

See:

`Governance/GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md`

# Authority Boundary

This standard governs reference mechanics only.

It does not create authority over Constitution, Governance, Architecture, Release or other higher-order decisions.

# Related Documents

- `PROJECT_BOOTSTRAP.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Architecture/ARC-001_PLATFORM_ARCHITECTURE.md`
- `Architecture/ARC-003_INFORMATION_FLOW.md`
- `Architecture/ARC-010_EVOLUTION_MODEL.md`
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Governance/GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md`
- `Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md`

# Historical Migration Note

Former identity:

`Standards/ARC-003_CROSS_REFERENCE_SYSTEM.md`

Former Document ID:

`ARC-003`

Reason for migration:

The former identity conflicted with canonical Architecture `ARC-003_INFORMATION_FLOW`, and the former content was too primitive for the current repository relationship-validation model.

The historical artifact remains historical evidence. The active standard uses `STD-003`.

---

# Guiding Statement

A reference becomes trustworthy only after ARGO proves what it points to, why the relationship exists, what authority supports it, and what changed when either side moved.

---

End of Document
