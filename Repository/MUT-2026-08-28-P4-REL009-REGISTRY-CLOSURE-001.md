# P4 REL-009 Registry Closure Mutation Matrix

Transaction ID: `MUT-2026-08-28-P4-REL009-REGISTRY-CLOSURE-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@94a9bbb43432f3e098854571130778a498f76299`
Working branch: `hermuz/p4-rel009-registry-closure-20260828`
Status: `ALL DECLARED ROWS APPLIED / SOURCE-READBACK VERIFIED / EXACT-HEAD CI RE-RUN REQUIRED AFTER C12`
Scope: controlled canonical registry synchronization and dependent evidence/gate reconciliation for `REL-009` only.

## Entry State

P3 executable proof was already merged and exact-main verified.

P4 semantic/evidence reconciliation was already merged and exact-main verified.

Bounded semantic disposition:

`REL-009 = INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`.

At transaction entry canonical `REP-014` retained the older `REVALIDATION REQUIRED` state. The transaction therefore required a full-content-preserving registry mutation plus reconciliation of current guards/status surfaces that depended on the older interpretation.

Entry `REP-014` blob:

`a6926b0b27e515b38b65594846fd82d1f1252ea9`.

## Prior-Learning Reuse

This transaction reused the proven REL-005 controlled-mutation method while rebuilding all REL-009-specific semantic assumptions.

Reusable method:

`exact source blob → runner-side full-content fetch → deterministic candidate builder → targeted-only assertions → isolated branch write → post-write full read-back → candidate blob verification → request disposition`.

## Mutation Rows

| ID | Target | Action | Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Tools/P4_REL009_CONTROLLED_MUTATION.py` | ADD | deterministic full-content candidate builder with exact-blob and targeted row/section guards | Y | Y |
| C02 | `Quality/Tests/test_p4_rel009_controlled_mutation.py` | ADD | targeted change / unrelated-content preservation / stale-SHA regressions | Y | Y |
| C03 | `.github/workflows/p4-rel009-controlled-mutation.yml` | ADD | isolated branch-only runner mutation path; refuses other branches and never targets main directly | Y | Y |
| C04 | `.github/workflows/full-stack-audit.yml` | UPDATE | obsolete state gate replaced by exact bounded directional registry state while negative normal-runtime gate remains intact | Y | Y |
| C05 | `Quality/Integrity/test_critical_graph_bidirectional_boundaries.py` | UPDATE | validates directional bounded state and isolated-vs-normal-runtime distinction instead of historical absence claim | Y | Y |
| C06 | `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | UPDATE | `SERVICE_DISPATCH` acknowledges isolated observation while ordinary connected-spine routing remains unproven | Y | Y |
| C07 | `Repository/P4_REL009_MUTATION_REQUEST.json` | ADD / WORKFLOW-UPDATE | exact source/branch transaction applied; request records candidate SHA, applied commit and verified read-back | Y | Y |
| C08 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | RUNNER-CONTROLLED UPDATE | REL-009 row + current reconciliation updated with unrelated registry content preserved | Y | Y |
| C09 | `Repository/P4_CRITICAL_GRAPH_VALIDATION_MATRIX_2026-08-17.md` | UPDATE | registry synchronization bound to listed critical-edge closure candidate; final CI explicitly pending | Y | Y |
| C10 | `Repository/P4_REL009_CONSUMER_BOUNDARY_MATRIX_2026-08-17.md` | UPDATE | B02 synchronized; bounded disposition canonical; final transaction CI explicitly pending | Y | Y |
| C11 | `Repository/REP-022_CURRENT_PRIORITY_RECONCILIATION_2026-08-17.md` | UPDATE | P3 bounded proof closed; P4 registry-synchronized closure candidate; broader Connected Baseline remains open | Y | Y |
| C12 | `Quality/Integration/test_control_plane_consumer_relationship_integrity.py` | UPDATE AFTER CI FAILURE | replace stale “no executable proof” assertion with bounded directional/non-universal registry assertions | Y | Y |

`Verified=Y` means target/source/read-back reconciliation for the row. It does not replace exact-head integration/Full-Stack CI.

## Controlled Registry Execution Evidence

Workflow `P4 REL-009 Controlled Mutation` run `33197498585` — `SUCCESS`.

- builder regressions: `3 passed`;
- source REP-014 blob: `a6926b0b27e515b38b65594846fd82d1f1252ea9`;
- applied registry commit: `dda16b3f2523fea03bf8d8c9724b237ab648046c`;
- candidate/read-back blob: `d75f460d152898709044a31433e8ae4c705d9191`;
- request state: `APPLIED`;
- `verified_readback = true`.

## Exact-Head CI Incident / Learning

PR #70 first complete-transaction CI at head `66cf5dde3ec3f7e4f94062df45a20ef70db3589e` produced:

- Full-Stack Repository Audit `33199333266` — `SUCCESS`;
- Runtime/Prototype/Integration workflow `33199333252` — `FAILURE` only in `integration-tests`;
- `integrity-tests` — `SUCCESS`;
- `prototype-tests` — `SUCCESS`;
- integration suite result: `1 failed, 294 passed, 11 subtests passed`.

Failure:

`Quality/Integration/test_control_plane_consumer_relationship_integrity.py::test_relationship_registry_preserves_partial_runtime_consumer_boundary`

The test still asserted the historical phrases:

- `executable consumer proof is not established`;
- `no executable VERIFIED state is added`.

This was a **consumer-impact discovery gap**, not a repository-state rollback. The initial impact search found the Full-Stack and critical-graph guards but missed this second semantic consumer.

C12 repairs the assertion without weakening the boundary. It now requires:

- the exact bounded REL-009 registry state;
- explicit non-universal semantics;
- explicit preservation of normal connected-spine non-production behavior.

Reusable learning:

`IMPACT SEARCH MUST FIND SEMANTIC ASSERTION CONSUMERS, NOT ONLY FILES RETURNED BY THE FIRST PHRASE/PATH SEARCH`.

A green broad audit does not override a failing narrower integration consumer; both must be reconciled.

## Registry Target State

Relationship identity/type remain unchanged:

`REL-009 | RUN-010 | SRV-009 | CONSUMES`.

State:

`INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`.

This means isolated executable evidence exists while normal connected-spine universal routing remains unsupported.

## Preservation Boundary

Preserved:

- REP-014 outside the REL-009 row/current reconciliation block;
- REL-005 / REL-061;
- REL-009 source/target/type;
- RUN-010 and SRV-009 contracts;
- normal connected-spine implementation;
- historical records/journals;
- concurrent HORUS/Experience-Spine workstreams.

Unexpected Changes = `0 observed` beyond declared transaction expansion C12.

## Multi-Writer / Concurrency Rule

Immediately before merge re-read:

`main HEAD → transaction head → all active PR heads → exact changed filenames → semantic overlap → exact-head CI`.

Prior no-overlap observations expire whenever any writer moves.

## Remaining Execution Order

1. Re-run exact-head Full-Stack + Runtime/Integration CI after C12.
2. If PASS, update P4 matrices + REP-022 + this matrix to bounded final closure wording.
3. Run final-head CI after that documentation-only closure commit.
4. Recheck multi-writer state.
5. Squash merge only if reviewed head/base remain current.
6. Observe post-merge exact-main CI before advancing roadmap.

## Closure Boundary

Only after the remaining gates pass:

`P4 LISTED CRITICAL-EDGE SET = CLOSED / REL-009 DIRECTIONAL DISPOSITION CANONICALLY SYNCHRONIZED / BROADER CONNECTED BASELINE OPEN`.

Repository-wide graph closure, universal RUN-010 routing and Global PASS remain unsupported.
