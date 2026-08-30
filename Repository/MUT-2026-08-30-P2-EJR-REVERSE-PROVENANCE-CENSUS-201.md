# MUT-2026-08-30 — P2 EJR REVERSE-DIRECTION PROVENANCE CENSUS — LEASE 201

Status: `CLOSED / EXECUTION-VERIFIED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-REVERSE-PROVENANCE-CENSUS-201`
Baseline: `main@62b08f67af7f1f58e23236f8563d590b4d24cf04`
Prewrite head: `041459ae60bcabeb53610af0d91b52da0c5d5f60`
Functional head: `f554672b8fced5e9aa71154b9c5ce5f7df3efa2b`

## Purpose and bounded result
Lease 201 added deterministic content/reference/consumer provenance observability for the four reverse-direction H1-only ambiguity groups proven by Lease 199:

- `EJR-178`
- `EJR-189`
- `EJR-222`
- `EJR-338`

The bounded classification is:

`REVERSE-DIRECTION GROUPS CENSUSED / NO PATH-LEVEL CONSUMER BINDING / MIXED PROVENANCE SHAPES / OWNERSHIP UNRESOLVED`.

No identity mutation or canonical-owner decision is authorized.

## Functional scope executed
1. `Quality/Integration/ejr_reverse_provenance_census.py` — ADD.
2. `Quality/Integration/test_ejr_reverse_provenance_census.py` — ADD.
3. `.github/workflows/internal-id-audit.yml` — MODIFY only to test, emit and upload the new evidence report.
4. `Repository/MUT-2026-08-30-P2-EJR-REVERSE-PROVENANCE-CENSUS-201_MUTATION_MATRIX.md` — synchronized same-change evidence.

Pre-ref compare proved exactly these four paths and no extras.

## Fail-closed contract
The classifier preserves the observed heterogeneous cardinalities as explicit evidence guards:
- `EJR-178 = 3`
- `EJR-189 = 2`
- `EJR-222 = 4`
- `EJR-338 = 2`

Every current member must remain `FIRST_H1_FALLBACK`. Shallow history returns `HISTORY_INCOMPLETE`; membership/cardinality/source drift returns `PARTIAL` rather than being silently reinterpreted.

## Exact-head verification
At functional head `f554672b8fced5e9aa71154b9c5ce5f7df3efa2b`:
- Internal Document-ID Audit `33322805862` — `SUCCESS`.
- Full-Stack Repository Audit `33322805741` — `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests `33322805722` — `SUCCESS`.
- M2 Multi-Channel Proposal Training `33322805724` — `SUCCESS`.
- Real Mutation Matrix Regression `33322805744` — `SUCCESS`.

Reverse-provenance artifact:
- ID `9735374854`.
- digest `sha256:05576555bf8754be22ed99440083400fc7b3783ca6d4ab8c0ab711e5abf7de2c`.
- `history_complete = true`.
- `classification_complete = true`.
- `decision = CENSUSED`.
- `group_count = 4`.

## Provenance observations
Across all `11` current members:
- every member has a distinct SHA-256 content digest within its ambiguity group;
- no external tracked-text consumer names any exact member path;
- therefore no path-level owner can be selected from current consumer evidence.

### EJR-178
Three distinct records (`ROOT_EJR=1`, `MEMORY_EJR=2`). The records concern different closure/revalidation episodes. `REP-020_REVALIDATION_ADDENDUM_2026-08-14_P8.md` contains an ID-level `EJR-178` conflict reference whose semantics align strongly with the PR #8 reconciliation member, but the consumer does not name that member's exact path. This narrows likely referent context but does not prove path binding.

### EJR-189
Two distinct records (`ROOT_EJR=1`, `MEMORY_EJR=1`) with different event labels/time contexts. Current evidence supports ID-reuse provenance, but no exact-path consumer selects an owner.

### EJR-222
Four distinct records (`ROOT_EJR=1`, `MEMORY_EJR=3`). This group is not safely classifiable as either "all duplicate" or "all independent reuse":
- the root P39 and memory P39 records share the same session/date/title and materially overlapping event facts but are different content variants;
- P40 and the later P4 record represent additional distinct journal events under the same ID.

Therefore `EJR-222` is a **compound ambiguity** containing same-event parallel/derivative variants plus later ID reuse.

### EJR-338
Two distinct records (`ROOT_EJR=1`, `MEMORY_EJR=1`) for materially different topics. `MUT-2026-08-28-EXPERIENCE-SPINE-IGT-001.md` refers to `EJR-338 transfer-learning evidence`, semantically aligning with the IGT/LPE transfer-learning member, but again no exact path is named. Context narrows the likely referent without establishing path-level authority.

## Learned rules
1. `HETEROGENEOUS AMBIGUITY CARDINALITY IS EVIDENCE AND MUST NOT BE NORMALIZED TO FIT A PREVIOUS CLASSIFIER.`
2. `SEMANTIC CONTEXT CAN NARROW THE LIKELY REFERENT OF AN AMBIGUOUS ID, BUT IT MUST NOT BE UPGRADED TO PATH-LEVEL BINDING WITHOUT AN EXPLICIT PATH, IMMUTABLE CONTENT FINGERPRINT, OR OTHER AUTHORITATIVE IDENTIFIER.`
3. `A REPEATED-ID GROUP MAY MIX SAME-EVENT VARIANTS WITH LATER ID REUSE; GROUP-LEVEL ALL-REUSE OR ALL-DUPLICATE LABELS CAN ERASE PROVENANCE STRUCTURE.`
4. `CONTENT DISTINCTNESS DOES NOT BY ITSELF PROVE EVENT DISTINCTNESS; SEMANTIC EVENT IDENTITY AND RECORD IDENTITY ARE SEPARATE QUESTIONS.`
5. `AN INITIAL ZERO WORKFLOW-RUN LOOKUP IMMEDIATELY AFTER REF UPDATE IS NOT EVIDENCE OF WORKFLOW ABSENCE; DIRECT EXACT-HEAD DISCOVERY MUST BE RETRIED BEFORE CLASSIFICATION.`

## Preserved boundaries
- no EJR mutation, migration, rename, delete, reassignment, normalization, suppression, replacement allocation, or canonical promotion;
- Internal Document-ID scanner semantics unchanged;
- REP-012, REP-016, REP-020 unchanged;
- six MIXED explicit-ID ambiguity groups remain separate and unsuppressed;
- Priority 2 historical/provenance identity scope remains `OPEN`;
- Phase 1 remains `OPEN`;
- Release Priority 20 remains `CLOSED_FOR_PHASE_1`;
- Global Connected Baseline remains `OPEN`;
- Provider Authentication remains `HARD HOLD` where no trust anchor exists;
- Memory full-folder integrity remains `NOT CERTIFIED`;
- Global `BOOTED / INTEGRITY PASS` remains `NOT CLAIMED`.

## Resume direction
Rediscover live `main`, re-enter from Room 071 Supplement 201, then inspect the current Priority-2 queue/authority evidence before selecting the next bounded historical/provenance work item. This lease authorizes no migration or ownership mutation.
