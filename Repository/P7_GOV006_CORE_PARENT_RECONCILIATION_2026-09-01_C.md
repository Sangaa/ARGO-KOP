# Priority 7 — GOV-006 Core Parent Reconciliation C

Date: 2026-09-01
State: `P7 PROGRESS / GOV-006 CORE PARENT FACT RECONCILED / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-GOV006-CORE-PARENT-RECONCILIATION-C`

## Finding
Current GOV-006 v1.3.0 declared the CORE prefix canonical parent as `Architecture/` and used `Architecture/CORE-003_CONSTITUTION.md` as its example. Exact repository search found that stale path only in GOV-006, while current repository consumers and the reconciled Core inventory consistently use `Core/CORE-003_CONSTITUTION.md`.

Historical commit evidence shows the Architecture example was preserved through earlier GOV-006 canonicalization; current repository evidence does not support moving Core authority into Architecture.

## Repair
GOV-006 is advanced to v1.3.1 and its CORE row is aligned to `Core/` / `Core/CORE-003_CONSTITUTION.md`. A direct integration regression prevents reintroduction of the stale Architecture example.

## Authority boundary
This is a factual path correction only. GOV-006 remains `Proposed / Audit-Derived Update`; no authority promotion is performed or implied. The separate question of GOV-006 promotion/approval remains open under Governance authority.

## Boundary
Priority 7 remains OPEN. `Core/_FOLDER_STATUS.md` synchronization for this now-resolved fact is intentionally deferred to a separate bounded status reconciliation. Material Core dependency/consumer validation, REP-014 relationship reconciliation, explicit Core certification, Phase 1 and Global Connected Baseline remain open; no global integrity PASS is claimed.
