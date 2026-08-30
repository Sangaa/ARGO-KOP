# R71-20260830-INTERNAL-ID-EJR-TRIGGER-COVERAGE-208

Status: PREWRITE / CORRECTIVE SUCCESSOR
Parent repair lease: `R71-20260830-P2-EJR-IDENTITY-REPAIR-207`
Baseline: `main@912447da46af44ab0b9805e8f3d2723a524745b4`

## Defect
The Internal Document-ID Audit workflow has complete-history execution and EJR-specific analyzers, but its push path filter does not include `EJR/**`. Therefore the first governed EJR identity repair completed without automatically invoking the audit that is required to validate its identity effect.

This is a CI coverage/configuration defect, not evidence that the repair is invalid and not permission to weaken the audit.

## Authorized correction
Add `EJR/**` to `.github/workflows/internal-id-audit.yml` push paths so direct current EJR mutations trigger the existing unchanged audit/analyzer suite.

No audit logic, test semantics, ambiguity suppression, or EJR content may change in this successor.

## Required verification
- functional diff limited to workflow path-filter addition + Matrix;
- exact-head Internal Document-ID Audit must run and pass;
- inspect its deterministic audit/census artifacts against the already repaired current tree;
- prove root EJR-214 member is absent and EJR-400 is not ambiguous;
- preserve all open global boundaries.

## Learning
`AN AUDIT THAT SCANS A DOMAIN BUT DOES NOT TRIGGER ON DIRECT MUTATIONS OF THAT DOMAIN HAS AN OBSERVABILITY COVERAGE GAP.`
