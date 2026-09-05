# Priority 12 — Models Relationship / Content Reconciliation — Transaction B — Unit 7 Mutation Matrix

Parent Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`

Unit: `7 — MOD-002 Entity Model boundary / consumer reconciliation`

Priority: `12 — Models`

State: `MATERIAL APPLIED / EXACT-HEAD CI PENDING`

Entry / predecessor HEAD: `29274886b54ce77125ca72d1ff071caaa44c9585`

Predecessor Unit 6 status: `VERIFIED / 4-of-4 exact-head SUCCESS`.

## Predecessor exact-head evidence

At `29274886b54ce77125ca72d1ff071caaa44c9585`:

- Real Mutation Matrix Regression — `33974133877` — SUCCESS;
- M2 Multi-Channel Proposal Training — `33974133824` — SUCCESS;
- Full-Stack Repository Audit — `33974133849` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests — `33974133883` — SUCCESS.

Therefore Unit 6 is verified and Unit 7 is authorized to proceed.

## Governing rules inherited from Transaction B

- `TEST THE SEMANTIC CONTRACT AT THE STABLEST CONTRACTUAL REPRESENTATION AVAILABLE.`
- `DISCOVERY ARROW != RELATIONSHIP DIRECTION != CONTROLLED TYPE`.
- `INDEX MEMBERSHIP != SEMANTIC RELATIONSHIP`.
- `PHYSICAL MAPPING != SEMANTIC RELATIONSHIP`.
- `RELATED DOCUMENT != DEPENDENCY` unless stronger current authority independently establishes dependency semantics.
- `GENERIC CONSUMER CLASS != CONCRETE RELATIONSHIP ENDPOINT`.
- Physical folder placement does not establish architectural layer or dependency authority.
- Reverse edges are not manufactured for symmetry.

## Historical evidence classification

`Repository/REP-020_SESSION_DELTA_2026-08-15_P59.md` identified a broad MOD-002 matrix including:

- MOD-002 → MOD-003 / MOD-004 / MOD-011;
- MOD-002 → REP-001 / REP-002;
- MOD-002 → generic Interfaces / Services consuming entity identity;
- MOD-002 → generic Runtime consumers;
- MOD-002 → Architecture decisions / dependency model.

P59 explicitly stated that these were declared/identified edges, not final relationship proofs, and required target reading before promotion.

Unit 7 therefore treats P59 as discovery evidence only.

## Current source authority

Current `Models/MOD-002_ENTITY_MODEL.md` directly lists under `Related Documents`:

- `Models/MOD-003_DOCUMENT_MODEL.md`;
- `Models/MOD-004_MEMORY_MODEL.md`;
- `Models/MOD-011_KNOWLEDGE_SOURCE_MODEL.md`;
- `Architecture/ARC-002_COMPONENT_ARCHITECTURE.md`;
- `Architecture/ARC-006_DEPENDENCY_MODEL.md`;
- `Architecture/ARC-009_ARCHITECTURE_DECISIONS.md`;
- `Architecture/ARC-010_EVOLUTION_MODEL.md`;
- `Governance/GOV-004_DOCUMENT_METADATA.md`;
- `Governance/GOV-012_DOMAIN_RECONSTRUCTION_STANDARD.md`.

Its `Revalidation Rule` separately names generic downstream classes: repository indexes, interfaces/services consuming entity identity, runtime consumers and affected architecture decisions.

Those two categories must not be collapsed into one relationship type.

## Architecture qualification

Historical P252 plus current `ARC-002` and `ARC-006` establish that:

- reference does not transfer ownership;
- physical folder placement is insufficient evidence of dependency;
- a textual file reference does not itself establish architectural dependency;
- Architecture retains ownership/dependency authority for its own contracts.

Therefore MOD-002 references to ARC-002/006/009/010 are bounded `REFERENCES`, not ownership or dependency transfer.

## Concrete consumer search disposition

Current exact-ID / exact-name searches for `MOD-002` / `Models/MOD-002_ENTITY_MODEL.md` returned direct current semantic hits in the maintained Models set, repository inventory/map surfaces and historical review records. No concrete current Service, Interface or Runtime artifact was established by those searches as directly naming or contractually consuming MOD-002.

Accordingly, the generic source phrases:

- `interfaces and services consuming entity identity`;
- `runtime consumers`

remain valid *revalidation classes*, but they are not canonical relationship endpoints until a concrete artifact is found and read.

Disposition:

`GENERIC CONSUMER CLASS / NO CONCRETE CURRENT ENDPOINT PROVEN / HOLD_NO_REGISTRATION`.

This is not a claim that no consumer can exist. It is a claim that the current bounded search does not authorize manufacturing a concrete graph edge.

## Unit-7 evidence surface

Created:

`Repository/REP-014_PRIORITY12_MOD002_BOUNDARY_EVIDENCE_2026-09-05_E.tsv`

Guard:

`Quality/Integrity/test_models_p12_mod002_boundary.py`

Current classification:

| Candidate class | Count | Disposition |
|---|---:|---|
| MOD-002 direct Related Documents → Models | 3 | `REFERENCES / REGISTRATION_CANDIDATE` |
| MOD-002 direct Related Documents → Architecture | 4 | `REFERENCES / REGISTRATION_CANDIDATE / NON-OWNERSHIP / NON-DEPENDENCY` |
| MOD-002 direct Related Documents → Governance | 2 | `REFERENCES / REGISTRATION_CANDIDATE`; GOV-012 remains non-dependency reconstruction reference |
| Repository index/map historical P59 arrows | 2 | `NONE / DO_NOT_REGISTER` |
| Generic Interfaces/Services/Runtime consumer class | 1 grouped hold record | `NONE / HOLD_NO_REGISTRATION` |

The separate Unit-3 relationship `MOD-004 → MOD-002 = DEPENDS_ON` remains intact and is not inverted merely because MOD-002 also references MOD-004.

## Material sequence

1. `e4f423c105f5dc4816233a869d5cf27eadf0f6fa` — created MOD-002 bounded evidence manifest.
2. `e7a0b593f7fbd4859fd7ea1f484f8e6b09e0bf34` — added executable semantic-boundary guard.
3. this Unit-7 Matrix commit — binds exact-head validation.

## Non-claims

Unit 7 does not:

- mutate REP-014;
- allocate final `REL-*` IDs;
- certify absence of all possible MOD-002 consumers repository-wide;
- turn repository inventory or physical map membership into relationships;
- infer Architecture ownership/dependency from Related Documents;
- promote MOD-002 maturity;
- close Models or Priority 12;
- claim Phase-1, Global Connected Baseline or Global Integrity closure.

## Exact-head gate

This Unit-7 Matrix HEAD must pass all four workflow families on the same SHA:

1. Full-Stack Repository Audit;
2. ARGO Runtime Prototype and Integration Tests;
3. M2 Multi-Channel Proposal Training;
4. Real Mutation Matrix Regression.

If any family fails, Unit 7 remains open and the failure must be classified before repair.

## Next safe chain after 4-of-4

Continue directly to MOD-003 Document Model consumer/boundary reconciliation. Prioritize:

- concrete consumers that directly name the current Document Model or its metadata/identity contract;
- Governance metadata authority;
- repository index/map as revalidation surfaces rather than automatic semantic edges;
- Runtime/document-loading and template/validator consumers only when concrete current endpoints are proven;
- comparison against historical P64 evidence without inheriting its arrows as authority.
