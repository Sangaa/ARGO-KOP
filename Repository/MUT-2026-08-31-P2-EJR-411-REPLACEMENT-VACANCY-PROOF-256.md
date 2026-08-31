# MUT-2026-08-31-P2-EJR-411-REPLACEMENT-VACANCY-PROOF-256

Status: PREWRITE / VACANCY PROOF PENDING
Scope: Candidate replacement identity EJR-411 only.

## Trigger
Disposition255 classified the later root EJR-217 as displaced and eligible for a fresh replacement identity only after a separate complete-history vacancy proof.

## Candidate discovery
- Current repository search for `EJR-411` found only the Checkpoint254 resume instruction warning not to assume vacancy.
- Commit search for `EJR-411` returned no matching commits.

These are discovery signals only. They do not establish vacancy.

## Authorized action
Run the existing complete-history vacancy gate against EJR-411 from a dedicated workflow using `fetch-depth: 0`, upload the deterministic JSON artifact, and enforce `decision=VACANT`.

No identity repair, rename, delete, H1 rewrite, consumer rewrite, allocation, baseline mutation, or global promotion is authorized inside Lease256.

Priority 2 remains OPEN. Current MEMORY_TO_ROOT baseline remains 26. Global Integrity remains HOLD.
