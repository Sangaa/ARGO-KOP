# P8 REL-003 Bounded Revalidation Mutation Matrix

Transaction ID: `MUT-2026-09-02-P8-REP014-REL003-REVALIDATION-001`
Priority: `8 — Governance`
State: `MATERIAL APPLIED / READ-BACK + EXACT-HEAD CI PENDING`
Entry HEAD: `6c618318b8fd02aa44d306fb3f8d312138607aa4`
Pre-write Matrix HEAD: `fed90cc205578f6b8be119b76120425821a48eb4`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / REP-014`

## Legal-entry proof

Priority 8 remains OPEN. REL-001 is closed/verified; queue reconstruction is not reopened. REL-003 is the next smallest unresolved registry seam selected from current REP-014.

## Selected material gap

`SRV-005 → ENG-004 = CONSUMES`

Original state: `Revalidation Required`.
Material bounded disposition: `Revalidated within inspected scope`.

Direct source evidence:
- `Services/SRV-005_VALIDATION_SERVICE.md` identifies SRV-005 as the Service-layer consumer of ENG-004 and names `Engine/ENG-004_VALIDATION_ENGINE.md` as a related document.
- `Engine/ENG-004_VALIDATION_ENGINE.md` identifies ENG-004 as the Engine-layer validation authority and states that it is consumed by SRV-005; it names the SRV-005 service document as related.
- Both artifacts are canonical and currently `Integrity Hold / Revalidated`; this transaction revalidates only the relationship.

Source checkpoints:
- REP-014 source blob: `4e52e20d70c44244ad13acd7ebf139b64dc1ded4`
- complete REP-014 source obtained through direct blob retrieval before candidate construction.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---:|---:|
| P8-REL003-01 | REP-014 REL-003 row | UPDATE | `Revalidated within inspected scope` | Y | N |
| P8-REL003-02 | all other REP-014 content | KEEP | exact Zero-Touch preservation | Y | N |
| P8-REL003-03 | this Matrix | UPDATE | material evidence in same protected change set | Y | N |

## Forbidden boundaries

- no queue promotion;
- no Priority-8 closure claim;
- no global graph/integrity PASS;
- no SRV-005 or ENG-004 source mutation;
- no relationship-type change;
- no reverse edge manufactured;
- no unrelated REP-014 edits.

## Verification contract

`ATOMIC REP-014 + MATRIX MATERIAL COMMIT → EXACT TWO-PATH COMPARE → READ-BACK → EXACT-HEAD CI → CLOSE OR HOLD`

Required: unexpected changes = `0`.
