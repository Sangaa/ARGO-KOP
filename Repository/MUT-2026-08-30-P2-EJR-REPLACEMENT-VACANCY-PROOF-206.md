# R71-20260830-P2-EJR-REPLACEMENT-VACANCY-PROOF-206

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Functional head: `2f3e139c2f9e096c058ae317db878efaa825e01f`
Target future repair: `EJR/EJR-214_P2_SESSION_CLOSURE_2026-08-17.md`
Replacement candidate: `EJR-400`

## Result
The execution-verified Lease-193 vacancy gate was run on exact functional head with complete locally reachable Git history. `EJR-400` is proven `VACANT` and is eligible for allocation only inside a separate governed repair-execution lease.

Artifact evidence:
- workflow run `33329388744` — SUCCESS;
- artifact `ejr-400-vacancy-proof` / ID `9737186617`;
- digest `sha256:89bac3857098024d48256135d112292f13cad0866368c57a8ea2df3e3db8cfc1`;
- report: candidate `EJR-400`, decision `VACANT`, history_complete `true`, history_scope `all locally reachable refs`, current_claims `[]`, historical_claims `[]`.

Exact-head supporting checks at the functional head:
- Full-Stack Repository Audit `33329388713` — SUCCESS.
- ARGO Runtime Prototype and Integration Tests `33329388749` — SUCCESS.
- M2 Multi-Channel Proposal Training `33329388725` — SUCCESS.
- Real Mutation Matrix Regression `33329388724` — SUCCESS.

## Packaging defect captured
The initially prepared atomic prewrite tree was not attached through `update_ref`; a contents-API write created a lease-only commit `94100cb65155179a010a246a3e235e775a699b17`. No functional mutation had occurred. Corrective commit `92a0d4fa3da630b9762e5d3685819775309ca309` restored the Lease+Matrix prewrite pair before the functional workflow change.

Reusable operational rule:
`PREPARED ATOMIC TREE MUST BE ATTACHED WITH UPDATE_REF; CONTENTS-API FILE WRITE IS NOT A SUBSTITUTE FOR ATOMIC PREWRITE ATTACHMENT.`

## Boundaries
This lease performs no EJR allocation, rename, content mutation, consumer rewrite, suppression, or authority promotion. `EJR-400` being VACANT is permission to enter the next gates, not itself an allocation transaction. Priority 2 remains OPEN; Phase 1 remains OPEN; Global Connected Baseline remains OPEN.

## Next legal action
Open a separate repair-execution lease for exactly one displaced record: root EJR-214. Re-enumerate current operational consumers, then atomically move/rewrite identity to `EJR-400` with content preservation, inspect Internal-ID evidence, and close independently.
