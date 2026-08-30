# MUT-2026-08-30-P2-ACTIVE-IDENTITY-SUBGATE-188

Date: 2026-08-30
Lease: `R71-20260830-P2-ACTIVE-IDENTITY-SUBGATE-188`
Execution role: HERMUZ
Entry evidence head: `91c259c04a22f72109fdd9dab75c30be6eebc22b`
Status: `CLOSED / EVIDENCE-VERIFIED / BOUNDED ACTIVE-IDENTITY SUBGATE`

## Purpose

Separate two questions that the raw Internal Document-ID report intentionally keeps distinct but that can be operationally confused:

1. Are current active/indexed canonical identity owners colliding?
2. Is every historical, non-authoritative, unindexed, deferred, series, and provenance identity occurrence globally reconciled?

The first question is an active-authority safety gate. The second is the broader Priority-2 traceability/reconciliation scope.

This lease closes only the first where exact current evidence supports it.

## Exact audit evidence

Internal Document-ID run:
`33303432377`

Artifact:
`internal-document-id-audit-report` / ID `9729674196`

Artifact digest:
`sha256:8ec9c359cd14c2839c85fcccfdca6df943e21fd4e87376ccf655daf9100a8b40`

Bound head:
`91c259c04a22f72109fdd9dab75c30be6eebc22b`

Observed report fields:

- `tracked_files_scanned = 2066`
- `document_id_records = 1099`
- `active_indexed_canonical_records = 111`
- `active_duplicate_pass = true`
- `duplicate_active_ids = {}`
- `filename_alignment_pass = true`
- `filename_internal_id_mismatches = []`
- `metadata_document_id_conflicts = []`
- `governance_heading_identity_collisions = {}`
- `unreadable = []`
- `shadowed_legacy_ids = 15` identity groups
- `deferred_domain_records = 42`
- `canonical_unindexed_records = 12`
- `ambiguous_duplicate_ids = 144`
- `identity_scope_reconciled = false`

## Semantic reconciliation with prior leases

### Canonical-unindexed population

Lease 185 classified all 15 prior canonical-unindexed paths. Lease 186/187 execution-verified closure removed the three genuine discoverability gaps from the report:

- `Core/ARGO_KERNEL.md`
- `Core/Core.md`
- `Quality/QLT-001_QUALITY_ASSURANCE.md`

The remaining 12 are exactly the already-classified non-admitted set:

- `Architecture/README.md`
- `Knowledge/KNW-001_KNOWLEDGE_MODEL.md` through `KNW-010_KNOWLEDGE_MAINTENANCE.md`
- `Templates/README.md`

Their continued raw presence does not authorize active-index promotion. Knowledge remains under canonical-validation hold; Architecture README and Templates README remain navigation/reconstruction surfaces under their current bounded dispositions.

### Ambiguous duplicate population

Lease 183 classified the 23 non-EJR ambiguity keys by owner/artifact class without proving an active-authority duplicate.

Lease 184 stratified the EJR population as historical/provenance traceability reuse and repaired the stale EJR-013 conflict evidence. The exact report now shows EJR ambiguity reduced from 122 to 121 and total ambiguity from 145 to 144.

These raw ambiguity records remain material for provenance and traceability. They are not silently erased and are not reclassified as globally reconciled.

## Decision

Current evidence supports:

`ACTIVE_INDEXED_CANONICAL_IDENTITY_UNIQUENESS = CLOSED / PASS / EXACT-HEAD EVIDENCE`.

Specifically, no current active/indexed canonical duplicate ID is reported by the namespace-independent detector, and no filename/internal-ID, metadata-ID, Governance heading, or unreadable-file blocker exists in the inspected report.

Current evidence does NOT support:

`REPOSITORY_WIDE_IDENTITY_SCOPE = CLOSED`.

The report explicitly remains:

`identity_scope_reconciled = false`.

## Boundary

This lease does not:

- close Priority 2 globally;
- promote any remaining canonical-unindexed path;
- erase EJR or other historical ID reuse;
- certify deferred domains;
- close Memory traceability;
- mutate REP-011, REP-014, or REP-016;
- claim Global Connected Baseline PASS.

## Learning

`ACTIVE AUTHORITY IDENTITY UNIQUENESS != GLOBAL HISTORICAL IDENTITY RECONCILIATION.`

`A NON-AUTHORITATIVE TRACEABILITY COLLISION CAN REMAIN OPEN WITHOUT INVALIDATING A SEPARATELY PROVED ACTIVE-CANONICAL UNIQUENESS SUBGATE.`

`RAW AUDIT AMBIGUITY SHOULD BE PARTITIONED BY AUTHORITY CLASS BEFORE IT IS USED AS A STOP/GO SIGNAL.`

## Closure

`P2_ACTIVE_IDENTITY_SUBGATE_188 = CLOSED / EVIDENCE-VERIFIED / BOUNDED`.

`P2_HISTORICAL_AND_PROVENANCE_TRACEABILITY = OPEN`.

`PRIORITY_2_GLOBAL_SCOPE = OPEN`.
