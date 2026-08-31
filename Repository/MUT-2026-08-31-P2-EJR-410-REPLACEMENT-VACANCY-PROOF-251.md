# MUT-2026-08-31-P2-EJR-410-REPLACEMENT-VACANCY-PROOF-251

Status: PREWRITE / VACANCY EXECUTION PENDING
Scope: Complete-history vacancy proof for candidate EJR-410 only.

## Candidate discovery
Current code search found no allocation claim for EJR-410; its only hit was Checkpoint249's warning not to assume EJR-410 availability. Commit search returned no EJR-410 match. These are discovery signals only and do not establish vacancy.

## Execution contract
Dedicated workflow `.github/workflows/ejr-replacement-vacancy-proof-251.yml` must checkout complete history and execute `Quality/Integration/ejr_allocation_vacancy_gate.py EJR-410`.

Allocation is authorized only if the produced artifact proves:
- current_claims=[]
- historical_claims=[]
- history_complete=true
- vacant=true
- decision=VACANT.

Any OCCUPIED or HISTORY_INCOMPLETE result blocks allocation.

## Boundaries
This lease performs no identity mutation, rename, delete, H1 rewrite, consumer rewrite, allocation, baseline change, or global promotion. EJR-410 remains only a candidate until execution evidence closes this lease.
