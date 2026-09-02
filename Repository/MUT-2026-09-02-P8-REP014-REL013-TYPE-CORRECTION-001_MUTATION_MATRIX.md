# P8 REL-013 Bounded Type Correction — Pre-Write Mutation Matrix

Transaction ID: `MUT-2026-09-02-P8-REP014-REL013-TYPE-CORRECTION-001`
Priority: `8 — Governance`
State: `CLOSED / TYPE-CORRECTED / VERIFIED / RESUME-SAFE`
Entry HEAD: `6ec2bd8b6fe461e3ccfd24469e0f0c7c783b3d7a`
Pre-write Matrix HEAD: `f7948195a2b18a162681df31f8e527ceb7a68131`
Target: `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
Source blob: `052e811421d2c02fc6cd5031187a2860bb46b469`
Protocols: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / REP-003 / REP-014 / KNW-008`

## Legal entry and disposition

REL-012 is closed/revalidated with closure-head four-workflow success. Priority 8 remains OPEN. REL-013 is the final unresolved row in the bounded REL-010..REL-014 MOD-011/Knowledge seam.

Current row: `MOD-011 → KNW-008 = DEPENDS_ON / Revalidation Required`.

Evidence gates:

- SOURCE AUTHORITY: MOD-011 is Canonical / Proposed / Future-Ready / Revalidated within its bounded source/provenance scope.
- TARGET AUTHORITY: KNW-008 is Canonical / Approved and owns general Knowledge traceability semantics.
- SEMANTIC DIRECTION: MOD-011 explicitly lists KNW-008 as a Related Document; KNW-008 does not name MOD-011 or claim authority over the source model.
- DEPENDENCY NECESSITY: FAIL for `DEPENDS_ON`; MOD-011 defines its source-record and provenance semantics without requiring KNW-008 to define or operate that boundary, while KNW-008 remains a relevant traceability surface.
- CONSUMER / IMPACT: exact-row, endpoint, Quality/Tools and historical searches found no executable consumer of the old dependency classification; impact is confined to REP-014 plus this Matrix.
- TYPE FIT: `REFERENCES` is the strongest supported type for the explicit one-way Related Documents declaration. `DEPENDS_ON` overstates necessity; `CONSUMES` is unstated; no `IMPLEMENTS/GOVERNS/VALIDATES` relation is supported.

Disposition: `TYPE CORRECTION REQUIRED`.

Authorized row: `REL-013 | MOD-011 | KNW-008 | REFERENCES | Revalidated within inspected scope`.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---:|---:|
| P8-REL013-01 | REP-014 REL-013 row | UPDATE | retain direction, change `DEPENDS_ON → REFERENCES`, set bounded revalidated state | Y | Y |
| P8-REL013-02 | all other REP-014 content | KEEP | byte-for-byte/content-equivalent | Y | Y |
| P8-REL013-03 | MOD-011 / KNW-008 | KEEP | no endpoint mutation or promotion | Y | Y |
| P8-REL013-04 | this Matrix | UPDATE | bind material compare, read-back and verification | Y | Y |

Atomicity: exactly one material commit after the pre-write Matrix HEAD, exactly REP-014 + this Matrix, unexpected paths `0`.

Forbidden: no companion edge, endpoint promotion, Models/Knowledge certification, P8/Phase-1/global closure, repository-wide graph claim or global integrity PASS.

Closure requires one-row REP-014 diff, immutable read-back, exact-head four-workflow success with Runtime job split reviewed, Matrix reconciliation and closure-head verification.

Pre-write Matrix HEAD verification: Full-Stack `33684734856`, Runtime/Integration `33684734657`, Real Mutation Matrix `33684734676`, and M2 `33684734806` all succeeded.

## Material verification and closure

- material HEAD: `a78eba525dbc99153bb8da4d8c1043597de69ced`;
- material compare: exactly `1` commit / `2` authorized paths / unexpected paths `0`;
- REP-014 material blob: `4f4c2dd8ba068a5ee19df1406e98fc3d6349347c`;
- REP-014 diff from the pre-write HEAD: one REL-013 type/state replacement only;
- immutable read-back: `REL-013 | MOD-011 | KNW-008 | REFERENCES | Revalidated within inspected scope`;
- Full-Stack `33684950650`, Runtime/Integration `33684951679`, Real Mutation Matrix `33684950789`, and M2 `33684950652` — SUCCESS;
- Runtime jobs `integrity-tests`, `prototype-tests`, and `integration-tests` — SUCCESS.

The unsupported dependency classification is replaced by the explicit documentary reference. No endpoint or broader state is promoted.

`P8 REL-013 = CLOSED / TYPE-CORRECTED / VERIFIED / RESUME-SAFE`.
