# MUT-2026-08-31-P2-EJR-411-REPLACEMENT-VACANCY-PROOF-256

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Candidate replacement identity EJR-411 only.

## Trigger
Disposition255 classified the later root EJR-217 as displaced and eligible for a fresh replacement identity only after a separate complete-history vacancy proof.

## Candidate discovery
- Current repository search for `EJR-411` found only the Checkpoint254 resume instruction warning not to assume vacancy.
- Commit search for `EJR-411` returned no matching commits.

These were discovery signals only and were not treated as vacancy proof.

## Execution evidence
Dedicated workflow `EJR Replacement Vacancy Proof 256`, run `33368058506`, executed from prewrite head `a120a03ea0015190e7584c565344049940261396` with complete checkout history and concluded SUCCESS.

Artifact `9748981322`, digest `sha256:9685d00ce7a4312b1a3c9d068ea467c48b0405da35ab03789327d289bf0dedcd`, proved:
- candidate=`EJR-411`
- current_claims=[]
- historical_claims=[]
- history_complete=true
- history_scope=`all locally reachable refs`
- occupied=false
- vacant=true
- decision=`VACANT`

## Decision
EJR-411 is authorized for exactly one bounded replacement allocation for the displaced root EJR-217 record under the next separate identity-repair lease.

## Boundaries
No identity repair, rename, delete, H1 rewrite, consumer rewrite, baseline mutation, or global promotion occurred inside Lease256. Priority 2 remains OPEN. Current MEMORY_TO_ROOT baseline remains 26. Global Integrity remains HOLD.
