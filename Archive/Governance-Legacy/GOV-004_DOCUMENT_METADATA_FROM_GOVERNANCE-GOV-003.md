# ARCHIVED GOVERNANCE ARTIFACT

---

Original Path: `Governance/GOV-003_DOCUMENT_METADATA.md`
Logical Document ID: `GOV-004`
Original Version: `1.1.0`
Archive Date: Aug 08, 2026
Reason: Identity/path drift during Governance canonicalization
Status: Archived Evidence
Canonical: No

---

# Original Content

# GOV-004

---

# DOCUMENT METADATA STANDARD

---

Platform: ARGO KOP (Knowledge Operating Platform) 
Document ID: GOV-004 
Version: 1.1.0 
Status: Approved 
Category: Governance / Standards 
Canonical: Yes 
Priority: Critical 
Last Audit Date: Aug 08, 2026 

---

# Purpose

This standard defines the mandatory metadata headers and classification blocks required for every canonical document within ARGO KOP.

---

# Mandatory Header Format

Every markdown file inside this repository MUST begin with the exact structural block below:

```text
# [DOCUMENT_ID]

---

# [EXACT_DOCUMENT_TITLE]

---

Platform: ARGO KOP (Knowledge Operating Platform) 
Document ID: [GOV-XXX / RUN-XXX / CORE-XXX] 
Version: [X.Y.Z] 
Status: [Draft / Review / Approved] 
Category: [Core / Governance / Architecture / Runtime] 
Canonical: [Yes / No] 
Priority: [Critical / High / Low] 
Last Audit Date: [MMM DD, YYYY] 
```

Validation Criteria
ID Uniqueness: No two documents shall share an identical code identifier.345
Temporal Alignment: The Last Audit Date MUST be synchronized using the "MMM DD, YYYY" notation format.
Completeness: Files missing the canonical status block or guiding statement shall be automatically rejected by the validation service (SRV-005).67
Related Documents
Governance/GOV-001_GOVERNANCE_FRAMEWORK.md
Models/MOD-003_DOCUMENT_MODEL.md
Services/SRV-005_VALIDATION_SERVICE.md
Guiding Statement
Structural standardization enables deterministic platform automation.8
End of Document
