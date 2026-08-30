# P2 EJR PATH-BOUND AUTHORITY REVIEW — 203

Status: EVIDENCE-BOUND / NO IDENTITY MUTATION AUTHORIZED
Baseline: main@fd5f54b12039a73b59da9077eea2c66030accf48
Scope: EJR-211, EJR-214, EJR-219, EJR-301, EJR-302

## Result
The five reviewed ambiguity groups are not byte-copy duplicates and are not safely reducible to one namespace-owner rule. Each contains independently legitimate records produced for different sessions or engineering purposes under a reused EJR number.

The bounded classification is:

`5 GROUPS = DISTINCT_LEGITIMATE_COLLISIONS / CONTEXTUAL REFERENTS RECOVERED / HISTORICAL IDENTITY REPAIR JUSTIFIED BUT NOT AUTHORIZED BY THIS LEASE`.

## Group dispositions

### EJR-211
- Governed contextual referent for P29 validated platform lessons: `Memory/Engineering_Journal/EJR-211_2026-08-14_P29_VALIDATED_PLATFORM_LESSONS.md`.
- Evidence: the record states `Validated / Promoted to Canonical Memory Record`; current `MEM-009` promotion provenance and P29 delta name this exact member path.
- Competing Root record `EJR/EJR-211_P2_REL007_REL008_RUNTIME_CONSUMER_REVIEW_2026-08-17.md` is a later, semantically distinct P2 relationship-review journal.
- Disposition: `GOVERNED_REFERENT (P29) + DISTINCT_LEGITIMATE_COLLISION`.

### EJR-214
- Governed contextual referent for P31 search-recovery/session closure: `Memory/Engineering_Journal/EJR-214_2026-08-14_P31_SESSION_CLOSURE.md`.
- Evidence: current canonical memory promotion provenance names the exact Memory member; the record documents the P31 learning promoted into MEM-009.
- Competing Root record `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md` is a later, semantically distinct P2 relationship-validation closure.
- Disposition: `GOVERNED_REFERENT (P31) + DISTINCT_LEGITIMATE_COLLISION`.

### EJR-219
- Governed contextual referent for P36 search-freshness learning: `Memory/Engineering_Journal/EJR-219_2026-08-14_P36_SESSION_CLOSURE.md`.
- Evidence: current `MEM-009` names the exact P36 session record as promotion provenance; the member itself records the permanent-memory promotion decision.
- Competing Root record `EJR/EJR-219_REP016_RESYNC_AND_P5_BOUNDARY_2026-08-17.md` is a later, semantically distinct REP-016/P5 boundary record.
- Disposition: `GOVERNED_REFERENT (P36) + DISTINCT_LEGITIMATE_COLLISION`.

### EJR-301
- Bounded checkpoint referent for GT-040: `EJR/EJR-301_2026-08-24_GT-040_MULTILEVEL_EXPLICIT_ROOT_AGREEMENT.md`.
- Evidence: `Repository/REP-021_SESSION_DELTA_2026-08-24_GT-040.md` names this exact learning-record path and the GT-040 test commit.
- Competing Memory record `Memory/Engineering_Journal/EJR-301_2026-08-22_HERMUZ_P6_CI_EXECUTION_RECHECK.md` is an earlier, semantically distinct P6 CI-execution diagnostic.
- The session delta is checkpoint evidence, not global canonical ownership authority.
- Disposition: `BOUNDED_CHECKPOINT_REFERENT (GT-040) + DISTINCT_LEGITIMATE_COLLISION`.

### EJR-302
Three independently meaningful records share the ID.

1. GT-041 bounded checkpoint referent: `EJR/EJR-302_2026-08-24_GT-041_DEEP_ROOT_CONFLICT.md`.
   - `Repository/REP-022_SESSION_DELTA_2026-08-24_GT-041.md` names this exact path.
2. P221 governance-learning referent: `EJR/EJR-302_2026-08-25_CI_DECISION_BOUNDARY_AND_TOOL_SURFACE_LEARNING.md`.
   - `GOV-013B` declares `Learning Provenance: EJR-302 / P221`; its purpose, incident, and proposed rule semantically match this P221 record, not the GT-041 or P6 records.
   - `GOV-013B` remains `Approved Candidate / Canonical Promotion Pending CI`, so this evidence establishes provenance identity within that governance-candidate context but does not grant global canonical EJR ownership.
3. Earlier Memory diagnostic: `Memory/Engineering_Journal/EJR-302_2026-08-22_HERMUZ_CURRENT_HEAD_STATUS_RECHECK.md`.
   - This is a distinct P6/current-HEAD connector-boundary diagnostic.

Disposition: `TWO CONTEXTUAL REFERENTS RECOVERED + ONE DISTINCT EARLIER RECORD / TRIPLE DISTINCT_LEGITIMATE_COLLISION`.

## Authority conclusion
A consumer can identify which record it means without deciding which record must permanently retain the reused EJR number. Therefore:

`REFERENT RECOVERY != IDENTITY OWNERSHIP`.

The evidence now justifies a future controlled identity-repair plan for these groups, but any reassignment must independently determine:
- which historical record, if any, retains the reused number;
- collision-safe replacement IDs for displaced records using the Lease-193 vacancy gate;
- exact consumer rewrites required for each moved record;
- chronology/provenance preservation;
- manifest/index/registry synchronization obligations;
- no semantic-content loss.

## Learned rules
1. `A DUPLICATE ID CAN REPRESENT MULTIPLE LEGITIMATE RECORDS; VALID CONTENT DOES NOT MAKE REUSED IDENTITY VALID.`
2. `A CURRENT GOVERNED CONSUMER MAY RECOVER A CONTEXTUAL REFERENT WITHOUT GRANTING GLOBAL OWNERSHIP OF THE IDENTIFIER.`
3. `WHEN TWO DIFFERENT GOVERNED CONTEXTS SEMANTICALLY RESOLVE THE SAME ID TO DIFFERENT RECORDS, THE DEFECT IS IDENTITY REUSE, NOT CONTENT DUPLICATION.`
4. `SAME-SURFACE COLLISIONS CAN BE AS REAL AS CROSS-SURFACE COLLISIONS; EJR-302 PROVES NAMESPACE LOCATION ALONE CANNOT RESOLVE OWNERSHIP.`
5. `IDENTITY REPAIR MUST PRESERVE BOTH THE LEGITIMATE CONTENT AND THE CONSUMER-PROVENANCE EDGE THAT IDENTIFIES IT.`

## Boundaries
No EJR mutation, rename, delete, reassignment, migration, normalization, suppression, replacement allocation, or canonical promotion occurred. REP-012, REP-016, REP-020 and integration scanner semantics remain unchanged. Priority 2 and Phase 1 remain OPEN. Global BOOTED / INTEGRITY PASS is not claimed.
