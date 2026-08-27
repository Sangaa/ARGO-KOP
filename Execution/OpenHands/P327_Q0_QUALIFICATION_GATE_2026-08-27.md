# P327 — OpenHands Q0 Qualification Gate

Status: `IMPLEMENTED / CI-PENDING / NO-AUTHORIZATION / NO-MUTATION`

## Purpose
The local environment previously failed Q0 because Docker was unavailable. Instead of weakening the gate or performing a partial installation, this session adds an isolated GitHub-hosted qualification path.

## Exact Boundary
- Runner: `ubuntu-latest`.
- No repository checkout is performed.
- Docker availability is tested with `docker version`, `docker info`, and a disposable `hello-world` container.
- OpenHands target is pinned to `1.14.0` and installed into an isolated `uv` tool environment using Python 3.12.
- Only identity/version/environment evidence is produced.
- GitHub repository credentials are explicitly asserted absent.
- No ARGO workspace is mounted into OpenHands.
- No repository write is attempted.

## Gate Meaning
A successful workflow proves that the qualification environment can supply the required Docker boundary and the pinned OpenHands executable. It does not authorize OpenHands, prove Q1 repository understanding, or establish any mutation capability.

## Promotion Boundary
Q1 remains separately gated and read-only. Q2+ remain unauthorized until their explicit qualification evidence exists.

`Q0 = ENVIRONMENT/IDENTITY GATE`
`Q1 = NOT AUTHORIZED`
`Q2-Q7 = NOT AUTHORIZED`
`REPOSITORY MUTATION = NONE`
`MAIN = UNCHANGED`
