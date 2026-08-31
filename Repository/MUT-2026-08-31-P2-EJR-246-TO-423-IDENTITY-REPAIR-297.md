# MUT-2026-08-31-P2-EJR-246-TO-423-IDENTITY-REPAIR-297

Status: OPEN / MUTATION AUTHORIZED
Opening main: `97826ce6864ef667b47253d661b889bf924bcc66`
Pre-write Matrix297: `cae5fe0210d9c18928616416474a26f97f440269`
Prerequisite: Lease296 CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

## Identity decision

- RETAIN unchanged: `Memory/Engineering_Journal/EJR-246_2026-08-15_P65_SESSION_CLOSURE.md`.
- DISPLACE from EJR-246: `EJR/EJR-246_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md`.
- RESERVED successor: `EJR-423`, proven complete-history VACANT by run `33409267610`, artifact `9764434172`, digest `sha256:f7ab8977442df306625d11897cfd79a7048ceb37af2a42efb7627729ed8ee202`.

## Authorized execution

Perform one atomic Git tree mutation that removes the displaced root EJR-246 path and creates `EJR/EJR-423_2026-08-17_M2_PROPOSAL_WRITE_VERIFICATION.md`. Only the first H1 identity token may change from EJR-246 to EJR-423; the remaining content must be preserved exactly. Memory EJR-246 must remain untouched.

Cohort baseline normalization is forbidden inside Repair297. Any deterministic count drift requires separate Lease298 after exact artifact inspection.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
