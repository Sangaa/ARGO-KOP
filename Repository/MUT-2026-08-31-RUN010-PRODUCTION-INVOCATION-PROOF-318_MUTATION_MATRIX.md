# MUT-2026-08-31-RUN010-PRODUCTION-INVOCATION-PROOF-318 — Mutation Matrix

Protocol: GOV-013 / GOV-014A
Status: OPEN / PRE-WRITE
Date: 2026-08-31

## Problem
Current repository evidence proves the live `ENG-006 -> SRV-009` adapter against a real GitHub connector, and separately proves the pure `RUN-010` handoff contract. It does not yet prove that an actual governed RUN-010 execution result is passed through `build_handoff_candidate(...)` and then reaches `Services.ENG006_SRV009_PRODUCTION_ADAPTER.execute_update(...)` over the real connector.

## Prior learning applied
- GOV-013 §4A: reuse existing implementation/tests before inventing a new path.
- GOV-013 §8/§9A: smallest sufficient mutation; runtime reachability requires runtime evidence.
- Existing `Quality/Integration/rel009_run010_srv009_observation.py` already composes the required path.
- Existing `.github/workflows/p3-runtime-github-e2e.yml` already supplies isolated-branch GitHub write/read-back/cleanup with `contents: write`.

## Mutation scope

| Change ID | Target | Action | Expected Change | Applied | Verified |
|---|---|---|---|---|---|
| 318-01 | `.github/workflows/p3-runtime-github-e2e.yml` | UPDATE | replace manual `ProductionExecutionCandidate` construction for the live probe with actual authorization + RUN-010 execution + existing REL-009 observation harness | N | N |
| 318-02 | `Quality/Integration/rel009_run010_srv009_observation.py` | KEEP | reuse unchanged | Y | Y |
| 318-03 | Runtime/Services production implementation | KEEP | no new wiring, no authority change, no adapter logic change | Y | Y |
| 318-04 | isolated E2E probe artifact | CREATE/DELETE DURING CI | one noncanonical write, mandatory read-back, then cleanup on isolated branch | N | N |

## Pre-write validation
- Current main HEAD at opening: `b6b1f89ea154e4199146e65e55399708b57a195a`.
- `rel009_run010_srv009_observation.py` performs `build_handoff_candidate -> ProductionExecutionCandidate -> execute_update` and returns attributable trace plus `post_read_verified`.
- `p3-runtime-github-e2e.yml` currently invokes `execute_update` over `GitHubRepositoryConnector` but constructs the candidate manually, leaving RUN-010 production invocation unproven.
- The required proof can therefore be obtained by changing only the live E2E harness; no production module mutation is justified.

## KEEP requirements
Do not alter `Runtime/Execution/run010_handoff_contract.py`, `Services/ENG006_SRV009_PRODUCTION_ADAPTER.py`, authorization semantics, connector implementation, canonical repository artifacts, INTF-006 status, or any production authority declaration.

## Closure gate
`workflow mutation -> isolated branch execution -> actual authorization -> actual RUN-010 result -> handoff builder -> execute_update -> real GitHub write -> read-back verified -> trace continuity asserted -> cleanup verified -> workflow success -> full-stack status checked -> matrix closed`.
