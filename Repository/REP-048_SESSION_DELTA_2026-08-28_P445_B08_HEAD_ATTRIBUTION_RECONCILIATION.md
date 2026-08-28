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

The two SHAs are different. The implementation commit adds `Quality/Integration/test_b08_run010_eng006_consumer.py` and has parent `7edef61...`. A pull-request workflow lookup and combined-status query for `f97728a...` return no observed CI/status entries.

The current PR head `f21ede4...` does have two successful pull-request workflow runs, but those results belong to that exact PR head and are not automatically attributable to `f97728a...`.

## Ancestry check
A direct comparison reports the two commits as `diverged`, with merge base `6f05acb...`; therefore the B08 implementation SHA is not an ancestor of the current PR head on the compared graph.

## Interpretation
This does NOT prove B08 failed. It proves that the B08 implementation SHA is outside the currently observed PR #64 execution head. Therefore prior CI success on `f21ede4...` cannot be used as B08 execution evidence for `f97728a...`.

## Decision
Stop exact-head conflation. B08 execution for the implementation SHA remains `UNOBSERVED`.

No code mutation and no promotion decision are justified by this evidence.

## Next decisive action
Determine whether the B08 implementation should be reintroduced into the governed PR lineage or independently executed through an authorized workflow. Any such action must preserve exact-head attribution.

## Close
P445 = CLOSED
HEAD ATTRIBUTION = CORRECTED
B08 = EXECUTION-UNOBSERVED
FUNCTIONAL MUTATION = NONE
PROMOTION = NOT AUTHORIZED
