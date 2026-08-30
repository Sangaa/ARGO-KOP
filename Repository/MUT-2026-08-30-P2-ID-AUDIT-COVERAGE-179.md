# MUT-2026-08-30-P2-ID-AUDIT-COVERAGE-179

Date: 2026-08-30
Lease: `R71-20260830-P2-ID-AUDIT-COVERAGE-179`
Execution role: HERMUZ
Entry baseline: `main@d4a6dd1b475602d5674fca838dd185c5c25a6931`
Status: `CLOSED / EXECUTION-VERIFIED / COVERAGE EXPANDED / PRIORITY-2 OPEN`

## Gap proved

Priority 2 is defined as an exhaustive repository-wide duplicate-ID audit, but the prior `Quality/Integration/internal_document_id_audit.py` recognized explicit `Document ID` values only when their prefix was present in a fixed namespace list.

That list omitted directly verified repository families including at least:
- `COG-*` (Cognition);
- `DEC-*` (Decision);
- `REL-*` (Release document IDs);
- root explicit identities such as `BOOTSTRAP-001` and `PROJECT_STATUS`.

Therefore a green result from the prior implementation could not support an exhaustive repository-wide internal Document-ID claim.

Classification:
`AUDIT COVERAGE DEFECT / FALSE-NEGATIVE RISK`.

## Prior learning applied

- Tool-limited evidence constrains claim scope.
- A successful audit is not proof beyond the exact scope the audit can observe.
- Identifier token equality does not imply collision across namespace/artifact class.
- Negative/clean findings require evidence that the detector actually covers the claimed population.

## Repair chain

Lease 179 expanded discovery beyond the fixed namespace allowlist and added path→identity evidence plus current-tree regressions for previously invisible identity families.

The stronger detector then exposed two additional tooling defects rather than being rolled back:

- Lease 180 constrained generic first-H1 parsing so ordinary human titles are not identities.
- Lease 181 made failed audit diagnostics persist as an artifact.
- Lease 182 corrected identity-source precedence so body references are not document identity and H1 remains fallback-only when qualified metadata exists.

This chain preserves the original 179 purpose: broader observation without manufacturing authority or hiding newly exposed findings.

## Final verification

Final repair head: `e04b073f268aa1291bbb747429d92ac69d83e9ec`.

Exact-head checks:

- Internal Document-ID Audit — `33298557071` — `SUCCESS`
- Full-Stack Repository Audit — `33298557075` — `SUCCESS`
- ARGO Runtime Prototype and Integration Tests — `33298557080` — `SUCCESS`
- M2 Multi-Channel Proposal Training — `33298557081` — `SUCCESS`

Internal-ID artifact `9728177701` proves the expanded detector observed:

- `tracked_files_scanned = 2052`
- `document_id_records = 1100`
- `active_duplicate_pass = true`
- `filename_alignment_pass = true`
- `metadata_document_id_conflicts = []`
- `governance_heading_identity_collisions = {}`
- `unreadable = []`

It also proves Priority 2 is not globally reconciled:

- `identity_scope_reconciled = false`
- `canonical_unindexed_records = 15`
- `ambiguous_duplicate_ids = 145`

Accordingly, Lease 179 closes as a tooling-coverage repair only. It does **not** close repository-wide Priority 2 and does not authorize bulk identity mutation.

## C1–C6 closure

- C1 PASS — unique lease record retained.
- C2 PASS — audit observability/identity detection only; no identity owner rewritten.
- C3 PASS — no release/baseline mutation.
- C4 PASS — tool output did not manufacture identity authority.
- C5 PASS — expanded artifact demonstrates the claimed detector population and remaining unresolved findings.
- C6 PASS — Priority 2 remains open exactly because the stronger detector now exposes unresolved identity scope.

## Learning

`AUDIT GREEN != DOMAIN COVERAGE.`

`DETECTOR EXPANSION FAILURE MAY BE NEW EVIDENCE, NOT REGRESSION.`

`A COVERAGE REPAIR IS SUCCESSFUL WHEN IT MAKES PREVIOUSLY INVISIBLE UNCERTAINTY VISIBLE, EVEN IF THAT PREVENTS THE HIGHER-LEVEL DOMAIN FROM CLOSING.`

Final state:
`P2_ID_AUDIT_COVERAGE_179 = CLOSED / EXECUTION-VERIFIED / PRIORITY-2 OPEN`.
