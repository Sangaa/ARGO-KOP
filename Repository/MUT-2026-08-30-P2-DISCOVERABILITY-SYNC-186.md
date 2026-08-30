# MUT-2026-08-30-P2-DISCOVERABILITY-SYNC-186

Date: 2026-08-30
Lease: `R71-20260830-P2-DISCOVERABILITY-SYNC-186`
Execution role: HERMUZ
Entry baseline: `main@0c5a5ef809ef4af430f7b32d069c1efb9ff5ea0d`
Status: `PREWRITE / LEASE ACTIVE / PROTECTED INDEX-MAP SYNC`

## Trigger

Lease 185 classified all 15 canonical-unindexed paths from exact-head artifact `9728177701`.

Only three were proved current discoverability gaps:

1. `Core/ARGO_KERNEL.md` — `CORE-KERNEL`, Revalidated / Integrity Hold, Canonical Yes.
2. `Core/Core.md` — `CORE-INDEX`, Validated for inventory / Integrity Hold, Canonical Yes.
3. `Quality/QLT-001_QUALITY_ASSURANCE.md` — `QLT-001`, Approved / Canonical; current Quality status identifies it as the canonical Quality specification.

The other twelve targets are explicitly excluded because current domain/state evidence does not authorize active-index admission.

## Protected targets

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- `Repository/MUT-2026-08-30-P2-DISCOVERABILITY-SYNC-186_MUTATION_MATRIX.md`

## Required semantic mutation

Add exact discoverability for only:

- `Core/ARGO_KERNEL.md`
- `Core/Core.md`
- `Quality/QLT-001_QUALITY_ASSURANCE.md`

Mapping/index wording must preserve:

- Core remains `INTEGRITY HOLD`; mapping is not Core certification.
- Quality remains `INTEGRITY HOLD / CROSS-LAYER VALIDATION OPEN`; mapping QLT-001 is not Quality global certification.
- no Knowledge, Architecture README, or Templates README promotion.
- no release/baseline change.
- no relationship promotion.

## Forbidden additions

Do not add under this lease:

- `Knowledge/KNW-001..010`
- `Architecture/README.md`
- `Templates/README.md`
- any other path discovered during editing

Any additional gap requires a new classification/prewrite.

## Protected transaction contract

Before mutation:

1. rediscover live `main`;
2. fetch fresh REP-001 and REP-002 content/blob identities from that live parent;
3. build finalized complete contents without truncation or partial-file reconstruction;
4. create finalized blobs;
5. create tree from the fresh live parent tree;
6. create one commit with fresh parent;
7. perform final live-parent recheck;
8. `update_ref(main, commit, force=false)` only if parent is unchanged;
9. compare parent→new commit and require exact changed-file set:
   - REP-001
   - REP-002
   - this lease's Mutation Matrix closure state if included in the same protected change;
10. read back exact paths;
11. verify exact-head CI.

A prepared Git object is not a live transaction until the ref is bound. Any parent movement invalidates the prepared transaction.

## Content-preservation gate

A protected registry must never be rebuilt from a truncated connector rendering or hand-reconstructed excerpt.

Required source condition:

`COMPLETE CURRENT FILE BYTES / CONTENT AVAILABLE → MODIFY MINIMALLY → DIFF EXACTLY`

If complete current content is not available on the working surface, HOLD the protected write rather than risk a content-preservation regression.

## C1-C6

- C1 PASS — unique lease and matrix paths.
- C2 PASS — exact three-path discoverability scope only.
- C3 PASS — mapping does not promote Core/Quality authority or global certification.
- C4 PASS — P2 remains open because EJR traceability reuse remains unresolved even after this sync.
- C5 PASS — Lease 185 direct evidence proves the three candidate paths and excludes the other twelve.
- C6 PASS — protected change can be resumed from a single explicit transaction contract.

## Verification contract

Required exact-head surfaces after mutation:

- Internal Document-ID Audit;
- Full-Stack Repository Audit;
- ARGO Runtime Prototype and Integration Tests;
- M2 Multi-Channel Proposal Training;
- exact changed-file compare;
- REP-001/REP-002 read-back.

The expected audit effect is narrower canonical-unindexed population. No exact count is asserted before execution because current EJR evidence and other state may have changed.

## Stop conditions

HARD HOLD if:

- live parent moves after candidate construction;
- complete current REP-001/REP-002 contents cannot be obtained safely;
- changed-file set expands;
- any required CI fails;
- index/map wording would imply domain promotion;
- another session has already synchronized one or more target paths.

Initial state:

`P2_DISCOVERABILITY_SYNC_186 = READY / PROTECTED WRITE NOT YET BOUND`.