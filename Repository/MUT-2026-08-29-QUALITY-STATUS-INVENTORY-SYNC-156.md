# MUT-2026-08-29 — QUALITY STATUS INVENTORY SYNC — 156

State: PREWRITE / NOT CLOSED
Role: HERMUZ via Room71
Baseline: `e514ce34001d5082d24c3d0d66b11e462f0b51cf`
Scope: `Quality/_FOLDER_STATUS.md` top-level inventory truthfulness only + regression

## Gap

Current Quality status says its verified inventory contains only QLT-001 and `_FOLDER_STATUS.md`, and later says `Local inventory reconciled`.

Current physical top-level Quality contents also contain:
- directories `Integration/`, `Integrity/`, `P4/`, `P5/`, `Tests/`;
- `P5_CONTROLLED_MUTATION_RECONCILIATION_HARNESS_TEST_MATRIX_2026-08-17.md`;
- empty tracked placeholders `QLT-002..005`.

Therefore the old status is a bounded under-reporting drift. Lease 153 already classified QLT-002..005 as empty legacy placeholders with no capability/authority established.

## Intended Mutation

- preserve Quality Version `1.1.0` and `INTEGRITY HOLD`;
- distinguish exact current top-level physical inventory from reviewed/canonical capability inventory;
- list QLT-002..005 as zero-byte legacy placeholders, not capabilities;
- list current Quality subdirectories and P5 matrix without converting their existence into certification;
- keep recursive/cross-layer/global Quality validation open;
- add regression preventing future `Local inventory reconciled` wording from coexisting with omission of the known top-level surfaces.

## Non-Claims

No Quality domain PASS, no QLT placeholder promotion, no recursive tree certification, no Core136 work, no Room71 JSON rewrite.

## Close Gate

Status + regression + finalized Matrix must enter one final Git tree/commit and pass exact-head read-back/CI where available.
