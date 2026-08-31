# MUT-2026-08-31-P2-EJR-173-DISPOSITION-AUTHORIZATION-230

Status: CLOSED / DISPOSITION-VERIFIED / RESUME-SAFE
Scope: one candidate group `EJR-173`

## Evidence and decision
Independent re-entry from Checkpoint229 recomputed the current MEMORY_TO_ROOT cohort rather than assuming the prior repair list was exhaustive. EJR-173 was selected as a bounded one-Memory/one-root group with zero exact-ID and zero exact-path consumers in the deterministic census.

Chronology:
- retained allocation candidate: `Memory/Engineering_Journal/EJR-173_2026-08-13_REP020_MATRIX_EXPANSION.md`, first path commit `f3c93ad327d79b7fd18061f313ea536e13796ad5` on 2026-08-13;
- displaced candidate: `EJR/EJR-173_2026-08-14_CURRENT_MAIN_REVALIDATION_HANDOFF.md`, first path commit `448822fdda4e630309811d4354fc2192c3e8ff14` on 2026-08-14.

Plan204 was bounded to its original five groups, while Stratification184 classified Memory+root reuse as a traceability conflict requiring provenance-aware review rather than auto-repair. Applying the already-proven first-valid-allocation rule to this newly inspected group, with no stronger evidence invalidating the earlier Memory allocation, retained Memory EJR-173 and classified the later root record as displaced.

Lease230 authorized only a separate replacement-vacancy proof and subsequent one-record repair after verified VACANT evidence.

## Preserved tool-sequencing incident
During prewrite sequencing an erroneous same-content Contents API update was issued to `Quality/Integration/ejr_memory_to_root_provenance_census.py` with commit message `noop`. GitHub created commit `fac71011336b11ae782b241b96867fae012f336b`, but its tree remained exactly `4cb5ef93276ccb820e1dd235e53a1e0831de6599`, identical to Checkpoint229. Therefore it was an unintended empty commit, not a content mutation.

The history was not rewritten. Lease230 was recreated on top of the live no-op commit and proceeded by non-force fast-forward. Learning: never use a same-content Contents API write as a state probe; same content may still create an empty commit. Prewrite state must be established by read/recheck plus explicit commit/ref sequencing.
