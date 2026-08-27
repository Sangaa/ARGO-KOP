# MUT-2026-08-27-P308 — RUN-010 → ENG-006 Mutation Matrix

Status: `GOVERNED / ISOLATED / NO-PRODUCTION-PROMOTION`

## Target
`Runtime/Execution/run010_eng006_consumer.py`

## Reason
P309 repository audit blocked the new executable-boundary file because it lacked a mutation matrix. This artifact closes that governance gap without changing production behavior.

## Classification
- Change type: runtime capability / consumer-boundary implementation
- Scope: isolated branch only
- Authority impact: none
- Production promotion: prohibited by this matrix alone

## Preconditions
1. Explicit evidence gap: `RUN-010 → ENG-006` not executable-verified.
2. Contract C1–C7 recorded.
3. Existing downstream `ENG-006 → SRV-009` evidence preserved.
4. CI must execute the isolated test suite.
5. No registry or production runner mutation is included.

## Acceptance
- Unauthorized requests rejected before consumer invocation.
- Only RUN-010 enters this boundary.
- Source trace is mandatory and preserved.
- ENG-006 callable is injected, not guessed.
- Test evidence cannot be interpreted as production connectivity evidence.
- Full repository governance/integrity checks remain green.

## Explicit Non-Claims
This matrix does not authorize:
- modification of `connected_spine_runner.py`;
- modification of `REP-014`;
- promotion of `REL-009`;
- production deployment;
- treating isolated consumer execution as connected-spine execution.

## Closure Gate
`MUTATION_MATRIX_PREFLIGHT = PASS` is necessary but not sufficient. A later promotion requires executable end-to-end evidence for `RUN-010 → ENG-006 → SRV-009` plus regression and authority reconciliation.
