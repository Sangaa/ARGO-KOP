# MUTATION MATRIX — P7 X INTEGRATION MARKDOWN SEMANTIC GUARD — SR1

Transaction: `MUT-2026-09-02-P7-X-INTEGRATION-MARKDOWN-GUARD-SR1`
Parent Transaction: `MUT-2026-09-01-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X`
Work Lease: `HERMUZ-P7-X-SR1-INTEGRATION-MARKDOWN-GUARD-20260902`
Priority: `7 — Core / Transaction X blocker side-repair`
State: `PRE-WRITE MATRIX / LEASE ACTIVE / SIDE-REPAIR / RETURN TO TRANSACTION X AFTER CLOSURE`
Entry HEAD: `43820d41728e39edbacb5b37de4d2ffc51063dda`
Historical failed run: `33542068223`
Historical failed job: `integration-tests / 99970488312`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / applicable Governance / REP-011 / REP-012 + W ADDENDUM / REP-013 / REP-014 / REP-015 / REP-016 + X ADDENDUM`

## Failure boundary

Transaction X candidate `43820d41728e39edbacb5b37de4d2ffc51063dda` remains HARD HOLD because required Runtime run `33542068223` failed both Integrity and Integration jobs.

The exact historical Integration failure is:

`Quality/Integration/test_core_p7_status_sync.py::test_priority7_current_state_is_explicit_bounded_closure`

with failing assertion:

`assert "does not auto-start Priority 8" in queue`

Direct exact-SHA source review proves the current queue addendum contains:

`This addendum does **not** auto-start Priority 8`

The durable no-auto-start invariant therefore exists. The failure is caused by raw-Markdown formatting sensitivity: `**not**` prevents the unformatted substring `does not` from matching.

Classification:

`REAL SEMANTIC / IMPLEMENTATION DEFECT — TEST IMPLEMENTATION DEFECT / MARKDOWN-FORMATTING-SENSITIVE SEMANTIC ASSERTION`.

This is not a missing queue invariant, not a Priority-8 start, and not a stale pre-certification state guard.

## Prior-learning retrieval

Recovered prior evidence:

1. T-C1/T-C2 — DIRECTLY APPLICABLE failure-discipline pattern: preserve failed exact-head evidence, classify the distinct remaining Integration contract, repair only the verified boundary, and re-run on a fresh exact HEAD.
2. Side-repair U — DIRECTLY APPLICABLE sequencing pattern: open a pre-write Matrix, keep the side repair non-promotional, require exact-head 4/4, close documentation-only, verify closure HEAD, then return to the interrupted Priority-7 transaction.
3. Repository search for an existing Markdown-normalization helper/pattern — NOT FOUND after exact, semantic and reverse/content searches. No general parser/helper is justified.

## Bounded simulation

Changing the queue addendum solely to remove Markdown emphasis would modify correct X evidence to satisfy a brittle test and would make presentation syntax control semantics. That is rejected.

Changing the assertion to the currently formatted literal `does **not** auto-start Priority 8` would pass but remain formatting-sensitive.

The smallest durable repair is local semantic normalization inside this test: remove Markdown bold markers from the queue text before asserting the unchanged semantic phrase. This preserves the invariant while decoupling it from emphasis syntax.

## Authorized material change set — exactly 3 paths

1. `Quality/Integration/test_core_p7_status_sync.py`
   - add a local normalized queue semantic view by removing Markdown `**` emphasis markers;
   - keep the exact semantic assertion `does not auto-start Priority 8`;
   - preserve every existing Core closure, Phase-1-open and repository-wide graph anti-overpromotion assertion.
2. `Repository/P7_X_INTEGRATION_MARKDOWN_GUARD_SIDE_REPAIR_2026-09-02_SR1.md`
   - record historical failure provenance, root cause, bounded repair, non-authority and return rule.
3. this Matrix
   - bind the material candidate and verification state in the same atomic material commit.

## Forbidden

- no mutation to `Core/_FOLDER_STATUS.md`;
- no mutation to the X REP-016 queue addendum merely to satisfy formatting;
- no deletion or weakening of the no-auto-start-P8 assertion;
- no mutation to the separately stale Integrity assertion in SR1;
- no X closure inside SR1;
- no Priority-8 start;
- no Phase-1 closure;
- no Connected Baseline closure;
- no repository-wide complete-graph claim;
- no Global `BOOTED / INTEGRITY PASS` claim;
- no reinterpretation of historical failed run `33542068223` as success.

## Atomicity contract

After this pre-write Matrix commit, SR1 material candidate MUST be exactly one commit changing exactly the three authorized paths. Unexpected path expansion = `0`.

## Verification contract

`PRE-WRITE MATRIX → LIVE-PARENT RECHECK → ONE-COMMIT/THREE-PATH MATERIAL CANDIDATE → EXACT-HEAD READ-BACK/COMPARE → FOUR REQUIRED WORKFLOWS → RUNTIME JOB REVIEW → DOCUMENTATION-ONLY SR1 CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION → RETURN TO TRANSACTION X`.

A green candidate does not retroactively alter run `33542068223`.

## Return rule

`BLOCKER SIDE-REPAIR SR1 CLOSED → RETURN TO TRANSACTION X → HANDLE SEPARATELY CLASSIFIED INTEGRITY STALE PRE-CERTIFICATION STATE GUARD`.

SR1 does not become a new global Priority or queue authority.

## Learning candidate

`A SEMANTIC TEST OVER MARKDOWN MUST NOT ACCIDENTALLY MAKE PRESENTATION EMPHASIS PART OF THE SEMANTIC CONTRACT.`

No Governance promotion is authorized from this isolated observation; verify the bounded repair first.