# OpenHands Installation & Q0 Baseline — 2026-08-27

Status: `PLANNING / NOT INSTALLED / NOT AUTHORIZED`
Authority: `Execution/OpenHands/OPENHANDS_INTEGRATION_AND_QUALIFICATION_PLAN.md`

## Product Selection

Selected qualification target: **OpenHands v1.14.0** (stable release).

Selection basis: current official OpenHands release evidence available on 2026-08-27. The qualification target is pinned to a release rather than `latest` or `main` so Q0 evidence remains reproducible.

## Installation Strategy

Preferred local qualification path: OpenHands CLI installed with `uv`, Python 3.12+, with Docker used as the sandbox provider.

Alternative local GUI path: `openhands serve` using Docker. No repository workspace is mounted during initial Q0 identity testing.

## Q0 Boundary

Q0 must record, without mutation:

- installed OpenHands version and executable path;
- source/release identifier;
- runtime and OS/workspace identity;
- selected model/provider;
- effective filesystem/workspace permissions;
- network/sandbox configuration;
- Git identity and repository visibility;
- enabled integrations/MCP servers.

No GitHub credentials, repository write token, or production secret is to be supplied during Q0.

## Authorization

`NOT AUTHORIZED` until Q0 evidence is recorded and reviewed.

Q1 requires read-only repository understanding in a safe workspace. Q3/Q4 mutation scopes require separate qualification evidence and dedicated sandbox/branch boundaries.

## Reproducibility Rule

Do not qualify against floating `latest`/`main`. Record exact release/version and runtime image identifiers before each qualification gate.

## Source Evidence

Official release: OpenHands v1.14.0, published 2026-08-17.
Official installation guidance: CLI with `uv`/Python 3.12+ and Docker-backed sandbox.

## Explicit Non-Claims

This record does not claim that OpenHands is installed, tested, connected to ARGO, or authorized to mutate the repository.

`Q0 = NOT TESTED`
`Q1 = NOT TESTED`
`Q2-Q6 = NOT AUTHORIZED`
`Q7 = NOT AUTHORIZED`
