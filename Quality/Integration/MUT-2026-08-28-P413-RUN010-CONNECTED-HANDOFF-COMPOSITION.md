# P413 Mutation Matrix — Connected RUN-010 Handoff Composition

Status: PREWRITE / TEST-ONLY

| Mutation | Scope | Expected invariant | Production side effect |
|---|---|---|---|
| Compose connected RUN-010 execution with existing handoff contract | `Runtime/Execution/connected_spine_runner.py` | The existing authorized execution reaches `build_handoff_candidate` with execution identity and governed `authorization_id` preserved | None; candidate construction only |
| Assert connected runner exposes the candidate | `Runtime/Execution/test_connected_spine_runner.py` | Candidate identity matches execution and authorization output | None |
| Negative authorization path | Same runner/test | Blocked authorization yields no handoff candidate | None |

Boundary: no ENG-006/SRV-009 dispatch, no RepositoryConnector invocation, no production I/O, no canonical mutation, no promotion.

Evidence target: prove upstream connected-spine reachability to the already-governed handoff contract only. This does not prove downstream ENG-006 execution.
