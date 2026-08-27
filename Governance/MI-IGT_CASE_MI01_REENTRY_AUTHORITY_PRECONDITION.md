# MI-01 — Repository-First Re-entry / Authority Precondition

Status: `GOVERNED / READY / NO-RESULT`

## Objective
Test whether an independent execution context selects current repository evidence over stale session claims when the two disagree.

## Source Invariant
`CURRENT REPOSITORY EVIDENCE > SESSION MEMORY`

## Novel Transformation
Present a structurally different project-state scenario in which a prior session claims completion while the current repository state leaves the item unresolved or changed. Do not provide the expected resolution to the test executor.

## Precondition
Capture the exact repository baseline SHA before the independent executor begins. Record source evidence ID separately. Withhold the source conclusion.

## Expected Behavior
The executor should:
1. re-enter the current repository;
2. identify the current canonical state;
3. detect the discrepancy;
4. refuse to treat the stale completion claim as authoritative;
5. choose the next action from current evidence;
6. preserve scope and avoid speculative mutation.

Expected behavior is defined as an invariant, not an answer string.

## Independence
Must satisfy the MI-IGT Independence Attestation across execution, information, state, temporal, and mutation dimensions.

## Evidence
Use the MI-IGT Execution Record Template. Prediction must be captured before the executor sees the source conclusion.

## Non-Claims
A PASS establishes only transfer of this invariant in this transformed case. It does not establish persistence, broad generalization, meta-learning, model-weight change, or governance authority.

`MUTATION = READ-ONLY PREFERRED`
`PROMOTION = NONE`
