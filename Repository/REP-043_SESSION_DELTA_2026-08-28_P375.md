# P375 — Experience Spine Candidate Build

Date: 2026-08-28
Branch: `feature/experience-spine-p375`
Base main SHA: `09b216e403fe99a6f1a4a35e3c3038831398f6a3`
Status: `CLOSED / VERIFIED CANDIDATE / NO CANONICAL PROMOTION`
Protocol: `GOV-013 / GOV-013A / GOV-014 / GOV-015 / GOV-016`

## RE-ENTRY

The GitHub connector verified repository identity, write access, default branch `main`, and current main SHA. Current bootstrap, status, control-plane, Knowledge, Memory, Learning, retrieval, promotion, and latest P374 evidence were read from current main.

P374 remains the current REL-009 continuation point. This work is isolated on a dedicated branch and does not alter REL-009, Runtime dispatch, production side effects, or `main`.

## PRIOR-LEARNING CLASSIFICATION

- `CORE-012`, `GOV-015`, `GOV-016`, `ENG-007`, `MEM-001`: `DIRECTLY APPLICABLE` for provenance, scope, validation, promotion, and memory-domain boundaries.
- `TASK_CONTEXT_ENVELOPE`, `knowledge_retrieval.py`, `contextual_retrieval.py`: `TRANSFERABLE`; they prove a bounded retrieval prototype but rely on narrow token matching and do not produce a reasoning-ready experience packet.
- EJR/REP session history: `HISTORICAL / NAVIGATION EVIDENCE`; it must not be bulk-loaded or treated as current authority.
- Exact `Experience Spine` artifact: `NOT FOUND` after filename/tree, connector search, and direct neighboring-artifact review. Connector code search returned false negatives for known current files and is classified as an `EVIDENCE SEARCH DEFECT / CONNECTOR INDEX COVERAGE LIMITATION` for this session.

## VERIFIED GAP

ARGO already has capture, evidence, promotion, memory-domain separation, task context, and minimal promoted-knowledge retrieval. The bounded gap is the absence of one deterministic packet contract that:

1. retrieves only explicit task-relevant experience;
2. preserves evidence and authority states separately;
3. reports conflicts instead of hiding them;
4. caps context size to avoid distraction;
5. gives reasoning a stable starting order without granting authority.

This is a retrieval/orchestration gap, not evidence of a missing memory domain or permission to create a new canonical model.

## MUTATION SCOPE

- Add `Knowledge/Learning/EXPERIENCE_SPINE_CONTRACT.md` as `CANDIDATE / NON-CANONICAL`.
- Add `Knowledge/Learning/experience_spine.py`.
- Add focused tests in `Knowledge/Learning/test_experience_spine.py`.
- Extend `TASK_CONTEXT_ENVELOPE.md` without removing or redefining its legacy fields.
- Add this checkpoint record.

Untouched: `main`, canonical promotion states, Memory storage, REP-014 relationships, Runtime, Engine, Services, release metadata, and production side effects.

## DESIGN DECISION

The spine is a read-only selector over existing records, not a database. It uses explicit domain/problem/artifact/failure keys, requires scope compatibility, preserves provenance and authority, and caps the packet at ten items.

Free-text similarity alone is deliberately insufficient because it can load attractive but irrelevant history and distract a model from current evidence.

## EVIDENCE STATE

- Need for task-bounded retrieval: `PROVEN` by existing task-context and reuse contracts.
- Existing capture/promotion/memory boundaries: `PROVEN` within inspected artifacts.
- Deterministic packet implementation: `CANDIDATE / TESTABLE`.
- Repository-wide integration: `UNPROVEN`.
- Model-wide behavioral compliance: `UNPROVEN`.
- Canonical authority or promotion: `NOT AUTHORIZED / NOT CLAIMED`.

## VERIFICATION PLAN

1. Run focused Experience Spine tests.
2. Run adjacent Knowledge/Learning tests.
3. Re-read every changed file from the branch.
4. Verify branch commit SHA and changed-file set.
5. Inspect applicable CI if triggered.
6. Update this record with the actual result before closure.

## LOCAL VERIFICATION RESULT

- Focused Experience Spine tests: `5 PASSED`.
- Adjacent retrieval regression tests: `4 PASSED`.
- Combined focused + adjacent result: `9 PASSED`.
- The bundled local Python runtime did not include `pytest`; this was classified as `INFRASTRUCTURE_FAILURE / LOCAL TOOLING LIMITATION`, not a code failure. The nine plain assertion-based test functions were then executed directly with the same Python runtime and all passed.
- Governed CI execution remains required before closure; local direct execution does not replace repository CI evidence.

## BRANCH READ-BACK AND SHA VERIFICATION

- Candidate commit: `25db88f79c2243ab34d0e238289fc4d12563e544`.
- Base/merge-base: `09b216e403fe99a6f1a4a35e3c3038831398f6a3`.
- Compare state: `ahead by 1 / behind by 0` at candidate verification.
- Changed-file set: exactly five planned files.
- All five branch files were fetched again from the candidate commit and their blob SHAs matched the pre-commit blobs.
- Draft PR: `#66`.

## CI VERIFICATION

- Full-Stack Repository Audit run `33193142252`: `SUCCESS`.
- ARGO Runtime Prototype and Integration Tests run `33193142257`: `SUCCESS`.
- Required jobs inspected: `integrity-tests`, `integration-tests`, and `prototype-tests`; all completed successfully, including their test/acceptance steps.

These results verify the candidate branch within the exercised CI scope. They do not prove repository-wide Experience Spine integration or model-wide compliance.

## CLOSE

`EXECUTE → VERIFY → DOCUMENT → RE-READ → COMMIT/SHA VERIFY → CHECKPOINT RECORD → CLOSE`

P375 is closed as a verified, non-canonical candidate on the isolated branch. `main` remains untouched. The next governed decision is review of PR #66 and, only if approved, a separate integration/promotion checkpoint.

## CHECKPOINT

`P375 → focused tests → adjacent regression → connector commit → branch read-back → SHA verification → CI inspection → closure or HOLD.`

