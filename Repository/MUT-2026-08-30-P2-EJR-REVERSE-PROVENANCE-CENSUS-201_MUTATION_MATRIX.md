# MUTATION MATRIX — P2 EJR REVERSE-DIRECTION PROVENANCE CENSUS — LEASE 201

Transaction: `MUT-2026-08-30-P2-EJR-REVERSE-PROVENANCE-CENSUS-201`
Lease: `R71-20260830-P2-EJR-REVERSE-PROVENANCE-CENSUS-201`
State: `CLOSED / VERIFIED / EXECUTION COMPLETE`
Baseline: `62b08f67af7f1f58e23236f8563d590b4d24cf04`
Prewrite head: `041459ae60bcabeb53610af0d91b52da0c5d5f60`
Functional head: `f554672b8fced5e9aa71154b9c5ce5f7df3efa2b`

| Path | Operation | Authorized purpose | Applied | Verified |
|---|---|---|:---:|:---:|
| `Quality/Integration/ejr_reverse_provenance_census.py` | ADD | deterministic evidence-only census for EJR-178/189/222/338 | Y | Y |
| `Quality/Integration/test_ejr_reverse_provenance_census.py` | ADD | fail-closed + heterogeneous-cardinality regression coverage | Y | Y |
| `.github/workflows/internal-id-audit.yml` | MODIFY | test, emit and upload report | Y | Y |
| `Repository/MUT-2026-08-30-P2-EJR-REVERSE-PROVENANCE-CENSUS-201_MUTATION_MATRIX.md` | MODIFY | synchronized same-change evidence | Y | Y |

## Verification evidence
- Functional compare: exactly four authorized paths / no extras — PASS.
- Live-parent recheck before `force=false` fast-forward — PASS.
- Internal-ID `33322805862` — SUCCESS.
- Full-Stack `33322805741` — SUCCESS.
- Runtime `33322805722` — SUCCESS.
- M2 `33322805724` — SUCCESS.
- Real Matrix `33322805744` — SUCCESS.
- Artifact `9735374854`, digest `sha256:05576555bf8754be22ed99440083400fc7b3783ca6d4ab8c0ab711e5abf7de2c` — inspected / CENSUSED / complete history.

## Evidence result
- expected current cardinalities held: `3 / 2 / 4 / 2`;
- every current member remained `FIRST_H1_FALLBACK`;
- all members were content-distinct within their group;
- no exact member path had an external tracked-text consumer;
- ID-level semantic context exists for EJR-178 and EJR-338 but does not establish exact-path binding;
- EJR-222 is a compound ambiguity combining same-event P39 variants with later ID reuse.

## Forbidden-scope verification
- EJR content/path/identity mutation: NO.
- REP-012 / REP-016 / REP-020 mutation: NO.
- scanner semantic change: NO.
- ambiguity suppression: NO.
- canonical promotion / owner assignment: NO.
- Priority-2 / Phase-1 / global closure claim: NO.
