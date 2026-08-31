# MUT-2026-08-31-P2-EJR-208-TO-407-IDENTITY-REPAIR-237

Status: CLOSED / SUCCESSOR-VERIFIED / ONE-RECORD REPAIR / RESUME-SAFE
Scope: one displaced root record only, EJR-208 → EJR-407.
Authority: Lease235 disposition + Lease236 complete-history VACANT proof.

Functional head: `070d11f6e4f8b19815485dabbf384d144c87802d`.

Mutation:
- retained `Memory/Engineering_Journal/EJR-208_2026-08-14_P26_SESSION_CLOSURE.md` unchanged;
- replaced only `EJR/EJR-208_P2_REL003_CONTROLLED_MUTATION_PREPARATION_2026-08-17.md` with `EJR/EJR-407_P2_REL003_CONTROLLED_MUTATION_PREPARATION_2026-08-17.md`;
- preserved semantic body/chronology and changed only identity/H1/path;
- no consumer rewrites were required because deterministic pre-repair evidence showed zero exact-ID and zero exact-path consumers;
- census baseline remained 30 inside this repair.

Compare from prewrite `2f104f4429f57b7377c76867980ab7f6b8ee904f` to functional head proved exactly one renamed file with one addition/one deletion.

Repair-head verification:
- M2 `33361956427`: SUCCESS;
- Full-Stack `33361956462`: SUCCESS;
- Internal-ID `33361956415`: FAILURE, preserved as evidence;
- Runtime and Real Mutation Matrix: NOT APPLICABLE / no run triggered for this EJR-only functional diff.

Internal-ID failed only at the MEMORY_TO_ROOT census after all preceding audit/chronology/lineage/provenance steps passed. Artifact `9746992753`, digest `sha256:fd28f7ed37dd863da865a98744545c116c79cdfb8b6dd8869151b4b9b7a1f4f4`, proved expected=30, observed=29, history_complete=true, decision=PARTIAL solely for `__COHORT_COUNT_DRIFT__`, with EJR-208/EJR-407 absent from the remaining cohort.

Lease238 separately rebaselined 30→29 and successor-verified the repair. No repair-head failure was rewritten or suppressed.
