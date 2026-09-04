# P11 GITHUB REPOSITORY PROVIDER RESPONSE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-REPOSITORY-PROVIDER-RESPONSE-C`
Priority: `11 — Interfaces`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `94db9b3005926a640e7acec54491b862be63791e`
Material HEAD: `4053a1b0999b6c194936de4015d1e908921e6002`
Protocol: GOV-014 / GOV-013 / INTF-010 / REPOSITORY_CONNECTOR_INTERFACE

## Boundary

Transaction B remains `CLOSED / VERIFIED / RESUME-SAFE` and is not reopened. This transaction addresses the next smallest material Interfaces gap: the concrete GitHub Contents connector already reports transport failures explicitly, but successful HTTP responses could escape the governed failure boundary as raw JSON/shape/decode exceptions or permissive base64 decoding.

`Interfaces/INTF-010_INTEGRATIONS.md` requires adapters to validate payload structure and report failures rather than infer success. `Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py` already enforces strict base64/JSON failure handling at another GitHub provider boundary, so this change completes an existing fail-closed pattern rather than introducing a new abstraction.

This transaction proves only local implementation behavior for malformed provider responses plus repository CI compatibility. It does not establish provider authentication, authorization, remote delivery, provider authenticity, production success, or external evidence admission.

## Material Gap

Pre-change `Services/GITHUB_REPOSITORY_CONNECTOR.py` could:

- allow `json.JSONDecodeError` to escape `_request` on malformed successful HTTP payloads;
- assume a mapping-shaped provider response before validating its structure;
- assume `sha` and `commit.sha` fields exist and thereby leak raw lookup failures;
- decode base64 without strict validation.

The preserved invariant is:

`MALFORMED PROVIDER RESPONSE != SUCCESS AND MUST FAIL THROUGH ConnectorError`.

The sibling evidence resolver demonstrates the same provider family can be handled strictly without changing provider authority semantics.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-C-01 | `Services/GITHUB_REPOSITORY_CONNECTOR.py` | UPDATE | validate response encoding/JSON/object shape, require provider SHA/commit SHA, strict base64 decode, normalize failures to ConnectorError | Y | Y |
| P11-C-02 | `Quality/Integration/test_github_repository_connector.py` | UPDATE | add malformed JSON, non-object payload, missing SHA, invalid base64 and missing commit-SHA regression tests | Y | Y |
| P11-C-03 | this Matrix | CREATE / CLOSE | bind exact scope, local evidence, preservation rules, read-back and exact-head CI proof | Y | Y |

## Local Execution Evidence

Targeted local execution before repository mutation:

`python -m pytest -q Quality/Integration/test_github_repository_connector.py`

Result: `11 passed`.

This is local executable evidence only. It is not remote provider execution evidence.

## Material Post-write read-back

Atomic material commit `4053a1b0999b6c194936de4015d1e908921e6002` is exactly one commit ahead of entry HEAD and changes exactly three authorized paths:

1. `Services/GITHUB_REPOSITORY_CONNECTOR.py` — blob `9636c18ae105ba2b44e075379871a2005fc02e9c`;
2. `Quality/Integration/test_github_repository_connector.py` — blob `834427650e1bb6434cdb92cd6afa1bd492abe146`;
3. this Matrix — material blob `26dc2b6b677750fc94774efb6f8cd25fbf6459c6`.

Post-write read-back matched all three intended blobs. No path outside the authorized material set changed.

## Exact-head Material Verification

All required workflow families completed `SUCCESS` on exact material HEAD `4053a1b0999b6c194936de4015d1e908921e6002`:

- Full-Stack Repository Audit — run `33876165559` — `SUCCESS`;
- ARGO Runtime Prototype and Integration Tests — run `33876165601` — `SUCCESS`;
- M2 Multi-Channel Proposal Training — run `33876165500` — `SUCCESS`;
- Real Mutation Matrix Regression — run `33876165506` — `SUCCESS`.

This establishes repository-side executable compatibility and control-plane compliance for the bounded change. It does not elevate local/provider-mock execution to provider authentication, remote delivery, or production success.

## KEEP Preservation

KEEP unchanged:

- `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` and Transaction-B relationship material;
- all Interface documentary contracts;
- repository connector method surface (`read_current`, `create_file`, `update_file`, `read_back`);
- 404-as-confirmed-absence behavior;
- stale-SHA rejection;
- create/update separation;
- post-write read-back semantics;
- credentials and provider configuration;
- Actions connector and evidence-resolver behavior.

No new authority or trust claim is introduced.

## Post-commit reconciliation

This closure binding changes only this Matrix. The closure commit itself must remain a fast-forward descendant of material HEAD and must pass the same exact-head required workflow families. If closure-head CI disagrees with this evidence, live repository evidence wins and the transaction returns to hold.

## Unexpected Changes

Unexpected Changes: `NONE`.

Any unrelated path, provider configuration, credential, Interface contract, relationship registry, or control-plane authority change requires abort/reclassification rather than silent inclusion.

## Closure

The material gap is repaired, bounded local tests pass, immutable read-back matches, and exact material-head CI is green. Transaction C is therefore `CLOSED / VERIFIED / RESUME-SAFE`, conditional only on the ordinary rule that contradictory later live evidence overrides this closure record.
