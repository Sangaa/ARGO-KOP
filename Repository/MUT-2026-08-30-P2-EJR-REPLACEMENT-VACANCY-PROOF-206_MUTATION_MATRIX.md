# MUT-2026-08-30-P2-EJR-REPLACEMENT-VACANCY-PROOF-206 — MUTATION MATRIX

Status: PREWRITE / EVIDENCE-ONLY / CORRECTED PACKAGING
Lease: R71-20260830-P2-EJR-REPLACEMENT-VACANCY-PROOF-206
Baseline: a622ae60dd4c19420cbd60c55e6dc3c3ccac401f
Prewrite packaging note: the lease file landed one commit before this matrix because the contents API was mistakenly used instead of the prepared atomic tree. No functional path had been mutated. This corrective commit restores the governed prewrite pair before any functional workflow change.

## Authorized functional paths
- `.github/workflows/ejr-replacement-vacancy-proof-206.yml`
- this matrix only for final evidence synchronization

## Read-only dependencies
- `Quality/Integration/ejr_allocation_vacancy_gate.py`
- `Quality/Integration/internal_document_id_audit.py`
- `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
- `Repository/P2_EJR_CONTROLLED_IDENTITY_REPAIR_PLAN_204.md`

## Forbidden
- any EJR content/path/identity mutation
- any scanner/gate semantics change
- REP-012 / REP-016 / REP-020 mutation
- authority promotion
- Priority 2 / Phase 1 / Connected Baseline closure

## Validation
1. workflow uses `actions/checkout` with `fetch-depth: 0`;
2. verify `git rev-parse --is-shallow-repository` returns false;
3. run `python Quality/Integration/ejr_allocation_vacancy_gate.py EJR-400`;
4. preserve JSON as artifact;
5. only `VACANT` authorizes opening a later repair-execution lease.
