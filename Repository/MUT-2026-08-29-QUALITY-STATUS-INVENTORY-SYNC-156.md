# MUT-2026-08-29 — QUALITY STATUS INVENTORY SYNC — 156

State: FINALIZED / AWAITING EXACT-HEAD VERIFICATION
Role: HERMUZ via Room71
Prewrite baseline: `e514ce34001d5082d24c3d0d66b11e462f0b51cf`
Prewrite commit: `2f2e4bee327bc54b7d967beca131be1836f134d3`

## Corrected Status Semantics

- preserves Quality Version `1.1.0` and `INTEGRITY HOLD`;
- replaces the under-reported two-file inventory with the exact current top-level Quality surface;
- distinguishes directories/files from capability/authority;
- classifies QLT-002..005 as tracked zero-byte legacy placeholders with no capability promotion;
- records QLT-001 semantic repair 155 without turning that bounded closure into global Quality certification;
- keeps recursive inventory, cross-layer relationships, execution enforcement and Connected Baseline open.

## Regression

`Quality/Integration/test_quality_folder_status_inventory.py` guards:
- all known current top-level Quality entries are represented;
- `INTEGRITY HOLD` and `TOP-LEVEL INVENTORY VERIFIED` remain explicit;
- placeholder non-capability language remains;
- top-level enumeration is not widened into recursive certification;
- stale `Local inventory reconciled.` wording does not return without an explicit scope.

## Learning

`INVENTORY RECONCILED` is unsafe language without an explicit enumeration boundary.

`TOP-LEVEL PHYSICAL INVENTORY != RECURSIVE INVENTORY != CAPABILITY INVENTORY != EXECUTION CERTIFICATION`.

## Close Gate

Final state becomes `CLOSED / EXECUTION-VERIFIED` only after status + regression + this finalized Matrix enter one Git tree/commit, exact read-back succeeds, and applicable exact-head CI succeeds.
