# P318 — GOV-013A RELATIONSHIP DIRECTION RESOLUTION

Date: 2026-08-17
Status: Recorded / Priority 1 Reconciliation / Integrity Hold
Checkpoint: P318

## Scope
Resolve the previously open relationship direction/type for `GOV-013A` using the canonical artifact as primary evidence.

## Evidence

`Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` states:

- `Document ID: GOV-013A`;
- `Status: Approved / Canonical Addendum`;
- `Authority: Supplements GOV-013`;
- the gate explicitly requires `GOV-013` and this addendum to be loaded before mutation;
- `GOV-013` is therefore a direct authority/reference target of `GOV-013A`.

## Controlled Relationship Mapping

The registry-controlled relationship types do not include `SUPPLEMENTS`.

Therefore the safe registry representation is:

`GOV-013A → GOV-013 = REFERENCES`

with the evidence description preserving the stronger semantic fact:

`Canonical Addendum / Supplements GOV-013`.

No new uncontrolled relationship type is introduced.

## Boundary

This resolves the **direction and controlled type** from current canonical evidence. It does not imply:

- governance authority above GOV-013A;
- replacement of GOV-013;
- automatic promotion of related session gates;
- closure of Ring 0.

## Next Safe Action

Register the controlled `REFERENCES` edge in `REP-014` using a content-preserving mutation, then re-read and revalidate affected control-plane edges.

## State

- GOV-013A relationship direction/type: RESOLVED FOR REGISTRATION
- Priority 1: OPEN
- Integrity: HOLD
- Global PASS: NOT CLAIMED

---

End of P318
