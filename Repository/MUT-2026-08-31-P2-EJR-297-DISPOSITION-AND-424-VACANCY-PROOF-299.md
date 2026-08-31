# MUT-2026-08-31-P2-EJR-297-DISPOSITION-AND-424-VACANCY-PROOF-299

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: evidence-only disposition confirmation for EJR-297 and complete-history vacancy proof for candidate EJR-424.
Opening main: `2981ed42ed8c48a93ce659d5d7ba7fe0ee068ba8`
Pre-write Matrix299: `b40b9fc89e7604bb142af31d66fc2c21755c954e`
Proof head: `7ce6cbec0a21567e22834c48f972a32e0817451b`

## Closed disposition

- RETAINED allocation: `Memory/Engineering_Journal/EJR-297_2026-08-21_HERMUZ_P6_SCOPE_BOUNDARY_REPAIR_STEP02_FETCH_GATE.md`.
- DISPLACED legitimate content: `EJR/EJR-297_2026-08-22_HERMUZ_BLIND_LAW_PREDICTION_TEST.md`.
- Memory allocation commit `edf6f4d2586ac2449b2b46cac3d94d2738144ce0` at 2026-08-21T16:20:41Z predates root allocation commit `ae7955021133b8e31c85e8b2a7915349f257b0ea` at 2026-08-22T02:01:56Z.
- Both records remain semantically legitimate independent records; no content identity was mutated under Lease299.

## Complete-history successor proof

Workflow run `33410673926`: SUCCESS.
Artifact `9764977768`, digest `sha256:68d1f7e5ea2cf9590f9477376c15edeaccd1cbeb5f4782057b5f907acadf5230`.
Exact JSON proves:
- candidate=`EJR-424`;
- decision=`VACANT`;
- current_claims=[];
- historical_claims=[];
- history_complete=true;
- history_scope=`all locally reachable refs`.

Proof-head Full-Stack run `33410673865`: SUCCESS.

EJR-424 is now reserved solely for the displaced root EJR-297 content. Identity repair requires a separate governed repair lease; no identity mutation occurred in Lease299.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
