# P4 REL-009 Registry Closure Mutation Matrix

Transaction ID: `MUT-2026-08-28-P4-REL009-REGISTRY-CLOSURE-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@94a9bbb43432f3e098854571130778a498f76299`
Working branch: `hermuz/p4-rel009-registry-closure-20260828`
Status: `BOUNDED CLOSURE RECORDED / FINAL-HEAD CI REQUIRED BEFORE MERGE`
Scope: controlled canonical registry synchronization and dependent evidence/gate reconciliation for `REL-009` only.

## Final Authorized Disposition

`REL-009 = INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`.

Authorized P4 closure claim:

`P4 LISTED CRITICAL-EDGE SET = CLOSED / REL-009 DIRECTIONAL DISPOSITION CANONICALLY SYNCHRONIZED / BROADER CONNECTED BASELINE OPEN`.

No repository-wide graph closure, universal RUN-010 routing, normal connected-spine production dispatch or Global PASS is authorized.

## Mutation Rows

| ID | Target | Action | Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Tools/P4_REL009_CONTROLLED_MUTATION.py` | ADD | deterministic full-content builder with exact-blob/target guards | Y | Y |
| C02 | `Quality/Tests/test_p4_rel009_controlled_mutation.py` | ADD | targeted-preservation and stale-SHA regressions | Y | Y |
| C03 | `.github/workflows/p4-rel009-controlled-mutation.yml` | ADD | isolated branch-only mutation runner | Y | Y |
| C04 | `.github/workflows/full-stack-audit.yml` | UPDATE | bounded registry gate while negative runtime gate remains intact | Y | Y |
| C05 | `Quality/Integrity/test_critical_graph_bidirectional_boundaries.py` | UPDATE | bounded directional state + isolated/normal runtime distinction | Y | Y |
| C06 | `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | UPDATE | isolated SERVICE_DISPATCH evidence without universal routing claim | Y | Y |
| C07 | `Repository/P4_REL009_MUTATION_REQUEST.json` | ADD / WORKFLOW-UPDATE | APPLIED request with source/candidate/applied/read-back evidence | Y | Y |
| C08 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | RUNNER UPDATE | REL-009 row/current block only; unrelated registry preserved | Y | Y |
| C09 | `Repository/P4_CRITICAL_GRAPH_VALIDATION_MATRIX_2026-08-17.md` | UPDATE | listed critical-edge set closed within bounded scope | Y | Y |
| C10 | `Repository/P4_REL009_CONSUMER_BOUNDARY_MATRIX_2026-08-17.md` | UPDATE | bounded directional consumer disposition closed | Y | Y |
| C11 | `Repository/REP-022_CURRENT_PRIORITY_RECONCILIATION_2026-08-17.md` | UPDATE | P3 bounded proof closed; P4 listed set closed; broader baseline open | Y | Y |
| C12 | `Quality/Integration/test_control_plane_consumer_relationship_integrity.py` | UPDATE AFTER CI FAILURE | stale absence assertion replaced by bounded-state/non-universal assertions | Y | Y |

## Registry Mutation Evidence

Controlled workflow `33197498585` — SUCCESS.

- builder regressions: 3 passed;
- source blob `a6926b0b27e515b38b65594846fd82d1f1252ea9`;
- mutation commit `dda16b3f2523fea03bf8d8c9724b237ab648046c`;
- candidate/read-back blob `d75f460d152898709044a31433e8ae4c705d9191`;
- request APPLIED;
- verified read-back true.

## CI Reconciliation

First complete-transaction head `66cf5dde3ec3f7e4f94062df45a20ef70db3589e`:

- Full-Stack `33199333266` — SUCCESS;
- Runtime/Integration `33199333252` — FAILURE in exactly one stale integration semantic consumer;
- integrity/prototype — SUCCESS;
- integration suite: 1 failed / 294 passed / 11 subtests passed.

The failure was not treated as noise or rerun blindly. It identified missed consumer C12.

After C12, head `58b1bae849481a22e76058b6f5ec6a4d05f88c46`:

- Full-Stack `33199477029` — SUCCESS;
- Runtime/Integration `33199477054` — SUCCESS.

That PASS authorizes the bounded closure wording now recorded in C09/C10/C11 and this matrix.

## Learning Captured

`IMPACT SEARCH MUST FIND SEMANTIC ASSERTION CONSUMERS, NOT ONLY FIRST-MATCH FILES`.

`BROAD AUDIT PASS ≠ PERMISSION TO IGNORE A NARROWER FAILING CONSUMER`.

`ISOLATED EXECUTION OBSERVATION ≠ UNIVERSAL RUNTIME ROUTING`.

`DIRECTIONAL CONSUMPTION ≠ REQUIRED REVERSE DEPENDENCY`.

`MULTI-WRITER NO-OVERLAP SNAPSHOT EXPIRES WHEN ANY WRITER MOVES`.

## Preservation Boundary

Preserved:

- REP-014 outside REL-009 row/current reconciliation;
- REL-005 / REL-061;
- REL-009 source/target/type;
- Runtime/RUN-010 and Services/SRV-009 contracts;
- normal connected-spine implementation;
- historical records/journals;
- concurrent Experience-Spine/HORUS workstreams.

Unexpected changes observed outside declared C01-C12: `0`.

## Final-Head Rule

The closure wording itself changes the branch head. Therefore one final exact-head Full-Stack + Runtime/Integration run is mandatory before merge.

After that final-head PASS:

- do not mutate this branch further;
- update PR metadata only with final run evidence;
- re-read main and every active PR head/path overlap;
- squash merge with expected head SHA;
- require post-merge exact-main CI before selecting the next engineering front.
