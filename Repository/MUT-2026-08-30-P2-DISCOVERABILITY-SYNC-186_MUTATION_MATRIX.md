# MUT-2026-08-30-P2-DISCOVERABILITY-SYNC-186 — MUTATION MATRIX

Date: 2026-08-30
Lease: `R71-20260830-P2-DISCOVERABILITY-SYNC-186`
Protocol: GOV-014 controlled mutation
State: `PREWRITE / PROTECTED CHANGE NOT EXECUTED`

## Authorized changes

| Change | Protected target | Exact semantic action | Expected result | Applied | Verified |
|---|---|---|---|:---:|:---:|
| 186-A | `Repository/REP-001_MASTER_INDEX.md` | add active discoverability entries for `Core/ARGO_KERNEL.md`, `Core/Core.md`, `Quality/QLT-001_QUALITY_ASSURANCE.md` only; preserve all existing content and holds | three classified active paths discoverable in master index without domain promotion | N | N |
| 186-B | `Repository/REP-002_REPOSITORY_MAP.md` | add corresponding physical mappings for the same three paths only; preserve all existing content and holds | physical map synchronized to REP-001 for the classified scope | N | N |
| 186-C | this Mutation Matrix | close with actual parent/commit/changed-set/read-back/CI evidence in the protected transaction or immediately governed closure unit | transaction evidence complete | N | N |

## Explicit exclusions

No change is authorized for:

- Knowledge/KNW-001..010
- Architecture/README.md
- Templates/README.md
- any target domain artifact
- REP-014 or REP-016
- Release/VERSION or baseline
- relationship state
- domain certification

## Expected changed-file set

At functional protected mutation:

1. `Repository/REP-001_MASTER_INDEX.md`
2. `Repository/REP-002_REPOSITORY_MAP.md`
3. `Repository/MUT-2026-08-30-P2-DISCOVERABILITY-SYNC-186_MUTATION_MATRIX.md` if closure metadata is committed in the same protected transaction

Any additional changed path = `UNEXPECTED CHANGE / HARD HOLD`.

## Preflight evidence

Lease 185 classification proves:

- `CORE-KERNEL = SHOULD-BE-INDEXED`
- `CORE-INDEX = SHOULD-BE-INDEXED`
- `QLT-001 = SHOULD-BE-INDEXED`
- other 12 canonical-unindexed paths = explicitly excluded from active-index synchronization in this lease.

## Content-preservation requirement

REP-001 and REP-002 must be mutated from complete current contents at a freshly rediscovered live parent. Truncated rendered snippets are insufficient source material for a protected replacement.

No write is legal until:

`COMPLETE SOURCE → MINIMAL EDIT → COMPLETE CANDIDATE → FRESH PARENT CHECK → ATOMIC REF BINDING`.

## Required post-write evidence

- exact parent SHA;
- candidate commit SHA;
- `force=false` ref update;
- compare confirms only expected files;
- exact REP-001/REP-002 read-back;
- Internal Document-ID Audit SUCCESS;
- Full-Stack Repository Audit SUCCESS;
- Runtime/Integration SUCCESS;
- M2 SUCCESS;
- no global/domain promotion.

## Current disposition

`READY / NOT EXECUTED / RESUME-SAFE`.

This matrix authorizes no partial or contents-API rewrite from incomplete source text.