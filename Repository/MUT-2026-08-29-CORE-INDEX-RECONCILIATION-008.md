# MUT-2026-08-29 — CORE-001/CORE-002 INDEX RECONCILIATION — 008

State: CLOSED / EXECUTION-VERIFIED
Lease: R71-20260829-CORE-INDEX-008
Baseline: c14320beb64add24a67ac56b7cc8e828d3ccfd28
Functional SHA: e3c8fa9e88ff7e30d896cadbd0ddb3196be3adba
Scope: Repository control-plane inventory only

## Evidence

- `Core/CORE-001_ARGO_MANIFEST.md`: Document ID CORE-001; Canonical Yes; Approved / Revalidated / Integrity Hold; Last Audit 2026-08-10.
- `Core/CORE-002_ARGO_IDENTITY.md`: Document ID CORE-002; Canonical Yes; Approved / Revalidated / Integrity Hold; Last Audit 2026-08-10.
- `Core/_FOLDER_STATUS.md` lists both as known canonical Core artifacts independently revalidated on 2026-08-10.
- Prior REP-001/REP-002 omitted both paths.
- Knowledge KNW-001..010 were explicitly NOT included because `Knowledge/_FOLDER_STATUS.md` says Canonical Validation is pending consolidated repository-wide validation.

## Mutation Matrix

| Protected surface | Before | After | Authority effect |
|---|---|---|---|
| REP-001 Core inventory | CORE-001/002 omitted | CORE-001/002 listed | inventory discoverability only; no promotion |
| REP-002 Core map | CORE-001/002 omitted | CORE-001/002 mapped | physical mapping only; no promotion |

## Exact-head verification

At `e3c8fa9e88ff7e30d896cadbd0ddb3196be3adba`:
- ARGO Runtime Prototype and Integration Tests: SUCCESS (run 33238991143)
- Full-Stack Repository Audit: SUCCESS (run 33238991153)
- M2 Multi-Channel Proposal Training: SUCCESS (run 33238991173)
- Full-Stack Mutation Matrix preflight, semantic regression, same-change-set enforcement, CI correlation and repository-wide audit: SUCCESS

## Threat controls

- No inference from filename alone.
- No promotion from index membership.
- No Knowledge-domain spillover.
- Core cross-layer certification remains open.

## Continuous-improvement learning

Index reconciliation must distinguish `canonical and revalidated but omitted` from `reviewed but canonical validation pending`. A single unindexed-canonical count is insufficient for safe bulk repair; authority evidence must be classified per domain before mutation.

## Closure

`CORE-001/CORE-002-INDEX-DISCOVERABILITY = CLOSED / EXECUTION-VERIFIED`.

Non-claim: this does not close Core cross-layer certification or Connected Baseline Global.
