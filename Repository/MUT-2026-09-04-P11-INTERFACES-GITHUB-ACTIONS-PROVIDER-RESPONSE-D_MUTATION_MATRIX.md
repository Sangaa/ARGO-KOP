# P11 GITHUB ACTIONS PROVIDER RESPONSE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-PROVIDER-RESPONSE-D`
Priority: `11 — Interfaces`
State: `MATERIAL APPLIED / LOCAL VERIFIED / EXACT-HEAD CI PENDING`
Entry HEAD: `dc2b1b48a9f06d84c4a8a821d9386c0444241c81`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction C is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction handles the same bounded fail-closed response class in the distinct GitHub Actions capability boundary; repository Contents authority and Actions execution observation remain separate.

The Actions contract states that repository authority, Actions invocation authority, and execution-observation authority must not be inferred from one another. `dispatch_workflow()` returns acceptance only, not workflow completion. Therefore an empty successful response is legal only for the dispatch endpoint, while observation GETs must not silently interpret an empty or malformed successful response as evidence.

This transaction does not authenticate GitHub, prove credentials/permissions, dispatch a real workflow, observe a remote run, or establish production success.

## Material Gap

Current `Services/GITHUB_ACTIONS_CONNECTOR.py` returns `{}` for every empty successful response and allows malformed/non-object JSON responses to escape or flow without the governed `ConnectorError` boundary.

Required invariant:

`DISPATCH ACCEPTANCE RESPONSE MAY BE EMPTY; OBSERVATION RESPONSE MAY NOT SILENTLY BE EMPTY OR MALFORMED.`

And:

`REQUESTED / ACCEPTED ACTION != COMPLETED ACTION`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-D-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | normalize encoding/JSON/object-shape failures, reject empty observation responses, permit empty response only for dispatch acceptance | Y | Y |
| P11-D-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress invalid JSON, non-object payload and empty observation while preserving 204 dispatch acceptance | Y | Y |
| P11-D-03 | this Matrix | CREATE | bind bounded capability scope, local evidence, preservation rules and exact-head hold | Y | Y |

## Local Execution Evidence

Targeted local execution before mutation:

`python -m pytest -q Quality/Integration/test_github_actions_connector.py`

Result: `8 passed`.

This is mock/local execution evidence only.

## KEEP Preservation

KEEP unchanged:

- Transaction C source/test/material and closure evidence;
- `Services/GITHUB_REPOSITORY_CONNECTOR.py`;
- Actions capability surface and method signatures;
- dispatch 204 acceptance semantics;
- HTTP/network failure normalization;
- authentication/configuration inputs;
- job-log retrieval behavior;
- all Interface documentary contracts and relationship registries.

No completion, authentication, provider-authenticity, remote-delivery, or production claim is introduced.

## Post-write read-back and exact-head verification

After the atomic write, perform Post-write read-back on all three changed paths and compare entry→material HEAD. No path outside this set is authorized. Exact-head repository workflow families must be green before closure.

`Verified=Y` means bounded source/test/local verification until exact-head CI is established.

## Unexpected Changes

Unexpected Changes: `NONE AUTHORIZED`.

Any additional provider adapter, credential/configuration, Interface contract, relationship, Runtime or Governance mutation requires reclassification.

## Closure Rule

Close only after immutable read-back and exact-head CI. Local 204 simulation proves only the dispatch-response contract, not remote dispatch acceptance or workflow completion.
