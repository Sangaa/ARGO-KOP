# TEMPLATES

Platform: ARGO KOP  
Knowledge Operating Platform

Document ID: TPL-README
Version: 1.3.0
Status: Validated / Reconstruction In Progress
Category: Templates
Canonical: Yes
Development Baseline: 3.2.1
Last Audit: 2026-08-16

---

# Purpose

This directory contains reusable document templates for ARGO KOP.

Templates define **structure**, not authority. Copying a template does not make the resulting document canonical, approved or valid.

# Template Authority

Templates MUST conform to the current Constitution, Governance, Architecture, Repository and applicable domain standards.

Legacy templates are source material only and may be replaced rather than incrementally repaired when their structure no longer matches the current ARGO model.

# Required Metadata for Canonical Documents

Where applicable, generated documents should preserve:

- Platform
- Document ID
- Title
- Version
- Status
- Category
- Canonical flag
- Owner / Authority
- Development Baseline
- Creation / Audit date
- Purpose
- Scope
- Evidence / Provenance
- Dependencies
- Related Documents
- Validation / Review state

The exact metadata depends on document type; templates MUST NOT force irrelevant fields into every artifact.

# Available Templates

- `TEMPLATE-001_DOCUMENT.md` — general document structure
- `TEMPLATE-002_BLUEPRINT.md` — blueprint structure
- `TEMPLATE-003_COMPONENT_SPEC.md` — component specification
- `TEMPLATE-004_DECISION.md` — architecture / governance decision record
- `TEMPLATE-005_PROJECT.md` — project record
- `TEMPLATE-006_UPDATE_PACK.md` — repository update handoff
- `TEMPLATE-007_BUILD_REPORT.md` — build completion / engineering report
- `TEMPLATE-008_RELEASE.md` — release record
- `TEMPLATE-009_COMPONENT.md` — component description
- `TEMPLATE-010_KNOWLEDGE_ENTRY.md` — knowledge entry

# Mandatory External Feedback

External model / reviewer reports MUST use `Governance/GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md` or preserve all of its required fields when another transport format is used.

Template files do not replace the external feedback standard.

# Template Lifecycle

Draft → Reviewed → Validated → Published → Superseded / Archived

Changes to canonical templates require governed review because downstream documents may depend on their structure.

# Rules

- Copy templates; do not edit a template for a single project.
- Preserve the template's identity and version when using it as a source.
- Do not infer canonical authority from template presence.
- Do not use a legacy template as evidence that the current architecture still requires its structure.
- When a template conflicts with current canonical architecture, prefer the current authority and rebuild the template.
- Material template changes require downstream impact review.

# Validation

Before promoting a template, verify:

- purpose and scope;
- metadata relevance;
- authority relationship;
- naming and identity;
- references;
- compatibility with current architecture;
- compatibility with repository policy;
- downstream impact;
- external feedback requirements where applicable.

# Related Documents

- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Governance/GOV-010_GOVERNANCE_MODEL.md`
- `Governance/GOV-011_EXTERNAL_FEEDBACK_REPORT_STANDARD.md`
- `Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md`
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`
- `Repository/REP-001_MASTER_INDEX.md`

---

# Guiding Statement

**A template standardizes form; validation and authority determine whether the resulting artifact is correct.**

---

End of Document
