# REP-001 MUTATION MATRIX — CORE/GOVERNANCE INVENTORY RECONCILIATION

Transaction ID: `MUT-2026-08-18-REP001-CORE-GOV-001`
Source Blob SHA: `783872b7cb91efeab2e4dac22dda7219d600454b`
Target: `Repository/REP-001_MASTER_INDEX.md`
Protocol: `GOV-014 v1.0.1`

## Intended Changes

| Change ID | Section ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|:---:|:---:|
| REP001-COREGOV-001 | REP001-SEC-03 | Core Layer | UPDATE | Add `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md` immediately after `Core/CORE-011_PLATFORM_CHARTER.md` | N | N |
| REP001-COREGOV-002 | REP001-SEC-05 | Governance Layer | UPDATE | Add `GOVERNANCE/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md` immediately after `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md` | N | N |

## KEEP Requirement

Every other section and content unit in REP-001 is `KEEP` and must remain content-equivalent to source blob `783872b7cb91efeab2e4dac22dda7219d600454b`.

Required preservation conditions:

- `SECTION_COUNT_UNCHANGED = Y`
- `SECTION_ORDER_UNCHANGED = Y`
- `KEEP_MISMATCHES = 0`
- `UNEXPECTED_ADDITIONS = 0`
- `UNEXPECTED_DELETIONS = 0`
- `IDENTITY_PATH_MISMATCHES = 0`
- `AUTHORITY_EVIDENCE_GAPS = 0`
- `EXPECTED_CHANGES_PRESENT = 2`

## Authority Evidence

- `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md` — `Document ID CORE-012`, `Canonical Yes`, `Status Canonical / Core / Mandatory`.
- `GOVERNANCE/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md` — `Status ACTIVE / MANDATORY`.

## Boundary

This transaction authorizes inventory synchronization only. It does not modify CORE-012, GOV-016, Runtime, relationships, semantic authority, or release state.

## Post-Commit Requirement

After commit, read REP-001 from the new HEAD using the resulting blob SHA and set both rows to `Applied=Y / Verified=Y` only after full-content reconciliation.

---

End of Mutation Matrix
