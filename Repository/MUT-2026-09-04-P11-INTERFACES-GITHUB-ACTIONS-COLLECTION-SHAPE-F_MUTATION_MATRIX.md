# P11 GITHUB ACTIONS COLLECTION SHAPE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-COLLECTION-SHAPE-F`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `8dcbcee70ae756ff9e93ae6716fc9be956c6da9e`
Material HEAD: `efb320a973634b307f60edcb6c8d042ed9e6f05f`
Protocol: GOV-014 / GOV-013 / INTF-010 / GITHUB_ACTIONS_CONNECTOR_INTERFACE

## Boundary

Transaction E remains `CLOSED / VERIFIED / RESUME-SAFE`. This transaction repaired only the collection-shape portion of the existing Actions observation contract. The top-level response was already required to be a JSON object; `list_workflow_runs()` and `list_workflow_run_jobs()` now also require the collection named by their method and mapping-shaped collection members.

This is provider-response structure validation inside the existing connector. It does not validate job-to-run identity, change dispatch behavior, authenticate GitHub, or establish remote execution success.

## Material Gap

`INTF-010` requires adapter payload-structure validation. The Actions interface promises workflow-run and workflow-job listing methods rather than arbitrary JSON-object retrieval.

Live provider observation confirms that GitHub represents these endpoints with top-level `workflow_runs` and `jobs` arrays. An empty array is a valid empty result; a missing key, non-array value, or scalar collection member is malformed for these methods.

Preserved invariants:

`EMPTY COLLECTION != MALFORMED COLLECTION`.

`LIST CONTRACT != ARBITRARY JSON OBJECT`.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-F-01 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | UPDATE | require object-list shape for `workflow_runs` and `jobs` while accepting empty arrays | Y | Y |
| P11-F-02 | `Quality/Integration/test_github_actions_connector.py` | UPDATE | regress empty valid collections plus missing/wrong/non-object collection forms | Y | Y |
| P11-F-03 | this Matrix | CREATE / CLOSE | bind collection-only scope, evidence, immutable read-back and exact-head proof | Y | Y |

## Local Execution Evidence

Targeted local execution before mutation:

`python -m pytest -q Quality/Integration/test_github_actions_connector.py`

Result: `15 passed`.

This is local controlled-response evidence only.

## Provider-shape observation

Independent live GitHub API observation showed the runs endpoint returning a top-level `workflow_runs` array and the jobs endpoint returning a top-level `jobs` array. This supports the structural contract used here but is not proof that the repository runtime connector is authenticated or production-authorized.

## Material Post-write read-back

Atomic material commit `efb320a973634b307f60edcb6c8d042ed9e6f05f` is exactly one commit ahead of entry HEAD and changes exactly three authorized paths:

1. `Services/GITHUB_ACTIONS_CONNECTOR.py` — blob `8c1ebbcd65d1534c4db3b0702933810acf0d108d`;
2. `Quality/Integration/test_github_actions_connector.py` — blob `6fa67f5d44d21c279c2e34f5c9684327de27ac4e`;
3. this Matrix — material blob `2a00020bbf25653d1b9b43d31fab5605964559cb`.

Post-write read-back matched all intended material blobs. No path outside the authorized set changed.

## Exact-head Material Verification

All four required repository workflow families completed successfully on exact material HEAD `efb320a973634b307f60edcb6c8d042ed9e6f05f`. The exact-head run set contained no `in_progress` and no `failure` result when closure was bound.

This establishes bounded repository-side executable compatibility and control-plane compliance. It does not establish provider authentication, remote connector execution, delivery, or production success.

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

## Post-commit reconciliation

This closure binding changes only this Matrix. The closure commit must remain a fast-forward descendant of material HEAD and pass the required exact-head workflow families. Contradictory later live evidence overrides this closure record.

## Unexpected Changes

Unexpected Changes: `NONE`.

Job-to-run identity binding, log-content validation, Runtime change, provider configuration change, Interface contract edit, relationship edit or Governance mutation remain outside this transaction.

## Closure

The collection-shape gap is repaired, targeted local tests pass, immutable read-back matches, and exact material-head CI is green. Transaction F is `CLOSED / VERIFIED / RESUME-SAFE`, subject to the ordinary rule that contradictory later live evidence wins.
