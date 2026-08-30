# MUTATION MATRIX — RELEASE VERSION DISCOVERABILITY 189

Transaction ID: `MUT-2026-08-30-RELEASE-VERSION-DISCOVERABILITY-189`
Protocol: GOV-014 v1.0.1
State: `PREWRITE / MUST BE MODIFIED IN EXACT PROTECTED CHANGE SET`

| Change ID | Target | Action | Expected State | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 189-001 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | explicitly register `Release/VERSION.md` as active current Release/version authority; no REL-001..005 promotion | N | N |
| 189-002 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | explicitly map `Release/VERSION.md` as active current Release/version authority; no REL-001..005 promotion | N | N |
| 189-003 | this Matrix | UPDATE IN SAME PROTECTED COMMIT | bind parent, exact changed set, read-back and CI evidence to the protected transaction | N | N |

## KEEP REQUIREMENT

All other repository content is `KEEP`.

Historical Release support artifacts remain in their bounded Foundation roles:

- `Release/RELEASE_MANIFEST.md` / REL-001
- `Release/COMPATIBILITY_MATRIX.md` / REL-002
- `Release/INSTALLATION.md` / REL-003
- `Release/QUICK_START.md` / REL-004
- `Release/KNOWN_LIMITATIONS.md` / REL-005

Their omission from active current-development inventory is intentional under Lease 178 and must not be treated as a symmetry defect.

## Expected changed-file set

Exactly:

1. `Repository/REP-001_MASTER_INDEX.md`
2. `Repository/REP-002_REPOSITORY_MAP.md`
3. `Repository/MUT-2026-08-30-RELEASE-VERSION-DISCOVERABILITY-189_MUTATION_MATRIX.md`

Any additional path = `UNEXPECTED CHANGE / HARD HOLD`.

## Required verification

- final live-parent recheck;
- `update_ref(... force=false)`;
- compare exact changed-file set;
- REP-001 read-back;
- REP-002 read-back;
- Matrix read-back from exact protected head;
- Internal Document-ID Audit success;
- Full-Stack Repository Audit success;
- Runtime/Integration success;
- M2 success;
- Real Mutation Matrix/GOV-014 enforcement success where triggered;
- explicit non-claim that Release or global integrity is automatically closed.

## Learning applied

`PREWRITE MATRIX PRESENCE != SAME-CHANGE-SET MATRIX BINDING.`

This file must be modified in the exact protected commit; its existence before that commit is not sufficient.
