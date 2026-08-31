# R71-20260831-P2-EJR-302B-TO-405-IDENTITY-REPAIR-227

Status: OPEN / PREWRITE AUTHORITY
Baseline: `main@d93c23a8df6d3c09b450aba97f44de0ea33324e7`
Vacancy authority: Lease226 / EJR-405 = VACANT
Target: `EJR/EJR-302_2026-08-25_CI_DECISION_BOUNDARY_AND_TOOL_SURFACE_LEARNING.md`
Replacement: `EJR-405`
Retained owner of EJR-302: `Memory/Engineering_Journal/EJR-302_2026-08-22_HERMUZ_CURRENT_HEAD_STATUS_RECHECK.md`

## Authorized repair
One displaced root record only:
- remove old EJR-302 root path;
- create `EJR/EJR-405_2026-08-25_CI_DECISION_BOUNDARY_AND_TOOL_SURFACE_LEARNING.md`;
- preserve semantic body, chronology, date, transaction provenance, and learning meaning;
- change only the record H1 identity from EJR-302 to EJR-405;
- synchronize direct semantic consumer `Governance/GOV-013B_HERMUZ_TOOL_SURFACE_DECISION_BOUNDARY.md` by changing `Learning Provenance: EJR-302 / P221` to `EJR-405 / P221`.

## Explicit non-authority
No Memory EJR-302 mutation. No governance status/version/policy semantic change. No REP synchronization unless exact evidence proves a material dependency. No analyzer/test/workflow weakening. No census baseline change inside this repair lease.

## Verification
Read-back old-path absence/new-path content, retained Memory read-back, GOV-013B provenance read-back, compare bounded diff, Internal-ID artifact, Full-Stack, Runtime, M2, Real Mutation Matrix. If the repair legitimately changes the MEMORY_TO_ROOT cohort, preserve the repair-head failure and use a separate successor lease for baseline reconciliation.
