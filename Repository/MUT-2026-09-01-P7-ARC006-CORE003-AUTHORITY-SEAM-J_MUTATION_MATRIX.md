# MUTATION MATRIX — P7 ARC-006 → CORE-003 AUTHORITY SEAM — J

Transaction: `MUT-2026-09-01-P7-ARC006-CORE003-AUTHORITY-SEAM-J`
Work Lease: `HERMUZ-P7-J-ARC006-CORE003-20260901`
Priority: `7 — Core cross-layer validation`
State: `MATERIAL CANDIDATE / LEASE ACTIVE / EXACT-HEAD VERIFICATION PENDING`
Entry HEAD: `a47cdb3ea5f8de6fd58e211a7f36047d320571db`
Pre-write Matrix HEAD: `bc273edcee8186e4c244728ebe1babcfa2a4a98e`
Protocol: `GOV-013 / GOV-013A / GOV-014A / GOV-015 / GOV-016`

## Reconstructed authority and scope

Current global queue = Priority 7 because Priorities 1–6 have explicit current closure evidence while Core remains `INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN` and Folder Certification is pending.

Transaction I was independently re-read on live main and remains `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY 7 OPEN`; it selected no successor transaction.

The bounded candidate is `Architecture/ARC-006_DEPENDENCY_MODEL.md → Core/CORE-003_CONSTITUTION.md`.

Direct source evidence: ARC-006 explicitly lists `Core/CORE-003_CONSTITUTION.md` under Related Documents and defines Architecture as permitted to depend on Core/Governance. CORE-003 does not directly name ARC-006. ARC-006 itself states that a textual reference does not establish an architectural dependency. Therefore this unit validates documentary evidence only and does not promote a relationship type.

## Prior-learning retrieval classification

| Prior evidence | Classification | Current use |
|---|---|---|
| Transaction H — `ARC-005 → CORE-011` | DIRECTLY APPLICABLE | Same Architecture→Core one-way Related-Documents boundary; reuse non-symmetry/non-promotion pattern. |
| Transaction E — `CORE-KERNEL → RUN-001` | TRANSFERABLE | Same evidence discipline for one-way documentary seams, different layer direction and contract context. |
| Transaction I — CORE-000 canonical architecture drift | NOT APPLICABLE | I required substantive source-content repair; J currently has no proven source-content defect. |
| Superseded historical relationship interpretations | STALE | Retained only as provenance; not used to authorize J. |

## Authorized material change set

| Change ID | Target | Action | Expected content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| J-01 | `Quality/Integrity/test_arc006_core003_authority_boundary.py` | CREATE | Assert direct ARC-006→CORE-003 documentary evidence, source direction, dependency-model boundary, and absence of unsupported stronger/reverse registry semantics. | Y | PENDING EXACT-HEAD |
| J-02 | `Repository/P7_ARC006_CORE003_AUTHORITY_SEAM_2026-09-01_J.md` | CREATE | Preserve bounded finding, learning classification, non-claims and verification state. | Y | PENDING EXACT-HEAD |
| J-03 | this Matrix | UPDATE IN SAME CHANGE SET | Bind pre-write authorization to the material diff and preserve exact scope. | Y | PENDING EXACT-HEAD |

## KEEP / non-authority requirements

- No mutation to `Architecture/ARC-006_DEPENDENCY_MODEL.md`.
- No mutation to `Core/CORE-003_CONSTITUTION.md`.
- No REP-014 relationship addition in this validation-first unit.
- No reverse `CORE-003 → ARC-006` edge for symmetry.
- No promotion to `DEPENDS_ON`, `GOVERNS`, `IMPLEMENTS`, `CONSUMES`, runtime or executable proof.
- No Core/Architecture certification, Phase-1 closure, Connected Baseline closure, or Global PASS.

## Pre-write validation

- Live main independently rediscovered: PASS.
- Bootstrap / Constitution / REP-001/002/011/012/013/014/015/016/020 inspected: PASS within current decision scope.
- Transaction I current-main closure/read-back: PASS / resume-safe.
- Prior learning retrieved and classified: PASS.
- Direct ARC-006 source read: PASS.
- Direct CORE-003 source read: PASS.
- REP-014 relationship set inspected through REL-066: PASS; no ARC-006→CORE-003 row present.
- Existing Transaction-H regression pattern inspected: PASS.
- Pre-write Matrix existed at parent HEAD before material mutation: PASS.
- Matrix is included in this same material change set: YES.
- Expected unexpected path expansion: `0`.

Material-candidate decision: `AUTHORIZED / EXACT-HEAD READ-BACK + REQUIRED CI PENDING`.
