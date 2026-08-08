# REPOSITORY POLICY

---

Document ID
GOV-009
Version
1.2.0
Status
Validated / Governance Re-audit
Owner
ARGO Governance
Category
Governance
Canonical
Yes
Last Audit
2026-08-08

---

# Repository Principles

The repository is the Single Source of Truth for persisted engineering state.

Conversation memory provides task intent and working context but never overrides repository content.

Knowledge duplication is avoided; references are preferred where they preserve meaning and authority.

Historical engineering state remains recoverable through repository history and approved archival mechanisms.

No working session that materially changes platform knowledge should end without recording the validated outcome through the applicable repository mechanism.

# Repository Engineering

Repository engineering follows:

Review

↓

Evidence / Scope

↓

Decision

↓

Authorized Change

↓

Validation

↓

Trace / Commit

# Change Rules

- Complete-file replacement is preferred when safe and practical.
- Targeted updates are permitted when their scope and resulting integrity are validated.
- Unrelated content must be preserved.
- Deletion of canonical history is not permitted without an approved archival/migration decision.
- Repository state must be synchronized and verified before issuing engineering decisions.
- Failed validation prevents acceptance of the change.

# Repository Reality

Current repository evidence overrides unsupported assumptions and stale status claims.

A status document is evidence of a previous or current assessment, not authority to ignore contradictory repository evidence.

# Traceability

Material changes should retain:

- change reason;
- affected artifact;
- validation result;
- commit/revision when available;
- relevant decision or authority reference.

# Related Documents

- `Governance/GOV-001_GOVERNANCE_FRAMEWORK.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

---

End of Document
