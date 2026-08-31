# MUTATION MATRIX — Lease 314 EJR-234 Disposition / EJR-429 Vacancy Proof

Transaction ID: MUT-2026-08-31-P2-EJR-234-DISPOSITION-AND-429-VACANCY-PROOF-314
Protocol: GOV-014
Status: OPEN

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| 314-01 | Lease 314 record | CREATE | evidence-only disposition and hard vacancy gate | Y | Y |
| 314-02 | `.github/workflows/ejr-replacement-vacancy-proof-314.yml` | CREATE | complete-history proof for EJR-429 | N | N |
| 314-03 | EJR-234 members | KEEP | no identity mutation before VACANT artifact | Y | Y |

## KEEP REQUIREMENT
Preserve both current EJR-234 member files byte-for-byte while Lease314 is evidence-only. Do not rename, delete, suppress, or reassign either identity until the complete-history vacancy decision is verified.

## Execution Evidence
Opening HEAD is the current main lineage after baseline 313. Memory chronology precedes root chronology. Current search found no EJR-429 allocation, but current search absence is explicitly insufficient for vacancy.

## Closure
Lease314 may close only after the complete-history vacancy workflow and Full-Stack validation are inspected. If EJR-429 is not VACANT, no identity repair is authorized.
