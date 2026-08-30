# MUTATION MATRIX — P2 EJR REVERSE-DIRECTION PROVENANCE CENSUS — LEASE 201

Transaction: `MUT-2026-08-30-P2-EJR-REVERSE-PROVENANCE-CENSUS-201`
Lease: `R71-20260830-P2-EJR-REVERSE-PROVENANCE-CENSUS-201`
State: `PREWRITE / OPEN`
Baseline: `62b08f67af7f1f58e23236f8563d590b4d24cf04`

| Path | Operation | Authorized purpose | Content preservation / boundary |
|---|---|---|---|
| `Quality/Integration/ejr_reverse_provenance_census.py` | ADD | deterministic evidence-only content/reference/consumer census for EJR-178/189/222/338 | no owner/canonical/migration action |
| `Quality/Integration/test_ejr_reverse_provenance_census.py` | ADD | fail-closed and heterogeneous-cardinality regression coverage | synthetic evidence only |
| `.github/workflows/internal-id-audit.yml` | MODIFY | run tests, emit report, upload artifact | preserve all existing jobs/steps/gates |
| `Repository/MUT-2026-08-30-P2-EJR-REVERSE-PROVENANCE-CENSUS-201_MUTATION_MATRIX.md` | MODIFY | synchronized same-change evidence | no other repository authority mutation |

## Explicitly forbidden
- EJR content/path/identity mutation;
- REP-012 / REP-016 / REP-020 mutation;
- Internal Document-ID scanner semantic changes;
- ambiguity suppression;
- canonical promotion or ownership assignment;
- closure of Priority 2, Phase 1, Global Connected Baseline, provider-authentication holds, Memory integrity, or global BOOTED/INTEGRITY PASS.

## Verification rows
| Check | Required | Current |
|---|---:|---:|
| Prewrite committed before functional write | Y | Y |
| Functional compare exactly four authorized paths | Y | PENDING |
| Live-parent recheck before `force=false` FF | Y | PENDING |
| Exact-head Internal-ID | Y | PENDING |
| Exact-head Full-Stack | Y | PENDING |
| Exact-head Runtime | Y | PENDING |
| Exact-head M2 | Y | PENDING |
| Exact-head Real Matrix | Y | PENDING |
| Artifact inspected | Y | PENDING |
| Room 071 closure checkpoint | Y | PENDING |
