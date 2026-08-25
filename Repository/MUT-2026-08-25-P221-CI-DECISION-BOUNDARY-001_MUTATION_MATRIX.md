# MUT-2026-08-25-P221-CI-DECISION-BOUNDARY-001

## Transaction

| Field | Value |
|---|---|
| Change ID | MUT-2026-08-25-P221-CI-DECISION-BOUNDARY-001 |
| Target | Governance learning / HERMUZ decision boundary |
| Action | Add canonical learning artifact; strengthen future-agent decision discipline |
| Expected Content | Require evidence-first CI failure analysis, prohibit conclusion/transition from partial CI evidence, and require tool-capability-aware revalidation when a prior inspection path reports no run/evidence |
| Applied | Y |
| Verified | PENDING |

## Scope

Document the repeatable failure observed at P220: the engineer initially relied on a narrow workflow-run lookup and treated absence of a run from that surface as sufficient evidence, while a broader GitHub Actions surface later exposed the actual failing run and root cause.

## KEEP / Preservation

- Preserve historical commits and failure evidence.
- Do not reinterpret the original P220 mutation as pre-write compliant.
- Do not weaken CI gates.
- Do not promote any architectural or runtime relationship.

## Pre-Write Validation

- Prior learning searched: GOV-013 §9B/9B.4; GOV-014A; EJR-280.
- Current GitHub evidence inspected using workflow-run listing, job inspection, and job-log retrieval.
- Root cause confirmed: protected mutation without pre-existing Mutation Matrix.

## Post-Write Verification

Required after mutation:
- target read-back;
- applicable CI run inspection;
- complete Job/Step/Log review;
- reconciliation and closure evidence.
