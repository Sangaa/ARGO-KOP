# MUTATION MATRIX — EJR-212 DISPOSITION + EJR-415 VACANCY PROOF 272

Status: CLOSED / EXECUTION-VERIFIED
Transaction ID: MUT-2026-08-31-P2-EJR-212-DISPOSITION-AND-415-VACANCY-PROOF-272
Opening main: `01d9ae0989cc29d151a17c8dd0377ba47ed5c166`
Prewrite head: `b2ff18d819e9bf483d60e14bc850c10c9768632d`
Lease-open commit: `e3a9a1f1932ba5e73c14e983261e8f3a65c355c7`
Proof-workflow head: `93cb025479f0935d29bf1ac52a62e01896ff8182`
Execution role: HERMUZ

## Verified disposition

Current census group EJR-212 contains two distinct legitimate records. Git path chronology proves the Memory P29 closure allocation predates the root P2 relationship-graph reconciliation allocation. Fresh exact-path and exact-ID review established no stronger consumer/authority evidence invalidating the earlier allocation.

Applying the already verified Lease204 first-valid-allocation rule:
- Memory EJR-212 = RETAINED;
- root EJR-212 = DISPLACED / legitimate content / future one-record repair.

## Verified candidate vacancy

Candidate EJR-415 progressed from discovery-only absence to complete-history VACANT proof through the existing fail-closed vacancy gate on a non-shallow checkout.

- proof run `33381701808`: SUCCESS;
- artifact `9753986473`;
- digest `sha256:84cadea292e357fee6e8b490d7e19cfd585d54ee6ab5f9214579444ee825616c`;
- result: current_claims=[], historical_claims=[], history_complete=true, occupied=false, vacant=true, decision=VACANT;
- Full-Stack #2399 / `33381701718`: SUCCESS;
- M2 #1056 / `33381701670`: SUCCESS.

EJR-415 is reserved solely for the displaced root EJR-212 allocation.

## Verified mutation boundary

Lease272 changed only governed Repository evidence and the dedicated proof workflow. It did not mutate either EJR-212 member, allocate EJR-415, change cohort baseline 22, alter classifier/test semantics, rewrite consumers, modify GOV/REP authority, or promote Global Integrity.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Next safe action: separate pre-write repair lease EJR-212 → EJR-415 with fresh source/blob, target-absence, consumer, and live-main checks.
