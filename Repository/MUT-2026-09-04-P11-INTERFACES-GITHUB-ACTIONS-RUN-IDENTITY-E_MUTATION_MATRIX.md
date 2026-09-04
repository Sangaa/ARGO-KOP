# P11 GITHUB ACTIONS RUN IDENTITY MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-RUN-IDENTITY-E`
Priority: `11 — Interfaces`
State: `MATERIAL APPLIED / LOCAL VERIFIED / EXACT-HEAD CI PENDING`
Entry HEAD: `ee3b425373dbb6df36a110c1db81ef2179ec791a`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction D is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addresses the next bounded Actions observation gap: `get_workflow_run(run_id)` is contractually an exact authoritative-identity lookup, but the concrete connector currently accepts any mapping returned from the requested endpoint without proving the returned provider identity matches the requested identity.

This is response-identity validation inside the existing connector boundary. It does not create a new abstraction, change provider selection, authenticate GitHub, or claim remote execution success.

## Material Gap

The provider-neutral Actions interface states:

`get_workflow_run(run_id) -> Return one exact workflow run by authoritative run identity.`

Current implementation validates only that the caller's numeric value is positive. A provider response with missing `id` or a different `id` can therefore be returned as though it were the requested run. Python boolean values also satisfy the old positive-integer checks because `bool` is a subclass of `int`.

Required invariants:

`REQUESTED RUN IDENTITY == RETURNED RUN IDENTITY`.

`BOOLEAN != EXECUTION IDENTITY`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-E-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | require exact returned run id for `get_workflow_run`; reject boolean run/job identities before transport | Y | Y |
| P11-E-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress matching, missing, mismatched and boolean execution identities | Y | Y |
| P11-E-03 | this Matrix | CREATE | bind identity-only scope, local evidence, KEEP constraints and exact-head hold | Y | Y |

## Local Execution Evidence

Targeted local execution before mutation:

`python -m pytest -q Quality/Integration/test_github_actions_connector.py`

Result: `11 passed`.

This proves only local connector behavior against controlled responses.

## KEEP Preservation

KEEP unchanged:

- Transaction D response-decoding and empty-response semantics;
- list-workflow-runs response semantics;
- list-workflow-run-jobs response semantics beyond strict caller run-id type;
- workflow dispatch behavior and 204 acceptance;
- job-log response content behavior beyond strict caller job-id type;
- provider authentication/configuration and credentials;
- Runtime connector handoff;
- all Interface documentary contracts and relationship registries.

No provider authenticity, authorization, remote delivery, workflow completion or production-success claim is introduced.

## Post-write read-back and exact-head verification

After the atomic write, perform Post-write read-back for all three changed paths and compare entry→material HEAD. No path outside this authorized set may change. Exact-head required workflow families must be green before closure.

`Verified=Y` is bounded source/test/local verification until exact-head CI is established.

## Unexpected Changes

Unexpected Changes: `NONE AUTHORIZED`.

Any collection-shape validation, Runtime mutation, provider configuration change, Interface contract edit, relationship edit or Governance mutation is outside this transaction.

## Closure Rule

Close only after immutable read-back and exact-head CI. Exact provider-response identity validation remains distinct from provider authentication and from proof that a workflow completed successfully.
