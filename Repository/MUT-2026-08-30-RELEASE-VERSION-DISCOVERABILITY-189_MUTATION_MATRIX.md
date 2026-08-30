# MUTATION MATRIX — RELEASE VERSION DISCOVERABILITY 189

Transaction ID: `MUT-2026-08-30-RELEASE-VERSION-DISCOVERABILITY-189`
Protocol: GOV-014 v1.0.1
State: `CLOSED / VERIFIED / EXECUTION COMPLETE`

| Change ID | Target | Action | Expected State | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 189-001 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | explicitly register `Release/VERSION.md` as active current Release/version authority; no REL-001..005 promotion | Y | Y |
| 189-002 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | explicitly map `Release/VERSION.md` as active current Release/version authority; no REL-001..005 promotion | Y | Y |
| 189-003 | this Matrix | UPDATE IN SAME PROTECTED COMMIT | bind exact changed set and verification handoff to protected transaction | Y | Y |

## KEEP REQUIREMENT

All other repository content was `KEEP` in the protected semantic transaction.

Historical Release support artifacts remain in their bounded Foundation roles:
- `Release/RELEASE_MANIFEST.md` / REL-001
- `Release/COMPATIBILITY_MATRIX.md` / REL-002
- `Release/INSTALLATION.md` / REL-003
- `Release/QUICK_START.md` / REL-004
- `Release/KNOWN_LIMITATIONS.md` / REL-005

Their omission from active current-development inventory remains intentional under Lease 178.

## Protected execution evidence

- Source parent: `264944f3827fdcb1a802d0444525fdfa96f40c18`.
- Protected head: `5b6b6001aca99367e20425db68cabdfb81050c71`.
- Source REP-001 blob: `17b432f27426d3692f9067ebf668d41f18e575b0`.
- Source REP-002 blob: `b02d2c1622845e5b9dd46907934ecaad547f050d`.
- Post-write REP-001 blob: `f6271483be89ee1b7ce35ad5a1441e38e209cde3`.
- Post-write REP-002 blob: `c9cd69054a862e3d2287c2eda2ed05fde26073c6`.
- Added active authority path: `Release/VERSION.md` only.
- No version value, Release artifact, REL-001..005, REP-014/016, relationship state, or global/domain hold changed in the protected transaction.

## Exact changed-file set

Exactly:
1. `Repository/REP-001_MASTER_INDEX.md`
2. `Repository/REP-002_REPOSITORY_MAP.md`
3. `Repository/MUT-2026-08-30-RELEASE-VERSION-DISCOVERABILITY-189_MUTATION_MATRIX.md`

Unexpected paths: `0`.

## Exact-head verification

For exact head `5b6b6001aca99367e20425db68cabdfb81050c71`:

- GOV-014 Controlled Document Mutation — `33303930551` — SUCCESS
- M2 Multi-Channel Proposal Training — `33303930561` — SUCCESS
- Real Mutation Matrix Regression — `33303930594` — SUCCESS
- Runtime Prototype and Integration Tests — `33303930548` — SUCCESS
- Full-Stack Repository Audit — `33303930567` — SUCCESS
- Internal Document-ID Audit — `33303930560` — SUCCESS

Internal-ID artifact:

- ID `9729833996`
- digest `sha256:7a91c9477eab6e7134eee50c37aaa62d712018a2e6dc6314164298c63b7b0af4`
- head `5b6b6001aca99367e20425db68cabdfb81050c71`

## Closure

`RELEASE_VERSION_DISCOVERABILITY_189 = CLOSED / EXECUTION-VERIFIED`.

Release Phase-1 closure remains a separate control-plane synchronization decision; `REP-016` still records the partition as open until that protected queue state is reconciled.

## Learning applied

`PREWRITE MATRIX PRESENCE != SAME-CHANGE-SET MATRIX BINDING.`

`ACTIVE AUTHORITY DISCOVERABILITY SHOULD FOLLOW VERIFIED SEMANTIC ROLE, NOT FOLDER SYMMETRY.`

`COMMIT-ASSOCIATED WORKFLOW LOOKUP MAY OMIT PUSH RUNS; DIRECT HEAD-SHA ACTIONS ENUMERATION IS THE REQUIRED RECHECK WHEN THE FIRST RESULT IS EMPTY.`
