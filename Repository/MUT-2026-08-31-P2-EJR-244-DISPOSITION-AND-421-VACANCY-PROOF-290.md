# MUT-2026-08-31-P2-EJR-244-DISPOSITION-AND-421-VACANCY-PROOF-290

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: evidence-only disposition confirmation for EJR-244 and complete-history vacancy proof for candidate EJR-421.
Opening main: `34bade3b130d54f827dd4abea99d6c83d4132429`
Pre-write Matrix290: `bbbab98aec1b3d7d71a61ee494614c29e864f2b2`
Proof head: `19804da36648a1968dc4ca2bd95678fd8f9daf5a`

## Disposition

- `Memory/Engineering_Journal/EJR-244_2026-08-15_P62_SESSION_CLOSURE.md`: RETAINED first valid historical allocation; allocation commit `82ccbdda485297ed8a206c5dad960ce44f076cbc` at 2026-08-15T07:27:45Z.
- `EJR/EJR-244_2026-08-17_MULTI_CHANNEL_TRAINING_PRIORITY.md`: DISPLACED legitimate content; allocation commit `1510161a687a336e8efa52b522ed8ea8aea942a4` at 2026-08-17T18:36:56Z.
- Both records are semantically legitimate and independent; zero exact-member-path consumers were observed in the verified cohort evidence.

## Complete-history vacancy proof

Workflow: `EJR Replacement Vacancy Proof 290`
Run: `33396768282` — SUCCESS
Artifact: `9759617449`
Digest: `sha256:28a790a1c1bf3a3a4425602426ea3351be2f09c4c469add1e21723970a55d96c`

Exact artifact result:
- candidate=`EJR-421`
- current_claims=[]
- historical_claims=[]
- history_complete=true
- history_scope=`all locally reachable refs`
- decision=`VACANT`
- occupied=false
- vacant=true

Proof-head Full-Stack Repository Audit run `33396768304`: SUCCESS.

EJR-421 is reserved solely for the displaced root EJR-244. Identity mutation requires a separate Repair291 Matrix/lease and fresh hard gate.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
