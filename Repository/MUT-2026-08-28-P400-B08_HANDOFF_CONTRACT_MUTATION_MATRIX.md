# MUTATION MATRIX — P400 B08 HANDOFF CONTRACT

Transaction ID: `MUT-2026-08-28-P400`
Protocol: `GOV-013`
Scope: isolated B08 handoff-contract seam only.

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| P400-001 | `Runtime/Execution/run010_handoff_contract.py` | ADD | Pure governed RUN-010 handoff contract; no I/O; no dispatch; identity/authorization/provenance checks only. | Y | N |
| P400-002 | `Runtime/Execution/test_run010_handoff_contract.py` | ADD | Focused regression coverage for identity preservation, authorization rejection, missing provenance, and trace identity mismatch. | Y | N |

## KEEP REQUIREMENT

All other repository content is `KEEP`. In particular:
- `main` / canonical authority remains unchanged.
- `connected_spine_runner.py` remains simulation-only.
- `execution_entrypoint.py` remains non-authoritative for production dispatch.
- No provider or production side effect is authorized by this transaction.

## Execution Evidence

- P400 was introduced as an isolated contract seam after the P399 construction gate.
- Exact-head CI execution is required before behavioral closure.
- Absence of execution evidence must remain `NO RUN`, never PASS.

## Closure

`TRANSACTION = CONTROLLED`
`PROMOTION = NOT AUTHORIZED`
