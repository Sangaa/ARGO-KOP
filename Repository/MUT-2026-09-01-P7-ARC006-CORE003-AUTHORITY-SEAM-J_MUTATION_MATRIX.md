# MUTATION MATRIX — P7 ARC-006 → CORE-003 AUTHORITY SEAM — J

Transaction: `MUT-2026-09-01-P7-ARC006-CORE003-AUTHORITY-SEAM-J`
Work Lease: `HERMUZ-P7-J-ARC006-CORE003-20260901`
Priority: `7 — Core cross-layer validation`
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY-7-OPEN`
Entry HEAD: `a47cdb3ea5f8de6fd58e211a7f36047d320571db`
Pre-write Matrix HEAD: `bc273edcee8186e4c244728ebe1babcfa2a4a98e`
Material candidate HEAD: `c2c3318194f0c78afe5f83a3c2e5d91fdec0af2c`
Protocol: `GOV-013 / GOV-013A / GOV-014A / GOV-015 / GOV-016`

## Reconstructed authority and scope

Current global queue = Priority 7 because Priorities 1–6 have explicit current closure evidence while Core remains `INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN` and Folder Certification is pending.

Transaction I was independently re-read on live main and remains `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY 7 OPEN`; it selected no successor transaction.

The bounded candidate was `Architecture/ARC-006_DEPENDENCY_MODEL.md → Core/CORE-003_CONSTITUTION.md`.

Direct source evidence: ARC-006 explicitly lists `Core/CORE-003_CONSTITUTION.md` under Related Documents and defines Architecture as permitted to depend on Core/Governance. CORE-003 does not directly name ARC-006. ARC-006 itself states that a textual reference does not establish an architectural dependency. Therefore J validates documentary evidence only and does not promote a relationship type.

## Prior-learning retrieval classification

| Prior evidence | Classification | Current use |
|---|---|---|
| Transaction H — `ARC-005 → CORE-011` | DIRECTLY APPLICABLE | Same Architecture→Core one-way Related-Documents boundary; reuse non-symmetry/non-promotion pattern. |
| Transaction E — `CORE-KERNEL → RUN-001` | TRANSFERABLE | Same evidence discipline for one-way documentary seams, different layer direction and contract context. |
| Transaction I — CORE-000 canonical architecture drift | NOT APPLICABLE | I required substantive source-content repair; J had no proven source-content defect. |
| Superseded historical relationship interpretations | STALE | Retained only as provenance; not used to authorize J. |

## Material change set

| Change ID | Target | Action | Expected content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| J-01 | `Quality/Integrity/test_arc006_core003_authority_boundary.py` | CREATE | Assert direct ARC-006→CORE-003 documentary evidence, source direction, dependency-model boundary, and absence of unsupported stronger/reverse registry semantics. | Y | Y |
| J-02 | `Repository/P7_ARC006_CORE003_AUTHORITY_SEAM_2026-09-01_J.md` | CREATE | Preserve bounded finding, learning classification, non-claims and verification state. | Y | Y |
| J-03 | this Matrix | UPDATE IN SAME CHANGE SET | Bind pre-write authorization to the material diff and preserve exact scope. | Y | Y |

Candidate diff from pre-write HEAD to material candidate = exactly 3 authorized paths / one commit / unexpected path expansion `0`.

## Exact-head verification

Candidate exact-head read-back: PASS for the focused regression and transaction surfaces.

Required exact-head workflows on `c2c3318194f0c78afe5f83a3c2e5d91fdec0af2c`:

- M2 Multi-Channel Proposal Training — run `33516187177` — SUCCESS.
- Real Mutation Matrix Regression — run `33516186945` — SUCCESS.
- Full-Stack Repository Audit — run `33516186989` — SUCCESS; repository-audit job and every reported step completed SUCCESS, including checkout-SHA binding, Mutation Matrix preflight/semantic enforcement, repository-wide audit, and runtime-evidence emission.
- ARGO Runtime Prototype and Integration Tests — run `33516186887` — SUCCESS.

Candidate result: `4/4 REQUIRED WORKFLOWS SUCCESS`.

No material failure occurred. No failure evidence was rewritten or suppressed.

## KEEP / non-authority requirements preserved

- No mutation to `Architecture/ARC-006_DEPENDENCY_MODEL.md`.
- No mutation to `Core/CORE-003_CONSTITUTION.md`.
- No REP-014 relationship addition in this validation-first unit.
- No reverse `CORE-003 → ARC-006` edge for symmetry.
- No promotion to `DEPENDS_ON`, `GOVERNS`, `IMPLEMENTS`, `CONSUMES`, runtime or executable proof.
- No Core/Architecture certification, Phase-1 closure, Connected Baseline closure, or Global PASS.

## Learning retention / session-close boundary

Retained learning: the Transaction-H one-way documentary-boundary pattern generalizes cleanly to canonical dependency-authority documents, but a canonical dependency model's Related Documents section still does not itself prove a `DEPENDS_ON` edge. This is retained as transaction-scoped evidence; no new governance rule is warranted because existing GOV-013/ARC-006 rules already cover the mechanism.

Work Lease disposition: `CLOSED / RESUME-SAFE`.

Next legal action is not authorized by this Matrix. A future session must rediscover live main and recompute Priority-7 ordering. The directly supported candidate continuation is REP-014 reconciliation for the now-tested ARC-006→CORE-003 documentary boundary, but it remains a candidate until revalidated against live repository state.
