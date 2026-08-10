# ARGO Knowledge Organization Specification

Document ID: SPEC-001-KNOWLEDGE-ORGANIZATION
Version: 3.1.2
Status: Foundation Specification / Integrity Hold
Category: Operational Specification
Development Baseline: 3.2.1
Last Audit: 2026-08-10

---

## Purpose

Defines how knowledge artifacts are organized, classified, validated, connected, maintained and archived inside ARGO KOP.

This document specifies organization and operating requirements. It does not independently establish platform authority, canonical schema ownership, governance authority, or repository integrity.

## Authority Boundary

Higher authority prevails when a conflict exists:

1. ARGO Constitution and applicable Governance authority
2. Canonical Architecture / approved Architecture decisions
3. Canonical Models applicable to the knowledge object
4. This Specification
5. Supporting standards, templates and examples
6. Legacy or exploratory material

A conflict MUST be recorded rather than silently resolved by interpretation.

The proposed `Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md` may provide reconstruction guidance during the current staged rebuild, but its proposed status does not grant it active Governance authority. Any reconstruction decision remains subject to currently ratified Governance, Architecture and Repository authority.

## Core Rules

1. Knowledge MUST distinguish observed facts, repository facts, assumptions, analysis, decisions, lessons, proposals and unknowns where materially relevant.
2. Evidence and interpretation MUST NOT be presented as the same thing.
3. External model output is evidence input, not ARGO authority.
4. Physical location and classification tier MUST NOT be treated as authority claims by themselves.
5. A reference is not a verified dependency until its target, identity, authority and relationship are checked.
6. Unknown or unavailable evidence MUST remain explicitly unknown/unavailable.
7. A legacy artifact may be replaced rather than incrementally patched when its structure no longer reflects the current architecture.
8. Material changes require impact review and re-read validation before promotion.

## Knowledge Classification

### Tier 1 — Foundational
Core principles, non-negotiable rules and foundational platform knowledge.

Typical locations: Core/, Governance/, Architecture/.

Changes normally require the applicable governance/architecture authority.

### Tier 2 — Operational
Validated processes, standards, reusable practices and operational definitions.

Typical locations: Specifications/, Runtime/, Services/, Models/ and other governed operational domains.

### Tier 3 — Domain
Verified domain facts, evidence-backed analysis and subject-matter knowledge.

Typical location: Knowledge/ or an explicitly governed project/domain location.

### Tier 4 — Exploratory
Hypotheses, preliminary research, emerging patterns and provisional ideas.

Exploratory material MUST remain visibly provisional and MUST NOT silently promote itself into canonical knowledge.

## Knowledge Object Minimum Structure

A knowledge artifact SHOULD contain, where applicable:

- Identity / Document ID
- Title
- Purpose
- Scope
- Status
- Owner / source
- Created / updated dates
- Evidence / provenance
- Facts
- Analysis or interpretation
- Assumptions
- Uncertainties / limitations
- Related documents
- References
- Validation state
- Review state

Required metadata remains subject to `Governance/GOV-004_DOCUMENT_METADATA.md` and the applicable canonical model.

## Domain Organization

A domain MAY use structures such as:

```text
Knowledge/
└── Domain/
    ├── Overview.md
    ├── Core-Facts.md
    ├── Analysis.md
    ├── References.md
    └── SubDomains/
```

This is a pattern, not a claim that these example files must exist everywhere.

A domain structure MUST be adapted to its actual purpose. Templates MUST NOT force meaningless files into a domain.

## Evidence and Provenance

For material claims, preserve enough provenance to answer:

- What was observed?
- From where?
- When?
- By whom/system?
- Is the source primary, derived or external?
- What could not be verified?

External model reports MUST follow `Governance/GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md` when that standard is applicable.

## Facts vs Analysis

### Verified Facts
Facts MUST have identifiable evidence appropriate to their domain.

### Analysis
Analysis may infer patterns, implications and recommendations from available facts, but MUST remain distinguishable from facts.

### Assumptions
Assumptions MUST be labeled when they materially influence analysis or decisions.

### Unknowns
Insufficient evidence MUST produce an explicit unknown/hold state rather than invented certainty.

## Quality and Validation

Before promotion, validate as applicable:

- Identity and metadata
- Evidence/provenance
- Fact support
- Assumption labeling
- Analysis separation
- Status accuracy
- Internal references
- Authority relationships
- Dependencies and consumers
- Security/privacy constraints
- Downstream impact
- Re-read after material mutation

Validation outcome MUST use an explicit state such as `PASS`, `PASS_WITH_WARNINGS`, `INTEGRITY_HOLD`, `FAIL`, or `INSUFFICIENT_EVIDENCE` where the applicable process requires it.

## Lifecycle

```text
Capture
  ↓
Classify
  ↓
Evidence / Provenance
  ↓
Analyze
  ↓
Review
  ↓
Validate
  ↓
Connect
  ↓
Promote / Hold / Archive
  ↓
Re-read after material change
```

Promotion does not erase provenance or prior states.

## Cross-Linking

Internal references SHOULD use relative paths where practical.

Before treating a link as a dependency, verify:

`Target Exists → Identity Correct → Authority Valid → Relationship Correct → Consumer/Impact Checked`

Cross-reference behavior is governed additionally by `STD-003_CROSS_REFERENCE_STANDARD.md`.

## Archival

Archive material when superseded, deprecated, obsolete, completed or otherwise no longer active.

Archival MUST preserve:

- original identity where known;
- reason for archival;
- successor/replacement where applicable;
- migration/reference traceability;
- relevant history.

Archive status does not mean "false"; it means no longer active authority/current material.

## Legacy Reconstruction

Legacy content MUST be evaluated before reuse.

The reconstruction decision MAY be:

- retain;
- revise;
- merge;
- split;
- relocate;
- archive;
- replace from scratch;
- mark unavailable.

`GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md` is currently a proposed process reference. Its reconstruction method may be used as guidance, but active Governance and Architecture authority remains controlling until GOV-012 is formally ratified.

## Review Rules

A specification change MUST identify:

- what changed;
- why it changed;
- evidence supporting the change;
- affected artifacts/domains;
- validation performed;
- unresolved issues;
- resulting status.

Material changes MUST trigger downstream review where the specification is consumed.

## Current Validation State

The specification was re-read during the 2026-08-10 audit and its development baseline was aligned to the authoritative `Release/VERSION.md` baseline `3.2.1`.

Current state remains `INTEGRITY HOLD` because repository-wide relationships with Models, Standards, Governance, Architecture, consumers and the active Repository Map have not yet been fully validated.

---

End of Document
