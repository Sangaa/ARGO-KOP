# MUTATION MATRIX — P7 CORE-003 ↔ ARC-011 AUTHORITY SEAM — L

Transaction: `MUT-2026-09-01-P7-CORE003-ARC011-AUTHORITY-L`
Work Lease: `HERMUZ-P7-L-CORE003-ARC011-20260901`
Priority: `7 — Core cross-layer validation`
State: `FUNCTIONAL-CLOSED / CI-VERIFIED / RESUME-SAFE / PRIORITY-7-OPEN`
Entry HEAD: `42133637e8f672dd1c6c2d1ce1be78ccfc00ba5b`
Pre-write Matrix HEAD: `bfca2ab112aa6950bdf5717f42b976488bae5a3a`
Material candidate HEAD: `6f818976889da9267f8004c8f0bf8ae540f6094c`
Protocol: `GOV-013 / GOV-013A / GOV-014A / GOV-015 / GOV-016`

## Reconstructed legal action

After Transaction K closed resume-safe, Priority 7 remained open. The highest-value Core authority boundary was Constitution ↔ Canonical Architecture because ARC-011 is the canonical architecture model and explicitly declares its authority subordinate to the Constitution and applicable Governance.

Direct current evidence supports the bounded candidate pair:

`CORE-003 → ARC-011 = GOVERNS`

`ARC-011 → CORE-003 = REFERENCES`

The first direction is supported by CORE-003's highest-governing-rules and repository-component compliance language together with ARC-011's explicit subordination. The reverse is documentary/semantic reference to the Constitution in ARC-011's own authority model. No dependency is inferred.

## Prior-learning classification

- Existing REL-037/038 CORE-003↔RUN-001 — DIRECTLY APPLICABLE.
- J/K ARC-006→CORE-003 — TRANSFERABLE.
- H ARC-005→CORE-011 — TRANSFERABLE.
- I CORE-000 repair — NOT APPLICABLE.
- Historical broad architecture compliance claims — STALE for current authority.

## Material change set

| Change ID | Target | Action | Applied | Verified |
|---|---|---|:---:|:---:|
| L-01 | `Quality/Integrity/test_core003_arc011_authority_boundary.py` | CREATE | Y | Y |
| L-02 | `Repository/P7_CORE003_ARC011_AUTHORITY_SEAM_2026-09-01_L.md` | CREATE | Y | Y |
| L-03 | this Matrix | UPDATE IN SAME CHANGE SET | Y | Y |

Candidate diff = exactly 3 authorized paths / one commit / unexpected path expansion `0`.

## Exact-head verification

- CORE-003 source unchanged and directly re-read.
- ARC-011 source unchanged and directly re-read.
- REP-014 unchanged by L.
- Focused integrity regression persists the authority/reference boundary and forbids unsupported dependency/implementation/consumer promotion.

Required exact-head workflows on `6f818976889da9267f8004c8f0bf8ae540f6094c`:

- Full-Stack Repository Audit — `33518055686` — SUCCESS; repository-audit job and all reported steps SUCCESS, including exact checkout binding, Matrix preflight/semantics/same-change-set enforcement and repository-wide audit.
- ARGO Runtime Prototype and Integration Tests — `33518055707` — SUCCESS.
- Real Mutation Matrix Regression — `33518055666` — SUCCESS.
- M2 Multi-Channel Proposal Training — `33518055708` — SUCCESS.

Result: `4/4 REQUIRED WORKFLOWS SUCCESS`.

No material failure occurred and no failure evidence was hidden or rewritten.

## KEEP / non-claims preserved

- No mutation to CORE-003, ARC-011 or REP-014.
- No `ARC-011 → CORE-003 = DEPENDS_ON` claim.
- No executable/runtime semantics.
- No Core or Architecture certification.
- No Phase-1, Connected Baseline, repository-wide graph or Global PASS claim.

## Learning / closure

Learning retained: authority subordination is not synonymous with dependency. A governing relationship can be independently supported by the higher-authority source and the subordinate artifact, while the subordinate artifact's constitutional reference remains documentary. Existing relationship discipline already covers this rule, so no governance promotion is warranted.

Work Lease: `CLOSED / RESUME-SAFE`.

A continuation must rediscover live main and recompute Priority-7 ordering. L does not itself authorize REP-014 mutation or a successor seam.
