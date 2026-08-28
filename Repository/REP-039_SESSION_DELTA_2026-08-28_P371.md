# P371 — Existing PR Reconciliation: RUN-010 → ENG-006

Date: 2026-08-28
Status: `CLOSED / VERIFIED / NO CANONICAL PROMOTION`
Protocol: `GOV-013`

## RE-ENTRY
Resumed from P370. The next action was to reconcile the already-existing PR #63 before creating any new implementation or PR.

## OBSERVED REPOSITORY STATE
PR #63 is open and targets `main`. It is explicitly described as governed isolated validation only, with no production runtime/registry mutation and REL-009 remaining open pending executable evidence.

Head branch: `hermuz/p302-rel009-contract-test-20260827`
Head SHA: `a18bf9bae5fbdc29cde0fd237830f0c63b71556c`
PR base SHA recorded by GitHub: `2ce52292f4d8d8cfebd5c7b24fe84bc89036a934`

## RECONCILIATION FINDINGS
The PR contains a substantial isolated validation package, including:
- `Runtime/Execution/run010_eng006_consumer.py`
- `Services/ENG006_REAL_PROVIDER_FACTORY.py`
- RUN-010/ENG-006 boundary tests
- real-provider fail-closed test
- P4 critical graph validation material
- mutation matrices and session records
- OpenHands Q0 qualification material
- `GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION_AMENDMENT.md`

The isolated consumer explicitly requires `RUN-010`, `AUTHORIZED`, and a source trace before dispatch. This proves an executable test seam, not production connectivity by itself.

The real-provider factory constructs the existing governed GitHub connector and production adapter, but the reviewed test only proves fail-closed behavior when required credentials are absent. Therefore production provider execution remains unproven from this evidence set.

## IMPORTANT TEMPORAL BOUNDARY
PR #63 was created against an older `main` base than the current P370/P368 lineage. Therefore its contents MUST NOT be treated as automatically current with `main` and MUST NOT be merged merely because the branch contains useful work.

A new PR was not created because GitHub confirmed that PR #63 already exists for the same head branch. This is evidence against duplicate-PR creation, not evidence of implementation correctness.

## CLAIM / EVIDENCE CLASSIFICATION
- Existing isolated consumer seam: `PROVEN`
- Authorization and trace guards in isolated consumer: `PROVEN`
- Fail-closed real-provider construction test: `PROVEN`
- Production GitHub connectivity: `UNPROVEN`
- Current-main compatibility of PR #63: `UNPROVEN / REQUIRES RECONCILIATION`
- REL-009 promotion: `NOT JUSTIFIED`
- Merge of PR #63 now: `NOT JUSTIFIED`
- Duplicate implementation/PR: `REJECTED`

## DECISION
Do not merge or recreate PR #63 at this checkpoint. First reconcile its changes against the current `main` head, then determine whether any subset is still required and safe to adapt. Only after that may an executable production observation be considered.

## KNOWLEDGE DELTA
**KD-045 — An existing implementation artifact is evidence of prior work, not evidence that it is current, compatible, or promotable.**

**KD-046 — Duplicate work must be prevented by repository/PR reconciliation, not by session memory.**

**KD-047 — A PR existing for a branch proves uniqueness of the review object, not correctness of the branch contents.**

## CHECKPOINT
`P371 → compare PR #63 head against current main → identify non-duplicative applicable changes → reconcile contracts/tests/matrices → run affected CI → determine minimum production observation required by the exact REL-009 claim → no promotion without evidence.`

## CLOSE
`CLOSED / VERIFIED / NO CANONICAL MUTATION / NO AUTHORITY PROMOTION`
