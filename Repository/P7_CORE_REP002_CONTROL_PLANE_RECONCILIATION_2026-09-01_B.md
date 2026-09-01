# Priority 7 — Core REP-002 Control-Plane Reconciliation B

Date: 2026-09-01
State: `P7 PROGRESS / REP-002 CORE MAPPING RECONCILED / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-CORE-REP002-RECONCILIATION-B`

## Finding
P336 established the exact current Core inventory and recorded that REP-002 omitted `Core/CORE-000A_PLATFORM_GLOSSARY.md` and `Core/CORE-012_GENERATIVE_KNOWLEDGE_AND_SELF_DEVELOPMENT.md`. Direct current REP-002 inspection confirms both omissions remained at session entry.

## Repair
REP-002 is advanced from v1.7.4 to v1.7.5 and both current Core paths are added to the Core Layer map. A direct integration regression binds their presence while explicitly preventing active promotion of legacy `Core/CORE-000_PLATFORM_IDENTITY.md`.

## Boundary
This closes only the REP-002 Core mapping drift for CORE-000A and CORE-012. Priority 7 remains OPEN. GOV-006 disposition, Core dependency/consumer validation, relationship-registry reconciliation and explicit Core certification remain open. Phase 1 and Global Connected Baseline remain open; no global integrity PASS is claimed.
