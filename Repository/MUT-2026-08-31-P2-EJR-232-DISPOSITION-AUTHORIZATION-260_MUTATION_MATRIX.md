# MUTATION MATRIX — EJR-232 DISPOSITION AUTHORIZATION 260

Status: CLOSED / AUTHORIZATION-VERIFIED / RESUME-SAFE
Transaction ID: MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260
Opening main: `6a73fd13f1559380bf537d5ba3a2b73d1d425f42`
Pre-write matrix commit: `1ec7f5350ce03a1119c00abcbac7fd192ec18cb6`
Authorization commit: `3a9b2518bb961c3e4454a1184aa70a4247a96cfb`
Target path: `Repository/MUT-2026-08-31-P2-EJR-232-DISPOSITION-AUTHORIZATION-260.md`
Target read-back blob: `4ef8904c6b2cffc7db3f4b09546c1827552942a9`

## Evidence and reconciliation

- Deterministic MEMORY_TO_ROOT baseline remained 25 throughout Lease260.
- EJR-232 remained a two-member ambiguity with distinct semantic bodies and zero external exact-ID / exact-member-path consumer obligations.
- Direct reads preserved the earlier Memory EJR-232 and later root EJR-232 byte-for-byte; Lease260 did not mutate either record.
- Path chronology remained: Memory allocation 2026-08-14 before root allocation 2026-08-17.
- The authorization retained the earlier Memory allocation and classified the later root allocation displaced.
- No replacement identity was selected or allocated.
- No consumer rewrite, H1 rewrite, rename, delete, move, Plan204 scope mutation, baseline mutation, or global promotion occurred.

## Mutation reconciliation

| Surface | Action | Expected state | Pre-write | Post-write |
|---|---|---|---|---|
| Memory EJR-232 | KEEP | Earlier allocation retained; no content/path/H1 change | VERIFIED | VERIFIED |
| Root EJR-232 | CLASSIFY ONLY | Later allocation classified displaced; no content/path/H1 change in Lease260 | VERIFIED | VERIFIED |
| Replacement identity | NONE | No number selected or allocated in Lease260 | VERIFIED | VERIFIED |
| Consumer rewrites | NONE | Zero direct obligations established; no rewrite in Lease260 | VERIFIED | VERIFIED |
| MEMORY_TO_ROOT baseline | KEEP | Remains 25 in Lease260 | VERIFIED | VERIFIED |
| Plan204 scope | KEEP | Original bounded scope is not silently expanded | VERIFIED | VERIFIED |
| Global integrity | KEEP | HOLD; no global PASS promotion | VERIFIED | VERIFIED |

## CI / integration evidence

Authorization commit `3a9b2518bb961c3e4454a1184aa70a4247a96cfb`:
- Full-Stack Repository Audit run `33370355523` / run number 2346: SUCCESS.
- ARGO Runtime Prototype and Integration Tests run `33370355516`: integrity, prototype, and integration jobs SUCCESS.
- Target authorization artifact was re-read from current main after write.

## Closure

`LEASE260 = CLOSED / AUTHORIZATION VERIFIED`

Priority 2 remains OPEN. Phase 1 remains OPEN. Global Integrity remains HOLD.

Next legal action: discover a candidate replacement identity and open a separate complete-history vacancy-proof lease. No candidate may be treated as vacant before that proof returns `VACANT`.
