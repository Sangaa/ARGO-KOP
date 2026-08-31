# MUTATION MATRIX — EJR-245 DISPOSITION + EJR-422 VACANCY PROOF 293

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-245-DISPOSITION-AND-422-VACANCY-PROOF-293
Opening main: `6e00c2a0ca138918ae7c2c9bf02fd97da8f57f41`
Execution role: HERMUZ

## Established disposition

Memory EJR-245 allocation commit `99e8d80c033da324f0e20dcd2b521cf7d0603d88` predates root EJR-245 allocation commit `499e90d71a6daadc124b6709910842e24b521795`. Both records are legitimate and distinct. Under the first-valid historical allocation rule, Memory EJR-245 is RETAINED and root EJR-245 is DISPLACED legitimate content.

## Vacancy proof

Dedicated workflow `EJR Replacement Vacancy Proof 293`, run `33402344919`, completed SUCCESS using complete checkout history and the existing fail-closed vacancy gate.
Artifact `9761723214`, digest `sha256:f584fccd977b27da606a9f1bf464c17e512f460d4aaaef8bb0ed87b39a10e7ba`, proves `EJR-422` has current_claims=[], historical_claims=[], history_complete=true, decision=VACANT.

Proof-head Full-Stack run `33402344855`: SUCCESS.

EJR-422 is reserved solely for displaced root EJR-245. No identity repair was executed under Matrix293.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
