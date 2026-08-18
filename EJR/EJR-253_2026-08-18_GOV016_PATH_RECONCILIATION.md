# EJR-253 — 2026-08-18 GOV-016 Path Reconciliation

Date: 2026-08-18
Status: `CLOSED / EXECUTION-VERIFIED PARTIAL / RESUME-SAFE`
Authority: `GOV-013 + GOV-014 + GOV-015 + GOV-016 + CORE-012`

## Result

The GOV-016 path inconsistency was reconciled as a controlled path/reference transaction.

Canonical current path:

`Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`

Legacy/non-canonical uppercase path:

`GOVERNANCE/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md`

The canonical file content remains SHA:

`0501fdf85a632c19db7755c8dfe38c10cb21503a`

## Execution

Transaction: `MUT-2026-08-18-GOV016-PATH-001`

Mutation Matrix: `Repository/MUT-2026-08-18-GOV016-PATH-RECONCILIATION_MATRIX.md`

All four mutation rows reached `Applied=Y / Verified=Y`:

1. Canonical Governance copy created.
2. REP-001 current inventory reference reconciled.
3. README current references reconciled.
4. Non-canonical uppercase path removed.

## Verification

- Direct read of canonical `Governance/GOV-016...` = PASS.
- Direct read of old uppercase `GOVERNANCE/GOV-016...` = NOT FOUND after deletion.
- REP-001 read-back confirms canonical lowercase path.
- README was updated to canonical lowercase links.

## Search Evidence Learning

Repository search continued returning historical results containing the old uppercase path after deletion. This was classified as **search-index/history staleness**, not current repository evidence.

Learning:

> **Direct current-path verification outranks stale indexed search hits when resolving path existence.**

This reinforces the GOV-013 three-search rule and the requirement to distinguish repository evidence from search/index artifacts.

## Boundary

No GOV-016 content, governance semantics, Core authority, Runtime behavior, relationships or release state were changed.

## Pending

- Authoritative CI evidence for the latest REP-001 mutation remains unavailable through the current status endpoint.
- Real-Matrix corpus execution evidence remains pending.
- GEN-001 Candidate-001 remains `VALIDATED_GENERATED_KNOWLEDGE`; no promotion claimed.
- REL-009 callable-consumer evidence remains unresolved.

---

End of EJR-253
