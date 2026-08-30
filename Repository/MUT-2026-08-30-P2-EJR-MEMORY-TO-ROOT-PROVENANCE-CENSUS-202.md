# MUT-2026-08-30 — P2 EJR MEMORY→ROOT COHORT PROVENANCE CENSUS — LEASE 202

Status: `OPEN / PREWRITE / NO FUNCTIONAL MUTATION YET`
Lease: `R71-20260830-P2-EJR-MEMORY-TO-ROOT-PROVENANCE-CENSUS-202`
Baseline: `main@ed0642f9d1fd579f7cf7b39a3c1e5406596a8d8d`

## Trigger
Leases 199–201 proved that namespace direction is provenance evidence, not ownership authority. The four non-monotonic and four reverse-direction exceptional H1-only ambiguity groups have independent content/reference/consumer census evidence. The next unresolved cross-surface cohort is the 36 `MEMORY_TO_ROOT_EJR` groups reported by Lease 199.

## Bounded purpose
Add deterministic evidence-only observability for the current `MEMORY_TO_ROOT_EJR` cohort by consuming the current namespace-lineage classification and current Internal Document-ID ambiguity report. Measure membership, content fingerprints/titles, exact-ID references, and exact-member-path consumers without assigning owner/canonical/migration disposition.

## Safety contract
- Expected cohort count = 36 from Lease 199; drift fails `PARTIAL`.
- Target membership is derived from current namespace-lineage evidence, not hardcoded IDs.
- H1-only identity-source drift fails `PARTIAL`.
- incomplete Git history fails closed.
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, replacement allocation, or canonical promotion.
- no REP-012/016/020 mutation.
- Internal Document-ID scanner semantics remain unchanged.

## Authorized functional paths
1. `Quality/Integration/ejr_memory_to_root_provenance_census.py` — ADD.
2. `Quality/Integration/test_ejr_memory_to_root_provenance_census.py` — ADD.
3. `.github/workflows/internal-id-audit.yml` — MODIFY only to test/emit/upload the new evidence report.
4. `Repository/MUT-2026-08-30-P2-EJR-MEMORY-TO-ROOT-PROVENANCE-CENSUS-202_MUTATION_MATRIX.md` — synchronize functional evidence.

## Verification required
Pre-ref compare → live-parent recheck → `force=false` fast-forward → read-back → exact-head Internal-ID + Full-Stack + Runtime/Integration + M2 + Real Matrix → artifact inspection → closure checkpoint.

Priority 2, Phase 1, Connected Baseline, Provider Authentication, Memory certification, and Global Boot/PASS boundaries remain unchanged.
