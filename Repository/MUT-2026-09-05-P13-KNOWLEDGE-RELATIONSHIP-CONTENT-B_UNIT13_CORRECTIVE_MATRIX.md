# CORRECTIVE MATRIX — P13 KNOWLEDGE B / UNIT 13 EXACT-HEAD INTEGRITY REPAIR

Parent transaction: `MUT-2026-09-05-P13-KNOWLEDGE-RELATIONSHIP-CONTENT-B`
Failed head: `239e8d827f4f3895e4abe5b803f26c9f947be72f`
Failed workflow: `ARGO Runtime Prototype and Integration Tests` run `33983831433`
Failure scope: `integrity-tests only / 9 assertions / prototype + integration passed`
State: `CORRECTIVE GUARD REALIGNMENT / NO SEMANTIC SOURCE ROLLBACK`

## Root cause classes

The nine failures are guard representation drift exposed after later verified P13 work, plus one Unit-12 projection assertion:

1. cross-layer target identity guard accepted only `Document ID` metadata and rejected legacy-stable first-H1 identity such as current `REP-009` (`# REP-009`);
2. KNW-006/010 identity-migration guards searched the whole document for historical stale paths, conflicting with intentionally preserved repair provenance; the stable contract is that stale paths are absent from the active `Related Documents` section;
3. KNW-006 and KNW-010 semantic guards remained pinned to v1.1.1 after Unit-8 identity repair legitimately advanced them to v1.1.2 without undoing their semantic repairs;
4. Unit-12 REP-013 addendum guard incorrectly required nested relative paths to appear as flat strings in a human-readable tree; exact path authority is the bound Transaction-A TSV + count/digest, while the tree is a projection;
5. Models closure guard required the pre-P13 REP-016 manifest boundary string even though P13 current-state refresh correctly added `P13 KNOWLEDGE OPEN` while retaining P12 bounded closure;
6. Models registry guard incorrectly required the entire current registry to equal `REL-001..123` and REP-014 v1.2.20, although Unit-7 validly added REL-124..167 and advanced REP-014 to v1.2.21. P12 invariants require its cohort to remain present and exact, not that later cohorts never exist.

## Verification-method learning

A separate process error was also identified: an earlier check treated absence of `in_progress` as completion without also excluding `queued`. Going forward, exact-head acceptance requires every expected workflow family to be explicitly `status=completed` and `conclusion=success`.

`NOT IN_PROGRESS != COMPLETED SUCCESS`.

## Authorized changes

Exactly eight guard/control paths; no semantic Knowledge source, REP-001/002/012/013/014/016/020 authority artifact, or allocation plan is changed:

1. `Quality/Integrity/test_knowledge_p13_cross_layer_allocation_plan.py`
2. `Quality/Integrity/test_knowledge_p13_identity_migration_residue.py`
3. `Quality/Integrity/test_knowledge_p13_knw006_authority_scope.py`
4. `Quality/Integrity/test_knowledge_p13_knw010_maintenance_disposition.py`
5. `Quality/Integrity/test_knowledge_p13_rep013_exact_content_tree_addendum.py`
6. `Quality/Integrity/test_models_p12_closure_state.py`
7. `Quality/Integrity/test_models_p12_registry_allocation_plan.py`
8. this corrective Matrix

## Corrective semantic boundaries

- accept identity at the stable representation actually used by the target: explicit Document-ID metadata where present, otherwise exact first-H1 identity;
- preserve historical stale-path provenance while prohibiting stale paths in active Related Documents;
- later artifact version repair must not invalidate an earlier semantic invariant if the invariant remains present;
- later relationship cohorts must not invalidate the exact P12 cohort; test subset/exact-row preservation rather than eternal end-of-registry position;
- later queue/current-manifest progress must not reopen or erase bounded P12 closure;
- Unit-12 exact path proof remains the immutable TSV/count/digest; Markdown tree representation need not flatten directory prefixes.

## Required gate

`CORRECTIVE COMMIT → COMPARE EXACT 8 PATHS → READ-BACK → ALL FOUR WORKFLOW FAMILIES EXPLICITLY COMPLETED/SUCCESS`

No Unit-14 work may begin before that gate passes.

---

End of Corrective Matrix
