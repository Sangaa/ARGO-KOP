# MUTATION MATRIX — P2 EJR COLLISION-SAFE ALLOCATION GATE 193

Transaction ID: `MUT-2026-08-30-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193`
Protocol: GOV-014 v1.0.1
Lease: `R71-20260830-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193`
State: `CLOSED / VERIFIED / EXECUTION COMPLETE`
Entry head: `cb9dd60f2d910958c792ccb53d2db15bee077786`
Prewrite head / functional parent: `804660b573af97ba4752393bfd8e7ea7696873a0`
Functional head: `2c6507ee6fced85a2c56eb17befadbd36ae1665f`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 193-001 | `Quality/Integration/ejr_allocation_vacancy_gate.py` | CREATE | deterministic EJR candidate-vacancy evidence across metadata, H1, filename and reachable Git history; fail closed on shallow history | Y | Y |
| 193-002 | `Quality/Integration/test_ejr_allocation_vacancy_gate.py` | CREATE | regress current occupancy, deleted historical occupancy, shallow-history hold, and complete-history vacancy | Y | Y |
| 193-003 | `.github/workflows/internal-id-audit.yml` | UPDATE | fetch complete history and execute vacancy-gate regressions without weakening existing Internal-ID audit/report behavior | Y | Y |
| 193-004 | this Matrix | UPDATE IN SAME FUNCTIONAL CHANGE SET | bind source/candidate identities, exact functional commit and verification evidence | Y | Y |

## Exact source / result identities

- vacancy-gate result blob: `9ff4e4c9f9ac089f20358814f041844773cd026f`;
- vacancy-gate test result blob: `34dcb291b85f091aecb7d7419677f03b59e5a098`;
- workflow source blob: `b7bddd598d82086574a56359a88b3cc74f7e772b`;
- workflow result blob: `27a2a9106c5adf80bfb0d04fed56b0e4b0414f18`;
- unchanged internal-ID scanner blob: `50454dd20a2a5691f788c4580cce234dac13f0c1`.

## KEEP verification

Verified preserved:

- existing `internal_document_id_audit.py` semantics/output;
- existing Internal Document-ID report artifact generation;
- workflow `contents: read` permission;
- EJR contents, paths and identities;
- REP-012 and REP-016;
- detector ambiguity membership.

Functional compare proved exactly four changed paths and unexpected paths = 0.

## Exact-head verification

Functional head `2c6507ee6fced85a2c56eb17befadbd36ae1665f`:

- Internal Document-ID Audit `33310451501` — SUCCESS;
- Full-Stack Repository Audit `33310451462` — SUCCESS;
- Runtime/Integration `33310451475` — SUCCESS;
- M2 `33310451492` — SUCCESS;
- Real Mutation Matrix Regression `33310451464` — SUCCESS.

Internal-ID artifact:

- ID `9731811306`;
- digest `sha256:8c1e8b89b6f5d10edd187f569e057327ac95869cff0cef6390008faee249ac7d`;
- exact head `2c6507ee6fced85a2c56eb17befadbd36ae1665f`.

## Bounded closure

Lease 193 closes only the executable collision-safe EJR vacancy-gate tooling subgate.

Priority 2 remains OPEN.

Next bounded transaction: `P2 REP-012 PRE-ALLOCATION VACANCY BINDING`.
