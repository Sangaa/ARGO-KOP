# MUT-2026-08-29 — CORE-001/CORE-002 INDEX RECONCILIATION — 008

State: Applied / Pending exact-head CI verification
Lease: R71-20260829-CORE-INDEX-008
Baseline: c14320beb64add24a67ac56b7cc8e828d3ccfd28
Scope: Repository control-plane inventory only

## Evidence

- `Core/CORE-001_ARGO_MANIFEST.md`: Document ID CORE-001; Canonical Yes; Approved / Revalidated / Integrity Hold; Last Audit 2026-08-10.
- `Core/CORE-002_ARGO_IDENTITY.md`: Document ID CORE-002; Canonical Yes; Approved / Revalidated / Integrity Hold; Last Audit 2026-08-10.
- `Core/_FOLDER_STATUS.md` lists both as known canonical Core artifacts independently revalidated on 2026-08-10.
- Current REP-001/REP-002 omitted both paths.
- Knowledge KNW-001..010 are explicitly NOT included in this mutation because `Knowledge/_FOLDER_STATUS.md` says Canonical Validation is pending consolidated repository-wide validation.

## Mutation Matrix

| Protected surface | Before | After | Authority effect |
|---|---|---|---|
| REP-001 Core inventory | CORE-001/002 omitted | CORE-001/002 listed | inventory discoverability only; no promotion |
| REP-002 Core map | CORE-001/002 omitted | CORE-001/002 mapped | physical mapping only; no promotion |

## Threat controls

- No inference from filename alone.
- No promotion from index membership.
- No Knowledge-domain spillover.
- Core cross-layer certification remains open.
- Exact-head Runtime/Integration, Full-Stack, and M2 CI required before closure.

## Continuous-improvement learning

Index reconciliation must distinguish `canonical and revalidated but omitted` from `reviewed but canonical validation pending`. A single unindexed-canonical count is insufficient for safe bulk repair; authority evidence must be classified per domain before mutation.
