# MUT-2026-09-04-P11-INTERFACES-GITHUB-REPOSITORY-CONFIG-BINDING-Q — MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-REPOSITORY-CONFIG-BINDING-Q`

Priority: `11 — Interfaces`

Protocol: governed bounded mutation; implementation + focused semantic test + mutation record were co-committed, material exact-head CI was required, and closure is Matrix-only with an independent closure-head CI cycle.

## Semantic contract

The GitHub Contents connector configuration boundary must reject missing, blank, or non-text values for repository identity, credential, branch, and API endpoint whether configuration is created from the environment or constructed directly. Direct construction must not bypass the minimum configuration validity already enforced by the environment path.

This transaction does **not** impose token format, repository-name syntax, branch-name syntax, URL reachability, or authority from possession of credentials.

## Mutation set

| Change ID | Target | Action | Expected Content | Applied | Verified |
| --- | --- | --- | --- | --- | --- |
| Q-001 | `Services/GITHUB_REPOSITORY_CONNECTOR.py` | MODIFY | Validate every explicit `GitHubConnectorConfig` boundary field as a nonblank string at construction time using the existing incomplete-configuration failure family. | YES | YES |
| Q-002 | `Quality/Integration/test_github_repository_connector_config_binding.py` | CREATE | Prove direct construction rejects missing/blank/non-text values and preserves valid explicit values without adding format claims. | YES | YES |
| Q-003 | This Matrix | CREATE / KEEP | Record scope, invariant, exclusions, post-write/read-back evidence, and unexpected-change discipline. | YES | YES |

## KEEP / exclusions

- KEEP `GitHubConnectorConfig.from_environment()` normalization and defaults unchanged.
- KEEP repository read/create/update/read-back semantics unchanged.
- KEEP token/repository/branch/API format validation outside scope beyond exact nonblank text.
- KEEP Actions connector configuration outside this transaction; it requires independent evidence and validation.
- Do not infer repository authority from a syntactically valid configuration.

## Post-write / read-back evidence

Material HEAD: `915f4b70a1ec06825fa3bab2d16dbe19028688c0`.

Entry-to-material comparison contained exactly the three authorized paths: the protected Contents connector source, the focused configuration-binding test, and this Matrix. Immutable material read-back confirmed the construction-time validation and focused test content.

Material exact-head CI succeeded independently for all required workflow families:
- Full-Stack Repository Audit — run `33910927876` — `completed / success`
- ARGO Runtime Prototype and Integration Tests — run `33910928125` — `completed / success`
- M2 Multi-Channel Proposal Training — run `33910928090` — `completed / success`
- Real Mutation Matrix Regression — run `33910928005` — `completed / success`

Closure mutation is restricted to this Matrix. Closure validity additionally requires a fresh four-family exact-head CI cycle on the resulting closure SHA; that evidence cannot be written into the same SHA without creating another SHA and is therefore verified externally after the Matrix-only closure commit.

## Unexpected Changes

No unexpected material path changes were observed. Any closure path outside this Matrix, any non-fast-forward baseline movement, or any closure-head CI failure invalidates closure until diagnosed.

## State

`CLOSED / VERIFIED MATERIAL / CLOSURE EXACT-HEAD CI REQUIRED`