# P9 Architecture — Runtime Navigation / CI Evidence Reconciliation — Transaction Q

Transaction ID: `MUT-2026-09-03-P9-RUNTIME-NAVIGATION-CI-EVIDENCE-Q`
Priority: `9 — Architecture`
State: `PRE-WRITE / ATOMIC MATERIAL MUTATION NOT YET APPLIED`
Entry HEAD: `29b5b419a00c668156199a5d0c4e6f8fd819e599`
Targets:
- `Runtime/README.md`
- `Runtime/RUN-010_RUNTIME_REFERENCE.md`
- `Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Target | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|
| `Runtime/README.md` | align current Runtime navigation with live inventory/evidence; distinguish RUN-001..010 core contracts from RUN-011..015 + Prototype candidate/prototype surfaces; add ARC-011 as current canonical Architecture authority; version/audit refresh | Status remains `Validated / Integrity Hold`; baseline `3.2.1`; no candidate/prototype promotion; Runtime remains subordinate to Architecture/Governance/Repository; no full Runtime certification | PASS | PENDING |
| `RUN-010` | extend current navigation from RUN-011/012 through RUN-013/014/015 + Prototype evidence boundary; add ARC-011 canonical Architecture reference; patch version/audit | Status remains `Validated / Integrity Hold / Revalidated`; canonical navigation role preserved; prototype remains non-executable/candidate; execution/authorization/UNKNOWN/learning boundaries preserved | PASS | PENDING |
| `RUN-015` | replace stale `Awaiting CI Evidence` state with bounded current CI-evidence-verified state; retain Candidate/Integrity Hold and explicitly limit proof to tested prototype | no full Runtime/production/executable promotion; CI success remains scope-bound; failed CI still becomes engineering input; related prototype contracts preserved | PASS | PENDING |

## Entry evidence

- Transaction P closure HEAD `29b5b419a00c668156199a5d0c4e6f8fd819e599` is live `main` and closure workflows are all SUCCESS: Full-Stack `33722045592`, Runtime/Integration `33722045550`, Real Mutation Matrix `33722045633`, M2 `33722045634`.
- `Runtime/_FOLDER_STATUS.md` currently includes RUN-011 through RUN-015 and `Runtime/Prototype/` in its evidence scope, states that successful prototype CI evidence exists, and explicitly preserves `CROSS-LAYER INTEGRATION HOLD` plus executable-promotion HOLD.
- `Runtime/README.md` still labels a `Canonical Runtime Structure` containing only RUN-001 through RUN-010 and folder status. This is stale navigation/inventory wording relative to current repository evidence and risks excluding current candidate/prototype surfaces or conflating inventory with authority.
- `RUN-010_RUNTIME_REFERENCE.md` already includes RUN-011/012 but omits RUN-013/014/015 and the Prototype evidence surface from its current navigation, despite its purpose claiming to summarize the current Runtime layer and cognitive-loop prototype boundary.
- `RUN-011`, `RUN-012`, `RUN-013`, and `RUN-014` directly declare `Candidate / Integrity Hold`; they define prototype/test/safety/learning boundaries and do not establish executable authority.
- `RUN-015` directly declares `Candidate / Awaiting CI Evidence` and says no PASS claim is made until CI execution evidence exists. Current exact-head Runtime/Integration run `33722045550` is SUCCESS, and Runtime folder status independently records successful prototype CI evidence; therefore `Awaiting CI Evidence` is stale while candidate/executable promotion holds remain valid.
- `ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` is current `Canonical: Yes` and explicitly authoritative for structural boundaries/dependency direction; it states `Runtime executes approved architecture and contracts`. Current Runtime navigation should reference this authority without displacing ARC-006 dependency semantics.
- GitHub code search did not return RUN-015 by filename even though direct current-path retrieval proves it exists; negative search is therefore not used as absence or coverage evidence.

## Atomic packaging rule

Transaction P proved that current protected-change enforcement requires the mutation matrix to be present in the same current change set as protected Runtime targets. Q will therefore use the Git Data atomic path from the start:

`create target blobs + finalized-in-change-set matrix blob → create tree from live base tree → create commit → fast-forward main ref`

No test weakening, force update, or unrelated rewrite is permitted.

## Non-claims

- Q does not close Architecture Gate 13 by itself.
- Q does not certify Runtime, Interfaces, connectors, provider behavior or repository-wide control-plane relationships.
- RUN-011..015 remain candidate/prototype evidence surfaces and are not promoted to canonical executable Runtime authority.
- `Runtime/_FOLDER_STATUS.md` remains `CROSS-LAYER INTEGRATION HOLD`.
- `Interfaces/_FOLDER_STATUS.md` remains on its own cross-layer/external-trust hold.
- Transaction B / REL-073 remains separate local Registry hold.

Validation plan:
`atomic targets+matrix material commit → immutable read-back → exact parent compare → exact-head 4-family CI → finalize matrix → closure-head CI`.
