# ROOM 071 — RECONSTRUCTION SUPPLEMENT 204 — 2026-08-30

Status: `CLOSED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-CONTROLLED-IDENTITY-REPAIR-PLAN-204`
Functional head: `106a6c0e5e25d4cada45bbed4f26b13f5b2b675e`

## What was resolved
Lease 204 converted the five proven identity-reuse collision groups from classification into a governed repair plan without executing any identity mutation.

Bounded retention rule:

`FIRST VALID HISTORICAL ALLOCATION RETAINS THE REUSED ID UNLESS STRONGER EVIDENCE PROVES THAT FIRST ALLOCATION WAS INVALID, UNAUTHORIZED, OR NEVER CONSTITUTED AN IDENTITY ALLOCATION.`

No invalidating evidence was established for the first allocations in EJR-211, EJR-214, EJR-219, EJR-301 or EJR-302.

## Planned retention
Retain the earlier Memory records under:
- EJR-211 — P29 validated platform lessons;
- EJR-214 — P31 session closure;
- EJR-219 — P36 session closure;
- EJR-301 — P6 CI execution recheck;
- EJR-302 — current-head status recheck.

## Planned displacement
Six later legitimate records require future replacement identities:
1. Root EJR-211 P2 REL007/REL008 runtime-consumer review.
2. Root EJR-214 P2 session closure.
3. Root EJR-219 REP-016 resync/P5 boundary.
4. Root EJR-301 GT-040 record.
5. Root EJR-302 GT-041 record.
6. Root EJR-302 P221 CI decision-boundary/tool-surface learning record.

No replacement number is currently allocated. Every future candidate remains blocked until the Lease-193 gate proves `VACANT` with complete locally reachable history.

## Consumer obligations
- GT-040 repair must update REP-021 exact-path/identity references consistently.
- GT-041 repair must update REP-022 exact-path/identity references consistently.
- P221 repair must update GOV-013B learning provenance consistently if the record remains retained under a new identity.
- retained Memory provenance edges must not be damaged.

## Exact-head functional evidence
At `106a6c0e5e25d4cada45bbed4f26b13f5b2b675e`:
- Full-Stack Repository Audit `33327837601` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33327837569` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33327837623` — `SUCCESS`.
- Real Mutation Matrix Regression `33327837648` — `SUCCESS`.

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
Rediscover live `main`, re-enter from this checkpoint, and choose exactly one displaced record for a separate repair-execution lease.

Selection principle: choose the lowest-risk record whose consumer surface is explicit enough to verify complete repair. Before mutation, prove one replacement candidate `VACANT`, enumerate all consumers and synchronization obligations, prewrite lease+matrix, then mutate and verify one material record only.
