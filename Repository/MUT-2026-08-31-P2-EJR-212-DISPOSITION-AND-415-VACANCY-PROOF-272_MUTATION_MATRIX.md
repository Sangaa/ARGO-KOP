# MUTATION MATRIX — EJR-212 DISPOSITION + EJR-415 VACANCY PROOF 272

Status: PREWRITE / EXECUTION NOT AUTHORIZED YET
Transaction ID: MUT-2026-08-31-P2-EJR-212-DISPOSITION-AND-415-VACANCY-PROOF-272
Opening main: `01d9ae0989cc29d151a17c8dd0377ba47ed5c166`
Execution role: HERMUZ

## Trigger and prior-learning retrieval

Repair270 + Lease271 closed the previous Priority-2 chain with a deterministic MEMORY_TO_ROOT census of 22/22, history_complete=true, classification_complete=true, decision=CENSUSED.

Fresh risk/consumer/chronology review selected EJR-212 rather than numeric-order continuation:

- current census group EJR-212 contains exactly two distinct records: earlier Memory P29 closure and later root P2 relationship-graph reconciliation;
- exact member-path searches for both current paths returned no consumers;
- current exact-ID search outside census/baseline evidence did not establish an operational consumer selecting either EJR-212 member;
- Git path history dates the Memory allocation to 2026-08-14 and the root allocation to 2026-08-17;
- both records are legitimate evidence records with distinct semantic content.

Prior learning is DIRECTLY APPLICABLE from Lease204 and subsequent verified repairs 207/212/216/220/224/227/266/270:

`FIRST VALID HISTORICAL ALLOCATION RETAINS THE REUSED ID UNLESS STRONGER EVIDENCE PROVES THAT FIRST ALLOCATION WAS INVALID, UNAUTHORIZED, OR NEVER CONSTITUTED AN IDENTITY ALLOCATION.`

No invalidating evidence was found for the Memory EJR-212 allocation. Therefore this prewrite classifies:

- `Memory/Engineering_Journal/EJR-212_2026-08-14_P29_SESSION_CLOSURE.md` = RETAINED earlier valid allocation;
- `EJR/EJR-212_P2_CURRENT_RELATIONSHIP_GRAPH_RECONCILIATION_2026-08-17.md` = DISPLACED later legitimate allocation / future one-record repair candidate.

## Candidate discovery boundary

Candidate `EJR-415` is only a discovery candidate at prewrite time.

Current evidence:
- exact current code search for `EJR-415` returned zero results;
- current target path probe returned 404;
- Git commits query for `EJR/EJR-415*` returned no path history.

These checks do NOT prove complete-history vacancy. EJR-415 MUST NOT be allocated until the existing fail-closed `Quality/Integration/ejr_allocation_vacancy_gate.py` runs on a non-shallow checkout and returns `decision=VACANT`.

## Authorized scope for Lease272

This transaction may only:
1. persist the EJR-212 retained/displaced disposition evidence;
2. add a dedicated complete-history vacancy-proof workflow for candidate EJR-415;
3. execute the existing vacancy gate with `fetch-depth: 0`;
4. record the resulting run/artifact/digest and close this Matrix only if the proof is complete.

## Explicit exclusions

Lease272 does NOT authorize:
- renaming/deleting/moving either EJR-212 member;
- allocating EJR-415;
- changing H1/body/footer content of any EJR or Memory record;
- changing MEMORY_TO_ROOT baseline 22;
- changing classifier, scanner, tests, GOV/REP authority, consumers, or Global Integrity;
- treating current-search absence as historical vacancy.

## Verification contract

Before closure:
- rediscover live main before every write;
- exact compare must show only this Matrix, its Lease272 evidence record, and the dedicated vacancy workflow as intended;
- vacancy workflow must prove non-shallow history and enforce `decision == VACANT`;
- Full-Stack/Runtime/M2/Real Mutation Matrix results applicable to the exact head must be read to completion;
- if EJR-415 is OCCUPIED or history is incomplete, stop and do not open an identity-repair lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
