# MUT-2026-09-04-P11-INTERFACES-GITHUB-REPOSITORY-CONFIG-BINDING-Q — MUTATION MATRIX

Transaction ID: `MUT-2026-09-04-P11-INTERFACES-GITHUB-REPOSITORY-CONFIG-BINDING-Q`

Priority: `11 — Interfaces`

Protocol: governed bounded mutation; implementation + focused semantic test + mutation record are co-committed, followed by exact-head CI and Matrix-only closure.

## Semantic contract

The GitHub Contents connector configuration boundary must reject missing, blank, or non-text values for repository identity, credential, branch, and API endpoint whether configuration is created from the environment or constructed directly. Direct construction must not bypass the minimum configuration validity already enforced by the environment path.

This transaction does **not** impose token format, repository-name syntax, branch-name syntax, URL reachability, or authority from possession of credentials.

## Mutation set

| Change ID | Target | Action | Expected Content | Applied | Verified |
| --- | --- | --- | --- | --- | --- |
| Q-001 | `Services/GITHUB_REPOSITORY_CONNECTOR.py` | MODIFY | Validate every explicit `GitHubConnectorConfig` boundary field as a nonblank string at construction time using the existing incomplete-configuration failure family. | YES | PENDING EXACT-HEAD CI |
| Q-002 | `Quality/Integration/test_github_repository_connector_config_binding.py` | CREATE | Prove direct construction rejects missing/blank/non-text values and preserves valid explicit values without adding format claims. | YES | PENDING EXACT-HEAD CI |
| Q-003 | This Matrix | CREATE / KEEP | Record scope, invariant, exclusions, post-write/read-back evidence, and unexpected-change discipline. | YES | PENDING CLOSURE |

## KEEP / exclusions

- KEEP `GitHubConnectorConfig.from_environment()` normalization and defaults unchanged.
- KEEP repository read/create/update/read-back semantics unchanged.
- KEEP token/repository/branch/API format validation outside scope beyond exact nonblank text.
- KEEP Actions connector configuration outside this transaction; it requires independent evidence and validation.
- Do not infer repository authority from a syntactically valid configuration.

## Post-write / read-back protocol

After the material commit, read back the exact source, focused test, and Matrix from the immutable material SHA; compare entry HEAD to material HEAD and require only the three authorized paths above. Exact-head CI must then succeed independently for Full-Stack Repository Audit, ARGO Runtime Prototype and Integration Tests, M2 Multi-Channel Proposal Training, and Real Mutation Matrix Regression before closure.

## Unexpected Changes

Any path outside the three authorized targets, any baseline movement that prevents a non-force fast-forward, or any semantic failure outside the bounded contract stops closure and requires diagnosis rather than weakening the invariant.

## Material state

`MATERIAL PENDING`