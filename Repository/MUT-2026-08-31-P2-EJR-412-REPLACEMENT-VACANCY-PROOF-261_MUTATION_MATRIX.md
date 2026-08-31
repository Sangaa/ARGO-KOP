# MUTATION MATRIX — EJR-412 REPLACEMENT VACANCY PROOF 261

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-412-REPLACEMENT-VACANCY-PROOF-261
Opening main: `d0d1d7a528f14cb3706e7fc3dc6ea642b1835e91`
Pre-write matrix commit: `5f0af85e41e439854f6ac78d192e065ca109b01d`
Lease opening commit: `fbd75ebf162917b1042d9ce5055931acf8dd8158`
Workflow commit: `e3ea184fd6fb094f9ea468912c68dc28111991c7`
Lease closure commit: `ab486dd6e273ee7d46f4afc2e14f3d3162a890cf`
Candidate: `EJR-412`
Source disposition: `MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260.md`

## Proof result

Dedicated complete-history run `33370689585` completed SUCCESS. Artifact `9749915855`, digest `sha256:911733c87a5879dc4805fd27509d1e156cfdc3879342ff4b46fb8ae590a162e7`, proved:
- `current_claims=[]`
- `historical_claims=[]`
- `history_complete=true`
- `occupied=false`
- `vacant=true`
- `decision=VACANT`

The proof workflow verified a non-shallow checkout and enforced `VACANT` as a hard condition.

## Mutation reconciliation

| Surface | Action in Lease261 | Expected state before proof | Post-proof |
|---|---|---|---|
| EJR-412 allocation | PROVE ONLY | unknown / unproven | VERIFIED VACANT; one bounded future allocation authorized |
| Complete history | READ/ANALYZE | required | VERIFIED COMPLETE |
| Vacancy artifact | CREATE BY CI | absent | VERIFIED artifact 9749915855 |
| Root EJR-232 | KEEP | displaced by Lease260 | VERIFIED unchanged |
| Memory EJR-232 | KEEP | retained by Lease260 | VERIFIED unchanged |
| Identity mutation | NONE | forbidden in Lease261 | VERIFIED none |
| MEMORY_TO_ROOT baseline | KEEP | 25 | VERIFIED unchanged |
| Global integrity | KEEP | HOLD | VERIFIED HOLD |

## CI / integration evidence

- Pre-write matrix commit passed Full-Stack run 2348 and Runtime run 2124.
- Lease opening commit passed Full-Stack run 2349 and Runtime run 2125.
- Workflow commit passed dedicated vacancy run `33370689585`, Full-Stack run `33370689532` / 2350, and M2 run `33370689524`.
- Lease closure commit `ab486dd6e273ee7d46f4afc2e14f3d3162a890cf` passed Full-Stack run `33370830647` / 2351, Runtime run `33370830255` / 2126, and M2 run `33370830233`.
- The closed Lease261 record was re-read from current main after write.

## Closure

`LEASE261 = CLOSED / EJR-412 VACANT / EXECUTION-VERIFIED / RESUME-SAFE`

EJR-412 is reserved for exactly one bounded replacement allocation for the displaced root EJR-232 record in the next separate identity-repair lease.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Next legal action: open a separate EJR-232 → EJR-412 identity-repair lease with a pre-write mutation matrix; re-read the current source and enumerate current consumer obligations before the atomic identity mutation.
