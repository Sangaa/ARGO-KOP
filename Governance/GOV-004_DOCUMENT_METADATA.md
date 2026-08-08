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

Every canonical Markdown document inside this repository MUST begin with the exact structural metadata block defined below.

```text
# [DOCUMENT_ID]

---

# [EXACT_DOCUMENT_TITLE]

---

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: [CORE-XXX / GOV-XXX / ARC-XXX / RUN-XXX / ENG-XXX / SRV-XXX / MOD-XXX / INT-XXX / INTF-XXX / PLG-XXX / QLT-XXX]
Version: [X.Y.Z]
Status: [Draft / Review / Approved]
Category: [Core / Governance / Architecture / Runtime / Engine / Service / Model / Intelligence / Interface / Plugin / Quality]
Canonical: [Yes / No]
Priority: [Critical / High / Medium / Low]
Last Audit Date: [MMM DD, YYYY]
```

---

# Validation Criteria

1. **ID Uniqueness:** No two active canonical documents shall share an identical logical Document ID.
2. **Identity Alignment:** The filename prefix and internal `Document ID` MUST represent the same logical identity.
3. **Path Alignment:** The active canonical path MUST match the allocation defined by `REP-001` and `REP-002`.
4. **Canonical Uniqueness:** A logical document may have only one active canonical artifact. Legacy evidence MUST be archived rather than retained as a competing active document.
5. **Temporal Alignment:** `Last Audit Date` MUST use the `MMM DD, YYYY` notation and reflect the latest verified repository audit.
6. **Completeness:** Canonical files missing the required metadata block or guiding statement MUST fail validation.
7. **Reference Integrity:** Related-document references MUST resolve to active repository paths or explicitly identified archived evidence.

---

# Related Documents

- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Services/SRV-005_VALIDATION_SERVICE.md`

---

# Guiding Statement

Structural standardization enables deterministic platform automation.

---

# Canonicalization Note

This canonical version supersedes the conflicting active artifacts previously stored at:

- `Governance/GOV-003_DOCUMENT_METADATA.md`
- `Standards/GOV-004_DOCUMENT_METADATA.md`

Those artifacts are preserved as archived evidence and are no longer active canonical documents.

---

End of Document
