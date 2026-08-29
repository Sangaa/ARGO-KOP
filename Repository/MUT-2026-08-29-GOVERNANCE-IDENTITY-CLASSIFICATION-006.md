# MUT-2026-08-29-GOVERNANCE-IDENTITY-CLASSIFICATION-006

Transaction: `R71-20260829-GOV-IDENTITY-CLASSIFY-006`
Entry baseline: `main@d4b4c7854c3c9859bf712bcf727cba4788b2516f`
Matrix created before migration writes: `Repository/GOVERNANCE_IDENTITY_MIGRATION_MATRIX_2026-08-29.md`
Status: `ACTIVE / CLASSIFICATION COMPLETE / MIGRATION AUTHORIZED BY MATRIX`

## Problem

Current Governance contains multiple materially distinct active/candidate documents using the same `GOV-*` identities. `GOV-006` requires one active canonical path per ID and explicit migration for historical conflicts. The current integration audit independently emits `governance_identity_hold_required=true`.

## Pre-Write Decision

The migration matrix classifies current owners and reserves unique target identities without promoting any Proposed/Candidate protocol.

Retained owners:
- `GOV-013A` → HERMUZ Bootstrap Integrity Gate;
- `GOV-014` → Controlled Document Mutation Protocol;
- `GOV-015` → Execution Documentation & Knowledge Transfer;
- `GOV-016` → Failure-to-Learning Protocol.

Reserved targets:
- `GOV-019` → Observation & Side-Effect Gate;
- `GOV-020` → Session Workgroup Continuation Amendment;
- `GOV-021` → Repository-First Multi-Instance Execution;
- `GOV-022` → ARGO Self-Assurance & Capability Evaluation;
- `GOV-023` → Controlled Diagnostic Experiment candidate;
- `GOV-024` → Solution Simulation & Effect Analysis candidate;
- `GOV-025` → Connector Self-Learning candidate;
- `GOV-026` → Solution Evolution & Stability candidate.

The earlier lighter Repository-First `_AMENDMENT` document is classified as superseded by the expanded effective form and will not receive a second active governing identity.

## Safety Boundary

Identity repair SHALL NOT:
- upgrade Proposed/Candidate status;
- alter substantive protocol requirements except references/identity metadata needed by migration;
- mutate `REP-001`/`REP-002` before Governance identity verification;
- delete historical evidence silently;
- claim content correctness from identity correctness.

## Required Closure

1. migrate targets with preserved substantive content and explicit identity/status;
2. preserve old colliding paths as explicit compatibility/supersession evidence or archive-equivalent history surface;
3. update material canonical references;
4. run identity audit and integration suite;
5. require `governance_identity_hold_required=false` for the migrated families, while separately classifying unrelated audit false positives/legacy collisions if any remain;
6. only then permit bounded `REP-001/REP-002` Governance inventory reconciliation;
7. exact-head Runtime/Integration + Full-Stack + M2 must be green.
