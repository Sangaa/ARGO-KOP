# MUT-2026-08-30 — P2 EJR CONTROLLED IDENTITY-REPAIR PLAN — LEASE 204

Status: `CLOSED / PLAN VERIFIED / RESUME-SAFE / NO IDENTITY EXECUTION`
Lease: `R71-20260830-P2-EJR-CONTROLLED-IDENTITY-REPAIR-PLAN-204`
Baseline: `main@329a7700f9d880674ed7ae317c1464be785ce2f8`
Prewrite head: `89c46c600550fb1d70054c6a2089c0507fb51681`
Functional head: `106a6c0e5e25d4cada45bbed4f26b13f5b2b675e`

## Trigger
Lease 203 proved that EJR-211, EJR-214, EJR-219, EJR-301 and EJR-302 are distinct legitimate identity-reuse collisions with recoverable contextual referents. Lease 204 produced the governed repair plan required before any EJR renumbering or path mutation.

## Closed result
The bounded retention rule is:

`FIRST VALID HISTORICAL ALLOCATION RETAINS THE REUSED ID UNLESS STRONGER EVIDENCE PROVES THAT FIRST ALLOCATION WAS INVALID, UNAUTHORIZED, OR NEVER CONSTITUTED AN IDENTITY ALLOCATION.`

No such invalidating evidence was established for the first allocations in these five groups.

Therefore the plan retains the earlier Memory allocations for EJR-211, EJR-214, EJR-219, EJR-301 and EJR-302 and classifies six later legitimate records as future displaced records requiring collision-safe replacement identities. EJR-302 accounts for two of those six displaced records.

No replacement number was allocated. Every future replacement remains blocked until the Lease-193 complete-history vacancy gate returns `VACANT`.

## Consumer/provenance obligations
The plan preserves both record content and referent edges. In particular:
- GT-040 displaced record requires consistent REP-021 exact-path/identity rewrite;
- GT-041 displaced record requires consistent REP-022 exact-path/identity rewrite;
- P221 CI-decision-boundary displaced record requires consistent GOV-013B learning-provenance rewrite if that record is retained under a new identity;
- retained Memory provenance edges remain protected.

## Exact-head functional verification
At `106a6c0e5e25d4cada45bbed4f26b13f5b2b675e`:
- Full-Stack Repository Audit `33327837601` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33327837569` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33327837623` — `SUCCESS`.
- Real Mutation Matrix Regression `33327837648` — `SUCCESS`.

No standalone Internal Document-ID run is claimed for this Repository-doc-only functional scope because none was observed at the exact head.

## Learned rules
1. `FIRST VALID ALLOCATION IS THE DEFAULT RETENTION ANCHOR; LATER CONSUMER AUTHORITY RECOVERS REFERENTS BUT DOES NOT RETROACTIVELY TRANSFER AN ALREADY-USED ID.`
2. `IDENTITY REPAIR IS INCOMPLETE IF A RECORD MOVES BUT A GOVERNED CONSUMER STILL NAMES THE OLD ID OR OLD PATH.`
3. `A TRIPLE COLLISION REQUIRES INDEPENDENT REPLACEMENT VACANCY PROOFS FOR EACH DISPLACED LEGITIMATE RECORD.`
4. `LEGITIMATE CONTENT MUST SURVIVE IDENTITY REPAIR; THE DEFECT IS THE REUSED ID, NOT THE ENGINEERING EVIDENCE.`
5. `REPAIR PLANNING AND REPAIR EXECUTION ARE DISTINCT GOVERNED STATES.`

## Preserved boundaries
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, replacement allocation, or canonical promotion;
- REP-012, REP-016, REP-020 unchanged;
- scanner/gate/workflow semantics unchanged;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- active indexed canonical uniqueness remains previously `CLOSED/PASS`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Resume target
Rediscover live `main`, re-enter from Room 204, then choose exactly one of the six displaced records for a separate execution lease. The first execution target should minimize rewrite risk while having sufficiently explicit consumers to verify repair.

Before any identity mutation:
1. discover a replacement candidate;
2. prove it `VACANT` through the Lease-193 complete-history gate;
3. enumerate exact ID/path consumers and registry/index/manifest obligations;
4. prewrite lease + Mutation Matrix;
5. mutate one displaced record and its required consumers as one governed functional unit;
6. read back and run exact-head verification;
7. close resume-safe.
