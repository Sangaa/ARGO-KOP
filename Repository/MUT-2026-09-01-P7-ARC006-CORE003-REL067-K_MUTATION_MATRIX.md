# MUTATION MATRIX — P7 ARC-006 → CORE-003 REL-067 RECONCILIATION — K

Transaction: `MUT-2026-09-01-P7-ARC006-CORE003-REL067-K`
Work Lease: `HERMUZ-P7-K-REL067-20260901`
Priority: `7 — Core cross-layer validation`
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY-7-OPEN`
Entry HEAD: `f5f6719c848123b7d2f07c27010efafbcae71af4`
Pre-write Matrix HEAD: `6aa15e2fb9e2d5da2da1933ee1b04901fe9f6629`
Material candidate HEAD: `0183adb2d4d064fdf0470b28ef74e8b211164d53`
Protocol: `GOV-013 / GOV-013A / GOV-014 / GOV-014A / GOV-015 / GOV-016`

## Reconstructed legal action

Current live main remained at Transaction-J closure when K was selected. REP-016 keeps Priority 7 as the first globally open Phase-1 partition. `Core/_FOLDER_STATUS.md` explicitly requires continued cross-layer validation plus REP-014 reconciliation where evidence requires it.

Transaction J was current, exact-head CI verified and resume-safe. It established direct current-source evidence for:

`ARC-006 → CORE-003 = documentary REFERENCES evidence only / stronger dependency semantics not established / reverse edge not established`.

REP-014 ended at REL-066 before K, so the tested evidence was not yet registered. This bounded synchronization gap made REP-014 reconciliation the highest-value legal continuation before opening another Core seam.

## Prior-learning classification

| Prior evidence | Classification | Use in K |
|---|---|---|
| Transaction J — ARC-006→CORE-003 validation-first unit | DIRECTLY APPLICABLE | Supplies the exact tested evidence boundary K registers. |
| Transaction H — ARC-005→CORE-011 registry reconciliation | DIRECTLY APPLICABLE | Same Architecture→Core one-way documentary registry pattern, manifest refresh and Core status synchronization. |
| Transaction E — CORE-KERNEL→RUN-001 | TRANSFERABLE | Reinforces non-symmetry and no dependency promotion. |
| Transaction I — CORE-000 semantic repair | NOT APPLICABLE | K has no source-content drift to repair. |
| Historical broader graph claims | STALE | Provenance only; not authority for K. |

## Material change set

| Change ID | Target | Action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| K-01 | `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md` | UPDATE | v1.2.10→1.2.11; add REL-067 `ARC-006 → CORE-003 = REFERENCES` with bounded one-way/non-dependency disposition and evidence section. | Y | Y |
| K-02 | `Repository/REP-020_CURRENT_CONTROL_PLANE_BOUNDARY_MANIFEST.md` | UPDATE | Refresh REP-014 row to v1.2.11 and bind K without changing closure semantics. | Y | Y |
| K-03 | `Core/_FOLDER_STATUS.md` | UPDATE | v1.3.7→1.3.8; record fifth bounded Core seam and keep certification pending. | Y | Y |
| K-04 | `Quality/Integrity/test_arc006_core003_authority_boundary.py` | UPDATE | Require exactly one REL-067 row while continuing to forbid reverse/stronger semantics. | Y | Y |
| K-05 | `Repository/P7_ARC006_CORE003_REL067_RECONCILIATION_2026-09-01_K.md` | CREATE | Preserve K scope, source evidence, non-claims and verification state. | Y | Y |
| K-06 | this Matrix | UPDATE IN SAME CHANGE SET | Rebind prewrite authority inside protected change diff and record exact result. | Y | Y |

Candidate diff from pre-write HEAD to material candidate = exactly 6 authorized paths / one commit / unexpected path expansion `0`.

## Exact-head verification

Candidate exact-head read-back: PASS.

- REP-014 v1.2.11 contains exactly one REL-067 row with the authorized `REFERENCES / INTENTIONAL ONE-WAY / CONSTITUTION-AUTHORITY-ALIGNED / NON-DEPENDENCY` disposition.
- The bounded REL-067 evidence section is present.
- REP-014 preservation comparison shows only the authorized version increment, REL-067 row and K evidence section; no unexpected deletion or path expansion was observed.
- Current control-plane manifest binds REP-014 v1.2.11 while preserving Phase-1 OPEN / Integrity HOLD / Global PASS NOT CLAIMED.
- Core status remains `INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN`; Folder Certification remains pending.
- ARC-006 and CORE-003 source artifacts remain unchanged.

Required exact-head workflows on `0183adb2d4d064fdf0470b28ef74e8b211164d53`:

- Full-Stack Repository Audit — run `33517426626` — SUCCESS. Repository-audit job and every reported step succeeded, including current-checkout SHA binding, Mutation Matrix preflight/semantic enforcement, same-change-set Matrix enforcement, repository-wide audit and runtime-evidence emission.
- ARGO Runtime Prototype and Integration Tests — run `33517426655` — SUCCESS. Integrity, integration and prototype jobs all succeeded; all reported steps succeeded.
- Real Mutation Matrix Regression — run `33517426686` — SUCCESS.
- M2 Multi-Channel Proposal Training — run `33517426621` — SUCCESS.

Candidate result: `4/4 REQUIRED WORKFLOWS SUCCESS`.

No material failure occurred. No failure evidence was rewritten, suppressed or converted into a false green state.

## KEEP / zero-touch requirements preserved

- `Architecture/ARC-006_DEPENDENCY_MODEL.md` unchanged.
- `Core/CORE-003_CONSTITUTION.md` unchanged.
- No `CORE-003 → ARC-006` relationship.
- No `ARC-006 → CORE-003 = DEPENDS_ON/GOVERNS/IMPLEMENTS/CONSUMES` promotion.
- No Core or Architecture certification.
- No Phase-1, Connected Baseline, repository-wide graph, or Global PASS claim.

## Learning retention / session-close boundary

Retained learning: a validation-first seam can be closed independently from its registry synchronization, but once exact-head evidence proves the bounded relationship and the active folder status requires registry reconciliation, the registry synchronization becomes the next local legal obligation before opening another seam. Existing HERMUZ/REP-014 controls already cover this sequencing, so no new governance rule is warranted.

Work Lease disposition: `CLOSED / RESUME-SAFE`.

Next legal action is not authorized by this Matrix. A continuing session must rediscover/reconfirm live main and recompute Priority-7 ordering from current Core authority evidence before selecting another seam or certification action.
