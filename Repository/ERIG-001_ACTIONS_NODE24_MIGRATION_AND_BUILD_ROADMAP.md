# ERIG-001 — Actions/Node24 Migration & Build Roadmap

Status: ACTIVE / GOVERNED

## 1. Trigger
Repeated successful CI runs carried a Node.js 20 deprecation warning. This is classified as an evidence-environment integrity issue, not a test failure.

## 2. Completed
- Inspected the Full-Stack workflow and identified deprecated action majors.
- Migrated `actions/checkout` from v4 to v6.
- Migrated `actions/setup-python` from v5 to v6.
- Migrated `actions/upload-artifact` from v4 to v6.
- Preserved workflow logic; no test semantics were intentionally changed.

## 3. Required verification
For the migration commit:
1. correlate workflow SHA with checkout SHA;
2. verify workflow execution completes;
3. inspect jobs and logs, not only conclusion;
4. confirm the Node20 deprecation warning is absent;
5. confirm all existing gates remain PASS;
6. compare changed files against the intended mutation set;
7. reconcile documentation and closure state.

A green conclusion with the warning still present is NOT a clean migration verification.

## 4. ERIG rule established
`CI PASS` does not imply `evidence-environment CLEAN`.

Absence of a searched artifact does not imply artifact absence until retrieval surfaces appropriate to the claim have been exhausted.

## 5. Currentness / tool-capability learning
For future discrepancies classify before acting:
- EXECUTION_ABSENT
- EVIDENCE_NOT_RETRIEVED
- EVIDENCE_FOUND_WRONG_SURFACE
- EXPECTATION_INVALID
- TOOL_CAPABILITY_MISUSED
- TRUE_EXECUTION_FAILURE

## 6. Mandatory session path
Every session must begin by loading current governance, latest checkpoint, prior learning, current repository state, and relevant relationship/dependency surfaces. Every mutation requires a matrix/preflight, execution, read-back, CI/evidence verification, reconciliation, learning update, and session closure.

## 7. KRS-001 future path
After the CI environment is clean:
KRS-001 pilot reconciliation -> currentness gate -> relationship review -> schema refinement -> second pilot only if justified -> controlled migration.

No bulk document migration before the pilot schema and currentness model are proven.

## 8. Session checkpoint
Migration commit: `5a0960bbeffb0b9757aef803ca4706b8ff01e6fc`
Verification: PENDING
Next mandatory action: CI/log verification and reconciliation.
