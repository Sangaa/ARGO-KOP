# P11 GITHUB REPOSITORY PROVIDER RESPONSE MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-REPOSITORY-PROVIDER-RESPONSE-C`
Priority: `11 — Interfaces`
State: `MATERIAL APPLIED / LOCAL VERIFIED / EXACT-HEAD CI PENDING`
Entry HEAD: `94db9b3005926a640e7acec54491b862be63791e`
Protocol: GOV-014 / GOV-013 / INTF-010 / REPOSITORY_CONNECTOR_INTERFACE

## Boundary

Transaction B remains `CLOSED / VERIFIED / RESUME-SAFE` and is not reopened. This transaction addresses the next smallest material Interfaces gap: the concrete GitHub Contents connector already reports transport failures explicitly, but successful HTTP responses can still escape the governed failure boundary as raw JSON/shape/decode exceptions or permissive base64 decoding.

`Interfaces/INTF-010_INTEGRATIONS.md` requires adapters to validate payload structure and report failures rather than infer success. `Services/GITHUB_EVIDENCE_RESOLVER_ADAPTER.py` already enforces strict base64/JSON failure handling at another GitHub provider boundary, so this change completes an existing fail-closed pattern rather than introducing a new abstraction.

This transaction proves only local implementation behavior for malformed provider responses. It does not establish provider authentication, authorization, remote delivery, provider authenticity, production success, or external evidence admission.

## Material Gap

Current `Services/GITHUB_REPOSITORY_CONNECTOR.py` can:

- allow `json.JSONDecodeError` to escape `_request` on malformed successful HTTP payloads;
- assume a mapping-shaped provider response before validating its structure;
- assume `sha` and `commit.sha` fields exist and thereby leak raw lookup failures;
- decode base64 without strict validation.

The required invariant is:

`MALFORMED PROVIDER RESPONSE != SUCCESS AND MUST FAIL THROUGH ConnectorError`.

The sibling evidence resolver demonstrates the same provider family can be handled strictly without changing provider authority semantics.

## Change Set

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| P11-C-01 | `Services/GITHUB_REPOSITORY_CONNECTOR.py` | UPDATE | validate response encoding/JSON/object shape, require provider SHA/commit SHA, strict base64 decode, normalize failures to ConnectorError | Y | Y |
| P11-C-02 | `Quality/Integration/test_github_repository_connector.py` | UPDATE | add malformed JSON, non-object payload, missing SHA, invalid base64 and missing commit-SHA regression tests | Y | Y |
| P11-C-03 | this Matrix | CREATE | bind exact scope, local evidence, preservation rules and exact-head CI hold | Y | Y |

## Local Execution Evidence

Targeted local execution before repository mutation:

`python -m pytest -q Quality/Integration/test_github_repository_connector.py`

Result: `11 passed`.

This is local executable evidence only. It is not remote provider execution evidence.

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

## Post-write read-back and exact-head verification

After the atomic write, perform Post-write read-back for all three changed paths and verify that no path outside the authorized set changed. Exact-head CI must then prove the current material state through the required repository workflow families before closure.

Until exact-head CI succeeds, `Verified=Y` in the table means bounded source/test/local verification only; transaction closure remains pending.

## Unexpected Changes

Unexpected Changes: `NONE AUTHORIZED`.

Any unrelated path, provider configuration, credential, Interface contract, relationship registry, or control-plane authority change requires abort/reclassification rather than silent inclusion.

## Closure Rule

Close only when the material commit is read back exactly and exact-head required CI is green. A green local test cannot be promoted to provider authentication, remote delivery, or production success.
