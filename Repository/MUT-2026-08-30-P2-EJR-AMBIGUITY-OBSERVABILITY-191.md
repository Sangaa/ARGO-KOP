# MUT-2026-08-30-P2-EJR-AMBIGUITY-OBSERVABILITY-191

Date: 2026-08-30
Lease: `R71-20260830-P2-EJR-AMBIGUITY-OBSERVABILITY-191`
Execution role: HERMUZ
Entry head: `17d9b2273307c476c886ce630a2dfd46e1d4d937`
State: `OPEN / PREWRITE GATE ESTABLISHED`

## Purpose

Improve Priority-2 historical/provenance identity observability without changing any repository identity, authority, canonical status, pass/fail gate, or ambiguity disposition.

Current `internal_document_id_audit.py` already records `identity_source`, canonical/index/status/deferred-domain state internally, but `ambiguous_duplicate_ids` emits only paths. Lease 184 therefore had to reconstruct EJR ambiguity classes manually even though the scanner already possessed most classification inputs.

This lease adds a structured companion field for ambiguous groups so HERMUZ can inspect provenance-sensitive identity groups directly before any rename, migration, suppression, or closure decision.

## Proven gap

Current audit behavior:

- `identity_sources_by_path` exists globally;
- `ambiguous_duplicate_ids` contains only `{document_id: [paths...]}`;
- group-local artifact attributes are discarded from the ambiguity output;
- `identity_scope_reconciled` intentionally remains driven by the existing ambiguity set.

Observed prior evidence:

- Lease 184: 122 EJR ambiguity keys were stratified manually; 116 were H1-only and 6 contained exactly one explicit `Document ID` source plus H1 peers.
- Lease 188: active indexed canonical uniqueness is already `CLOSED / PASS`; historical/provenance traceability remains OPEN.
- Memory Engineering Journal status explicitly requires cross-reference and session-index/template alignment before integrity promotion.

## Allowed paths

- `Quality/Integration/internal_document_id_audit.py`
- `Quality/Integration/test_internal_document_id_audit.py`
- this Lease record
- `Repository/MUT-2026-08-30-P2-EJR-AMBIGUITY-OBSERVABILITY-191_MUTATION_MATRIX.md`
- bounded Room71 closure/checkpoint record after verification

## Forbidden semantic changes

- no EJR rename/delete/reassignment;
- no detector suppression or filtering of `ambiguous_duplicate_ids`;
- no change to `identity_scope_reconciled` semantics;
- no change to active duplicate, filename alignment, Governance collision, metadata-conflict or unreadable gates;
- no REP-001/REP-002/REP-014/REP-016 mutation;
- no canonical promotion;
- no Phase-1, Priority-2 global, Memory, or Connected-Baseline closure.

## Candidate contract

Add `ambiguous_duplicate_records` keyed by the same ambiguous document ID. Each member must expose only already-observed scanner facts sufficient for provenance triage:

- `path`
- `identity_source`
- `canonical`
- `indexed_active`
- `status`
- `deferred_domain`
- `filename_prefix`

The existing `ambiguous_duplicate_ids` output remains byte/semantic compatible in shape and meaning.

Add regressions proving:

1. a mixed explicit-metadata + H1 ambiguity group exposes both identity-source classes;
2. the legacy `ambiguous_duplicate_ids` field is unchanged;
3. observability does not make `identity_scope_reconciled` true while ambiguity remains.

## Learning applied

`OBSERVABILITY SHOULD EXPOSE CLASSIFICATION INPUTS BEFORE POLICY SUPPRESSES OR MUTATES IDENTITY.`

`ACTIVE-AUTHORITY PASS DOES NOT REMOVE THE NEED FOR PROVENANCE-GROUP DETAIL.`

`STRUCTURED EVIDENCE IS SAFER THAN REPEATED MANUAL RECONSTRUCTION.`
