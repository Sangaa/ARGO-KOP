# P4 REL-009 Registry Closure Mutation Matrix

Transaction ID: `MUT-2026-08-28-P4-REL009-REGISTRY-CLOSURE-001`
Protocol: `GOV-013 / GOV-014 / GOV-015`
Base: `main@94a9bbb43432f3e098854571130778a498f76299`
Working branch: `hermuz/p4-rel009-registry-closure-20260828`
Scope: controlled canonical registry synchronization and dependent evidence/gate reconciliation for `REL-009` only.

## Entry State

P3 executable proof is merged and exact-main verified.

P4 semantic/evidence reconciliation is merged and exact-main verified.

Current bounded semantic disposition:

`REL-009 = INTENTIONAL ONE-WAY / CONSUMES / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`.

Canonical `REP-014` still retains the older state `REVALIDATION REQUIRED`, so P4 canonical closure remains open until a full-content-preserving registry mutation succeeds and dependent guards are reconciled.

Current `REP-014` source blob at transaction entry:

`a6926b0b27e515b38b65594846fd82d1f1252ea9`.

## Prior-Learning Reuse

This transaction reuses the proven method from:

- `Tools/P4_REL005_CONTROLLED_MUTATION.py`;
- `Quality/Tests/test_p4_rel005_controlled_mutation.py`;
- `.github/workflows/p4-rel005-controlled-mutation.yml`.

Classification: `DIRECTLY APPLICABLE METHOD / RELATIONSHIP-SPECIFIC ASSUMPTIONS MUST BE REBUILT`.

The reusable method is:

`exact source blob -> runner-side full-content fetch -> deterministic candidate builder -> targeted-only assertions -> branch write -> post-write full read-back -> candidate blob verification -> request disposition`.

No REL-005 semantic assumption is copied into REL-009.

## Consumer Impact Findings

Fresh impact review found that a registry-only change would intentionally break stale safety assumptions:

1. `.github/workflows/full-stack-audit.yml` still requires `REVALIDATION REQUIRED` for REL-009.
2. `Quality/Integrity/test_critical_graph_bidirectional_boundaries.py` still asserts the historical statement that executable consumer proof is not established.
3. `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` still states `SERVICE_DISPATCH` has no independent callable-consumer source evidence, which is stale after merged P3/P4 evidence.
4. `Repository/P4_CRITICAL_GRAPH_VALIDATION_MATRIX_2026-08-17.md` and `Repository/P4_REL009_CONSUMER_BOUNDARY_MATRIX_2026-08-17.md` currently say registry sync pending and therefore require closure reconciliation after successful mutation.
5. `Repository/REP-022_CURRENT_PRIORITY_RECONCILIATION_2026-08-17.md` still records P3/P4 as open; it is the current-priority reconciliation surface and should be synchronized while preserving historical queue wording in REP-016.

`REP-016` is deliberately not rewritten by this transaction. It is a large historical/current queue surface; current-state precedence is handled through REP-022, consistent with the existing P2 reconciliation pattern.

## Mutation Rows

| ID | Target | Action | Expected Result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| C01 | `Tools/P4_REL009_CONTROLLED_MUTATION.py` | ADD | deterministic full-content candidate builder guarded by exact source blob and targeted row/section boundaries | N | N |
| C02 | `Quality/Tests/test_p4_rel009_controlled_mutation.py` | ADD | builder regressions prove targeted change + unrelated-content preservation + stale-SHA rejection | N | N |
| C03 | `.github/workflows/p4-rel009-controlled-mutation.yml` | ADD | isolated branch-only runner fetch/write/read-back mutation path; never targets main directly | N | N |
| C04 | `.github/workflows/full-stack-audit.yml` | UPDATE | replace obsolete REVALIDATION-required gate with bounded directional/non-universal registry gate | N | N |
| C05 | `Quality/Integrity/test_critical_graph_bidirectional_boundaries.py` | UPDATE | preserve isolated-vs-ordinary-runtime distinction and validate intentional directional state | N | N |
| C06 | `Repository/REP-020_DEPENDENCY_CONSUMER_IMPACT_MATRIX.md` | UPDATE | SERVICE_DISPATCH acknowledges isolated observation while ordinary connected-spine routing remains unproven | N | N |
| C07 | `Repository/P4_REL009_MUTATION_REQUEST.json` | ADD / WORKFLOW-UPDATE | exact source blob + approved branch transaction; workflow records APPLIED/read-back evidence | N | N |
| C08 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | RUNNER-CONTROLLED UPDATE | change only REL-009 row + REL-009 current reconciliation block; preserve all other registry content | N | N |
| C09 | `Repository/P4_CRITICAL_GRAPH_VALIDATION_MATRIX_2026-08-17.md` | UPDATE AFTER C08 | mark REL-009 registry synchronized and close listed P4 critical-edge set within bounded scope | N | N |
| C10 | `Repository/P4_REL009_CONSUMER_BOUNDARY_MATRIX_2026-08-17.md` | UPDATE AFTER C08 | mark registry sync complete and bounded REL-009 disposition closed | N | N |
| C11 | `Repository/REP-022_CURRENT_PRIORITY_RECONCILIATION_2026-08-17.md` | UPDATE AFTER C08 | record P3 proof closed and P4 listed critical-edge set closed; preserve broader Connected-Baseline open state | N | N |

## Registry Target State

Relationship identity and type remain unchanged:

`REL-009 | RUN-010 | SRV-009 | CONSUMES`.

Only State becomes:

`INTENTIONAL ONE-WAY / ISOLATED EXECUTION-OBSERVED / GOVERNED / NON-UNIVERSAL`.

The current REL-009 reconciliation block will state:

- executable evidence exists in the isolated governed observation seam;
- exact-main CI verifies that seam and the negative connected-spine boundary together;
- the normal connected spine remains simulation-only and does not establish universal routing;
- no `SRV-009 -> RUN-010` reverse dependency is created;
- provider-backed ENG-006/SRV-009 evidence and isolated RUN-010 observation remain distinct evidence classes.

## Preservation Boundary

Mandatory KEEP:

- all REP-014 content outside the REL-009 row and REL-009 reconciliation block;
- REL-005 row and reconciliation;
- REL-061 row and reconciliation;
- registry source/target/type for REL-009;
- Runtime/RUN-010 contract;
- Services/SRV-009 contract;
- normal connected spine implementation;
- historical records and journal evidence;
- HORUS/Experience Spine branches and files.

Unexpected Changes = `0`.

## Concurrency Rule

HORUS PR #66 is concurrently active. This transaction must re-read immediately before PR merge:

`main HEAD -> transaction head -> HORUS #66 head -> exact changed filenames -> semantic overlap -> CI state`.

No HORUS branch rebase, merge or mutation is authorized by this transaction.

## Execution Order

1. Add builder/test/workflow.
2. Reconcile dependent gate/test/impact surfaces.
3. Re-read all pre-trigger files and branch diff.
4. Create mutation request LAST to trigger controlled branch mutation.
5. Inspect mutation workflow job/steps/log and request read-back.
6. Verify REP-014 full-content mutation by row, reconciliation block, blob SHA and changed-file diff.
7. Update P4 matrices + REP-022 to final bounded closure state.
8. Update this matrix to `Applied/Verified = Y` only from evidence.
9. Open PR and run exact-head Full-Stack + Runtime/Integration CI.
10. Recheck concurrency and merge only if clean.
11. Run post-merge exact-main CI and update resume surface.

## Closure Boundary

Successful C08 does not imply repository-wide graph closure.

Target closure claim is only:

`P4 LISTED CRITICAL-EDGE SET = CLOSED / REL-009 DIRECTIONAL DISPOSITION CANONICALLY SYNCHRONIZED / BROADER CONNECTED BASELINE OPEN`.
