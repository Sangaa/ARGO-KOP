# Priority 12 — Models Relationship / Content Reconciliation — Transaction B — Unit 8 Mutation Matrix

Parent Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`

Unit: `8 — MOD-003 Document Model boundary / consumer reconciliation`

Priority: `12 — Models`

State: `MATERIAL APPLIED / EXACT-HEAD CI PENDING`

Predecessor Unit 7 HEAD: `4744123935eaf71b29443f4b04738c1ecbdb1d89`

## Predecessor exact-head evidence

At `4744123935eaf71b29443f4b04738c1ecbdb1d89`:

- Real Mutation Matrix Regression — `33974345294` — SUCCESS;
- M2 Multi-Channel Proposal Training — `33974345256` — SUCCESS;
- Full-Stack Repository Audit — `33974345253` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests — `33974345289` — SUCCESS.

Therefore Unit 7 is `VERIFIED` and Unit 8 is authorized.

## Current source contract

Current `Models/MOD-003_DOCUMENT_MODEL.md` defines an implementation-independent semantic Document Model. Its material-change ripple rule requires review of Governance metadata, Repository indexes, folder status conventions, Architecture references, Release/version authority, Runtime/document loading dependencies and affected templates/validators.

That ripple list is not a list of canonical graph edges.

The same artifact separately lists nine exact `Related Documents` paths. Those direct source declarations establish bounded documentary references from MOD-003 unless stronger current evidence establishes another controlled type.

## P64 provenance classification

Historical `REP-020_MATRIX_ADDENDUM_2026-08-15_P64.md` was explicitly `PROVISIONAL EVIDENCE / MATRIX EXTENSION / NOT AUTHORITY`.

Its useful current contribution is discovery/provenance:

- it correctly identified the same direct Related Documents cohort;
- it explicitly warned that documentary proof does not establish executable coupling;
- its semantic consumer search for a document-model implementation/metadata parser/runtime loader returned no indexed result;
- it did not authorize speculative relationship promotion.

Unit 8 re-derives direction/type from current source text rather than inheriting P64 labels.

## Unit-8 evidence surface

Created:

`Repository/REP-014_PRIORITY12_MOD003_BOUNDARY_EVIDENCE_2026-09-05_F.tsv`

Guard:

`Quality/Integrity/test_models_p12_mod003_boundary.py`

### Current disposition

| Candidate class | Count | Disposition |
|---|---:|---|
| MOD-003 → active Models related documents | 3 | `REFERENCES / REGISTRATION_CANDIDATE` |
| MOD-003 → GOV-004 / GOV-012 | 2 | `REFERENCES`; GOV-004 remains Governance metadata authority; GOV-012 is non-dependency reconstruction reference |
| MOD-003 → REP-001 / REP-002 | 2 | `REFERENCES` because MOD-003 directly names them; the direction is **not** inferred from index/map membership |
| MOD-003 → ARC-009 / ARC-010 | 2 | `REFERENCES / ARCHITECTURE REVIEW REFERENCES` |
| Runtime / Templates / Quality generic ripple classes | 1 grouped hold | `NONE / HOLD_NO_REGISTRATION`; no concrete current consumer endpoint proven |

## Directional nuance

The fact that REP-001 indexes MOD-003 and REP-002 maps its path does not itself create a semantic edge. The bounded edges here are instead supported by the opposite fact: MOD-003 itself explicitly names REP-001 and REP-002 under `Related Documents`.

Likewise, current GOV-004 defines metadata/identity authority but does not name MOD-003 as a reverse dependency. No reverse GOV-004 → MOD-003 edge is manufactured.

`MOD-004 → MOD-003 = DEPENDS_ON` remains a separate current semantic-composition candidate from Unit 3. It is not inverted into `MOD-003 → MOD-004 = DEPENDS_ON`; MOD-003's own direction remains a documentary `REFERENCES` edge.

## Material sequence

1. `73d31914cd7aa5b3bcdf0edc71a26dc6c725eee9` — created MOD-003 bounded evidence manifest.
2. `fc19650eb92b0b2efc1f965702af824ebec8844b` — added executable MOD-003 boundary guard.
3. this Matrix commit — binds exact-head validation.

## Non-claims

Unit 8 does not:

- mutate REP-014;
- allocate final REL IDs;
- establish executable document loading;
- certify templates or validators as concrete MOD-003 consumers;
- create reverse Governance/Repository/Architecture edges;
- promote MOD-003 maturity;
- close Models or Priority 12;
- claim Phase-1 or Global Integrity closure.

## Exact-head gate

The Unit-8 Matrix HEAD must pass the four required workflow families on the same SHA:

1. Full-Stack Repository Audit;
2. ARGO Runtime Prototype and Integration Tests;
3. M2 Multi-Channel Proposal Training;
4. Real Mutation Matrix Regression.

Failure keeps Unit 8 open and must be classified before repair.

## Next safe chain after 4-of-4

Continue to MOD-004 current consumer/reverse relationship proof. Reuse Unit-3's corrected source semantics but search concrete downstream endpoints independently before assigning `CONSUMES`, `REFERENCES`, `VALIDATES` or other types. Then continue remaining MOD-011 non-Knowledge consumers and repository/status consolidation.
