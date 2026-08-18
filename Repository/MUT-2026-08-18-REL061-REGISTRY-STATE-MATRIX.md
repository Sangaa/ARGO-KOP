# MUT-2026-08-18-REL061-REGISTRY-STATE-MATRIX

Date: `2026-08-18`
Status: `CANDIDATE / WRITE PENDING`
Authority: `GOV-013 + GOV-013A + GOV-014 + GOV-015`
Target: `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
Current target blob SHA at preparation: `57c872e8bed3fec34e114d72d2093bd134e0ae2b`

## Purpose

Prepare the smallest sufficient registry-state mutation for `REL-061` without changing relationship identity, direction, semantic authority, or unrelated REP-014 content.

## Evidence Basis

- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` declares `Approved / Canonical Addendum` and states that it supplements `GOV-013`.
- `Repository/P4_REL061_INTENTIONAL_ONE_WAY_DISPOSITION_2026-08-17.md` establishes the relationship as intentionally asymmetric.
- `REP-014` already uses the controlled relationship type `REFERENCES` for `REL-061` because `SUPPLEMENTS` is not a controlled registry type.

## Intended Mutation

Current row:

`| REL-061 | GOV-013A | GOV-013 | REFERENCES | Revalidated within governance scope |`

Proposed row state:

`| REL-061 | GOV-013A | GOV-013 | REFERENCES | INTENTIONAL ONE-WAY / GOVERNANCE-REVALIDATED |`

No change to:

- Relationship ID
- source
- target
- controlled relationship type
- direction
- `GOV-013` authority
- `GOV-013A` authority

The existing reconciliation narrative should remain preserved. A concise current-cycle evidence note may be appended only after the full target content is preserved and re-read.

## Required Mutation Sequence

`PRE-SHA RECHECK → FULL-CONTENT READ → MINIMUM EDIT → WRITE → FULL RE-READ → VERIFY REL-061 → VERIFY REP-014 SHA → REGISTRY/INDEX IMPACT CHECK → CHECKPOINT`

## Safety Boundary

Do not replace REP-014 from a shortened or reconstructed copy. Do not modify REL-009, REL-005, or unrelated relationships in the same write.

## Closure Condition

This matrix can be marked `APPLIED / VERIFIED` only after the resulting REP-014 content is fully re-read and the exact REL-061 state is confirmed on current `main`.

Until then, the canonical registry remains unchanged and P4 remains open.

---

End of mutation matrix
