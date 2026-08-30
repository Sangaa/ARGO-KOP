# MUTATION MATRIX — RELEASE VERSION DISCOVERABILITY 189

Transaction ID: `MUT-2026-08-30-RELEASE-VERSION-DISCOVERABILITY-189`
Protocol: GOV-014 v1.0.1
State: `PROTECTED CHANGE CANDIDATE / APPLIED PENDING EXACT-HEAD VERIFICATION`

| Change ID | Target | Action | Expected State | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 189-001 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | explicitly register `Release/VERSION.md` as active current Release/version authority; no REL-001..005 promotion | Y | N |
| 189-002 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | explicitly map `Release/VERSION.md` as active current Release/version authority; no REL-001..005 promotion | Y | N |
| 189-003 | this Matrix | UPDATE IN SAME PROTECTED COMMIT | bind exact changed set and verification handoff to protected transaction | Y | N |

## KEEP REQUIREMENT

All other repository content is `KEEP`.

Historical Release support artifacts remain in their bounded Foundation roles:
- `Release/RELEASE_MANIFEST.md` / REL-001
- `Release/COMPATIBILITY_MATRIX.md` / REL-002
- `Release/INSTALLATION.md` / REL-003
- `Release/QUICK_START.md` / REL-004
- `Release/KNOWN_LIMITATIONS.md` / REL-005

Their omission from active current-development inventory is intentional under Lease 178.

## Candidate evidence

- Source parent: `264944f3827fdcb1a802d0444525fdfa96f40c18` pending final live-parent recheck.
- Source REP-001 blob: `17b432f27426d3692f9067ebf668d41f18e575b0`.
- Source REP-002 blob: `b02d2c1622845e5b9dd46907934ecaad547f050d`.
- Desired REP-001 blob: `f6271483be89ee1b7ce35ad5a1441e38e209cde3`.
- Desired REP-002 blob: `c9cd69054a862e3d2287c2eda2ed05fde26073c6`.
- Added active authority path: `Release/VERSION.md` only.
- No version value, Release artifact, REL-001..005, REP-014/016, relationship state, or global/domain hold is changed.

## Expected changed-file set

Exactly:
1. `Repository/REP-001_MASTER_INDEX.md`
2. `Repository/REP-002_REPOSITORY_MAP.md`
3. `Repository/MUT-2026-08-30-RELEASE-VERSION-DISCOVERABILITY-189_MUTATION_MATRIX.md`

Any additional path = `UNEXPECTED CHANGE / HARD HOLD`.

## Required post-bind verification

- final live-parent recheck;
- `update_ref(... force=false)`;
- exact compare and unexpected paths = 0;
- REP-001/REP-002/Matrix read-back;
- Internal Document-ID Audit SUCCESS;
- Full-Stack SUCCESS;
- Runtime/Integration SUCCESS;
- M2 SUCCESS;
- Real Mutation Matrix/GOV-014 enforcement SUCCESS where triggered;
- explicit Release Phase-1 closure review remains separate.

## Learning applied

`PREWRITE MATRIX PRESENCE != SAME-CHANGE-SET MATRIX BINDING.`

`ACTIVE AUTHORITY DISCOVERABILITY SHOULD FOLLOW VERIFIED SEMANTIC ROLE, NOT FOLDER SYMMETRY.`
