# MUT-2026-08-30-P2-EJR-AMBIGUITY-OBSERVABILITY-191

Date: 2026-08-30
Lease: `R71-20260830-P2-EJR-AMBIGUITY-OBSERVABILITY-191`
Execution role: HERMUZ
Entry head: `17d9b2273307c476c886ce630a2dfd46e1d4d937`
Prewrite head: `774d9b83c9d6b6ccc3ada51fde3ff4193d702acc`
Functional commit: `044c5c41c31f98d944c663b33cc73d88784a71d6`
Status: `CLOSED / EXECUTION-VERIFIED / OBSERVABILITY ONLY / P2 REMAINS OPEN`

## Purpose and result

Priority-2 historical/provenance identity analysis proved that active indexed canonical identity uniqueness was already closed by Lease 188, while EJR traceability reuse remained open. Lease 184 had manually stratified 122 EJR ambiguity keys and found that most were H1-derived, with a small mixed population containing explicit `Document ID` owners plus H1 peers.

The current detector already held the facts needed for this distinction inside each `ArtifactRecord`, but `ambiguous_duplicate_ids` emitted paths only. Lease 191 closed that observability gap without changing identity ownership, ambiguity membership, policy or pass/fail semantics.

The scanner now emits a companion field:

`ambiguous_duplicate_records`

For every existing ambiguous ID member it exposes:

- `path`
- `identity_source`
- `canonical`
- `indexed_active`
- `status`
- `deferred_domain`
- `filename_prefix`

The legacy `ambiguous_duplicate_ids` field remains unchanged in shape and membership and continues to drive `identity_scope_reconciled` exactly as before.

## Exact functional change set

Comparison:

`774d9b83c9d6b6ccc3ada51fde3ff4193d702acc → 044c5c41c31f98d944c663b33cc73d88784a71d6`

Exactly three files changed:

1. `Quality/Integration/internal_document_id_audit.py` — +16 / -0.
2. `Quality/Integration/test_internal_document_id_audit.py` — +37 / -0.
3. `Repository/MUT-2026-08-30-P2-EJR-AMBIGUITY-OBSERVABILITY-191_MUTATION_MATRIX.md` — transaction update only.

Unexpected paths: `0`.

Exact blobs:

- scanner source `482dac833210131c609c0d896fc9e8e4a78c8718` → `50454dd20a2a5691f788c4580cce234dac13f0c1`;
- tests source `bb770b98caf215add1be4ecd51bb2ae5d23dcf9d` → `25b22f7d5794d8720ad31496e5bf9985d623df12`.

Pre-bind diff inspection confirmed no deletions and only the intended companion-field logic plus one bounded regression test.

## Regression contract verified

The new regression proves a mixed synthetic EJR group with:

- one `DOCUMENT_ID_FIELD` member;
- one `FIRST_H1_FALLBACK` member.

It simultaneously proves:

- the existing `ambiguous_duplicate_ids` paths remain unchanged;
- the companion output exposes the two identity-source classes;
- `identity_scope_reconciled` remains false while ambiguity exists.

No EJR owner was renamed, deleted, reassigned, indexed, canonicalized or suppressed.

## Exact-head CI

Functional SHA `044c5c41c31f98d944c663b33cc73d88784a71d6`:

- Internal Document-ID Audit — run `33309485540` — SUCCESS;
- Full-Stack Repository Audit — run `33309485534` — SUCCESS;
- M2 Multi-Channel Proposal Training — run `33309485537` — SUCCESS;
- Real Mutation Matrix Regression — run `33309485557` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests — run `33309485602` — SUCCESS.

Internal-ID artifact:

- artifact ID `9731526902`;
- name `internal-document-id-audit-report`;
- digest `sha256:92e07c6b47bf17d97f76e8a2557acd039101a5fddde366c18f452202c38ae67d`;
- head SHA `044c5c41c31f98d944c663b33cc73d88784a71d6`.

## Construction incidents and learning

A local clone attempt failed because the execution runtime could not resolve `github.com`. No repository mutation depended on that copy.

A first manual candidate was rejected before Git-object binding when it was noticed that source comments/docstrings would not be preserved. The actual candidate was rebuilt from complete GitHub blob content; its reconstructed source identity was independently checked against the exact original Git blob SHA before transformation.

Reusable learning:

`CANDIDATE CONSTRUCTION CONVENIENCE MUST NOT OVERRIDE ZERO-TOUCH SOURCE PRESERVATION.`

`OBSERVABILITY SHOULD EXPOSE CLASSIFICATION INPUTS BEFORE POLICY SUPPRESSES OR MUTATES IDENTITY.`

`STRUCTURED EVIDENCE IS SAFER THAN REPEATED MANUAL RECONSTRUCTION.`

## Closed scope / preserved holds

`P2_EJR_AMBIGUITY_OBSERVABILITY_191 = CLOSED / EXECUTION-VERIFIED`.

Preserved:

- Priority 2 historical/provenance identity scope = OPEN;
- active indexed canonical identity uniqueness = CLOSED / PASS from Lease 188;
- no EJR migration/rename decision made;
- Phase 1 overall = OPEN;
- Global Connected Baseline = OPEN;
- Provider Authentication and existing global/domain holds unchanged;
- Global `BOOTED / INTEGRITY PASS` = NOT CLAIMED.

## Next legal action

Use the new exact-head structured ambiguity evidence to perform an **EJR provenance group census**, starting with EJR groups containing at least one `DOCUMENT_ID_FIELD` member. For each selected group:

`IDENTITY SOURCE → PATH/DATE/CONTENT → HISTORY → REFERENCES → CONSUMERS → OWNER/SHADOW/REUSE DISPOSITION`

No rename, delete, suppression or detector exemption is authorized until that provenance/consumer review proves it safe.
