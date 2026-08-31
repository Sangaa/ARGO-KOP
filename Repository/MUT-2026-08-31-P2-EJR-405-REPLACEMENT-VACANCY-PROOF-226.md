# R71-20260831-P2-EJR-405-REPLACEMENT-VACANCY-PROOF-226

Status: OPEN / PREWRITE / VACANCY EVIDENCE PENDING
Baseline: `main@2af2ccd9f982e5b9e8ccfc735c6d7d09f3b9c9e4`
Target future repair: `EJR/EJR-302_2026-08-25_CI_DECISION_BOUNDARY_AND_TOOL_SURFACE_LEARNING.md`
Replacement candidate: `EJR-405`

## Selection boundary
Supplement225 and Plan204 establish the remaining displaced root EJR-302 record as a separate repair unit. The retained Memory allocation remains EJR-302. The remaining root record has semantic provenance consumed by `Governance/GOV-013B_HERMUZ_TOOL_SURFACE_DECISION_BOUNDARY.md` via `Learning Provenance: EJR-302 / P221`.

This lease performs replacement-vacancy proof only. It does not rename or rewrite the EJR record, GOV-013B, Memory EJR-302, any census baseline, analyzer, test, registry, or governance status.

## Candidate discovery
Repository code search for `EJR-405` returned no result. Repository commit search for `EJR-405` returned no result. These are candidate-discovery signals only and are not treated as vacancy proof.

## Required vacancy gate
`EJR-405` may be allocated only if the dedicated complete-history workflow returns:
- current_claims=[];
- historical_claims=[];
- history_complete=true;
- occupied=false;
- vacant=true;
- decision=`VACANT`.

`OCCUPIED` or `HISTORY_INCOMPLETE` blocks allocation.

## Closure rule
Close this lease only after exact-head workflow/artifact evidence is inspected and proves `VACANT`. No functional identity repair is authorized inside this lease.
