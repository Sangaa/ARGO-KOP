# MUT-2026-08-30-P2-ID-AUDIT-IDENTITY-SOURCE-182

**Status:** PREWRITE / LEASE ACTIVE / HARD-HOLD ROOT-CAUSE REPAIR
**Baseline:** `main@0ce5d667ac9ff1f4af48281a7474041172d1b1b2`
**Parent evidence:** `Repository/MUT-2026-08-30-P2-ID-AUDIT-COVERAGE-179.md`, `Repository/MUT-2026-08-30-P2-ID-AUDIT-PARSER-180.md`, `Repository/MUT-2026-08-30-P2-ID-AUDIT-OBSERVABILITY-181.md`

## Exact failure evidence

Lease 181 preserved failure diagnostics without changing audit semantics. Exact-head Internal Document-ID Audit run `33298252068` remained failed and produced artifact `internal-document-id-audit-report` (`9728089302`). The deterministic report proves:

- `active_duplicate_pass = true`
- `filename_alignment_pass = true`
- `governance_heading_identity_collisions = {}`
- `unreadable = []`
- `explicit_heading_identity_conflicts` contains 18 entries and is the remaining current pytest gate failure family.

Direct inspection proves two semantic defects behind that list:

1. `Memory/Engineering_Journal/EJR-288_2026-08-21_HERMUZ_P6_SCOPE_BOUNDARY_REPAIR_STEP01.md` has document-level H1 `EJR-288`, but the scanner incorrectly captures `Document ID: P6-SCOPE-001` from the body where the journal describes a different artifact it created.
2. `Repository/REP-020_SESSION_DELTA_2026-08-14_P24.md` legitimately declares metadata `Document ID: REP-020-P24-DELTA` while its H1 is the parent/series label `REP-020`; `Services/ENG006_SRV009_PRODUCTION_ADAPTER_CONTRACT.md` similarly declares metadata `SRV-009-ADAPTER-001` while its H1 names the ENG-006 → SRV-009 relationship. H1 is not an independent metadata authority when an explicit Document ID exists.

`Governance/GOV-004_DOCUMENT_METADATA.md` states that document identity is determined by canonical Document ID plus repository allocation. `Governance/GOV-006_NAMING_CONVENTION_STANDARD.md` requires canonical filename identity to match internal Document ID. Neither authority requires a human/series H1 token to equal explicit metadata identity.

## Root cause

The detector combines two incompatible assumptions:

- it searches the entire document for any `Document ID` occurrence, including body references to other artifacts;
- although its own contract says explicit `Document ID` is primary and first-H1 is only a fallback, it then treats any structurally-shaped H1 that differs from explicit metadata as a conflict.

This grants body references and fallback headings identity authority they do not possess.

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
- **C2 semantic collision:** PASS — only identity-source detection semantics are changed; no repository identity owner is rewritten.
- **C3 authority collision:** PASS — repair follows current GOV-004/GOV-006 identity authority rather than modifying it.
- **C4 promotion collision:** PASS — green audit alone will not promote repository-wide identity closure.
- **C5 evidence collision:** PASS — artifact-backed deterministic report plus three direct representative reads establish the defect.
- **C6 handoff collision:** PASS — 179-181 remain bounded; 182 resolves the newly exposed root cause only.

## Learning candidate

`A REFERENCE TO AN ID IS NOT THE IDENTITY OF THE REFERENCING DOCUMENT.`

`PRIMARY/FALLBACK DETECTION MUST NOT TURN THE FALLBACK INTO A SECOND AUTHORITY.`
