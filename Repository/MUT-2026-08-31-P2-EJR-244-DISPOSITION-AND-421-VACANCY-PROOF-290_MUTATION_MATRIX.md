# MUTATION MATRIX — EJR-244 DISPOSITION + EJR-421 VACANCY PROOF 290

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-244-DISPOSITION-AND-421-VACANCY-PROOF-290
Opening main: `34bade3b130d54f827dd4abea99d6c83d4132429`
Execution role: HERMUZ

## Established disposition

Memory EJR-244 allocation commit `82ccbdda485297ed8a206c5dad960ce44f076cbc` predates root EJR-244 allocation commit `1510161a687a336e8efa52b522ed8ea8aea942a4`. Both records are legitimate and distinct. Under the first-valid historical allocation rule, Memory EJR-244 is RETAINED and root EJR-244 is DISPLACED legitimate content.

## Vacancy proof

Dedicated workflow `EJR Replacement Vacancy Proof 290`, run `33396768282`, completed SUCCESS using complete checkout history and the existing fail-closed vacancy gate.
Artifact `9759617449`, digest `sha256:28a790a1c1bf3a3a4425602426ea3351be2f09c4c469add1e21723970a55d96c`, proves `EJR-421` has current_claims=[], historical_claims=[], history_complete=true, decision=VACANT.

Proof-head Full-Stack run `33396768304`: SUCCESS.

EJR-421 is reserved solely for displaced root EJR-244. No identity repair was executed under Matrix290.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
