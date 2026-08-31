# MUTATION MATRIX — EJR-235 DISPOSITION AUTHORIZATION 268

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-235-DISPOSITION-AUTHORIZATION-268
Opening main: `5110931da7780972b920a6bf35c211e204b04da7`
Pre-write commit: `1b696932ba9643402ec3442a4f462266c08402a3`
Authorization commit: `33d8b6dfebc09c186d3d773757fc7c75b3c10e7e`

| Surface | Before | Final disposition state |
|---|---|---|
| Memory EJR-235 | earlier allocation | RETAIN / identity owner |
| Root EJR-235 | later distinct allocation | DISPLACED / replacement required |
| EJR/Memory file content | current | unchanged |
| Exact-ID consumers | zero in verified census | no rewrite |
| Exact-path consumers | zero in verified census | no rewrite |
| Replacement identity | unselected | unselected |
| Vacancy proof | not executed | separate successor required |
| MEMORY_TO_ROOT baseline | 23 | 23 |
| Global integrity | HOLD | HOLD |

Validation: Full-Stack #2380 / `33376982878` SUCCESS for pre-write Matrix; Full-Stack #2381 / `33377042503` SUCCESS for authorization record.

Lease268 is disposition-only. No identity mutation or vacancy claim occurred.