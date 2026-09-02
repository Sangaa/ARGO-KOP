# P7 X — Integration Markdown Semantic Guard Side-Repair SR1

Date: 2026-09-02
Transaction: `MUT-2026-09-02-P7-X-INTEGRATION-MARKDOWN-GUARD-SR1`
Parent: `MUT-2026-09-01-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X`
State: `MATERIAL CANDIDATE PREPARED / SIDE-REPAIR / CI PENDING / RETURN TO X REQUIRED`
Entry HEAD: `43820d41728e39edbacb5b37de4d2ffc51063dda`
Pre-write Matrix HEAD: `7df9530775e7a4244dd54e901bc867d05f11af5c`
Historical failed run: `33542068223`
Historical failed Integration job: `99970488312`

## Proven failure boundary

Historical Runtime evidence on X candidate `43820d41728e39edbacb5b37de4d2ffc51063dda` failed in:

`Quality/Integration/test_core_p7_status_sync.py::test_priority7_current_state_is_explicit_bounded_closure`

Exact failing assertion:

`assert "does not auto-start Priority 8" in queue`

The exact X queue addendum already states:

`This addendum does **not** auto-start Priority 8`

Therefore the no-auto-start-P8 semantic invariant is present. The failure is a test implementation defect caused by raw Markdown emphasis syntax interrupting an unformatted substring match.

Classification:

`REAL SEMANTIC / IMPLEMENTATION DEFECT — TEST IMPLEMENTATION DEFECT / MARKDOWN-FORMATTING-SENSITIVE SEMANTIC ASSERTION`.

It is not a missing invariant, not evidence that Priority 8 started, and not a stale pre-certification state assertion.

## Bounded repair

The test now derives only a local semantic view:

`queue_semantic = queue.replace("**", "")`

and applies the unchanged durable semantic assertion to that view:

`assert "does not auto-start Priority 8" in queue_semantic`

All other assertions remain unchanged, including:

- bounded Core closure markers;
- `CORE CERTIFIED`;
- validated-not-registered boundary;
- repository-wide graph non-completion;
- `CORE CLOSED_FOR_PHASE_1 != PHASE 1 CLOSED`;
- `CORE CERTIFIED != REPOSITORY-WIDE GRAPH COMPLETE`;
- `PRIORITY 7 = CLOSED_FOR_PHASE_1`;
- `GLOBAL PHASE 1 REMAINS OPEN`.

The queue addendum is not changed merely to satisfy test presentation syntax.

## Prior learning applied

- T-C1/T-C2: preserve failed evidence and repair only the independently classified failure boundary.
- Side-repair U: side-repair is non-promotional, must pass fresh exact-head verification, must close resume-safe, then returns to the interrupted Priority-7 transaction.
- No reusable Markdown-normalization helper or established Quality convention was found; no new parser/helper is introduced.

## Historical evidence preservation

Run `33542068223` remains a failed X candidate run. SR1 does not rewrite or reinterpret it. A later successful run, if achieved, is new repair evidence only.

## Non-authority preserved

SR1 does not:

- change Core certification evidence;
- alter the X queue meaning;
- repair the separately classified Integrity stale pre-certification guard;
- close Transaction X;
- start Priority 8;
- close Phase 1;
- close the repository-wide graph or Connected Baseline;
- claim global `BOOTED / INTEGRITY PASS`.

## Return rule

After exact-head material verification and documentation-only closure verification:

`SR1 CLOSED → RETURN TO TRANSACTION X → ADDRESS THE SEPARATE INTEGRITY STALE PRE-CERTIFICATION STATE GUARD`.

## Learning candidate

`A SEMANTIC TEST OVER MARKDOWN SHOULD TOLERATE PRESENTATION EMPHASIS WHEN THE UNDERLYING REQUIRED STATEMENT IS UNCHANGED.`

This remains candidate learning until the bounded repair is verified; no Governance promotion is made here.
