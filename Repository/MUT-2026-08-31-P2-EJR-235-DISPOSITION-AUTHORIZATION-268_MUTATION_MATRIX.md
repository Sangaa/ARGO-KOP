# MUTATION MATRIX — EJR-235 DISPOSITION AUTHORIZATION 268

Status: PREWRITE / DISPOSITION PENDING
Transaction ID: MUT-2026-08-31-P2-EJR-235-DISPOSITION-AUTHORIZATION-268
Opening main: `5110931da7780972b920a6bf35c211e204b04da7`

## Current evidence

The execution-verified Lease267 MEMORY_TO_ROOT census reports EJR-235 as a two-member `MEMORY_EJR → ROOT_EJR` group with distinct content, `external_exact_id_reference_count=0`, and zero exact member-path references.

Direct current-main readbacks establish:
- Memory member: `Memory/Engineering_Journal/EJR-235_2026-08-14_P53_SESSION_CLOSURE.md`, blob `28216a14168c44875273f7edd5747dfd54e92f3d`.
- Root member: `EJR/EJR-235_2026-08-17_GOV-015_FIXTURE_TEST_FIELD_VALIDATION.md`, blob `a326b6195ecd66b26d8b379706c8965e78bde153`.

Direct path history establishes the Memory allocation at `7b7daffe7605950d3826975322236e7eca075574` on 2026-08-14T21:10:02Z, before the root allocation at `9a3d2e314662cff7f9e7d6586c40bc6dc53f06ff` on 2026-08-17T16:26:49Z.

## Authorized disposition-only scope

| Surface | Current state | Authorized disposition state |
|---|---|---|
| Memory EJR-235 | earlier allocation | RETAIN / identity owner |
| Root EJR-235 | later distinct allocation | DISPLACED / replacement identity required |
| EJR/Memory file content | current | unchanged |
| Exact-ID consumers | zero in verified census | no rewrite |
| Exact-path consumers | zero in verified census | no rewrite |
| Replacement identity | unselected | remains unselected |
| Vacancy proof | not executed | separate successor lease required |
| MEMORY_TO_ROOT baseline | 23 | unchanged |
| Global integrity | HOLD | HOLD |

This lease authorizes classification only. It does not authorize rename, replacement-number allocation, content mutation, consumer rewrite, census-baseline change, or Global Integrity promotion.

Priority 2 remains OPEN. Phase 1 remains OPEN.