# AMENDMENT MATRIX — P7 CORE ALLOCATION RECONCILIATION W-A

Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-A`
Parent Transaction: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W`
Work Lease: `HERMUZ-P7-W-A-CORE-ALLOCATION-MANIFEST-20260901`
Priority: `7 — Core`
State: `SUPERSEDED-BEFORE-MATERIAL-WRITE BY W-B / LEARNING RETAINED`
Entry HEAD: `f2543f809e1058c576c59de372354bf17ee2cdb1`
Superseding amendment: `MUT-2026-09-01-P7-CORE-ALLOCATION-RECONCILIATION-W-B`

## Valid finding retained

W-A correctly established that if canonical REP-012 were version-mutated, REP-020 boundary-manifest synchronization would be required. W-A also correctly required a focused regression binding Core physical inventory, Core local index and allocation evidence.

## Why its material plan is superseded

Before material mutation, deeper inspection established that canonical REP-012 contains a long historical/control-plane evidence body. W-B chooses a lower-risk non-replacing REP-012 allocation addendum, so canonical REP-012 version/status/identity no longer changes. Therefore the REP-020 synchronization trigger identified by W-A is not activated.

No W-A direct REP-012/REP-020 material mutation occurred before supersession.

## Durable verification retained under W-B

The focused regression remains required and must preserve:

- exact current 18-file physical Core inventory;
- `Core.md` self-exclusion semantics;
- exact allocation-addendum coverage;
- legacy/noncanonical `CORE-000_PLATFORM_IDENTITY.md` treatment;
- no inference that allocation means review, relationship validation, certification or Phase-1 closure.

## Authority boundary

W-B is the controlling material scope. W-A remains provenance explaining why manifest synchronization was considered and why it became unnecessary after the write surface changed.

## Learning

`A PRE-WRITE MATRIX IS REVIEWABLE, AND A VALID CONDITIONAL REQUIREMENT MAY BECOME INAPPLICABLE WHEN A LATER PRE-WRITE AMENDMENT REMOVES THE CONDITION THAT TRIGGERED IT.`
