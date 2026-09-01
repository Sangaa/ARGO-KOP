# MUTATION MATRIX — P7 CORE-003 ↔ RUN-003 AUTHORITY VALIDATION — P

Transaction: `MUT-2026-09-01-P7-CORE003-RUN003-AUTHORITY-P`
Work Lease: `HERMUZ-P7-P-CORE003-RUN003-20260901`
Priority: `7 — Core cross-layer validation`
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY-7-OPEN`
Entry HEAD: `1392b031a49c187453daa2f03cfa8250aa08e6db`
Pre-write Matrix HEAD: `86fe1d5d4ea905dd70104b8d3d9bb15753a659f8`
Material candidate HEAD: `0e8329f822fd78302add191eba62a95d0b9a421e`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Closed finding

Direct current source evidence validates only the bounded pair:

`CORE-003 → RUN-003 = GOVERNS`

`RUN-003 → CORE-003 = REFERENCES`

Disposition: `BIDIRECTIONAL-AUTHORITY/DOCUMENTARY / RUNTIME-CONFIGURATION-NON-OVERRIDE / NON-DEPENDENCY`.

CORE-003 establishes the highest governing rules and repository-component compliance within applicable scope. RUN-003 is canonical/critical Runtime configuration, explicitly says configuration controls runtime behavior without modifying repository architecture or authority, explicitly says Runtime configuration does not override CORE-003, directly lists CORE-003, and keeps repository authority above runtime assumptions.

## Material change set

| Change ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| P-01 | `Quality/Integrity/test_core003_run003_authority_boundary.py` | CREATE | Y | Y |
| P-02 | `Repository/P7_CORE003_RUN003_AUTHORITY_SEAM_2026-09-01_P.md` | CREATE | Y | Y |
| P-03 | this Matrix | UPDATE IN SAME MATERIAL CHANGE SET | Y | Y |

Candidate comparison from pre-write Matrix HEAD `86fe1d5d4ea905dd70104b8d3d9bb15753a659f8` to material candidate `0e8329f822fd78302add191eba62a95d0b9a421e` proved exactly one commit and exactly three authorized paths. Unexpected path expansion = `0`.

## Exact-head verification

Required workflows on `0e8329f822fd78302add191eba62a95d0b9a421e`:

- Full-Stack Repository Audit — `33525165000` — SUCCESS. Repository-audit job and all reported steps succeeded, including exact checkout SHA binding, Mutation Matrix preflight, Matrix semantic regression, same-change-set enforcement, repository-wide audit and evidence emission.
- ARGO Runtime Prototype and Integration Tests — `33525165065` — SUCCESS. Integrity, prototype and integration jobs all succeeded.
- Real Mutation Matrix Regression — `33525164918` — SUCCESS.
- M2 Multi-Channel Proposal Training — `33525164899` — SUCCESS.

Result: `4/4 REQUIRED WORKFLOWS SUCCESS`.

No material failure occurred in P.

## KEEP / non-authority

- CORE-003 source content unchanged.
- RUN-003 source content unchanged.
- REP-014 unchanged by P; no relationship row is registered yet.
- REP-020 and Core status unchanged by P.
- Existing REL-001..REL-070 unchanged.
- No `RUN-003 → CORE-003 = DEPENDS_ON`.
- No reverse `RUN-003 → CORE-003 = GOVERNS`.
- No IMPLEMENTS or CONSUMES promotion in either direction.
- No executable/runtime reachability proof.
- No Runtime/Core certification.
- No Priority-7 closure, Phase-1 closure, Connected Baseline closure, repository-wide graph closure or Global PASS.

## Learning assessment

REL-037/038 CORE-003↔RUN-001 was directly applicable prior learning. Transactions L/M and N/O supplied transferable authority/non-dependency and validation-first discipline. The current result is successful reuse of existing rules; no new governance rule is warranted.

Work Lease: `CLOSED / RESUME-SAFE`.

A future continuation must rediscover live `main` and recompute Priority 7. REP-014 synchronization of this validated pair is only a candidate and receives no future mutation authority from this record.
