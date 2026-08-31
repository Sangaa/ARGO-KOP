# MUT-2026-08-31-P2-EJR-410-REPLACEMENT-VACANCY-PROOF-251

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Complete-history vacancy proof for candidate EJR-410 only.

## Candidate discovery
Current code search found no allocation claim for EJR-410; its only hit was Checkpoint249's warning not to assume EJR-410 availability. Commit search returned no EJR-410 match. These were discovery signals only and were not treated as proof.

## Execution evidence
Dedicated workflow `EJR Replacement Vacancy Proof 251`, run `33365364420`, completed SUCCESS at exact head `729e52116771a1f90c302deb34274bb550bdaf44`.

Artifact `9748081220`, digest `sha256:d768a156daa894a30cfd2bf18f3f1a37e3cfdda97914383622e6933fd95800e5`, proved:
- candidate=`EJR-410`
- current_claims=[]
- historical_claims=[]
- history_complete=true
- history_scope=`all locally reachable refs`
- occupied=false
- vacant=true
- decision=`VACANT`.

EJR-410 is therefore authorized for one subsequent bounded replacement allocation.

## Boundaries
This lease performed no identity mutation, rename, delete, H1 rewrite, consumer rewrite, allocation, baseline change, or global promotion. Current MEMORY_TO_ROOT baseline remains 27. Priority 2 remains OPEN; Global Integrity remains HOLD.
