# GOV-004

---

# DOCUMENT METADATA STANDARD

---

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: GOV-004
Version: 1.2.0
Status: Validated / Governance Re-audit
Category: Governance
Canonical: Yes
Priority: Critical
Last Audit Date: Aug 08, 2026

---

# Purpose

Defines the mandatory metadata and identity rules for canonical ARGO KOP documents.

# Mandatory Metadata

Canonical documents should identify, where applicable:

- Platform
- Document ID
- Version
- Status
- Category
- Canonical status
- Priority
- Last audit date

Additional ownership, authority and release metadata may be required by the applicable layer.

# Status Model

Status describes the current evidence-backed lifecycle state of the artifact.

Supported states include:

- Draft
- Review
- Validated
- Approved
- Released
- Deprecated
- Archived
- HOLD

`Approved` and `Released` are authority/lifecycle states and MUST NOT be used merely to mean that a file was inspected.

# Validation Criteria

1. ID uniqueness among active canonical artifacts.
2. Filename prefix and internal Document ID alignment.
3. Canonical path alignment with repository allocation.
4. One active canonical artifact per logical document identity.
5. Audit date reflects the latest verified audit of the stated scope.
6. Required metadata is present for the artifact's classification.
7. Related-document references resolve to active repository paths or explicitly identified archived evidence.
8. Status claims do not exceed the evidence supporting them.

# Identity Rule

Document identity is determined by the canonical Document ID and repository allocation. Filename similarity alone does not establish authority.

# Canonicalization

If competing active artifacts represent the same logical document, the conflict must enter `HOLD` until authority and canonical ownership are resolved. Legacy evidence should be archived through the applicable repository policy rather than silently deleted.

# Related Documents

- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Services/SRV-005_VALIDATION_SERVICE.md`

# Guiding Statement

Metadata establishes identity and evidence-backed status; it does not create authority by itself.

---

End of Document
