# MUTATION MATRIX — P2 EJR AMBIGUITY OBSERVABILITY 191

Transaction ID: `MUT-2026-08-30-P2-EJR-AMBIGUITY-OBSERVABILITY-191`
Protocol: GOV-014 v1.0.1
Lease: `R71-20260830-P2-EJR-AMBIGUITY-OBSERVABILITY-191`
State: `CLOSED / VERIFIED / EXECUTION COMPLETE`
Entry head: `17d9b2273307c476c886ce630a2dfd46e1d4d937`
Prewrite head / functional parent: `774d9b83c9d6b6ccc3ada51fde3ff4193d702acc`
Functional commit: `044c5c41c31f98d944c663b33cc73d88784a71d6`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 191-001 | `Quality/Integration/internal_document_id_audit.py` | UPDATE | add structured `ambiguous_duplicate_records` companion output from existing ArtifactRecord facts; preserve all existing ambiguity/pass-fail semantics | Y | Y |
| 191-002 | `Quality/Integration/test_internal_document_id_audit.py` | UPDATE | regress mixed explicit/H1 ambiguity observability while proving legacy ambiguity output and identity hold are unchanged | Y | Y |
| 191-003 | this Matrix | UPDATE IN SAME FUNCTIONAL CHANGE SET | bind exact functional commit and verification evidence | Y | Y |

## KEEP verification

Exact functional compare showed:

- scanner: +16 / -0;
- tests: +37 / -0;
- Matrix: transaction state/evidence only;
- unexpected paths: 0.

Pre-bind commit-diff inspection confirmed all original scanner/test content remained and the only functional additions were the companion ambiguity records plus one regression.

Preserved semantics:

- `ambiguous_duplicate_ids` construction and membership;
- `identity_scope_reconciled` expression;
- active canonical duplicate logic;
- filename alignment;
- metadata preamble/Document ID parsing;
- Governance heading collision behavior;
- deferred-domain and legacy classification behavior.

## Exact identities

- scanner source blob: `482dac833210131c609c0d896fc9e8e4a78c8718`.
- scanner resulting blob: `50454dd20a2a5691f788c4580cce234dac13f0c1`.
- test source blob: `bb770b98caf215add1be4ecd51bb2ae5d23dcf9d`.
- test resulting blob: `25b22f7d5794d8720ad31496e5bf9985d623df12`.

Post-write read-back matched both resulting blobs.

## Exact-head CI verification

Functional SHA: `044c5c41c31f98d944c663b33cc73d88784a71d6`.

- Internal Document-ID Audit `33309485540` — SUCCESS.
- Full-Stack Repository Audit `33309485534` — SUCCESS.
- M2 Multi-Channel Proposal Training `33309485537` — SUCCESS.
- Real Mutation Matrix Regression `33309485557` — SUCCESS.
- ARGO Runtime Prototype and Integration Tests `33309485602` — SUCCESS.

Internal-ID artifact:

`9731526902 / internal-document-id-audit-report / sha256:92e07c6b47bf17d97f76e8a2557acd039101a5fddde366c18f452202c38ae67d / head=044c5c41c31f98d944c663b33cc73d88784a71d6`.

## Construction incident

A local clone attempt failed due runtime DNS. It was discarded as a construction path; GitHub remained the authority.

A first manually reconstructed candidate was rejected before any repository write when KEEP-preservation risk was detected. The final candidate was rebuilt from complete GitHub blob content and source blob identity was independently reproduced before transformation.

Learning:

`CANDIDATE CONSTRUCTION CONVENIENCE MUST NOT OVERRIDE ZERO-TOUCH SOURCE PRESERVATION.`

`OBSERVABILITY SHOULD EXPOSE CLASSIFICATION INPUTS BEFORE POLICY SUPPRESSES OR MUTATES IDENTITY.`

## Closure

`P2_EJR_AMBIGUITY_OBSERVABILITY_191 = CLOSED / EXECUTION-VERIFIED`.

Priority 2 remains OPEN for historical/provenance traceability. No identity mutation or global promotion is implied.
