# REP-002 SECTION MATRIX — TRANSACTION 001

Transaction ID: `MUT-2026-08-17-REP002-001`
Source: `Repository/REP-002_REPOSITORY_MAP.md`
Source Blob SHA: `386308c528cdb80c48b2aad7208753e864728a1f`

| Seq | Section | Action | Intent |
|---:|---|---|---|
| 1 | `4. Repository Layer` | UPDATE | Add canonical `REP-004`, `REP-005`, `REP-007`, `REP-008` paths to physical map. |
| 2 | `5. Governance Layer` | UPDATE | Add canonical `GOV-014` path to physical map. |
| 3–20 | All remaining sections | KEEP | Preserve byte/content-equivalent state. |
| P290/P357 | Historical reconciliation sections | KEEP | Preserve prior reconciliation evidence. |

## Preconditions

- SOURCE_READ_COMPLETE = Y
- TARGET_SECTION_COUNT = 2
- UNAUTHORIZED_MUTATION_SECTIONS = 0
- MATRIX_STAGE_ONLY = Y
