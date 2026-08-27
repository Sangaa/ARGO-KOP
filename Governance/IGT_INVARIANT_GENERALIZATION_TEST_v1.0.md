# IGT — Invariant Generalization Test v1.0

Status: `VALIDATION PROTOCOL / NOT AUTHORITY`
Purpose: distinguish behavioral transfer from repetition or wording recall for reusable learning candidates.

## 1. Unit of Evaluation
A learning candidate `R` is decomposed into invariants `I1..In`. Each test case changes surface details while preserving one or more target invariants.

## 2. Required Case Structure
Each case MUST contain:
- novel surface/object identities;
- a conflict or decision point;
- target invariant(s);
- hidden expected authority/decision where practical;
- pre-action prediction;
- action selection;
- post-action evidence explanation;
- scope/non-claim check.

## 3. Scoring Dimensions
Score independently:
1. invariant identification;
2. authority selection;
3. scope preservation;
4. action selection;
5. evidence quality;
6. explanation fidelity.

A case passes only when the relevant invariant is applied correctly and the explanation does not exceed the available evidence.

## 4. Anti-Leakage Boundary
The expected answer MUST NOT be exposed before prediction. Cases should use materially different surface forms and object identities from the source learning cases. A test that can be solved solely by repeating the exact learned wording is insufficient.

## 5. Baseline Comparison
At minimum compare:
- `B0`: generic repository-first wording without source-case details;
- `L1`: candidate learning available;
- `L2`: candidate learning plus provenance envelope when the experiment is testing provenance use.

Interpret differences cautiously: IGT alone does not prove causal learning, statistical independence, or durable model weight changes.

## 6. Failure Semantics
`Failure → Boundary → Revised Invariant → New Test`.

If no boundary can be derived, record the failure as unresolved evidence rather than learning gain.

## 7. Minimum Promotion Evidence
Before governance promotion, require at least two materially novel authority-conflict cases and evidence from materially separate execution contexts. Record both successes and failures. Promotion remains subject to the existing learning/governance gate.

## 8. Output Contract
Each experiment records:
`CASE_ID / CONTEXT / TARGET_INVARIANT / PREDICTION / ACTION / EVIDENCE / SCORE / FAILURE_OR_BOUNDARY / REVISION / PROMOTION_IMPACT`.

`IGT = VALIDATION METHOD ONLY`
`NO RESULT = AUTOMATIC PROMOTION`
