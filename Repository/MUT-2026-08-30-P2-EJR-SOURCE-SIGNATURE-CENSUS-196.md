# P2 EJR AMBIGUITY SOURCE-SIGNATURE CENSUS — LEASE 196

Transaction ID: `MUT-2026-08-30-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
Lease: `R71-20260830-P2-EJR-SOURCE-SIGNATURE-CENSUS-196`
Protocol: HERMUZ / GOV-014
Status: `OPEN / PREWRITE / FUNCTIONAL MUTATION NOT YET APPLIED`
Entry head: `afe52f71cef0041e7f58218d6846f9182c868f83`

## Bounded purpose

Expose deterministic source-signature census data for current ambiguous duplicate identity groups so Priority-2 analysis can distinguish metadata-only, first-H1-only, and mixed-source ambiguity before any identity migration or ownership decision.

Lease 192 classified the six EJR ambiguity groups containing at least one explicit `Document ID` claim. Lease 191 already exposed member-level `ambiguous_duplicate_records`. The current gap is a group-level census suitable for bounded prioritization.

## Design refinement before functional write

The existing internal-ID gate already exposes every required member attribute. Therefore Lease 196 MUST NOT modify `Quality/Integration/internal_document_id_audit.py` merely to aggregate its output. A companion evidence analyzer is the lower-risk construction:

`internal_document_id_audit.scan() → ejr_ambiguity_source_signature_census.summarize() → evidence JSON`

This preserves gate semantics and keeps census policy outside identity discovery.

## Authorized functional scope

1. `Quality/Integration/ejr_ambiguity_source_signature_census.py`
2. `Quality/Integration/test_ejr_ambiguity_source_signature_census.py`
3. `Repository/MUT-2026-08-30-P2-EJR-SOURCE-SIGNATURE-CENSUS-196_MUTATION_MATRIX.md`

## Required behavior

- consume existing `ambiguous_duplicate_records` without changing audit membership;
- deterministic signature per ambiguous group from member `identity_source` values;
- signatures: `DOCUMENT_ID_FIELD_ONLY`, `FIRST_H1_FALLBACK_ONLY`, `MIXED`, with unknown sources preserved fail-visible as `OTHER:<sorted-sources>`;
- expose counts by source signature and group cardinality;
- expose EJR-only group IDs and counts while leaving scanner grammar generic;
- executable CLI emits JSON from the current repository scan;
- tests prove metadata-only, H1-only, mixed, unknown-source visibility, cardinality counting, and source-report immutability.

## Forbidden scope

- no EJR rename, delete, reassignment, migration, normalization, suppression, or replacement allocation;
- no modification to `internal_document_id_audit.py` or its tests;
- no change to active duplicate pass semantics or `identity_scope_reconciled` semantics;
- no REP-012, REP-016, REP-020, or authority-index mutation;
- no Priority-2 or global closure.

## Closure conditions

- Mutation Matrix exists before functional write;
- functional compare contains exactly the three authorized paths;
- current ambiguity membership is not filtered or reduced at the source gate;
- companion tests and exact-head workflows pass;
- current EJR census is recorded as evidence only;
- Room71 checkpoint is persisted `CLOSED / RESUME-SAFE` or `HOLD / RESUME-SAFE` according to evidence.
