# Branch Disposition — hermuz/igt-untrusted-external-evidence-intake-20260829

Date: `2026-08-29`
Status: `CLOSED CLASSIFICATION / HISTORICAL IMPLEMENTATION BRANCH / NO MERGE REQUIRED / NO DELETE AUTHORIZED`
Authority: `BRANCH HYGIENE EVIDENCE ONLY`

## Evidence

- Branch tip observed: `e2c639deb5c446d33ad257650777407bce0993e1`.
- Merge base with current lineage: `949acd74d65751786bc732a65902fbb00271d685`.
- Branch has six historical commits beyond that base.
- The functional intake implementation on the branch and current `main` has identical blob SHA `d6202e8a80353e9634b9204a127f1c421eb9959e`.
- The direct intake test on the branch and current `main` has identical blob SHA `c472c4c96f42f2f3e36e1f14b91b7a94b4fded51`.
- The intake contract on the branch and current `main` has identical blob SHA `172bcf4855f9855ad30ee06ae12d591be383f857`.
- The historical branch Mutation Matrix is not byte-identical to current `main` because `main` contains the later post-merge closure evidence. Current main matrix explicitly records merged main commit `28e3ec16f1b0e6decee6623f77f48cda74e229c7`, exact post-merge CI success, and transaction `CLOSED`.

## Semantic Reconciliation

The only non-identical declared branch artifact is the transaction record whose branch form still says `FINAL-HEAD CI PENDING`. Current `main` contains the legitimate later closure state after merge and exact-main CI. Therefore replaying or merging the branch record would regress evidence state rather than add missing functionality.

Disposition:

`SUPERSEDED_BY_MERGED_MAIN_IMPLEMENTATION_AND_POST_MERGE_CLOSURE_EVIDENCE`

No merge is required.

## Preservation Rule

The branch remains useful as historical provenance for the pre-merge candidate sequence. This classification does not authorize branch deletion.

`BRANCH DELETE = NOT AUTHORIZED BY THIS TRANSACTION`

## Non-Claims

- This does not authenticate any external provider.
- This does not close the external-evidence lifecycle beyond the already verified quarantine/intake boundary.
- This does not classify any other branch.
- This does not prove repository-wide Connected Baseline.

## Learning

Branch equivalence must distinguish functional artifacts from transaction/evidence records. A later main-side closure record may legitimately differ from its pre-merge branch ancestor while proving that the branch is operationally superseded rather than missing work.
