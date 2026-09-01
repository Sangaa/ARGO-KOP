# Priority 7 — GOV-006 Core Parent Reconciliation C

Date: 2026-09-01
State: `P7 PROGRESS / GOV-006 CORE PARENT FACT RECONCILED / CI-VERIFIED / PRIORITY 7 OPEN`
Transaction: `MUT-2026-09-01-P7-GOV006-CORE-PARENT-RECONCILIATION-C`

## Finding
Current GOV-006 v1.3.0 declared the CORE prefix canonical parent as `Architecture/` and used `Architecture/CORE-003_CONSTITUTION.md` as its example. Exact repository search found that stale active-path claim only in GOV-006, while current repository consumers and the reconciled Core inventory consistently use `Core/CORE-003_CONSTITUTION.md`.

Historical commit evidence shows the Architecture example was preserved through earlier GOV-006 canonicalization; current repository evidence does not support moving Core authority into Architecture.

## Repair
GOV-006 is advanced to v1.3.1 and its authoritative CORE row is aligned to `Core/` / `Core/CORE-003_CONSTITUTION.md`.

The direct integration regression now checks the semantic authority boundary: the current authoritative CORE row must exist and the stale `Architecture/` authority row must not exist. Historical explanatory mention of `Architecture/CORE-003_CONSTITUTION.md` remains permitted as provenance.

## CI failure and recovery
Initial functional HEAD `fa7a85d538c0e111596f277dc82bb7569dcd3bf1` produced a Runtime/Integration failure because the first regression asserted that `Architecture/CORE-003_CONSTITUTION.md` could not appear anywhere in the document, even though the reconciliation narrative intentionally preserved that string as historical evidence.

Failure classification: `TEST DEFECT / SEMANTIC AUTHORITY BOUNDARY TOO BROAD`.

Prior-learning retrieval recovered `Memory/Engineering_Journal/EJR-179_2026-08-16_FOLDER_INVENTORY_IDENTITY_DRIFT_LEARNING.md` as DIRECTLY APPLICABLE. EJR-179 already records the same failure mode: historical references inside explanatory evidence must not be confused with active metadata.

The regression was narrowed at `f19f7af8b86c8fdddaf9ff640eecdfacba0bb2f5` without changing GOV-006 again.

Exact-head validation on `f19f7af8b86c8fdddaf9ff640eecdfacba0bb2f5`:
- ARGO Runtime Prototype and Integration Tests run `33475437864`: SUCCESS.
- Full-Stack Repository Audit run `33475437728`: SUCCESS.
- M2 Multi-Channel Proposal Training run `33475437912`: SUCCESS.

No new learning rule is promoted because the applicable durable rule already exists in EJR-179; this transaction demonstrates successful prior-learning reuse rather than a novel control principle.

## Authority boundary
This is a factual path correction only. GOV-006 remains `Proposed / Audit-Derived Update`; no authority promotion is performed or implied. The separate question of GOV-006 promotion/approval remains open under Governance authority.

## Boundary
Priority 7 remains OPEN. `Core/_FOLDER_STATUS.md` synchronization for this now-resolved fact is intentionally deferred to a separate bounded status reconciliation. Material Core dependency/consumer validation, REP-014 relationship reconciliation, explicit Core certification, Phase 1 and Global Connected Baseline remain open; no global integrity PASS is claimed.
