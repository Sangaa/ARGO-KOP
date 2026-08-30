# MUT-2026-08-30-P2-EJR-REPLACEMENT-VACANCY-PROOF-206 — MUTATION MATRIX

Status: FUNCTIONAL / EVIDENCE-ONLY
Lease: R71-20260830-P2-EJR-REPLACEMENT-VACANCY-PROOF-206
Baseline: 92a0d4fa3da630b9762e5d3685819775309ca309
Prewrite packaging note: the lease file landed one commit before the matrix because the contents API was mistakenly used instead of the prepared atomic tree. No functional path had been mutated. Corrective commit `92a0d4fa3da630b9762e5d3685819775309ca309` restored the governed prewrite pair before this functional change.

## Authorized functional paths
- `.github/workflows/ejr-replacement-vacancy-proof-206.yml`
- this matrix

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
1. workflow uses `actions/checkout@v4` with `fetch-depth: 0`;
2. workflow verifies `git rev-parse --is-shallow-repository == false`;
3. workflow runs the unchanged Lease-193 gate for `EJR-400`;
4. JSON evidence is uploaded as `ejr-400-vacancy-proof`;
5. workflow fails unless decision is exactly `VACANT`;
6. only a successful exact-head run plus inspected JSON authorizes a later repair-execution lease.
