# MUT-2026-08-30-P2-ID-AUDIT-IDENTITY-SOURCE-182

**Status:** CLOSED / EXECUTION-VERIFIED / ROOT-CAUSE REPAIRED / P2 REMAINS OPEN
**Baseline:** `main@0ce5d667ac9ff1f4af48281a7474041172d1b1b2`
**Repair commit:** `e04b073f268aa1291bbb747429d92ac69d83e9ec`
**Parent evidence:** `Repository/MUT-2026-08-30-P2-ID-AUDIT-COVERAGE-179.md`, `Repository/MUT-2026-08-30-P2-ID-AUDIT-PARSER-180.md`, `Repository/MUT-2026-08-30-P2-ID-AUDIT-OBSERVABILITY-181.md`

## Exact failure evidence

Lease 181 preserved failure diagnostics without changing audit semantics. Exact-head Internal Document-ID Audit run `33298252068` remained failed and produced artifact `internal-document-id-audit-report` (`9728089302`). The deterministic report proved:

- `active_duplicate_pass = true`
- `filename_alignment_pass = true`
- `governance_heading_identity_collisions = {}`
- `unreadable = []`
- `explicit_heading_identity_conflicts` contained 18 entries and was the remaining pytest gate failure family.

Direct inspection proved two semantic defects behind that list:

1. `Memory/Engineering_Journal/EJR-288_2026-08-21_HERMUZ_P6_SCOPE_BOUNDARY_REPAIR_STEP01.md` has document-level H1 `EJR-288`, but the scanner incorrectly captured `Document ID: P6-SCOPE-001` from the body where the journal describes a different artifact it created.
2. `Repository/REP-020_SESSION_DELTA_2026-08-14_P24.md` legitimately declares metadata `Document ID: REP-020-P24-DELTA` while its H1 is the parent/series label `REP-020`; `Services/ENG006_SRV009_PRODUCTION_ADAPTER_CONTRACT.md` similarly declares metadata `SRV-009-ADAPTER-001` while its H1 names the ENG-006 → SRV-009 relationship. H1 is not an independent metadata authority when an explicit Document ID exists.

`Governance/GOV-004_DOCUMENT_METADATA.md` states that document identity is determined by canonical Document ID plus repository allocation. `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md` requires canonical filename identity to match internal Document ID. Neither authority requires a human/series H1 token to equal explicit metadata identity.

## Root cause

The detector combined two incompatible assumptions:

- it searched the entire document for any `Document ID` occurrence, including body references to other artifacts;
- although its own contract said explicit `Document ID` is primary and first-H1 is only a fallback, it then treated any structurally-shaped H1 that differed from explicit metadata as a conflict.

This granted body references and fallback headings identity authority they do not possess.

## Allowed paths

- `Quality/Integration/internal_document_id_audit.py`
- `Quality/Integration/test_internal_document_id_audit.py`
- `Repository/MUT-2026-08-30-P2-ID-AUDIT-IDENTITY-SOURCE-182.md`
- bounded Repository closure/learning records for 179-182 after verification

## Forbidden paths

- all repository document identity owners outside the audit/test/evidence files above
- `.github/workflows/**` under this lease
- `Core/**`
- `Governance/**`
- `Runtime/**`
- `Engine/**`
- `Services/**`
- `Interfaces/**`
- `Knowledge/**`
- `Release/**`
- `Repository/REP-001_*`
- `Repository/REP-002_*`
- `Repository/REP-014_*`
- `Repository/REP-016_*`
- `PROJECT_STATUS.md`
- `Repository/ROOM071_CURRENT_STATE.json`
- branch deletion or force ref mutation

## Minimal repair contract

1. Explicit document identity must come from a metadata-like context, not an arbitrary body mention.
2. A qualified explicit metadata Document ID remains the primary identity source.
3. First structural H1 is used only as fallback when qualified explicit metadata is absent.
4. Do not require H1 equality when explicit metadata exists.
5. Detect a real intra-document metadata conflict when multiple qualified metadata Document IDs disagree.
6. Preserve namespace-independent discovery and the 180 human-title regressions.
7. Add regression proving a body mention such as `Document ID: P6-SCOPE-001` does not override an `EJR-288` document identity.
8. Add regression proving an explicit child/contract ID may coexist with a structural series/relationship H1 without becoming a false conflict.
9. Keep current active-duplicate, filename-alignment and Governance collision gates unchanged.
10. Verify exact-head Internal-ID, Full-Stack, M2 and relevant Runtime/Integration checks before closure.

## C1-C6 collision gate

- **C1 path collision:** PASS — evidence path is unique.
- **C2 semantic collision:** PASS — only identity-source detection semantics were changed; no repository identity owner was rewritten.
- **C3 authority collision:** PASS — repair follows current GOV-004/GOV-006 identity authority rather than modifying it.
- **C4 promotion collision:** PASS — green audit did not promote repository-wide identity closure.
- **C5 evidence collision:** PASS — artifact-backed deterministic report plus representative direct reads established the defect.
- **C6 handoff collision:** PASS — 179-181 remain bounded and are closed only as repair-chain work; Priority 2 remains independently open.

## Verification and closure evidence

Exact-head repair commit `e04b073f268aa1291bbb747429d92ac69d83e9ec` changed exactly:

- `Quality/Integration/internal_document_id_audit.py`
- `Quality/Integration/test_internal_document_id_audit.py`

Required checks on that same head completed successfully:

- Internal Document-ID Audit — run `33298557071` — `SUCCESS`
- Full-Stack Repository Audit — run `33298557075` — `SUCCESS`
- ARGO Runtime Prototype and Integration Tests — run `33298557080` — `SUCCESS`
- M2 Multi-Channel Proposal Training — run `33298557081` — `SUCCESS`

The successful Internal-ID run produced deterministic artifact `internal-document-id-audit-report` (`9728177701`). Its current-tree evidence proves:

- `tracked_files_scanned = 2052`
- `document_id_records = 1100`
- `active_duplicate_pass = true`
- `filename_alignment_pass = true`
- `metadata_document_id_conflicts = []`
- `governance_heading_identity_collisions = {}`
- `unreadable = []`
- `identity_scope_reconciled = false`
- `canonical_unindexed_records = 15`
- `ambiguous_duplicate_ids = 145`

Therefore the parser/root-cause repair is closed and execution-verified, but Priority 2 repository-wide identity reconciliation is explicitly **not closed**. The newly visible ambiguous/unindexed population is next-stage evidence, not a regression and not permission for bulk renaming.

## Learning

`A REFERENCE TO AN ID IS NOT THE IDENTITY OF THE REFERENCING DOCUMENT.`

`PRIMARY/FALLBACK DETECTION MUST NOT TURN THE FALLBACK INTO A SECOND AUTHORITY.`

`A GREEN AUDIT GATE MAY VERIFY THE DETECTOR CONTRACT WHILE THE DETECTOR REPORT LEGITIMATELY KEEPS THE DOMAIN RECONCILIATION OPEN.`

Final lease state:
`P2_ID_AUDIT_IDENTITY_SOURCE_182 = CLOSED / EXECUTION-VERIFIED / P2 OPEN`.
