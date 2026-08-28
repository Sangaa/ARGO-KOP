# REP-049 — P446 B08 Ancestry Reconciliation

Date: 2026-08-28
Protocol: GOV-013
Mode: EXACT-HEAD / ANCESTRY RECONCILIATION

## Objective
Resolve whether the B08 implementation commit is part of the current PR #64 head before attributing any CI result or promotion evidence to it.

## Evidence
B08 implementation commit:
`f97728a568dab2876a0740eba823e6c15eba06eb`

Current PR #64 head:
`f21ede4a9b9941e51813b4fdb3db858d23255426`

GitHub commit comparison reports the refs as `diverged`, with merge base:
`6f05acbaad0da5c5139c5db8edad7ab989d0d4c6`

The comparison reports the current PR head as not containing the B08 implementation commit; the only file shown between the two selected refs is the later REP-039 documentation addition on the PR side. Therefore the B08 implementation SHA is not an ancestor of the current PR head on the observed graph.

## Interpretation
The prior attribution warning was correct and is now strengthened: CI evidence attached to `f21ede4...` cannot be used as execution evidence for the B08 test introduced at `f97728a...`.

This does not establish that the B08 implementation is defective. It establishes a provenance/branch-lineage boundary.

## Decision
Do not merge, cherry-pick, recreate, or otherwise transplant the B08 test merely to manufacture CI evidence. First determine the intended governed promotion path for the isolated B08 proof.

## Next decisive action
Compare the B08 implementation against the current canonical branch/PR worktree and identify whether an equivalent test already exists at the current head. If absent, a new mutation requires an explicit Gap and a governed target branch; it must not be justified by stale attribution.

## Close
P446 = CLOSED
ANCESTRY = DIVERGED / B08 NOT IN CURRENT PR HEAD
CI ATTRIBUTION = BLOCKED
FUNCTIONAL MUTATION = NONE
PROMOTION = NOT AUTHORIZED
