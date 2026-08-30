# P2 EJR COLLISION-SAFE ALLOCATION GATE — LEASE 193

Transaction ID: `MUT-2026-08-30-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193`
Lease: `R71-20260830-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193`
Protocol: HERMUZ / GOV-014
Status: `CLOSED / EXECUTION-VERIFIED / COLLISION-SAFE VACANCY GATE ACTIVE`
Entry head: `cb9dd60f2d910958c792ccb53d2db15bee077786`
Prewrite head: `804660b573af97ba4752393bfd8e7ea7696873a0`
Functional head: `2c6507ee6fced85a2c56eb17befadbd36ae1665f`

## Evidence basis

Lease 192 proved that historical identity-repair allocations selected already-occupied EJR IDs because vacancy was not established across every identity-bearing surface and history.

Required gate from Lease 192:

`METADATA → H1 → FILENAME → GIT HISTORY → ALLOCATE`

REP-012 currently begins material mutation with `ALLOCATE → READ → ...`. Lease 193 intentionally did not edit REP-012; it first built and execution-verified the missing deterministic vacancy checker so control-plane binding can be a separate governed transaction.

## Functional result

Created:

- `Quality/Integration/ejr_allocation_vacancy_gate.py`
  - blob `9ff4e4c9f9ac089f20358814f041844773cd026f`;
- `Quality/Integration/test_ejr_allocation_vacancy_gate.py`
  - blob `34dcb291b85f091aecb7d7419677f03b59e5a098`.

Updated:

- `.github/workflows/internal-id-audit.yml`
  - source blob `b7bddd598d82086574a56359a88b3cc74f7e772b`;
  - verified result blob `27a2a9106c5adf80bfb0d04fed56b0e4b0414f18`.

The functional compare from `804660b573af97ba4752393bfd8e7ea7696873a0` to `2c6507ee6fced85a2c56eb17befadbd36ae1665f` contained exactly the four authorized paths and no unexpected path.

## Verified semantic contract

A candidate `EJR-NNN` is treated as occupied when a qualifying claim is established on any of these surfaces:

- qualified `Document ID` metadata;
- document-level first-H1 identity;
- filename identity prefix;
- reachable Git history containing a historical qualifying content or filename claim.

The gate is evidence-only. It does not allocate, rename, delete or rewrite any ID.

Decision states are:

- `OCCUPIED`;
- `HISTORY_INCOMPLETE`;
- `VACANT`.

A shallow repository cannot produce `VACANT`. The workflow now checks out complete history with `fetch-depth: 0` and independently asserts `git rev-parse --is-shallow-repository = false` before executing the gate regressions.

History scope is explicitly bounded to `all locally reachable refs`; this lease makes no stronger claim about unreachable external history.

## Regression evidence

The exact-head suite proves:

1. current metadata, H1 and filename claims independently block allocation;
2. a deleted historical metadata identity remains occupied;
3. a deleted historical filename identity remains occupied;
4. a shallow clone returns `HISTORY_INCOMPLETE`, never `VACANT`;
5. an unused candidate returns `VACANT` only with complete locally reachable history;
6. candidate syntax is restricted to `EJR-NNN`.

## Exact-head execution evidence

Functional head: `2c6507ee6fced85a2c56eb17befadbd36ae1665f`.

- Internal Document-ID Audit — run `33310451501` — SUCCESS.
- Full-Stack Repository Audit — run `33310451462` — SUCCESS.
- ARGO Runtime Prototype and Integration Tests — run `33310451475` — SUCCESS.
- M2 Multi-Channel Proposal Training — run `33310451492` — SUCCESS.
- Real Mutation Matrix Regression — run `33310451464` — SUCCESS.

Internal-ID artifact:

- artifact ID `9731811306`;
- name `internal-document-id-audit-report`;
- digest `sha256:8c1e8b89b6f5d10edd187f569e057327ac95869cff0cef6390008faee249ac7d`;
- head SHA `2c6507ee6fced85a2c56eb17befadbd36ae1665f`.

## Preserved boundaries

No EJR content/path/identity was mutated.

No detector suppression or ambiguity-membership reduction occurred.

`internal_document_id_audit.py` remained unchanged at blob `50454dd20a2a5691f788c4580cce234dac13f0c1`.

REP-012 and REP-016 were not mutated in this lease.

Priority 2 remains OPEN.

## New learning

`VACANCY IS A PROVEN NEGATIVE CLAIM, NOT THE ABSENCE OF A CURRENT-TREE MATCH.`

Refinement:

`A VACANCY CHECK WITH INCOMPLETE HISTORY MUST FAIL CLOSED, NOT RETURN UNUSED.`

## Resume point

Next bounded work:

`P2 REP-012 PRE-ALLOCATION VACANCY BINDING`

Use the execution-verified gate from Lease 193 as evidence for a separate protected REP-012 contract amendment that places a collision-safe vacancy proof before `ALLOCATE`. Do not perform an EJR migration in the same binding transaction.

Global Connected Baseline, Provider Authentication holds, Phase 1 overall and global `BOOTED / INTEGRITY PASS` remain unchanged.
