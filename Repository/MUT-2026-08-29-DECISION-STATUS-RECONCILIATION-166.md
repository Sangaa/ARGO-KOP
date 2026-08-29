# MUT-2026-08-29 — DECISION STATUS RECONCILIATION — 166

State: REPAIR FINALIZED / AWAITING EXACT-HEAD VERIFICATION
Role: HERMUZ via Room71
Prewrite baseline: `a34902b1317bc265d6431b83235c06817dfde1ba`
Prewrite commit: `cd06d506e73f15c2056080ef8f1f3edd13be1f3b`
Initial functional commit: `80289ef8256ed48d9ed52100bbce8df3f66cdf4a`

## Intended Semantic Change — Preserved

- `Decision/_FOLDER_STATUS.md` created from exact recursive Git-tree evidence (`truncated:false`, 22 tracked files, no subdirectories).
- DEC-001..010 remain the Decision document/navigation family; contracts, Python support and tests remain distinct physical/support surfaces.
- DEC-010 stale `Module Status: Completed` replaced by `INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER VALIDATION OPEN`.
- placeholder `Last Updated: YYYY-MM-DD` replaced by `2026-08-29`.
- Decision-versus-Decision-Memory authority boundary remains preserved.

## Initial Exact-Head Failure

At `80289ef8256ed48d9ed52100bbce8df3f66cdf4a`:
- M2 succeeded.
- Runtime/Integration failed only in `integrity-tests`; prototype and integration jobs succeeded.
- pytest result: `112 passed, 1 failed`.
- failing regression: `test_decision_folder_status_reconciliation.py`.
- failure: `FileNotFoundError` for `Decision/_FOLDER_STATUS.md`.

Root cause:

`TEST_PATH_MODEL_FAILURE / PROCESS_CWD_ASSUMED_TO_BE_REPOSITORY_ROOT`

The Decision status and DEC-010 read-backs were correct. The regression used `Path("Decision/...")`, which depended on process working directory rather than locating the repository from the test file.

## Repair

The semantic assertions are unchanged.

The regression now anchors repository paths using:

`ROOT = Path(__file__).resolve().parents[2]`

and reads Decision targets relative to `ROOT`.

## Learning

`TEST REPOSITORY PATHS MUST BE ANCHORED TO A STABLE REPOSITORY ROOT, NOT PROCESS CWD`.

A test that fails because of an unstated working-directory assumption is a test-model failure, not evidence that the target repository artifact is absent.

## Authority / Claim Boundary

`EXACT PHYSICAL INVENTORY != DECISION DOMAIN CERTIFICATION`

`DECISION_MEMORY != DECISION AUTHORITY`

`TEST PRESENCE != TEST EXECUTION`

Cross-layer, consumer and global Connected Baseline validation remain open.

## Close Gate

Final state becomes `CLOSED / EXECUTION-VERIFIED` only after this repaired regression + this Matrix enter the same repair commit, exact read-back succeeds, and Runtime/Integration, Full-Stack and M2 succeed on the repair head.
