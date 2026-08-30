# P2 REP-012 PRE-ALLOCATION VACANCY BINDING — LEASE 194

Transaction ID: `MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
Lease: `R71-20260830-P2-REP012-PREALLOCATION-VACANCY-BINDING-194`
Protocol: HERMUZ / GOV-014
Status: `OPEN / PREWRITE / FUNCTIONAL MUTATION NOT YET APPLIED`
Entry head: `b2eb68d7bb2dd5831ac5009103faba66b4922f6f`

## Bounded purpose

Bind the execution-verified EJR vacancy proof from Lease 193 into the REP-012 allocation control contract so an EJR identity candidate cannot reach `ALLOCATE` merely because the current tree appears unused.

This lease is control-plane binding only.

## Evidence basis

Lease 193 established an execution-verified vacancy gate with decisions `OCCUPIED`, `HISTORY_INCOMPLETE`, and `VACANT` across qualified Document ID metadata, first-H1 identity, filename prefix, and all locally reachable Git history.

Current REP-012 v1.0.9 still begins its material mutation sequence with:

`ALLOCATE → READ → VERIFY IDENTITY → ...`

That sequence lacks an explicit pre-allocation vacancy proof for new EJR identities.

## Authorized functional scope

1. `Repository/REP-012_REPOSITORY_ALLOCATION_REGISTRY.md`
2. `Repository/MUT-2026-08-30-P2-REP012-PREALLOCATION-VACANCY-BINDING-194_MUTATION_MATRIX.md`

Expected REP-012 changes are narrowly limited to:

- version increment for the governed contract amendment;
- replacement of the Section 14 material-mutation sequence with an explicit EJR candidate vacancy-proof stage before `ALLOCATE`;
- explicit fail-closed semantics for `HISTORY_INCOMPLETE`;
- explicit occupancy surfaces and bounded reachable-history scope;
- reference to the execution-verified gate implementation and Lease 193 evidence.

All unrelated REP-012 content is `KEEP` and must be preserved.

## Forbidden scope

- no EJR content/path/identity migration;
- no rename, delete, reassignment, or replacement EJR allocation;
- no ambiguity suppression or detector-membership reduction;
- no REP-016 change;
- no Release Priority 20 reopening;
- no authority promotion;
- no claim that unreachable external history was inspected;
- no Priority 2 or global closure.

## Closure conditions

- Mutation Matrix exists before the functional repository write;
- exact source REP-012 blob is read completely;
- candidate preserves all non-target content;
- functional compare contains only authorized paths;
- final live parent is rechecked before `force=false` fast-forward;
- post-write REP-012 read-back matches the candidate blob;
- exact-head CI/integrity evidence is observed and recorded;
- session checkpoint is persisted as CLOSED / RESUME-SAFE.
