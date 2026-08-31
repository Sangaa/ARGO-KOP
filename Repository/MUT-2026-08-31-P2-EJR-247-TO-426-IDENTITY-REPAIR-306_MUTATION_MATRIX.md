# Mutation Matrix — Lease 306 — EJR-247 → EJR-426 Identity Repair

Status: CLOSED / VALIDATED
Date: 2026-08-31

## Executed Mutation

| Surface | Result |
|---|---|
| old root EJR-247 | removed atomically |
| successor root EJR-426 | created atomically |
| Memory EJR-247 | preserved unchanged |

Atomic repair commit: `957b2b710c821d48cbf285b9e0c1d4b739c4fa2a`.
Successor vacancy was pre-proven under Lease305.

## Validation

- old root read-back: 404;
- successor blob: `1c7fc2ea333a515cf8191b992a9797b4d6b75454`;
- preserved Memory blob: `57e7928eed5ff4c3dd7d1e2583f9544571349276`;
- Full-Stack `33413681805`: SUCCESS;
- only deterministic follow-up was cohort baseline drift 11 → 10.

No Runtime/Core/Governance semantic mutation. Closed with baseline normalization delegated to Lease307.
