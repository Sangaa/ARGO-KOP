# P11 GITHUB ACTIONS RUN IDENTITY MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-RUN-IDENTITY-E`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `ee3b425373dbb6df36a110c1db81ef2179ec791a`
Material HEAD: `fa66ff244cd04f9d4e333d57e3c511990100f41e`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction D remains `CLOSED / VERIFIED / RESUME-SAFE`. This transaction repaired the bounded Actions observation gap in `get_workflow_run(run_id)`: the concrete connector now proves that the returned provider run identity matches the exact requested identity.

This is response-identity validation inside the existing connector boundary. It does not create a new abstraction, change provider selection, authenticate GitHub, or claim remote execution success.

## Material Gap

The provider-neutral Actions interface states:

`get_workflow_run(run_id) -> Return one exact workflow run by authoritative run identity.`

Pre-change implementation validated only that the caller's numeric value was positive. A provider response with missing `id` or a different `id` could therefore be returned as though it were the requested run. Python boolean values also satisfied the old positive-integer checks because `bool` is a subclass of `int`.

Preserved invariants:

`REQUESTED RUN IDENTITY == RETURNED RUN IDENTITY`.

`BOOLEAN != EXECUTION IDENTITY`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-E-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | require exact returned run id for `get_workflow_run`; reject boolean run/job identities before transport | Y | Y |
| P11-E-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress matching, missing, mismatched and boolean execution identities | Y | Y |
| P11-E-03 | this Matrix | CREATE / CLOSE | bind identity-only scope, local evidence, immutable read-back and exact-head proof | Y | Y |

## Local Execution Evidence

Targeted local execution before mutation:

`python -m pytest -q Quality/Integration/test_github_actions_connector.py`

Result: `11 passed`.

This proves only local connector behavior against controlled responses.

## Material Post-write read-back

Atomic material commit `fa66ff244cd04f9d4e333d57e3c511990100f41e` is exactly one commit ahead of entry HEAD and changes exactly three authorized paths:

1. `Services/GITHUB_ACTIONS_CONNECTOR.py` — blob `eee4480fbb7d8b42cfd66e3b890358bec1986ad8`;
2. `Quality/Integration/test_github_actions_connector.py` — blob `cf4e4da6e1521cf89576167f50b9366ca452b126`;
3. this Matrix — material blob `dd8241d0eb229c159d5e1f6db2ad656e552f04f1`.

Post-write read-back matched all intended material blobs. No path outside the authorized material set changed.

## Exact-head Material Verification

All required workflow families completed `SUCCESS` on exact material HEAD `fa66ff244cd04f9d4e333d57e3c511990100f41e`:

- Full-Stack Repository Audit — run `33877256853` — `SUCCESS`;
- ARGO Runtime Prototype and Integration Tests — run `33877256860` — `SUCCESS`;
- M2 Multi-Channel Proposal Training — run `33877256840` — `SUCCESS`;
- Real Mutation Matrix Regression — run `33877256827` — `SUCCESS`.

This establishes bounded repository-side executable compatibility and control-plane compliance. It does not elevate local/mocked connector execution to provider authentication, remote delivery, or production success.

## Provider-shape observation

Independent live GitHub API observation for run `33877256827` returned provider field `id=33877256827`, matching the exact run requested. Its jobs endpoint returned a top-level `jobs` collection whose entries include `run_id`. This supports the provider-response shape used by the contract but is not evidence that the repository's runtime connector credentials are configured, authorized, or production-valid.

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

## Post-commit reconciliation

This closure binding changes only this Matrix. The closure commit must remain a fast-forward descendant of material HEAD and pass the required exact-head workflow families. Any contradictory later live evidence overrides this closure record.

## Unexpected Changes

Unexpected Changes: `NONE`.

Collection-shape validation, Runtime mutation, provider configuration change, Interface contract edit, relationship edit or Governance mutation remain outside this transaction.

## Closure

The exact-run identity gap is repaired, targeted local tests pass, immutable read-back matches, and exact material-head CI is green. Transaction E is `CLOSED / VERIFIED / RESUME-SAFE`, subject to the ordinary rule that contradictory later live evidence wins.
