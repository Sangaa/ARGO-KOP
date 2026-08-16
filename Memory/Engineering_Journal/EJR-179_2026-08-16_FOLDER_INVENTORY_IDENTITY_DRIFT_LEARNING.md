# EJR-179 — 2026-08-16 Folder Inventory Identity Drift Learning

## Scope

Repository: `Sangaa/ARGO-KOP`

Related checkpoint: `P246`

Affected layer: `Interfaces`

Affected artifact: `Interfaces/INTF-004_API.md`

Affected authority surface: `Interfaces/_FOLDER_STATUS.md`

## Observed Finding

The canonical API artifact had already been reconciled to `Document ID = INTF-004`, but the current folder inventory still declared the active identity as `INT-004`.

The artifact and its inventory therefore disagreed even though the artifact itself was correct.

## Classification

`IDENTITY DRIFT / ACTIVE INVENTORY METADATA MISMATCH`

This was not a historical reference problem. The incorrect value existed in a current authoritative inventory surface.

## Root Cause

Identity verification had been applied to the canonical artifact and filename, but not to the independent folder-inventory metadata that repeated the same identity.

## Corrective Action

Updated `Interfaces/_FOLDER_STATUS.md` using the governed existing-file Update path and current blob SHA.

The inventory now records:

`INTF-004_API.md | INTF-004`

The historical `INT-004` form remains mentioned only inside the reconciliation narrative as provenance.

## Verification

- Post-update Read-back: PASS.
- Runtime Prototype: PASS.
- Integration: PASS.
- Integrity: PASS after correcting the test boundary.
- Full-Stack Repository Audit: PASS on the corresponding verified current-main cycle.

## Failure Learning

The first regression assertion searched the entire folder-status document and incorrectly treated a historical reference in the reconciliation narrative as an active identity. That assertion was then narrowed to the authoritative inventory table.

This produced two durable learning rules:

1. **Identity reconciliation must validate every authoritative surface that declares an identity, not only the canonical artifact.**
2. **An integrity assertion must target the semantic authority boundary being tested; historical references inside explanatory evidence must not be confused with active metadata.**

## Governance Boundary

Correcting inventory metadata does not make the interface implementation operational and does not change transport or execution authority.

Folder status remains an evidence/control surface and does not by itself certify global repository integrity.

## Reusable Pattern

```text
Canonical Filename
      ↓
Document Metadata
      ↓
Folder Inventory
      ↓
Registry / Matrix
      ↓
Cross-Layer Authority
```

Identity is reconciled only when each applicable authoritative layer agrees or explicitly records a governed historical/noncanonical exception.

## Next Learning Application

Apply the same pattern to the next namespace with evidence of current-vs-historical identity overlap, while preserving the distinction between:

`active authority` → `historical provenance` → `reference mention`.

---

End of EJR-179
