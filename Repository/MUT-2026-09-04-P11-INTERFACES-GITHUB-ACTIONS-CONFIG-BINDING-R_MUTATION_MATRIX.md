# MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-CONFIG-BINDING-R — MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-ACTIONS-CONFIG-BINDING-R`

Priority: `11 — Interfaces`

Protocol: governed bounded mutation; protected implementation + focused semantic test + mutation record are co-committed, followed by exact-head CI and Matrix-only closure.

## Semantic contract

The GitHub Actions connector direct-construction boundary must reject missing, blank, or non-text repository owner, repository name, credential, and API endpoint values. Direct construction must not bypass the same minimum identity/credential validity already enforced by `from_environment()`.

This transaction does **not** impose token format, repository-name syntax, URL reachability, timeout policy, workflow authority, or execution success from possession of configuration.

## Mutation set

| Change ID | Target | Action | Expected Content | Applied | Verified |
| --- | --- | --- | --- | --- | --- |
| R-001 | `Services/GITHUB_ACTIONS_CONNECTOR.py` | MODIFY | Validate direct `owner`, `repo`, `token`, and `api_base` inputs as exact nonblank strings using the existing Actions incomplete-configuration failure family. | YES | PENDING EXACT-HEAD CI |
| R-002 | `Quality/Integration/test_github_actions_connector_config_binding.py` | CREATE | Prove direct construction rejects missing/blank/non-text boundary values and preserves valid explicit routing values. | YES | PENDING EXACT-HEAD CI |
| R-003 | This Matrix | CREATE / KEEP | Record scope, exclusions, read-back discipline, and unexpected-change handling. | YES | PENDING CLOSURE |

## KEEP / exclusions

- KEEP `from_environment()` stripping and incomplete-configuration behavior unchanged.
- KEEP workflow listing, observation, dispatch, job-lineage, and job-log semantics unchanged.
- KEEP `timeout` outside this transaction; no local contract currently binds its type/range to the environment configuration seam.
- KEEP token/repository/API endpoint format and connectivity claims outside scope beyond exact nonblank text.
- Do not infer Actions authority or workflow completion from syntactically valid configuration.

## Post-write / read-back protocol

After material commit, immutable read-back must confirm the exact source, focused test, and Matrix at the material SHA. Entry-to-material comparison must contain only those three authorized paths. Exact-head CI must then succeed for Full-Stack Repository Audit, ARGO Runtime Prototype and Integration Tests, M2 Multi-Channel Proposal Training, and Real Mutation Matrix Regression before closure.

## Unexpected Changes

Any path outside the three authorized targets, any non-fast-forward baseline movement, or any semantic/CI failure stops closure and requires diagnosis rather than weakening the boundary invariant.

## Material state

`MATERIAL PENDING`