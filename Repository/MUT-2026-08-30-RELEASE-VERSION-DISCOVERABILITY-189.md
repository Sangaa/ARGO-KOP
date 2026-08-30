# MUT-2026-08-30-RELEASE-VERSION-DISCOVERABILITY-189

Date: 2026-08-30
Lease: `R71-20260830-RELEASE-VERSION-DISCOVERABILITY-189`
Execution role: HERMUZ
Status: `PREWRITE / PROTECTED TRANSACTION READY / NOT EXECUTED`

## Proven gap

`Release/VERSION.md` is current live authority for:

- official release `1.0.0`;
- development baseline `3.2.1`;
- the separation between released version and development baseline;
- release/version compatibility and upgrade planning.

The current Release closure evidence (`Repository/RELEASE_PARTITION_CLOSURE_REVIEW_2026-08-30.md`) independently established:

`RELEASE_VERSION_ACTIVE_AUTHORITY_INDEX/MAP GAP = OPEN`.

It also established the exact legal correction:

- register **only** `Release/VERSION.md` as active Release authority in REP-001 and REP-002;
- do not bulk-promote historical Foundation support artifacts `REL-001..005` merely for symmetry.

## Objective

Perform one protected same-change-set transaction that adds only:

`Release/VERSION.md`

to the active Release discoverability surfaces in:

1. `Repository/REP-001_MASTER_INDEX.md`;
2. `Repository/REP-002_REPOSITORY_MAP.md`;
3. a Mutation Matrix modified in that exact protected change set.

## Semantic boundary

The transaction may state:

- `Release/VERSION.md` = active current version authority;
- official release = 1.0.0 Foundation;
- development baseline = 3.2.1;
- discoverability/mapping only.

It must not:

- promote `REL-001..005` into current-development authority;
- change version numbers;
- close Release automatically;
- claim current consumers for historical Foundation support where semantic role does not require them;
- change REP-014/REP-016 unless separately authorized;
- claim Global PASS.

## Required protected procedure

`FRESH MAIN → COMPLETE REP-001/002 SOURCE → MINIMAL ADDITIVE CANDIDATE → MATRIX IN SAME CHANGE SET → FINAL PARENT RECHECK → FORCE=FALSE FAST-FORWARD → EXACT COMPARE → READ-BACK → EXACT-HEAD CI`.

No protected write is valid merely because a prewrite Matrix already exists. The Matrix must be visible in the exact protected change set enforced by CI.

## C1-C6

- C1 PASS — unique Lease 189 path.
- C2 PASS — one live authority path only; no historical Release document promotion.
- C3 PASS — authority already exists in `Release/VERSION.md`; transaction only repairs discoverability.
- C4 PASS — mapping cannot auto-close Release or global integrity.
- C5 PASS — direct VERSION read + Lease 178 closure review independently establish the gap.
- C6 PASS — P2 repair 187 is closed; this is an independent Release partition continuation.

## Stop conditions

HOLD if:

- live REP-001/REP-002 already changed to include `Release/VERSION.md`;
- main moves after final parent check;
- candidate changes any path beyond REP-001, REP-002, and same-change-set Matrix;
- Full-Stack preflight reports protected change without Matrix;
- any exact-head required workflow fails.

Initial state:

`RELEASE_VERSION_DISCOVERABILITY_189 = READY / NOT EXECUTED`.
