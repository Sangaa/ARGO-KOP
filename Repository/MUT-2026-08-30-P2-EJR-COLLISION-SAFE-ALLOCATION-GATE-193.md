# P2 EJR COLLISION-SAFE ALLOCATION GATE — LEASE 193

Transaction ID: `MUT-2026-08-30-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193`
Lease: `R71-20260830-P2-EJR-COLLISION-SAFE-ALLOCATION-GATE-193`
Protocol: HERMUZ / GOV-014
Status: `PREWRITE / FUNCTIONAL MUTATION NOT YET APPLIED`
Entry head: `cb9dd60f2d910958c792ccb53d2db15bee077786`

## Evidence basis

Lease 192 proved that historical identity-repair allocations selected already-occupied EJR IDs because vacancy was not established across every identity-bearing surface and history.

Required gate from Lease 192:

`METADATA → H1 → FILENAME → GIT HISTORY → ALLOCATE`

REP-012 currently begins material mutation with `ALLOCATE → READ → ...`; this lease does not edit REP-012. It first builds and verifies a deterministic executable vacancy checker so control-plane binding can be a separate governed change after execution evidence exists.

## Authorized functional scope

Exactly:

1. create `Quality/Integration/ejr_allocation_vacancy_gate.py`;
2. create `Quality/Integration/test_ejr_allocation_vacancy_gate.py`;
3. update `.github/workflows/internal-id-audit.yml` so the vacancy-gate tests run with complete checkout history (`fetch-depth: 0`);
4. update the companion Mutation Matrix in the same functional change set.

No EJR rename, deletion, ID rewrite, detector suppression, ambiguity-membership reduction, REP-012 mutation, REP-016 mutation, or authority promotion is authorized.

## Semantic contract

A candidate `EJR-NNN` is considered occupied when any qualifying claim is found on these surfaces:

- qualified `Document ID` metadata;
- document-level first-H1 identity;
- filename identity prefix;
- reachable Git history containing a historical qualifying claim or filename occupancy.

The gate must fail closed when Git reports a shallow repository. A shallow checkout cannot prove historical vacancy.

The gate reports evidence; it does not allocate or rewrite an ID.

## Required verification

- prewrite must precede functional mutation;
- exact live-parent recheck before fast-forward;
- exact functional changed-set compare / unexpected paths = 0;
- regression tests for current metadata/H1/filename occupancy;
- regression proving deleted historical identity remains occupied;
- regression proving shallow history cannot return vacant;
- regression proving a genuinely unused candidate can return vacant only with complete history;
- Internal Document-ID Audit workflow SUCCESS on exact functional head;
- Full-Stack, Runtime/Integration, M2 and Real Mutation Matrix SUCCESS where triggered;
- read-back of code, tests, workflow and Matrix;
- Priority 2 remains OPEN after this bounded tooling gate.

## Learning boundary

`VACANCY IS A PROVEN NEGATIVE CLAIM, NOT THE ABSENCE OF A CURRENT-TREE MATCH.`
