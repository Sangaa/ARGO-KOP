# GOV-012

---

# DOMAIN RECONSTRUCTION STANDARD

Platform: ARGO KOP
Knowledge Operating Platform

Document ID: GOV-012
Version: 1.0.0
Status: Proposed / Integrity Hold
Category: Governance / Domain Reconstruction
Canonical: No
Development Baseline: 3.3.0
Last Audit: 2026-08-09

---

# Purpose

Defines how ARGO KOP rebuilds mature repository domains whose existing contents were created as early drafts, sketches, partial models, obsolete structures or incomplete implementations.

The objective is to preserve useful evidence without allowing historical structure to constrain the current architecture.

# Governing Rule

**Legacy Content is Evidence, not Authority.**

A folder, filename, old Document ID, populated draft or historical reference does not become canonical merely because it already exists.

# Reconstruction Lifecycle

Read → Inventory → Classify → Identify Authority → Detect Conflicts → Extract Useful Evidence → Define Current Purpose → Rebuild → Validate → Connect → Re-read → Promote or Hold

# Classification

Each existing artifact MUST be classified as one of:

- `CANONICAL_CANDIDATE`
- `VALID_SUPPORTING_ARTIFACT`
- `DRAFT`
- `LEGACY`
- `DUPLICATE`
- `CONFLICTING`
- `OBSOLETE`
- `UNAVAILABLE`
- `UNKNOWN`

No classification may be upgraded by assumption.

# First-Principles Rebuild

Rewriting a domain from first principles is preferred when its previous structure:

- predates the current architectural foundation;
- contains obsolete assumptions;
- mixes multiple responsibilities;
- has identity or authority conflicts;
- cannot be reconciled cleanly with current architecture;
- was created primarily as a planning sketch.

Reconstruction MUST NOT become a cosmetic renaming exercise.

# Domain Definition Before Documents

Before creating or rewriting documents, ARGO MUST establish:

1. Domain purpose.
2. Domain boundary.
3. Architectural role.
4. Authority relationship.
5. Inputs and outputs.
6. Dependencies.
7. Consumers.
8. Security implications.
9. Memory / learning implications where applicable.
10. Lifecycle and release implications.
11. Required canonical artifacts.
12. Required supporting artifacts.

# Folder Classes Covered

This standard applies, where relevant, to domains including:

- Templates
- Standards
- Specifications
- Release
- Plugins
- Models
- Assets
- Blueprints
- Knowledge
- Memory
- Decision
- AI
- Services
- Intelligence
- Quality
- Projects

The list is illustrative, not exhaustive.

# Templates

Templates define reusable document or operational structures.

A template MUST NOT be treated as the authority of the artifact produced from it.

Templates must identify:

- intended artifact type;
- required fields;
- optional fields;
- validation expectations;
- applicable authority.

# Standards

Standards define repeatable rules or constraints.

A Standard MUST identify its scope and authority relationship and MUST NOT silently override Governance or Constitution-level rules.

# Specifications

Specifications define an expected behavior, structure, interface or contract.

A Specification MUST distinguish:

- requirement;
- constraint;
- implementation detail;
- assumption;
- unresolved item.

# Release

Release artifacts describe publishable state and compatibility.

A release artifact MUST NOT claim an official release merely because a development baseline exists.

Release validation MUST remain connected to the applicable Release authority and repository evidence.

# Plugins

Plugin artifacts define extension boundaries and contracts.

A plugin specification is not implementation proof. Each plugin remains subject to manifest, interface, security, sandbox, provenance and quality validation.

# Models

Models describe structures or relationships.

Model reconstruction MUST validate consumers and producers before promotion. Schema changes MUST be checked for downstream impact and compatibility.

# Assets

Assets are supporting repository resources unless explicitly assigned another authority.

Assets MUST preserve provenance where material and MUST NOT be mistaken for architectural or policy artifacts.

# Blueprints

Blueprints are design proposals or construction plans.

A Blueprint MUST NOT be treated as an implemented state unless implementation evidence exists.

A Blueprint may be superseded without implying that the underlying repository is broken.

# Identity and Naming

During reconstruction:

- preserve one active identity per logical artifact;
- do not recycle an active Document ID for a different meaning;
- do not assign numeric identities to maps/status/navigation artifacts when doing so would collide with canonical content;
- move obsolete identities to governed history when necessary;
- update indexes only after identity and path validation.

# Relationship Validation

A rebuilt domain is not complete when its documents merely exist.

Before promotion, validate:

- inbound references;
- outbound references;
- dependency direction;
- consumers;
- providers;
- authority relationships;
- version alignment;
- security boundaries;
- runtime implications;
- memory / learning boundaries.

Material relationships should be checked in both directions where practical.

# Re-read After Mutation

Every material reconstruction MUST be followed by:

1. Re-reading changed artifacts.
2. Re-checking their internal identity.
3. Re-checking affected indexes.
4. Re-checking direct references.
5. Reviewing ripple effects.
6. Recording unresolved evidence.

# Promotion States

A reconstructed domain may be:

- `RECONSTRUCTION_PENDING`
- `RECONSTRUCTED / HOLD`
- `VALIDATED / HOLD`
- `PROMOTED / CANONICAL`
- `PARTIAL / HOLD`
- `BLOCKED`

Promotion to Canonical requires sufficient evidence and applicable authority. Filling every file is not a promotion criterion.

# Archive and Provenance

When legacy material has migration value, preserve it through governed Archive/history.

Archive preservation MUST retain enough information to identify:

- former path;
- former identity where applicable;
- reconstruction reason;
- successor artifact where known;
- relevant commit/history evidence.

Archive is preservation, not active authority.

# Multi-Domain Rebuild

When several domains are reconstructed together, establish the shared boundaries first.

Preferred order:

**Foundation → Authority → Architecture → Repository → Standards / Specifications → Models / Blueprints → Templates → Plugins / Interfaces → Runtime / Services → Release → Applied Domains**

This order may change when evidence requires it, but the reason must be recorded.

# External Review

External model feedback may identify reconstruction risks or useful candidates.

It remains evidence input and MUST follow `GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md` when submitted as formal review.

External consensus does not create canonical authority.

# Completion Rule

A domain is considered ready for canonical promotion only when:

- purpose is clear;
- boundary is clear;
- authority is clear;
- identity is consistent;
- required artifacts are present or explicitly unavailable;
- relationships are validated;
- conflicts are resolved or explicitly held;
- security and runtime impacts are addressed;
- repository indexes are synchronized;
- post-mutation re-read is complete.

# Authority Boundary

This standard governs reconstruction process. It does not override the Constitution, Governance authority, Canonical Architecture Model, Repository authority or Release authority.

# Related Documents

- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Governance/GOV-010_GOVERNANCE_MODEL.md`
- `Governance/GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md`
- `Architecture/ARC_MAP.md`
- `Architecture/ARC-009_ARCHITECTURE_DECISIONS.md`
- `Architecture/ARC-010_EVOLUTION_MODEL.md`
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Release/VERSION.md`

---

# Guiding Statement

Do not repair yesterday's sketch by extending it blindly. Preserve its evidence, rebuild its meaning from the current foundation, then connect it only after the new structure survives validation.

---

End of Document
