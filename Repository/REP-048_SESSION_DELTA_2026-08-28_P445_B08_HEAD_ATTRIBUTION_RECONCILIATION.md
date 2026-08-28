# REP-048 — P445 B08 HEAD Attribution Reconciliation

Date: 2026-08-28
Protocol: GOV-013
Mode: EXACT-HEAD / PROVENANCE RECONCILIATION

## Finding
P444 correctly treated the B08 implementation commit as source-verified and CI-unobserved. This round checked whether that commit is actually the head of the governed PR/Actions path.

## Evidence
PR #64 is open, unmerged, and its current head is:
`f21ede4a9b9941e51813b4fdb3db858d23255426`

The B08 implementation commit referenced by P444 is:
`f97728a568dab2876a0740eba823e6c15eba06eb`

The two SHAs are different. A pull-request workflow lookup for `f97728a...` returns no workflow runs, and its combined status is empty.

## Interpretation
This does NOT prove B08 failed. It proves only that the B08 implementation SHA is not the current PR #64 head, so the absence of PR-triggered CI at that SHA cannot be used as evidence about the current PR execution state.

Likewise, CI observed on `f21ede4...` must not be attributed to `f97728a...` without an explicit ancestry/content equivalence proof appropriate to the claim.

## Decision
Stop exact-head conflation. B08 execution remains `UNOBSERVED` for the implementation SHA under review.

No code mutation and no promotion decision are justified.

## Next decisive action
Reconcile the ancestry between `f97728a...` and PR #64 head `f21ede4...`, and identify which exact commit contains the B08 test. Then obtain execution evidence for that exact commit through the governed path.

## Close
P445 = CLOSED
HEAD ATTRIBUTION = CORRECTED
B08 = EXECUTION-UNOBSERVED
FUNCTIONAL MUTATION = NONE
PROMOTION = NOT AUTHORIZED
