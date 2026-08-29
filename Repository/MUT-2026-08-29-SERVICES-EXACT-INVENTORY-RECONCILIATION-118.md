# MUT-2026-08-29-SERVICES-EXACT-INVENTORY-RECONCILIATION-118

Date: 2026-08-29
Lease: `R71-20260829-SERVICES-INVENTORY-118`
Baseline: `main@c6c83d21d7321f23ea94b2951b0b72a988382147`
Protocol: `PROJECT_BOOTSTRAP + GOV-013 + GOV-014 + GOV-013A`
Status: `PREWRITE / NOT CLOSED`

## Evidence

Exact Services Git tree `94088ae4ae54699ae267a32dda033463591573c8` returned `truncated:false` and 20 file entries.

Current `Services/_FOLDER_STATUS.md` correctly keeps the domain on Integrity Hold but its physical inventory sentence lists only `SRV-001..010 + README + status`, omitting eight current implementation/connector surfaces.

## Authorized change

1. update `Services/_FOLDER_STATUS.md` to distinguish the 10-document SRV catalog from the exact current 20-file physical tree;
2. add a regression checking the exact inventory set and the distinction `catalog != physical tree`;
3. finalize this Matrix in the same protected change set.

## Forbidden expansion

No service is promoted by physical presence. No Runtime, connector-authentication, provider-authentication, REP-001/002, SRV contract, or executable relationship claim may be widened.

## Verification

`PREWRITE → STATUS + TEST + FINALIZED MATRIX SAME CHANGE SET → READ-BACK → EXACT-HEAD CI → CLOSE OR HOLD`.
