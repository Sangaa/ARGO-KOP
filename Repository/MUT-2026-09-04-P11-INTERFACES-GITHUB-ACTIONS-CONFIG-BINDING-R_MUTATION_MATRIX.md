# MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-CONFIG-BINDING-R — MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-CONFIG-BINDING-R`

Priority: `11 — Interfaces`

Protocol: governed bounded mutation; protected implementation + focused semantic test + mutation record were co-committed, material exact-head CI was required, and closure is Matrix-only with an independent closure-head CI cycle.

## Semantic contract

The GitHub Actions connector direct-construction boundary must reject missing, blank, or non-text repository owner, repository name, credential, and API endpoint values. Direct construction must not bypass the same minimum identity/credential validity already enforced by `from_environment()`.

This transaction does **not** impose token format, repository-name syntax, URL reachability, timeout policy, workflow authority, or execution success from possession of configuration.

## Mutation set

| Change ID | Target | Action | Expected Content | Applied | Verified |
| --- | --- | --- | --- | --- | --- |
| R-001 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | MODIFY | Validate direct `owner`, `repo`, `token`, and `api_base` inputs as exact nonblank strings using the existing Actions incomplete-configuration failure family. | YES | YES |
| R-002 | `Quality/Integration/test_github_actions_connector_config_binding.py` | CREATE | Prove direct construction rejects missing/blank/non-text boundary values and preserves valid explicit routing values. | YES | YES |
| R-003 | This Matrix | CREATE / KEEP | Record scope, exclusions, read-back discipline, and unexpected-change handling. | YES | YES |

## KEEP / exclusions

- KEEP `from_environment()` stripping and incomplete-configuration behavior unchanged.
- KEEP workflow listing, observation, dispatch, job-lineage, and job-log semantics unchanged.
- KEEP `timeout` outside this transaction; no local contract currently binds its type/range to the environment configuration seam.
- KEEP token/repository/API endpoint format and connectivity claims outside scope beyond exact nonblank text.
- Do not infer Actions authority or workflow completion from syntactically valid configuration.

## Post-write / read-back evidence

Entry HEAD: `80499a07a3631ec9fbe28d2058d98bbe36d2766e`.

Material HEAD: `b96f21b76f175bf9fcd81165c89d1bb6ed1a7ae5`.

Entry-to-material comparison contained exactly the three authorized paths: the protected Actions connector source, the focused configuration-binding test, and this Matrix. Immutable material read-back confirmed the direct-construction guard and focused semantic test.

Material exact-head CI succeeded independently for all required workflow families:
- Full-Stack Repository Audit — run `33911358159` — `completed / success`
- ARGO Runtime Prototype and Integration Tests — run `33911358266` — `completed / success`
- M2 Multi-Channel Proposal Training — run `33911358197` — `completed / success`
- Real Mutation Matrix Regression — run `33911358322` — `completed / success`

Closure mutation is restricted to this Matrix. Closure validity additionally requires a fresh four-family exact-head CI cycle on the resulting closure SHA; that evidence is verified externally because writing it into the same commit would create another SHA.

## Unexpected Changes

No unexpected material path changes were observed. Any closure path outside this Matrix, any non-fast-forward baseline movement, or any closure-head CI failure invalidates closure until diagnosed.

## State

`CLOSED / VERIFIED MATERIAL / CLOSURE EXACT-HEAD CI REQUIRED`