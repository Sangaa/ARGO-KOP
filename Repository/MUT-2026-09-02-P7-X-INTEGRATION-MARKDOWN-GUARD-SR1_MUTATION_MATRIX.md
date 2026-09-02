# MUTATION MATRIX — P7 X INTEGRATION MARKDOWN SEMANTIC GUARD — SR1

Transaction: `MUT-2026-09-02-P7-X-INTEGRATION-MARKDOWN-GUARD-SR1`
Parent Transaction: `MUT-2026-09-01-P7-CORE-EXPLICIT-CERTIFICATION-CLOSURE-X`
Work Lease: `HERMUZ-P7-X-SR1-INTEGRATION-MARKDOWN-GUARD-20260902`
Priority: `7 — Core / Transaction X blocker side-repair`
State: `MATERIAL CANDIDATE PREPARED / CI PENDING / SIDE-REPAIR / LEASE ACTIVE`
Entry HEAD: `43820d41728e39edbacb5b37de4d2ffc51063dda`
Pre-write Matrix HEAD: `7df9530775e7a4244dd54e901bc867d05f11af5c`
Historical failed run: `33542068223`
Historical failed job: `integration-tests / 99970488312`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-013A / applicable Governance / REP-011 / REP-012 + W ADDENDUM / REP-013 / REP-014 / REP-015 / REP-016 + X ADDENDUM`

## Failure boundary and classification

Exact historical Integration failure:

`Quality/Integration/test_core_p7_status_sync.py::test_priority7_current_state_is_explicit_bounded_closure`

`assert "does not auto-start Priority 8" in queue`

Exact X queue evidence contains:

`This addendum does **not** auto-start Priority 8`

Classification:

`REAL SEMANTIC / IMPLEMENTATION DEFECT — TEST IMPLEMENTATION DEFECT / MARKDOWN-FORMATTING-SENSITIVE SEMANTIC ASSERTION`.

The durable no-auto-start invariant exists; Markdown emphasis alone caused the raw substring mismatch.

## Prior-learning disposition

- T-C1/T-C2 — DIRECTLY APPLICABLE failure isolation and preserved-failure pattern.
- Side-repair U — DIRECTLY APPLICABLE pre-write/atomic/exact-head/return sequencing pattern.
- Existing Markdown-normalization helper/convention — NOT FOUND after materially different searches.

## Material repair decision

SR1 does not rewrite correct queue evidence and does not bind semantics to the current bold formatting. It creates a local semantic view with Markdown bold markers removed and runs the unchanged no-auto-start assertion against that view.

## Authorized material change set — exactly 3 paths

| ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| SR1-01 | `Quality/Integration/test_core_p7_status_sync.py` | locally normalize Markdown `**` emphasis for the no-auto-start semantic assertion while preserving all existing durable guards | Y | PENDING CI |
| SR1-02 | `Repository/P7_X_INTEGRATION_MARKDOWN_GUARD_SIDE_REPAIR_2026-09-02_SR1.md` | preserve historical failure, root cause, bounded repair and return rule | Y | PENDING CI |
| SR1-03 | this Matrix | bind the candidate in the same material commit | Y | PENDING CI |

Candidate binding: `THIS MATERIAL COMMIT`.

Required atomicity: exactly one commit after `7df9530775e7a4244dd54e901bc867d05f11af5c`, exactly three authorized paths, unexpected path expansion `0`.

## Durable boundaries preserved

- no-auto-start Priority 8 invariant remains asserted;
- `GLOBAL PHASE 1 REMAINS OPEN` remains asserted;
- Core closure does not imply Phase-1 closure;
- Core certification does not imply repository-wide graph completion;
- validated-not-registered and non-complete-graph boundaries remain asserted;
- X historical failure evidence remains failed evidence.

## Forbidden

- no `Core/_FOLDER_STATUS.md` mutation;
- no X REP-016 addendum mutation to appease formatting;
- no test deletion or semantic weakening;
- no separately stale Integrity-guard mutation in SR1;
- no X closure;
- no Priority-8 start;
- no Phase-1 / Connected Baseline / repository-wide graph / Global PASS promotion.

## Verification contract

`ONE-COMMIT/THREE-PATH COMPARE → LIVE-PARENT RECHECK → NON-FORCE FAST-FORWARD → EXACT-HEAD READ-BACK → FOUR REQUIRED WORKFLOWS → FULL-STACK/RUNTIME JOB REVIEW → DOCUMENTATION-ONLY SR1 CLOSURE → CLOSURE-HEAD FOUR-WORKFLOW VERIFICATION → RETURN TO TRANSACTION X`.

## Return rule

`BLOCKER SIDE-REPAIR SR1 CLOSED → RETURN TO TRANSACTION X → HANDLE SEPARATE INTEGRITY STALE PRE-CERTIFICATION STATE GUARD`.

SR1 does not become global NEXT authority.

## Learning candidate

`A SEMANTIC TEST OVER MARKDOWN MUST NOT ACCIDENTALLY MAKE PRESENTATION EMPHASIS PART OF THE SEMANTIC CONTRACT.`

No Governance promotion is authorized from this isolated repair before verification.
