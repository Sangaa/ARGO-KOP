# Mutation Matrix 303 — EJR-218 to EJR-425 Identity Repair

Status: OPEN / PRE-MUTATION
Date: 2026-08-31

Prerequisite Lease302: vacancy proof for EJR-425 = VACANT, history_complete=true; proof workflow and Full-Stack SUCCESS on head `75389550390e0412eb46456e4c7d185fd87baa16`.

| Surface | Mutation | Preservation |
|---|---|---|
| Memory/Engineering_Journal/EJR-218_2026-08-14_P35_SESSION_CLOSURE.md | none | EJR-218 retained unchanged |
| EJR/EJR-218_CURRENT_BUILD_RECONCILIATION_2026-08-17.md | remove old root path | content preserved into successor |
| EJR/EJR-425_CURRENT_BUILD_RECONCILIATION_2026-08-17.md | create successor | same body, H1 identity changed to EJR-425 |

Execution rule: source deletion and successor creation MUST occur in one Git tree/commit. No historical narrative references are rewritten cosmetically.

Expected validation: Full-Stack success; Internal-ID may fail only on deterministic cohort count drift 12→11, which must be normalized under a separate lease if proven.

Global Integrity remains HOLD.
