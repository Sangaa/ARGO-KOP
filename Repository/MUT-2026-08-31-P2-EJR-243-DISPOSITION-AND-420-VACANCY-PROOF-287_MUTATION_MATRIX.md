# MUTATION MATRIX — EJR-243 DISPOSITION + EJR-420 VACANCY PROOF 287

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-243-DISPOSITION-AND-420-VACANCY-PROOF-287
Opening main: `bd0ba60c65c957a90026b390513d0c40be329ea6`
Execution role: HERMUZ

## Established disposition

Memory EJR-243 allocation commit `3b4853da0da0e21891b59ad21625f1ed7460396e` predates root EJR-243 allocation commit `7fbe379e0960499a13e381d2b3d9dca8bec78c8c`. Both records are legitimate and distinct. Under the first-valid historical allocation rule, Memory EJR-243 is RETAINED and root EJR-243 is DISPLACED legitimate content.

## Vacancy proof

Dedicated workflow `EJR Replacement Vacancy Proof 287`, run `33394503875`, completed SUCCESS using complete checkout history and the existing fail-closed vacancy gate.
Artifact `9758767482`, digest `sha256:fb3f6e3047c63c0db05f655a201d168157bdb9e10c32c6e30f0d151ddd7cf22c`, proves `EJR-420` has current_claims=[], historical_claims=[], history_complete=true, decision=VACANT.

Proof-head Full-Stack run `33394503789`: SUCCESS.

EJR-420 is reserved solely for displaced root EJR-243. No identity repair was executed under Matrix287.

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.
