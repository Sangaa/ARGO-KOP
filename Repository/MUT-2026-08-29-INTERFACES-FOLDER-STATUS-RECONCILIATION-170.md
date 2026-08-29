# MUT-2026-08-29 — INTERFACES FOLDER STATUS RECONCILIATION — 170

Status: FINALIZED / SAME-CHANGE-SET / CI REVALIDATION PENDING
Date: 2026-08-29
Baseline SHA: `2ccdbebeae78774a1ff2b30b9d4fc7cc86877cec`
Prewrite Commit: `fe30b9691eb0beb4938b04cf43cefaa5927f9331`
Initial Functional Commit: `7f3bad32b990e6a41a1a2dbb002033a3607deeb7`
Target: `Interfaces/_FOLDER_STATUS.md`
Regression: `Quality/Integrity/test_interfaces_folder_status_reconciliation.py`

## Evidence

- Current `Interfaces/` Git tree `8c8fbcca37e5c4105999146dd72713bba539e168` enumerated recursively with `truncated:false`.
- The tree contained exactly 12 tracked files and no subdirectories.
- The prior folder status listed only five files.
- `INTF-006_ENVIRONMENT_SENSING.md` declares active `Document ID: INTF-006`, `Canonical: Yes`, `Status: Proposed / Integrity Hold`.
- `INTF-006_WEB.md` declares internal `INT-006`, `Legacy / Noncanonical / Integrity Hold`, `Canonical: No`, and explicitly denies active INTF-006 ownership.
- `INTF-010_INTEGRATIONS.md` preserves provider-neutral connector, authorization, provenance and execution-result boundaries.

## First exact-head CI observation

At `7f3bad32b990e6a41a1a2dbb002033a3607deeb7`:
- M2 passed.
- prototype-tests passed.
- integration-tests passed.
- integrity-tests failed with `1 failed, 114 passed`.

The failure was not a semantic contradiction in the new Interface claims. Existing `test_active_document_id_uniqueness.py` consumes `Interfaces/_FOLDER_STATUS.md` as a table-shaped identity surface and requires the substring `` `INTF-004_API.md` | `INTF-004` | `` before the `# Audit Findings` heading.

## Learned compatibility rule

`DOCUMENT STRUCTURE WITH ACTIVE CONSUMERS = CONTRACT SURFACE`

A status file may be human-readable documentation and simultaneously a machine-consumed interface. Structural rewrites therefore require consumer-impact validation even when the semantic content is preserved.

## Repair

1. Preserved the new exact 12-file inventory and INTF-006 authority classification.
2. Restored a table-shaped inventory compatible with the existing consumer contract.
3. Restored the `# Audit Findings` boundary expected by the existing integrity test.
4. Did not weaken or remove any existing assertion.
5. Kept the new cwd-independent regression unchanged.

## Bounded closure target

`INTERFACES_PHYSICAL_INVENTORY = CLOSED_FOR_CURRENT_EXACT_TREE`

`INTF006_FILENAME_DUPLICATION = CLASSIFIED / NO_ACTIVE_AUTHORITY_COLLISION`

The Interfaces domain remains `INTEGRITY HOLD / LOCAL INVENTORY VERIFIED / CROSS-LAYER AND EXTERNAL-TRUST VALIDATION OPEN`.

## Non-claims

- No provider-authentication trust anchor acquired.
- No connector implementation certified.
- No external-evidence authenticity stage closed.
- No legacy file renamed, deleted or promoted.
- No global Connected Baseline closure claimed.

## Verification state

Read-back of the initial functional change succeeded. Exact-head CI after the compatibility repair remains required before marking mutation 170 Execution-Verified.
