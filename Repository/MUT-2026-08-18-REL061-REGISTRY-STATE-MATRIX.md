# MUT-2026-08-18-REL061-REGISTRY-STATE-MATRIX

Date: `2026-08-18`
Status: `APPLIED / VERIFIED`
Authority: `GOV-013 + GOV-013A + GOV-014 + GOV-015`
Target: `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
Pre-mutation target blob SHA: `57c872e8bed3fec34e114d72d2093bd134e0ae2b`
Post-mutation target commit: `e5262fba000228725a0638909b983577bc12b873`
Post-mutation target blob SHA: `a6926b0b27e515b38b65594846fd82d1f1252ea9`

## Purpose

Prepare and record the smallest sufficient registry-state mutation for `REL-061` without changing relationship identity, direction, semantic authority, or unrelated REP-014 content.

## Evidence Basis

- `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` declares `Approved / Canonical Addendum` and states that it supplements `GOV-013`.
- `Repository/P4_REL061_INTENTIONAL_ONE_WAY_DISPOSITION_2026-08-17.md` establishes the relationship as intentionally asymmetric.
- `REP-014` uses the controlled relationship type `REFERENCES` for `REL-061` because `SUPPLEMENTS` is not a controlled registry type.

## Applied Mutation

Previous row:

`| REL-061 | GOV-013A | GOV-013 | REFERENCES | Revalidated within governance scope |`

Applied row:

`| REL-061 | GOV-013A | GOV-013 | REFERENCES | INTENTIONAL ONE-WAY / GOVERNANCE-REVALIDATED |`

No change was made to:

- Relationship ID
- source
- target
- controlled relationship type
- direction
- `GOV-013` authority
- `GOV-013A` authority
- REL-009
- REL-005
- unrelated REP-014 relationships or narrative

## Verification Sequence

`PRE-SHA RECHECK → FULL-CONTENT READ → MINIMUM EDIT → WRITE → CURRENT FILE RE-READ → VERIFY REL-061 → VERIFY POST-WRITE SHA → CHECK IMPACT`

Results:

- Pre-write SHA matched the current canonical REP-014 blob: `57c872e8bed3fec34e114d72d2093bd134e0ae2b`.
- Mutation committed successfully as `e5262fba000228725a0638909b983577bc12b873`.
- Post-write blob SHA: `a6926b0b27e515b38b65594846fd82d1f1252ea9`.
- Current-path read-back confirms the exact `REL-061` row is present.
- The surrounding relationship table remains preserved; `REL-009` remains `REVALIDATION REQUIRED` and `REL-005` remains executable-verified.
- No workflow run was associated with this direct commit, so no new CI PASS is claimed from this mutation alone.

## State Decision

`REL-061 = INTENTIONAL ONE-WAY / GOVERNANCE-REVALIDATED`

This is a relationship-state reconciliation only. It does not promote P4, close Priority 1, or establish Global PASS.

## Closure Condition

Mutation is `APPLIED / VERIFIED` at the file/relationship scope. P4 remains open because `REL-009` still lacks independent callable consumer evidence.

---

End of mutation matrix
