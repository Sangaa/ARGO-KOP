# MUT-2026-08-31-P2-EJR-412-REPLACEMENT-VACANCY-PROOF-261

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Candidate replacement identity EJR-412 only.
Opening main: `5f0af85e41e439854f6ac78d192e065ca109b01d`
Source disposition: `MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260.md`
Workflow commit: `e3ea184fd6fb094f9ea468912c68dc28111991c7`

## Trigger

Lease260 retained the earlier Memory EJR-232 allocation and classified the later root EJR-232 allocation displaced. It authorized replacement discovery only after a separate complete-history vacancy proof.

## Candidate discovery

- Current `EJR/` directory listing contained no EJR-412 allocation before proof execution.
- Repository search for `EJR-412` surfaced only the Session259 warning not to assume vacancy.
- These signals were used only for candidate discovery, not as absence proof.

## Execution evidence

Dedicated workflow `EJR Replacement Vacancy Proof 261`, run `33370689585`, executed from commit `e3ea184fd6fb094f9ea468912c68dc28111991c7` with complete checkout history and concluded SUCCESS.

Artifact `9749915855`, digest `sha256:911733c87a5879dc4805fd27509d1e156cfdc3879342ff4b46fb8ae590a162e7`, proved:
- candidate=`EJR-412`
- current_claims=[]
- historical_claims=[]
- history_complete=true
- history_scope=`all locally reachable refs`
- occupied=false
- vacant=true
- decision=`VACANT`

The workflow also explicitly verified the checkout was not shallow and failed unless the decision was exactly `VACANT`.

## Integration evidence

The same workflow commit passed Full-Stack Repository Audit run `33370689532` / run number 2350 with all audit, mutation-matrix, runtime-evidence, and CI-correlation steps SUCCESS.

M2 Multi-Channel Proposal Training run `33370689524` also completed SUCCESS.

## Decision

EJR-412 is authorized for exactly one bounded replacement allocation for the displaced root EJR-232 record under the next separate identity-repair lease.

## Boundaries

Lease261 performed no rename, delete, move, EJR-412 allocation, EJR-232 body/H1 rewrite, consumer rewrite, census baseline mutation, Plan204 expansion, or global integrity promotion.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

## Next safe entry

Open a separate EJR-232 → EJR-412 identity-repair lease with its own pre-write mutation matrix. Re-read the current source record and enumerate current consumer obligations before the atomic identity mutation. Do not consume EJR-412 for any other purpose.
