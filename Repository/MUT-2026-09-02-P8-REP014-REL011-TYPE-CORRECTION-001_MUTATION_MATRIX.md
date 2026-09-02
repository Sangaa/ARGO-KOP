# P8 REL-011 Bounded Type-Correction — Pre-Write Mutation Matrix

Transaction ID: `MUT-2026-09-02-P8-REP014-REL011-TYPE-CORRECTION-001`
Priority: `8 — Governance`
State: `TYPE-CORRECTED MATERIAL CANDIDATE / CI PENDING`
Entry HEAD: `892793eb125989c68c25f1c37d93c45f2743cb6b`
Pre-write Matrix HEAD: `db8250eba384fe5dedc12cb64692ae982e5efb4d`
Target: `Repository/REP-014_REPOSITORY_RELATIONSHIP_REGISTRY.md`
Source blob: `0a076c273462e88f6f8be68bc415b208109cd48c`
Protocols: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / REP-003 / REP-014 / KNW-003`

## Legal entry and disposition

REL-010 is closed/type-corrected with closure-head four-workflow success. Priority 8 remains OPEN. REL-011 is the next smallest existing over-certification candidate in the same inspected seam.

Current row: `MOD-011 → KNW-003 = DEPENDS_ON / Revalidation Required`.

Evidence gates:

- SOURCE AUTHORITY: MOD-011 is Canonical / Proposed / Future-Ready / Revalidated within its bounded source/provenance semantic scope.
- TARGET AUTHORITY: KNW-003 is Canonical / Approved / Revalidation Required; no target promotion is authorized.
- SEMANTIC DIRECTION: MOD-011 directly lists KNW-003 under Related Documents.
- DEPENDENCY NECESSITY: FAIL; MOD-011 defines its source/provenance model without importing or requiring KNW-003 relationship semantics. Its revalidation rule identifies KNW-003 as an affected review surface, not a prerequisite.
- CONSUMER / IMPACT: exact-row, semantic/path, reverse/Quality/Tools and history searches found no executable consumer relying on the `DEPENDS_ON` type; current impact is REP-014 plus this Matrix.
- TYPE FIT: `REFERENCES` is the strongest supported type. `DEPENDS_ON` overstates necessity; `CONSUMES`, `IMPLEMENTS`, `GOVERNS`, `VALIDATES` and a manufactured reverse edge are unsupported.

Disposition: `TYPE CORRECTION REQUIRED / RETAIN REVALIDATION REQUIRED`.

Authorized row: `REL-011 | MOD-011 | KNW-003 | REFERENCES | Revalidation Required`.

## Mutation Matrix

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---:|---:|
| P8-REL011-01 | REP-014 REL-011 row | UPDATE | `DEPENDS_ON → REFERENCES`; preserve source, target and `Revalidation Required` | Y | PENDING CI |
| P8-REL011-02 | all other REP-014 content | KEEP | byte-for-byte/content-equivalent | Y | Y |
| P8-REL011-03 | MOD-011 / KNW-003 | KEEP | no endpoint mutation or promotion | Y | Y |
| P8-REL011-04 | this Matrix | UPDATE | bind material compare, read-back and verification | Y | PENDING CI |

Atomicity: exactly one material commit after the pre-write Matrix HEAD, exactly REP-014 + this Matrix, unexpected paths `0`.

Forbidden: no direction reversal, companion edge, endpoint revalidation, relationship promotion, folder/domain certification, P8/Phase-1/global closure or global integrity PASS.

Closure requires one-row REP-014 diff, immutable read-back, exact-head four-workflow success with Runtime job split reviewed, Matrix reconciliation and closure-head verification.

Pre-write Matrix HEAD verification: Full-Stack `33682799466`, Runtime/Integration `33682799430`, Real Mutation Matrix `33682799436`, and M2 `33682799447` all succeeded.
