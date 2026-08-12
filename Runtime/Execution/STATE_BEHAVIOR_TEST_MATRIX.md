# Connected Spine — State Behavior Test Matrix

| Scenario | Expected state | Decision | Authorization | Execution |
|---|---|---:|---:|---:|
| Clean context | SIMULATED | allowed | governed | simulated |
| Current/history conflict | HOLD | blocked | blocked | blocked |
| Unrelated historical evidence | SIMULATED | allowed | governed | simulated |

## Interpretation

The same execution spine must change behavior according to cognition state while preserving the independent authorization and execution gates.

A clean context does not bypass authorization. A cognition hold blocks downstream progression. Historical evidence that does not conflict with the current fact set does not itself trigger a hold.
