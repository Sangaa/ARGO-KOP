# Priority 12 — Models Relationship / Content Reconciliation — Transaction B — Unit 10 Matrix Addendum

Parent Transaction: `MUT-2026-09-05-P12-MODELS-RELATIONSHIP-CONTENT-B`
Priority: `12 — Models`
State: `OPEN / UNIT-9 EXACT-HEAD VERIFIED / MATERIAL UNIT 10 APPLIED / EXACT-HEAD CI PENDING`

Unit-9 exact-head: `92a590dc45e35944982e5aa475db13414158195b`

## Scope

Reconcile non-Knowledge consumers/references of `MOD-011` using current source text while separating relationship semantics from endpoint maturity.

## Current-source dispositions

- `MOD-011 → ENG-007 = REFERENCES` and `ENG-007 → MOD-011 = REFERENCES`; both endpoints directly list the other, but neither source establishes dependency/consumption for this pair.
- `MOD-011 → AI-006 = REFERENCES`; `AI-006 → MOD-011 = CONSUMES` because AI-006 explicitly states that it consumes MOD-011 source identity/provenance/evidence-state semantics.
- `MOD-011 → AI-007 = REFERENCES`; `AI-007 → MOD-011 = DEPENDS_ON` as a qualified semantic dependency because AI-007 requires external source claims/provenance handling to remain aligned with MOD-011 semantics.
- `AI-008 → MOD-011 = DEPENDS_ON` as a qualified semantic dependency because AI-008 normatively requires external source claims to remain distinguishable according to MOD-011.
- `MOD-011 → GOV-011 = REFERENCES`; GOV-011 remains `Proposed / Integrity Hold`, `Canonical: No`, so the format reference is not promoted to active dependency authority.
- `MOD-011 → SESSION_LEARNING_HANDOFF_TEMPLATE = REFERENCES`; no reverse edge is proven from the current template.
- no reverse `GOV-011 → MOD-011` edge is proven from current GOV-011 content.

## Maturity boundary

Relationship classification does not promote AI endpoint maturity. `AI-006`, `AI-007` and `AI-008` remain `Integrity Hold / Revalidation Required` because their 2026-08-09 semantic mutations still require independent post-session verification in their own domain.

Therefore candidate relationship semantics can be evidence-ready while registry insertion/promotion remains held by endpoint maturity.

Invariant:

`RELATIONSHIP SEMANTICS != ENDPOINT MATURITY != REGISTRY PROMOTION`.

## Material

- `Repository/REP-014_PRIORITY12_MOD011_EXTERNAL_CONSUMER_EVIDENCE_2026-09-05_H.tsv`
- `Quality/Integrity/test_models_p12_mod011_external_consumers.py`
- this Matrix addendum

## Non-claims

Unit 10 does not mutate REP-014, does not revalidate the AI partition, does not promote GOV-011 to canonical Governance authority, and does not close Models/P12.

## Next gate

1. exact-head four-family CI;
2. reconcile Models `_FOLDER_STATUS.md` and REP-016 queue against Units 3-10 so stale broad consumer/dependency wording no longer overstates unresolved work;
3. evaluate remaining blocker set for Transaction-B material completeness;
4. keep stable-ID canonical REP-014 corrections and new IDs pending until full-content-preserving registry mutation is safe.
