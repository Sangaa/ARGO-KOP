# P9 Architecture — Runtime Navigation / CI Evidence Reconciliation — Transaction Q

Transaction ID: `MUT-2026-09-03-P9-RUNTIME-NAVIGATION-CI-EVIDENCE-Q`
Priority: `9 — Architecture`
State: `MATERIAL CANDIDATE / ATOMIC CHANGE SET READY`
Entry HEAD: `29b5b419a00c668156199a5d0c4e6f8fd819e599`
Pre-write HEAD: `6a8084a4fdef3d29a230133513ef8289c97e63b9`
Targets:
- `Runtime/README.md`
- `Runtime/RUN-010_RUNTIME_REFERENCE.md`
- `Runtime/RUN-015_RUNTIME_PROTOTYPE_CI_VALIDATION.md`
Protocol: `GOV-013 / GOV-014 / GOV-014A / GOV-015 / GOV-016`

| Target | Expected change | KEEP / preservation | Pre-write | Post-write |
|---|---|---|---|---|
| `Runtime/README.md` | align current Runtime navigation with live inventory/evidence; distinguish RUN-001..010 core contracts from RUN-011..015 + Prototype candidate/prototype surfaces; add ARC-011 as current canonical Architecture authority; Version `3.3.0 → 3.3.1`; Last Audit `2026-09-03` | Status remains `Validated / Integrity Hold`; baseline `3.2.1`; no candidate/prototype promotion; Runtime remains subordinate to Architecture/Governance/Repository; no full Runtime certification | PASS | PENDING CI |
| `RUN-010` | extend current navigation through RUN-013/014/015 + Prototype evidence boundary; add ARC-011 canonical Architecture reference; Version `1.4.0 → 1.4.1`; Last Audit `2026-09-03` | Status remains `Validated / Integrity Hold / Revalidated`; canonical navigation role preserved; prototype remains non-executable/candidate; execution/authorization/UNKNOWN/learning boundaries preserved | PASS | PENDING CI |
| `RUN-015` | replace stale `Candidate / Awaiting CI Evidence` with bounded `Candidate / Integrity Hold / CI Evidence Available`; Version `1.0.0 → 1.0.1`; add exact prior runtime-CI evidence and explicit current-head revalidation boundary | no full Runtime/production/executable promotion; prior CI does not pre-certify later heads; CI success remains scope-bound; failed CI remains engineering input; related prototype contracts preserved | PASS | PENDING CI |

## Entry evidence

- Transaction P closure HEAD `29b5b419a00c668156199a5d0c4e6f8fd819e599` is the predecessor and closure workflows are all SUCCESS: Full-Stack `33722045592`, Runtime/Integration `33722045550`, Real Mutation Matrix `33722045633`, M2 `33722045634`.
- `Runtime/_FOLDER_STATUS.md` includes RUN-011 through RUN-015 and `Runtime/Prototype/` in its evidence scope, states successful prototype CI evidence exists, and explicitly preserves `CROSS-LAYER INTEGRATION HOLD` plus executable-promotion HOLD.
- `Runtime/README.md` labels a `Canonical Runtime Structure` containing only RUN-001 through RUN-010 and folder status. This is stale navigation/inventory wording relative to current repository evidence and risks excluding current candidate/prototype surfaces or conflating inventory with authority.
- `RUN-010_RUNTIME_REFERENCE.md` includes RUN-011/012 but omits RUN-013/014/015 and the Prototype evidence surface from its current navigation, despite its purpose claiming to summarize the current Runtime layer and cognitive-loop prototype boundary.
- `RUN-011`, `RUN-012`, `RUN-013`, and `RUN-014` directly declare `Candidate / Integrity Hold`; they define prototype/test/safety/learning boundaries and do not establish executable authority.
- `RUN-015` declares `Candidate / Awaiting CI Evidence` and says no PASS claim is made until real CI evidence exists. Exact-head Runtime/Integration run `33722045550` is SUCCESS, earlier recovery run `33721850938` is SUCCESS, and Runtime folder status independently records successful prototype CI evidence. Therefore the absence-of-evidence status is stale, while candidate/executable-promotion holds remain valid.
- `ARC-011_CANONICAL_ARCHITECTURE_MODEL.md` is `Canonical: Yes`, authoritative for structural boundaries/dependency direction, and states that Runtime executes approved architecture and contracts. Runtime navigation should reference ARC-011 without displacing ARC-006 dependency semantics.
- Negative GitHub search did not return RUN-015 even though direct current-path retrieval proves it exists; direct-path evidence controls.

## Material design

### Runtime README

- replace the stale all-canonical inventory presentation with explicit `Core Runtime contracts` and `Candidate / prototype evidence surfaces` groups;
- add RUN-011 through RUN-015 and `Runtime/Prototype/` to current navigation while retaining their non-promotion boundary;
- add ARC-011 to Runtime authority references;
- retain current Runtime Integrity Hold and baseline.

### RUN-010

- retain its canonical navigation role while making its navigation actually current through RUN-015 and Prototype;
- preserve controlled-handoff, learning-promotion and prototype-CI distinctions;
- add ARC-011 as current canonical Architecture authority while preserving ARC-006 dependency semantics.

### RUN-015

- record that real CI evidence is available on concrete predecessor heads;
- explicitly state that prior successful runs do not pre-certify the Q material head or future heads;
- preserve Candidate / Integrity Hold and scope-bound proof semantics.

## Atomic packaging rule

Transaction P proved that current protected-change enforcement requires the mutation matrix to be present in the same current change set as protected Runtime targets. Q therefore uses:

`target blobs + this material matrix blob → tree based on pre-write tree → commit → fast-forward main ref`

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
