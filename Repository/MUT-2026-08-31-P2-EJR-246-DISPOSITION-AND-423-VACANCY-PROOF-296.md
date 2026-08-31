# MUT-2026-08-31-P2-EJR-246-DISPOSITION-AND-423-VACANCY-PROOF-296

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: evidence-only disposition confirmation for EJR-246 and complete-history vacancy proof for candidate EJR-423.
Opening main: `98c81b0920425b2dc9a14baf5026c72ddf46b56e`
Pre-write Matrix296: `759602558deddd46ba525b1c2f56c64c352ca0ea`
Proof head: `300f8df41af7c6d1e9f12bf914916c6718ebf6bd`

## Closed disposition

- RETAINED allocation: `Memory/Engineering_Journal/EJR-246_2026-08-15_P65_SESSION_CLOSURE.md`.
- DISPLACED legitimate content: `EJR/EJR-246_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md`.
- Memory allocation commit `899924bf6916129db59ef2a5eb035c5f969ea5c7` at 2026-08-15T07:35:51Z predates root allocation commit `35ec18ca6a0444ecc945e72fe10ac4374713dbdd` at 2026-08-17T18:54:52Z.
- Both records remain semantically legitimate independent records; no content was mutated under Lease296.

## Complete-history successor proof

Workflow run `33409267610`: SUCCESS.
Artifact `9764434172`, digest `sha256:f7ab8977442df306625d11897cfd79a7048ceb37af2a42efb7627729ed8ee202`.
Exact JSON proves:
- candidate=`EJR-423`;
- decision=`VACANT`;
- current_claims=[];
- historical_claims=[];
- history_complete=true;
- history_scope=`all locally reachable refs`.

Proof-head Full-Stack run `33409267656`: SUCCESS.

EJR-423 is now reserved solely for the displaced root EJR-246 content. Identity repair requires a separate governed repair lease; no identity mutation occurred in Lease296.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
