# MUT-2026-08-31-P2-EJR-245-TO-422-IDENTITY-REPAIR-294

Status: OPEN / MUTATION AUTHORIZED
Opening main: `229afce4a6b354254ff1a9b4146628bef9edfbf1`
Pre-write Matrix294: `c074b4cd0147d5085e7f03cb3a5072afb3620b4c`
Prerequisite: Lease293 CLOSED / EXECUTION-VERIFIED / RESUME-SAFE.

## Identity decision

- RETAIN unchanged: `Memory/Engineering_Journal/EJR-245_2026-08-15_P64_SESSION_CLOSURE.md`.
- DISPLACE from EJR-245: `EJR/EJR-245_2026-08-17_M1_MULTI_CHANNEL_VERIFICATION.md`.
- RESERVED successor: `EJR-422`, proven complete-history VACANT by run `33402344919`, artifact `9761723214`, digest `sha256:f584fccd977b27da606a9f1bf464c17e512f460d4aaaef8bb0ed87b39a10e7ba`.

## Authorized execution

Perform one atomic Git tree mutation that removes the displaced root EJR-245 path and creates `EJR/EJR-422_2026-08-17_M1_MULTI_CHANNEL_VERIFICATION.md`. Only the first H1 identity token may change from EJR-245 to EJR-422; the remaining content must be preserved exactly. Memory EJR-245 must remain untouched.

Cohort baseline normalization is forbidden inside Repair294. Any deterministic count drift requires separate Lease295 after exact artifact inspection.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
