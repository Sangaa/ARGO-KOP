# MUT-2026-08-31-P2-EJR-245-DISPOSITION-AND-422-VACANCY-PROOF-293

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: evidence-only disposition confirmation for EJR-245 and complete-history vacancy proof for candidate EJR-422.
Opening main: `6e00c2a0ca138918ae7c2c9bf02fd97da8f57f41`
Pre-write Matrix293: `b5da911147c076ab058b20a5f67d9943a0b09957`
Proof head: `e0c4969f237e2c10aa7752bb1796c9f7f481a7a0`

## Disposition

- `Memory/Engineering_Journal/EJR-245_2026-08-15_P64_SESSION_CLOSURE.md`: RETAINED first valid historical allocation.
- `EJR/EJR-245_2026-08-17_M1_MULTI_CHANNEL_VERIFICATION.md`: DISPLACED legitimate content.
- Memory allocation commit `99e8d80c033da324f0e20dcd2b521cf7d0603d88` at 2026-08-15T07:34:09Z predates root allocation commit `499e90d71a6daadc124b6709910842e24b521795` at 2026-08-17T18:41:14Z.
- Both records are semantically legitimate and independent; zero exact-member-path consumers were observed in the verified cohort evidence.

## Complete-history vacancy proof

Workflow: `EJR Replacement Vacancy Proof 293`
Run: `33402344919` — SUCCESS
Artifact: `9761723214`
Digest: `sha256:f584fccd977b27da606a9f1bf464c17e512f460d4aaaef8bb0ed87b39a10e7ba`

Exact artifact result:
- candidate=`EJR-422`
- current_claims=[]
- historical_claims=[]
- history_complete=true
- history_scope=`all locally reachable refs`
- decision=`VACANT`
- occupied=false
- vacant=true

Proof-head Full-Stack Repository Audit run `33402344855`: SUCCESS.

EJR-422 is reserved solely for the displaced root EJR-245. Identity mutation requires a separate Repair294 Matrix/lease and a fresh hard gate against live main.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
