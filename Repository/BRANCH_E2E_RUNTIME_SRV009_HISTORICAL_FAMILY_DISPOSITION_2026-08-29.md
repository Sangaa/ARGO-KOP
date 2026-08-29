# Branch Family Disposition — Historical SRV-009 E2E Surfaces

Date: 2026-08-29
Baseline inspected: `main@98d78edab9cac1ab14b0e831d1c1c3ed0e585a61`

Leases:
- `R71-20260829-BRANCH-HYGIENE-068` — `e2e/runtime-srv009-live-20260817`
- `R71-20260829-BRANCH-HYGIENE-069` — `e2e/runtime-srv009-p418-20260828`
- `R71-20260829-BRANCH-HYGIENE-070` — `e2e/runtime-srv009-p423-20260828`

## Current-main authority/evidence

Current main's bounded P4 closure records the later accepted evidence state:
- REL-005 is bidirectional, executable-verified, governed and isolated-E2E verified;
- the historical P3 runtime E2E executed CREATE + UPDATE through the production adapter and real GitHub connector with read-back and cleanup;
- REL-009 is closed only as intentional one-way, isolated execution-observed, governed and non-universal;
- exact-main P3/P4 CI and registry synchronization evidence are preserved in the current P4 matrix.

## Branch-specific reading

### `e2e/runtime-srv009-live-20260817`
Carries historical adapter/connector variants plus an E2E trigger artifact. Current main has later connector/adapter lineage and current bounded P3/P4 evidence.

Disposition:
`HISTORICAL_P3_LIVE_E2E_EXECUTION_SURFACE / LATER_MAINLINE_ADAPTER_CONNECTOR_AND_BOUNDED_EVIDENCE / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

### `e2e/runtime-srv009-p418-20260828`
P418 explicitly records `SOURCE-VERIFIED / EXECUTION-PENDING`; the authorization-id workflow repair produced `NO RUN` on that branch and made no promotion claim. Later evidence stages superseded that pending checkpoint.

Disposition:
`HISTORICAL_E2E_AUTHORIZATION_CONTRACT_REPAIR / OWN_CHECKPOINT_EXECUTION_PENDING / LATER_EVIDENCE_SUPERSEDES_PENDING_STATE / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

### `e2e/runtime-srv009-p423-20260828`
P423 records exact-head Full-Stack and Runtime/Integration success but explicitly states production connector E2E on that exact head was `NOT OBSERVED`, canonical promotion `NOT JUSTIFIED`, and main unchanged. It is therefore historical exact-head evidence, not current promotion authority.

Disposition:
`HISTORICAL_EXACT_HEAD_CI_RECONCILIATION / NO_FUNCTIONAL_MUTATION / NO_PROMOTION / CURRENT_MAIN_HAS_LATER_BOUNDED_P4_CLOSURE / NO_WHOLESALE_MERGE / NO_DELETE_AUTHORIZED`

## Learning

Execution evidence must retain the exact checkpoint it proved. Later closure may supersede a pending or unobserved branch state, but must not rewrite the historical checkpoint into a PASS it never observed.
