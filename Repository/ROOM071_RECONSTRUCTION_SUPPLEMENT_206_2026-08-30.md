# ROOM 071 — RECONSTRUCTION SUPPLEMENT 206 — 2026-08-30

Status: `CLOSED / RESUME-SAFE`
Lease: `R71-20260830-P2-EJR-REPLACEMENT-VACANCY-PROOF-206`
Functional head: `2f3e139c2f9e096c058ae317db878efaa825e01f`

## What was resolved
The first controlled identity-repair candidate was selected as root `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md` because current evidence shows a lower rewrite-risk than records with explicit operational consumers.

`EJR-400` was tested as the replacement candidate through the execution-verified Lease-193 vacancy gate using complete locally reachable Git history.

Result:
- decision: `VACANT`;
- history complete: `true`;
- current claims: none;
- historical claims: none;
- history scope: `all locally reachable refs`.

Artifact evidence:
- workflow `33329388744` — SUCCESS;
- artifact ID `9737186617`;
- digest `sha256:89bac3857098024d48256135d112292f13cad0866368c57a8ea2df3e3db8cfc1`.

Supporting exact-head checks:
- Full-Stack `33329388713` — SUCCESS;
- Runtime `33329388749` — SUCCESS;
- M2 `33329388725` — SUCCESS;
- Real Mutation Matrix `33329388724` — SUCCESS.

## Packaging defect and learning
A prepared atomic prewrite commit was mistakenly not attached through `update_ref`; a contents-API write created a lease-only prewrite commit `94100cb65155179a010a246a3e235e775a699b17`. No functional path had been mutated. Corrective commit `92a0d4fa3da630b9762e5d3685819775309ca309` restored the governed Lease+Matrix pair before functional execution.

Learning:
`PREPARED ATOMIC TREE MUST BE ATTACHED WITH UPDATE_REF; CONTENTS-API FILE WRITE IS NOT A SUBSTITUTE FOR ATOMIC PREWRITE ATTACHMENT.`

## Preserved boundaries
This lease allocates nothing and mutates no EJR record. `EJR-400 = VACANT` only satisfies the pre-allocation proof gate. Priority 2 remains OPEN; Phase 1 remains OPEN; Release Priority 20 remains CLOSED_FOR_PHASE_1; Global Connected Baseline remains OPEN; Global BOOTED / INTEGRITY PASS remains NOT CLAIMED.

## Resume target
Open the next separate repair-execution lease for exactly root EJR-214:
1. re-enumerate current exact-path and semantic-ID consumers;
2. distinguish current operational consumers from immutable historical/provenance evidence;
3. prewrite repair lease + matrix;
4. atomically replace old root path/identity with `EJR-400` while preserving semantic content and chronology;
5. run exact-head Internal Document-ID Audit plus applicable full-stack/runtime/regression checks;
6. inspect evidence that EJR-214 collision is removed and EJR-400 remains unique;
7. close independently.
