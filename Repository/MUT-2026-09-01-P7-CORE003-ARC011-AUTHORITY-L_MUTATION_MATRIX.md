# MUTATION MATRIX — P7 CORE-003 ↔ ARC-011 AUTHORITY SEAM — L

Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-AUTHORITY-L`
Work Lease: `HERMUZ-P7-L-CORE003-ARC011-20260901`
Priority: `7 — Core cross-layer validation`
State: `MATERIAL CANDIDATE / LEASE ACTIVE / EXACT-HEAD VERIFICATION PENDING`
Entry HEAD: `42133637e8f672dd1c6c2d1ce1be78ccfc00ba5b`
Pre-write Matrix HEAD: `bfca2ab112aa6950bdf5717f42b976488bae5a3a`
Protocol: `GOV-013 / GOV-013A / GOV-014A / GOV-015 / GOV-016`

## Reconstructed legal action

Transaction K is closed/resume-safe and its closure HEAD passed all four required workflows. Priority 7 remains globally open and Core remains under cross-layer validation.

The highest-value current Core authority seam is the Constitution ↔ Canonical Architecture boundary:

- CORE-003 states its rules have higher authority and repository components shall comply within applicable scope;
- ARC-011 declares itself the authoritative canonical architecture reference subordinate only to the Constitution and applicable Governance authority;
- ARC-011 explicitly represents the authority chain `Constitution / applicable Governance authority → Canonical Architecture Model → Other Architecture Documents`.

This directly supports a bounded candidate pair for validation:

`CORE-003 → ARC-011 = GOVERNS`

`ARC-011 → CORE-003 = REFERENCES`

The reverse `REFERENCES` candidate is semantic/documentary reference to the uniquely identified repository Constitution, not a dependency claim. No `ARC-011 → CORE-003 = DEPENDS_ON` promotion is authorized by this unit.

## Prior-learning classification

| Prior evidence | Classification | Use in L |
|---|---|---|
| Existing REL-037/038 CORE-003↔RUN-001 reconciliation | DIRECTLY APPLICABLE | Same independently evidenced GOVERNS + reverse REFERENCES pattern across a Core authority boundary. |
| Transaction J/K ARC-006→CORE-003 | TRANSFERABLE | Reinforces distinction between reference, dependency and authority semantics. |
| Transaction H ARC-005→CORE-011 | TRANSFERABLE | Same Architecture/Core non-symmetry discipline, but weaker documentary seam. |
| Transaction I CORE-000 content repair | NOT APPLICABLE | No source-content defect is established in L. |
| Historical broad architecture compliance claims | STALE | Provenance only; current sources control. |

## Material change set

| Change ID | Target | Action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| L-01 | `Quality/Integrity/test_core003_arc011_authority_boundary.py` | CREATE | Assert current two-direction authority/reference evidence and prohibit unsupported dependency/implementation/consumer semantics. | Y | PENDING EXACT-HEAD |
| L-02 | `Repository/P7_CORE003_ARC011_AUTHORITY_SEAM_2026-09-01_L.md` | CREATE | Preserve finding, evidence classification, non-claims and verification state. | Y | PENDING EXACT-HEAD |
| L-03 | this Matrix | UPDATE IN SAME CHANGE SET | Rebind prewrite authority in material diff and record result. | Y | PENDING EXACT-HEAD |

## KEEP / non-authority requirements

- No mutation to `Core/CORE-003_CONSTITUTION.md`.
- No mutation to `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`.
- No REP-014 mutation in this validation-first unit.
- No `ARC-011 → CORE-003 = DEPENDS_ON` inference merely from subordination.
- No `ARC-011 → CORE-003 = GOVERNS/IMPLEMENTS/CONSUMES`.
- No Core or Architecture certification, Phase-1 closure, Connected Baseline closure, or Global PASS.

## Pre-write verification

- Live main rediscovered after K closure: PASS.
- K closure-head 4/4 required workflows: PASS.
- ARC-011 direct current read: PASS; canonical, subordinate to Constitution/Governance, explicit authority chain.
- CORE-003 direct current read: PASS; highest governing rules and repository-component compliance rule.
- Existing REP-014 CORE-003/RUN-001 GOVERNS+REFERENCES pattern retrieved: DIRECTLY APPLICABLE.
- Current repository search found no existing ARC-011↔CORE-003 registry row.
- Search/index results were treated as discovery only; direct current source reads remain authority.
- Pre-write Matrix existed before material mutation at `bfca2ab112aa6950bdf5717f42b976488bae5a3a` and is rebound in this same material change set.

Material-candidate decision: `AUTHORIZED / EXACT-HEAD READ-BACK + REQUIRED CI PENDING`.
