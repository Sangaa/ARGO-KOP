# P4 REL-009 Registry Closure Mutation Matrix

Transaction ID: `MUT-2026-08-28-P4-REL009-REGISTRY-CLOSURE-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@94a9bbb43432f3e098854571130778a498f76299`
Working branch: `hermuz/p4-rel009-registry-closure-20260828`
Status: `ALL DECLARED ROWS APPLIED / SOURCE-READBACK VERIFIED / FINAL EXACT-HEAD CI PENDING`
Scope: controlled canonical registry synchronization and dependent evidence/gate reconciliation for `REL-009` only.

## Entry State

P3 executable proof was already merged and exact-main verified.

P4 semantic/evidence reconciliation was already merged and exact-main verified.

Bounded semantic disposition:

`REL-009 = INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`.

At transaction entry canonical `REP-014` retained the older `REVALIDATION REQUIRED` state. The transaction therefore required a full-content-preserving registry mutation plus reconciliation of every current guard/status surface that depended on the older interpretation.

Entry `REP-014` blob:

`a6926b0b27e515b38b65594846fd82d1f1252ea9`.

## Prior-Learning Reuse

This transaction reused the proven method from:

- `Tools/P4_REL005_CONTROLLED_MUTATION.py`;
- `Quality/Tests/test_p4_rel005_controlled_mutation.py`;
- `.github/workflows/p4-rel005-controlled-mutation.yml`.

Classification:

`DIRECTLY APPLICABLE METHOD / RELATIONSHIP-SPECIFIC ASSUMPTIONS REBUILT`.

Reusable method:

`exact source blob → runner-side full-content fetch → deterministic candidate builder → targeted-only assertions → isolated branch write → post-write full read-back → candidate blob verification → request disposition`.

No REL-005 semantic assumption was copied into REL-009.

## Consumer Impact Findings

Fresh impact review found that a registry-only update would leave or intentionally break stale safety assumptions:

1. `.github/workflows/full-stack-audit.yml` required `REVALIDATION REQUIRED` for REL-009.
2. `Quality/Integrity/test_critical_graph_bidirectional_boundaries.py` asserted the historical absence of executable consumer proof.
3. `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` stated `SERVICE_DISPATCH` had no independent callable-consumer evidence.
4. Both P4 matrices still treated registry synchronization as pending.
5. `REP-022` still recorded P3/P4 as open.

`REP-016` was deliberately preserved as historical queue evidence. Current-state precedence remains in REP-022, consistent with the existing P2 reconciliation model.

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
| C08 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | RUNNER-CONTROLLED UPDATE | REL-009 row + current reconciliation updated with all unrelated registry content preserved | Y | Y |
| C09 | `Repository/P4_CRITICAL_GRAPH_VALIDATION_MATRIX_2026-08-17.md` | UPDATE | registry synchronization bound to listed critical-edge closure candidate; final CI explicitly pending | Y | Y |
| C10 | `Repository/P4_REL009_CONSUMER_BOUNDARY_MATRIX_2026-08-17.md` | UPDATE | B02 synchronized; bounded disposition canonical; final transaction CI explicitly pending | Y | Y |
| C11 | `Repository/REP-022_CURRENT_PRIORITY_RECONCILIATION_2026-08-17.md` | UPDATE | P3 bounded proof closed; P4 registry-synchronized closure candidate; broader Connected Baseline remains open | Y | Y |

`Verified=Y` above means target/source/read-back reconciliation has been completed for the declared mutation row. It does **not** replace the remaining exact-head integration/Full-Stack CI gate on the complete transaction.

## Controlled Registry Execution Evidence

Workflow:

`P4 REL-009 Controlled Mutation` run `33197498585` — `SUCCESS`.

Job evidence:

- mutation builder regressions: `3 passed`;
- source REP-014 blob: `a6926b0b27e515b38b65594846fd82d1f1252ea9`;
- applied registry commit: `dda16b3f2523fea03bf8d8c9724b237ab648046c`;
- candidate/read-back blob: `d75f460d152898709044a31433e8ae4c705d9191`;
- request state: `APPLIED`;
- `verified_readback = true`.

Independent connector read-back confirmed the synchronized REL-009 row and current reconciliation block at the same candidate blob.

## Registry Target State

Relationship identity/type remain unchanged:

`REL-009 | RUN-010 | SRV-009 | CONSUMES`.

State is now:

`INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`.

This means:

- executable evidence exists in the isolated governed observation seam;
- normal connected spine remains simulation-oriented and is not universal production routing;
- no `SRV-009 → RUN-010` reverse dependency is created;
- provider-backed ENG-006/SRV-009 evidence and isolated RUN-010 observation remain distinct evidence classes.

## Preservation Boundary

Preserved:

- all REP-014 content outside the REL-009 row/current reconciliation block;
- REL-005 row/reconciliation;
- REL-061 row/reconciliation;
- registry source/target/type for REL-009;
- RUN-010 and SRV-009 contracts;
- normal connected-spine implementation;
- historical records/journals;
- concurrent HORUS/Experience-Spine workstreams.

Current diff reconciliation against `main@94a9bbb...` shows exactly the declared transaction paths and no unrelated Runtime/Engine/Service implementation change.

Unexpected Changes = `0 observed`.

## Multi-Writer / Concurrency Rule

Multiple controlled sessions may write concurrently. Therefore any earlier no-overlap observation expires whenever main or an active branch moves.

Immediately before PR merge re-read:

`main HEAD → transaction head → all active PR heads → exact changed filenames → semantic overlap → exact-head CI`.

No concurrent branch rebase, merge or mutation is authorized by this transaction.

## Remaining Execution Order

1. Open PR on the complete current transaction payload.
2. Observe exact-head Full-Stack + Runtime/Integration CI.
3. If PASS, update P4 matrices + REP-022 + this matrix to bounded final closure wording only.
4. Run final-head CI after that documentation-only closure commit.
5. Recheck multi-writer state.
6. Squash merge only if the reviewed HEAD and base remain the observed state.
7. Observe post-merge exact-main CI before advancing the roadmap.

## Closure Boundary

The only authorized closure claim after the remaining CI gates pass is:

`P4 LISTED CRITICAL-EDGE SET = CLOSED / REL-009 DIRECTIONAL DISPOSITION CANONICALLY SYNCHRONIZED / BROADER CONNECTED BASELINE OPEN`.

Repository-wide graph closure, universal RUN-010 routing and Global PASS remain explicitly unsupported.
