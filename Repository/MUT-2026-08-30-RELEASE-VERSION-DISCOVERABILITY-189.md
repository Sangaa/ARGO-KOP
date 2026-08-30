# MUT-2026-08-30-RELEASE-VERSION-DISCOVERABILITY-189

Date: 2026-08-30
Lease: `R71-20260830-RELEASE-VERSION-DISCOVERABILITY-189`
Execution role: HERMUZ
Status: `CLOSED / EXECUTION-VERIFIED`

## Proven gap

`Release/VERSION.md` is current live authority for:

- official release `1.0.0`;
- development baseline `3.2.1`;
- the separation between released version and development baseline;
- release/version compatibility and upgrade planning.

The Release closure evidence established:

`RELEASE_VERSION_ACTIVE_AUTHORITY_INDEX/MAP GAP = OPEN`.

The authorized correction was bounded to registering only `Release/VERSION.md` in REP-001 and REP-002, without promoting historical Foundation support artifacts `REL-001..005`.

## Executed transaction

Protected commit:

`5b6b6001aca99367e20425db68cabdfb81050c71`

Parent:

`264944f3827fdcb1a802d0444525fdfa96f40c18`

Exact compare proves one commit ahead and exactly these three changed paths:

1. `Repository/REP-001_MASTER_INDEX.md`;
2. `Repository/REP-002_REPOSITORY_MAP.md`;
3. `Repository/MUT-2026-08-30-RELEASE-VERSION-DISCOVERABILITY-189_MUTATION_MATRIX.md`.

Unexpected changed paths: `0`.

Post-write protected blobs:

- REP-001 = `f6271483be89ee1b7ce35ad5a1441e38e209cde3`;
- REP-002 = `c9cd69054a862e3d2287c2eda2ed05fde26073c6`.

## Exact-head verification

All observed push workflows for exact head `5b6b6001aca99367e20425db68cabdfb81050c71` completed successfully:

- GOV-014 Controlled Document Mutation — run `33303930551` — SUCCESS;
- M2 Multi-Channel Proposal Training — run `33303930561` — SUCCESS;
- Real Mutation Matrix Regression — run `33303930594` — SUCCESS;
- ARGO Runtime Prototype and Integration Tests — run `33303930548` — SUCCESS;
- Full-Stack Repository Audit — run `33303930567` — SUCCESS;
- Internal Document-ID Audit — run `33303930560` — SUCCESS.

Internal-ID artifact:

- artifact ID `9729833996`;
- name `internal-document-id-audit-report`;
- digest `sha256:7a91c9477eab6e7134eee50c37aaa62d712018a2e6dc6314164298c63b7b0af4`;
- exact head `5b6b6001aca99367e20425db68cabdfb81050c71`.

## Evidence-search note

The commit-associated workflow wrapper returned an empty set because that wrapper is limited to pull-request-triggered runs. Direct `actions/runs?head_sha=...` retrieval recovered the six push runs above. This is classified as a tool-coverage limitation already anticipated by GOV-013 search-recheck rules, not a repository defect.

## Closed scope

`RELEASE_VERSION_DISCOVERABILITY_189 = CLOSED / EXECUTION-VERIFIED`.

The closure proves only the bounded active-authority discoverability repair. It does not automatically close the Release partition, Priority 2, the Connected Baseline, or global integrity.

## Next legal action

Perform explicit Release Phase-1 control-plane closure synchronization. `REP-016` still records Release as partition-open and must be reconciled through a fresh protected transaction before claiming `Release = CLOSED_FOR_PHASE_1`.
