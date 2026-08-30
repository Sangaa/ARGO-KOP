# MUT-2026-08-30-P2-EJR-PATH-BOUND-AUTHORITY-REVIEW-203

Status: `CLOSED / EXECUTION-VERIFIED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-PATH-BOUND-AUTHORITY-REVIEW-203`
Functional head: `311d1b7e6928a47bd45df594b65ffe7aa3797b71`

## Scope closed
A bounded evidence-only authority/disposition review was completed for `EJR-211`, `EJR-214`, `EJR-219`, `EJR-301`, and `EJR-302`.

Result:

`5 GROUPS = DISTINCT_LEGITIMATE_COLLISIONS / CONTEXTUAL REFERENTS RECOVERED / HISTORICAL IDENTITY REPAIR JUSTIFIED BUT NOT AUTHORIZED BY THIS LEASE`.

No identity mutation is authorized by this closure.

## Dispositions
- `EJR-211`: governed P29 contextual referent = `Memory/Engineering_Journal/EJR-211_2026-08-14_P29_VALIDATED_PLATFORM_LESSONS.md`; competing Root record is a distinct later P2 relationship review.
- `EJR-214`: governed P31 contextual referent = `Memory/Engineering_Journal/EJR-214_2026-08-14_P31_SESSION_CLOSURE.md`; competing Root record is a distinct later P2 session closure.
- `EJR-219`: governed P36 contextual referent = `Memory/Engineering_Journal/EJR-219_2026-08-14_P36_SESSION_CLOSURE.md`; competing Root record is a distinct later REP-016/P5 record.
- `EJR-301`: bounded GT-040 checkpoint referent = `EJR/EJR-301_2026-08-24_GT-040_MULTILEVEL_EXPLICIT_ROOT_AGREEMENT.md`; competing Memory record is a distinct earlier P6 diagnostic.
- `EJR-302`: triple distinct legitimate collision. GT-041 resolves to `EJR/EJR-302_2026-08-24_GT-041_DEEP_ROOT_CONFLICT.md` through REP-022; P221 governance-learning resolves semantically to `EJR/EJR-302_2026-08-25_CI_DECISION_BOUNDARY_AND_TOOL_SURFACE_LEARNING.md` through GOV-013B; the Memory member is a distinct earlier P6/current-HEAD diagnostic.

## Authority boundary
`REFERENT RECOVERY != IDENTITY OWNERSHIP`.

Current governed consumers identify which record they mean in bounded contexts, but they do not by themselves decide which historical record permanently retains a reused EJR number.

## Exact-head functional verification
At `311d1b7e6928a47bd45df594b65ffe7aa3797b71`:
- Full-Stack Repository Audit `33326986664` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33326986700` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33326986683` — `SUCCESS`.
- Real Mutation Matrix Regression `33326986675` — `SUCCESS`.

The first immediate `head_sha` Actions lookup returned zero runs. This was not accepted as absence evidence. A broader branch/event retrieval recovered the exact-head push runs, and a later direct `head_sha` query returned the four exact runs above. The event is classified as transient retrieval/timing surface lag, with no unsupported claim about GitHub implementation cause.

## Learned rules
1. `A DUPLICATE ID CAN REPRESENT MULTIPLE LEGITIMATE RECORDS; VALID CONTENT DOES NOT MAKE REUSED IDENTITY VALID.`
2. `A CURRENT GOVERNED CONSUMER MAY RECOVER A CONTEXTUAL REFERENT WITHOUT GRANTING GLOBAL OWNERSHIP OF THE IDENTIFIER.`
3. `WHEN TWO DIFFERENT GOVERNED CONTEXTS SEMANTICALLY RESOLVE THE SAME ID TO DIFFERENT RECORDS, THE DEFECT IS IDENTITY REUSE, NOT CONTENT DUPLICATION.`
4. `SAME-SURFACE COLLISIONS CAN BE AS REAL AS CROSS-SURFACE COLLISIONS; EJR-302 PROVES NAMESPACE LOCATION ALONE CANNOT RESOLVE OWNERSHIP.`
5. `IDENTITY REPAIR MUST PRESERVE BOTH THE LEGITIMATE CONTENT AND THE CONSUMER-PROVENANCE EDGE THAT IDENTIFIES IT.`
6. `AN IMMEDIATE ZERO-RUN ACTIONS LOOKUP IS NOT EVIDENCE THAT NO RUN EXISTS WHEN AN INDEPENDENT ACTIONS SURFACE CAN STILL RECOVER THE EXACT-HEAD RUN.`

## Preserved boundaries
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, replacement allocation, or canonical promotion;
- REP-012, REP-016, REP-020 unchanged;
- integration scanner/gate semantics unchanged;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- active indexed canonical uniqueness remains previously `CLOSED/PASS`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no real trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Next governed step
A separate lease must build a controlled identity-repair plan before any reassignment. It must decide retention/reassignment record-by-record, prove every replacement candidate vacant using the Lease-193 collision-safe vacancy gate, enumerate exact consumer rewrites, preserve chronology and provenance, and account for registry/index/manifest synchronization. This lease does not authorize that mutation.
