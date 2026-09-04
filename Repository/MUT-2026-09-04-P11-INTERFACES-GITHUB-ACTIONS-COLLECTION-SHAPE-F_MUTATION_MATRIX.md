# P11 GITHUB ACTIONS COLLECTION SHAPE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-COLLECTION-SHAPE-F`
Priority: `11 — Interfaces`
State: `MATERIAL APPLIED / LOCAL VERIFIED / EXACT-HEAD CI PENDING`
Entry HEAD: `8dcbcee70ae756ff9e93ae6716fc9be956c6da9e`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction E is `CLOSED / VERIFIED / RESUME-SAFE`. This transaction addresses only the collection-shape portion of the existing Actions observation contract. The top-level response is already required to be a JSON object, but `list_workflow_runs()` and `list_workflow_run_jobs()` can still return an object that lacks the collection named by the method or whose collection members are not objects.

This is provider-response structure validation inside the existing connector. It does not validate job-to-run identity, change dispatch behavior, authenticate GitHub, or establish remote execution success.

## Material Gap

`INTF-010` requires adapter payload-structure validation. The Actions interface promises workflow-run and workflow-job listing methods rather than arbitrary JSON-object retrieval.

Live provider observation confirms that GitHub represents these endpoints with top-level `workflow_runs` and `jobs` arrays. An empty array is a valid empty result; a missing key, non-array value, or scalar collection member is malformed for these methods.

Required invariants:

`EMPTY COLLECTION != MALFORMED COLLECTION`.

`LIST CONTRACT != ARBITRARY JSON OBJECT`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-F-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | require object-list shape for `workflow_runs` and `jobs` while accepting empty arrays | Y | Y |
| P11-F-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress empty valid collections plus missing/wrong/non-object collection forms | Y | Y |
| P11-F-03 | this Matrix | CREATE | bind collection-only scope, evidence, KEEP constraints and exact-head hold | Y | Y |

## Local Execution Evidence

Targeted local execution before mutation:

`python -m pytest -q Quality/Integration/test_github_actions_connector.py`

Result: `15 passed`.

This is local controlled-response evidence only.

## Provider-shape observation

Independent live GitHub API observation shows the runs endpoint returning a top-level `workflow_runs` array and the jobs endpoint returning a top-level `jobs` array. This supports the structural contract used here but is not proof that the repository runtime connector is authenticated or production-authorized.

## KEEP Preservation

KEEP unchanged:

- Transaction E exact-run identity checks;
- empty HTTP observation-response rejection from Transaction D;
- empty arrays as valid zero-result collections;
- job-to-run identity semantics beyond collection object shape;
- dispatch 204 acceptance and requested-vs-completed distinction;
- provider configuration, credentials and authentication;
- Runtime consumers;
- Interface documentary contracts and relationship registries.

No provider-authenticity, remote-delivery, execution-completion or production-success claim is introduced.

## Post-write read-back and exact-head verification

After atomic mutation, read back all three changed paths and compare entry→material HEAD. No path outside the authorized set may change. Exact-head required workflow families must be green before closure.

`Verified=Y` means bounded source/test/local verification until exact-head CI succeeds.

## Unexpected Changes

Unexpected Changes: `NONE AUTHORIZED`.

Any job-to-run identity binding, log-content validation, Runtime change, provider configuration change, Interface contract edit, relationship edit or Governance mutation is outside this transaction.

## Closure Rule

Close only after immutable read-back and exact-head CI. Correct response collection shape remains distinct from provider authentication and from proof that a remote workflow completed successfully.
