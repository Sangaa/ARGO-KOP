# P8 REL-014 Bounded Type/Direction Correction — Pre-Write Mutation Matrix

Transaction ID: `MUT-2026-09-02-P8-REP014-REL014-TYPE-CORRECTION-001`
Priority: `8 — Governance`
State: `CLOSED / TYPE-CORRECTED / VERIFIED / RESUME-SAFE`
Entry HEAD: `19f7cadc95fc83f9bcee1d1a6ca349cb8d7b8d51`
Pre-write Matrix HEAD: `4622576d3d092dfca4d915d57257476816ee6ddc`
Target: `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
Source blob: `58feb2db2bf13047f2837b6834d6f1163dc18cf2`
Protocols: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / REP-003 / REP-014 / KNW-009`

## Legal entry and disposition

REL-010 and REL-011 are closed/type-corrected with closure-head four-workflow success. Priority 8 remains OPEN. REL-014 has the strongest remaining explicit consumer wording in the same MOD-011/Knowledge seam.

Current row: `MOD-011 → KNW-009 = DEPENDS_ON / Revalidation Required`.

Evidence gates:

- SOURCE AUTHORITY: KNW-009 is Canonical / Integrity Hold / Revalidated and owns Knowledge Evolution semantics.
- TARGET AUTHORITY: MOD-011 is Canonical / Proposed / Future-Ready / Revalidated within its bounded source/provenance scope.
- SEMANTIC DIRECTION: KNW-009 explicitly states that Knowledge evolution consumes MOD-011 source/provenance semantics; the current direction is reversed.
- DEPENDENCY NECESSITY: PASS for the corrected edge; external-source evolution relies on MOD-011's source identity, evidence and source-versus-ARGO distinction. MOD-011 does not require KNW-009 to define that boundary.
- CONSUMER / IMPACT: exact-row, semantic/path, reverse/Quality/Tools and history searches found no executable consumer of the old row direction/type; impact is confined to REP-014 plus this Matrix.
- TYPE FIT: `CONSUMES` exactly matches current KNW-009 wording and is more precise than generic `DEPENDS_ON`; `REFERENCES` is too weak and no `IMPLEMENTS/GOVERNS/VALIDATES` relation is supported.

Disposition: `TYPE CORRECTION REQUIRED`.

Authorized row: `REL-014 | KNW-009 | MOD-011 | CONSUMES | Revalidated within inspected scope`.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---:|---:|
| P8-REL014-01 | REP-014 REL-014 row | UPDATE | reverse direction, change `DEPENDS_ON → CONSUMES`, set bounded revalidated state | Y | Y |
| P8-REL014-02 | all other REP-014 content | KEEP | byte-for-byte/content-equivalent | Y | Y |
| P8-REL014-03 | MOD-011 / KNW-009 | KEEP | no endpoint mutation or promotion | Y | Y |
| P8-REL014-04 | this Matrix | UPDATE | bind material compare, read-back and verification | Y | Y |

Atomicity: exactly one material commit after the pre-write Matrix HEAD, exactly REP-014 + this Matrix, unexpected paths `0`.

Forbidden: no companion edge, endpoint promotion, Models/Knowledge certification, P8/Phase-1/global closure, repository-wide graph claim or global integrity PASS.

Closure requires one-row REP-014 diff, immutable read-back, exact-head four-workflow success with Runtime job split reviewed, Matrix reconciliation and closure-head verification.

Pre-write Matrix HEAD verification: Full-Stack `33683313441`, Runtime/Integration `33683313510`, Real Mutation Matrix `33683313543`, and M2 `33683313416` all succeeded.

## Material verification and closure

- material HEAD: `be33a3d2fb2cad756dc9445ae0e8d9c811cf6144`;
- material compare: exactly `1` commit / `2` authorized paths / unexpected paths `0`;
- REP-014 material blob: `bc1f1b7d17805ac950132ec56bba584570ee5b77`;
- REP-014 diff from the pre-write HEAD: one REL-014 row replacement only;
- immutable read-back: `REL-014 | KNW-009 | MOD-011 | CONSUMES | Revalidated within inspected scope`;
- Full-Stack `33683463907`, Runtime/Integration `33683463885`, Real Mutation Matrix `33683463934`, and M2 `33683463874` — SUCCESS;
- Runtime jobs `integrity-tests`, `prototype-tests`, and `integration-tests` — SUCCESS.

The old reversed generic dependency is replaced by the exact current consumer direction/type. No endpoint or broader state is promoted.

`P8 REL-014 = CLOSED / TYPE-CORRECTED / VERIFIED / RESUME-SAFE`.
