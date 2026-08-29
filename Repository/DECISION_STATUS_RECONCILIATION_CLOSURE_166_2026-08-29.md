# DECISION STATUS RECONCILIATION — CLOSURE 166

Date: 2026-08-29
Role: HERMUZ via Room71
State: CLOSED / EXECUTION-VERIFIED
Initial functional SHA: `80289ef8256ed48d9ed52100bbce8df3f66cdf4a`
Repair SHA: `836d6840713002fd12a4c51abc719c874658ba7b`

## Closed

- created `Decision/_FOLDER_STATUS.md` from exact current Decision Git tree: 22 tracked files, no subdirectories, `truncated:false`;
- separated DEC-001..010 document/navigation family from boundary contracts, Python support and tests;
- replaced stale DEC-010 `Module Status: Completed` with `INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER VALIDATION OPEN`;
- replaced `Last Updated: YYYY-MM-DD` with `2026-08-29`;
- preserved Decision-versus-Decision-Memory authority separation;
- added regression `Quality/Integrity/test_decision_folder_status_reconciliation.py`.

## Initial Failure and Repair

At initial functional SHA `80289ef...`, Runtime/Integration failed only in the new Decision status regression while prototype/integration jobs succeeded. Failure was `FileNotFoundError` caused by assuming process CWD was repository root.

The target Decision artifacts themselves read back correctly.

Repair changed only test path anchoring:

`ROOT = Path(__file__).resolve().parents[2]`

Semantic assertions remained unchanged.

Root cause:

`TEST_PATH_MODEL_FAILURE / PROCESS_CWD_ASSUMED_TO_BE_REPOSITORY_ROOT`

## Exact-Head Verification

At repair head `836d6840713002fd12a4c51abc719c874658ba7b`:

- Full-Stack Repository Audit run `33269834095` — SUCCESS.
- ARGO Runtime Prototype and Integration Tests run `33269834008` — SUCCESS.
- M2 Multi-Channel Proposal Training run `33269834091` — SUCCESS.
- Decision status read-back matched blob `8a443646d1644c957d89244491e8a6ed35101bd2`.
- DEC-010 read-back matched blob `e14b57e9c830dc5ea13518ee449241efa4b2b17c`.
- repaired regression read-back matched blob `c89ccc475c48bb52c50d2a0214551e58a8e9bdef`.

## Bounded Result

`DECISION_STATUS_SURFACE_GAP = CLOSED / EXECUTION-VERIFIED`

`DECISION_PHYSICAL_INVENTORY = CLOSED_FOR_CURRENT_EXACT_TREE`

`DECISION_CROSS_LAYER_VALIDATION = OPEN`

`CONNECTED_BASELINE_GLOBAL = NOT_CLOSED`

## Learning

`TEST REPOSITORY PATHS MUST BE ANCHORED TO A STABLE REPOSITORY ROOT, NOT PROCESS CWD`.

A path-model failure in a regression must not be misclassified as absence of the repository target it intended to inspect.
