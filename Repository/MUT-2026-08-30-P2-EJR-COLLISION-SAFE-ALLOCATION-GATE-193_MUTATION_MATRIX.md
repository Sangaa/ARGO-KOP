# MUTATION MATRIX — P2 EJR COLLISION-SAFE ALLOCATION GATE 193

Transaction ID: `MUT-2026-08-30-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193`
Protocol: GOV-014 v1.0.1
Lease: `R71-20260830-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193`
State: `FUNCTIONAL CANDIDATE / APPLIED PENDING EXACT-HEAD VERIFICATION`
Entry head: `cb9dd60f2d910958c792ccb53d2db15bee077786`
Prewrite head / functional parent: `804660b573af97ba4752393bfd8e7ea7696873a0`

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 193-001 | `Quality/Integration/ejr_allocation_vacancy_gate.py` | CREATE | deterministic EJR candidate-vacancy evidence across metadata, H1, filename and reachable Git history; fail closed on shallow history | Y | N |
| 193-002 | `Quality/Integration/test_ejr_allocation_vacancy_gate.py` | CREATE | regress current occupancy, deleted historical occupancy, shallow-history hold, and complete-history vacancy | Y | N |
| 193-003 | `.github/workflows/internal-id-audit.yml` | UPDATE | fetch complete history and execute vacancy-gate regressions without weakening existing Internal-ID audit/report behavior | Y | N |
| 193-004 | this Matrix | UPDATE IN SAME FUNCTIONAL CHANGE SET | bind source/candidate identities, exact functional commit and verification evidence | Y | N |

## Exact source / candidate identities

- vacancy-gate candidate blob: `9ff4e4c9f9ac089f20358814f041844773cd026f`;
- vacancy-gate test candidate blob: `34dcb291b85f091aecb7d7419677f03b59e5a098`;
- workflow source blob: `b7bddd598d82086574a56359a88b3cc74f7e772b`;
- workflow candidate blob: `27a2a9106c5adf80bfb0d04fed56b0e4b0414f18`.

## KEEP requirements

- existing `internal_document_id_audit.py` semantics and output are KEEP;
- existing `test_internal_document_id_audit.py` is KEEP;
- existing Internal Document-ID report artifact generation is KEEP;
- existing workflow permissions are KEEP (`contents: read`);
- no EJR content/path/identity mutation;
- no REP-012 or REP-016 mutation in this lease;
- no detector suppression or ambiguity-membership reduction.

Unexpected path or semantic change = HARD HOLD.

## Expected functional changed-file set

Exactly four paths:

1. `Quality/Integration/ejr_allocation_vacancy_gate.py`
2. `Quality/Integration/test_ejr_allocation_vacancy_gate.py`
3. `.github/workflows/internal-id-audit.yml`
4. `Repository/MUT-2026-08-30-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193_MUTATION_MATRIX.md`

Lease record already exists as prewrite evidence and is not part of the functional set.

## Verification gate

A functional commit is not verified until:

- exact compare proves only the four expected paths changed;
- code/test/workflow/Matrix read-back succeeds;
- vacancy returns false when any current qualified identity surface is occupied;
- a deleted historical qualified claim remains occupancy evidence;
- shallow history cannot produce a vacant verdict;
- complete history with no qualifying claim can produce a vacant verdict;
- exact-head applicable CI is successful.

Priority 2 remains OPEN regardless of this bounded tooling success.
