# MUTATION MATRIX — P7 ARC-006 → CORE-003 REL-067 RECONCILIATION — K

Transaction: `MUT-2026-09-01-P7-ARC006-CORE003-REL067-K`
Work Lease: `HERMUZ-P7-K-REL067-20260901`
Priority: `7 — Core cross-layer validation`
State: `PRE-WRITE AUTHORIZED / LEASE ACTIVE / PROTECTED MUTATION PENDING`
Entry HEAD: `f5f6719c848123b7d2f07c27010efafbcae71af4`
Protocol: `GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Reconstructed legal action

Current live main remains at Transaction-J closure. REP-016 keeps Priority 7 as the first globally open Phase-1 partition. `Core/_FOLDER_STATUS.md` explicitly requires continued cross-layer validation plus REP-014 reconciliation where evidence requires it.

Transaction J is current, exact-head CI verified and resume-safe. It established direct current-source evidence for:

`ARC-006 → CORE-003 = documentary REFERENCES evidence only / stronger dependency semantics not established / reverse edge not established`.

REP-014 still ends at REL-066, so the current evidence is not yet registered. This creates a bounded synchronization gap and makes REP-014 reconciliation the highest-value legal continuation before opening another Core seam.

## Prior-learning classification

| Prior evidence | Classification | Use in K |
|---|---|---|
| Transaction J — ARC-006→CORE-003 validation-first unit | DIRECTLY APPLICABLE | Supplies the exact tested evidence boundary K will register. |
| Transaction H — ARC-005→CORE-011 registry reconciliation | DIRECTLY APPLICABLE | Same Architecture→Core one-way documentary registry pattern, manifest refresh and Core status synchronization. |
| Transaction E — CORE-KERNEL→RUN-001 | TRANSFERABLE | Reinforces non-symmetry and no dependency promotion. |
| Transaction I — CORE-000 semantic repair | NOT APPLICABLE | K has no source-content drift to repair. |
| Historical broader graph claims | STALE | Provenance only; not authority for K. |

## Authorized protected change set

| Change ID | Target | Action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| K-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | v1.2.10→1.2.11; add REL-067 `ARC-006 → CORE-003 = REFERENCES` with bounded one-way/non-dependency disposition and evidence section. | N | N |
| K-02 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | Refresh REP-014 row to v1.2.11 and bind K without changing closure semantics. | N | N |
| K-03 | `Core/_FOLDER_STATUS.md` | UPDATE | v1.3.7→1.3.8; record fifth bounded Core seam and keep certification pending. | N | N |
| K-04 | `Quality/Integrity/test_arc006_core003_authority_boundary.py` | UPDATE | Require exactly one REL-067 row while continuing to forbid reverse/stronger semantics. | N | N |
| K-05 | `Repository/P7_ARC006_CORE003_REL067_RECONCILIATION_2026-09-01_K.md` | CREATE | Transaction evidence, read-back/CI status, non-claims and resume-safe closure when verified. | N | N |
| K-06 | this Matrix | UPDATE IN SAME CHANGE SET | Rebind prewrite authority inside protected change diff and record exact result. | N | N |

## KEEP / zero-touch requirements

- `Architecture/ARC-006_DEPENDENCY_MODEL.md` unchanged.
- `Core/CORE-003_CONSTITUTION.md` unchanged.
- All REP-014 content outside version increment, REL-067 row, and bounded K evidence section preserved.
- No `CORE-003 → ARC-006` relationship.
- No `ARC-006 → CORE-003 = DEPENDS_ON/GOVERNS/IMPLEMENTS/CONSUMES` promotion.
- No Core or Architecture certification.
- No Phase-1, Connected Baseline, repository-wide graph, or Global PASS claim.

## Pre-write verification

- Live main rediscovered: PASS.
- Transaction J re-read: PASS / resume-safe.
- J closure-head four required workflows: PASS.
- Direct ARC-006 source re-read: PASS; explicit Related Documents reference exists and path-alone dependency warning remains.
- Direct CORE-003 source re-read: PASS; no ARC-006 direct reverse reference found.
- REP-014 direct read through REL-066: PASS; REL-067 absent.
- Three materially different search/reverse checks performed for existing stronger/reverse ARC-006↔CORE-003 registration: no current evidence recovered.
- Transaction H pattern re-read: PASS.
- GOV-014A prewrite requirement re-read: PASS.

Decision: `AUTHORIZED FOR ATOMIC SAME-CHANGE-SET PROTECTED MUTATION ONLY`.
