# MUT-2026-08-31-P2-EJR-236-TO-417-IDENTITY-REPAIR-279

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: one-record Priority-2 identity repair: displaced root EJR-236 → EJR-417.
Opening main: `b6a7050d5290e059580287c971671d6a84c33562`
Pre-write Matrix279: `8175e78547f144f2edaedc05c163297922732683`
Functional repair head: `84409b606d24c3a9d6ee5ad04efcff72116c2c57`

## Result

Retained `Memory/Engineering_Journal/EJR-236_2026-08-14_P54_SESSION_CLOSURE.md` unchanged. Renamed displaced root `EJR/EJR-236_2026-08-17_P4_REL009_CONSUMER_BOUNDARY_GATE.md` to `EJR/EJR-417_2026-08-17_P4_REL009_CONSUMER_BOUNDARY_GATE.md`, changing only the first H1 identity.

Exact compare from repair-open head `73738fe2221298cb4a7e4b60e52cb01015f56943` to functional head classifies one renamed file with additions=1, deletions=1. No exact old-member-path consumer required rewrite.

Repair-head Full-Stack #2436 / run `33386572852`: SUCCESS. Internal Document-ID Audit #69 proved the expected sole cohort-count drift 20→19 via artifact `9755813652`, digest `sha256:f16e386eec759e34757099271ab50f04dfca4d5c0b01bb008b2107b04ff2fad2`.

Separate Lease280 normalized the deterministic baseline and then passed Full-Stack #2439 and Internal Document-ID #70 with final 19/19 CENSUSED evidence.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
