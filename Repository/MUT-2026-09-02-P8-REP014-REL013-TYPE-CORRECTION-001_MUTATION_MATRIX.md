# P8 REL-013 Bounded Type Correction — Pre-Write Mutation Matrix

Transaction ID: `MUT-2026-09-02-P8-REP014-REL013-TYPE-CORRECTION-001`
Priority: `8 — Governance`
State: `PRE-WRITE / READY`
Entry HEAD: `6ec2bd8b6fe461e3ccfd24469e0f0c7c783b3d7a`
Pre-write Matrix HEAD: `PENDING`
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
| P8-REL013-01 | REP-014 REL-013 row | UPDATE | retain direction, change `DEPENDS_ON → REFERENCES`, set bounded revalidated state | N | N |
| P8-REL013-02 | all other REP-014 content | KEEP | byte-for-byte/content-equivalent | N | N |
| P8-REL013-03 | MOD-011 / KNW-008 | KEEP | no endpoint mutation or promotion | N | N |
| P8-REL013-04 | this Matrix | UPDATE | bind material compare, read-back and verification | N | N |

Atomicity: exactly one material commit after the pre-write Matrix HEAD, exactly REP-014 + this Matrix, unexpected paths `0`.

Forbidden: no companion edge, endpoint promotion, Models/Knowledge certification, P8/Phase-1/global closure, repository-wide graph claim or global integrity PASS.

Closure requires one-row REP-014 diff, immutable read-back, exact-head four-workflow success with Runtime job split reviewed, Matrix reconciliation and closure-head verification.
