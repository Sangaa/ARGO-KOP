# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-248

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Scope: Deterministic MEMORY_TO_ROOT cohort baseline reconciliation after Repair247 only.

Repair247 preserved baseline 28 and its exact-head Internal-ID failed only at the deterministic MEMORY_TO_ROOT census. Artifact `9747775478`, digest `sha256:d2e8aabcfef6ea933828eefb55b2a5e7054b25caf149778d8ed6c3e8b6229c75`, proved expected=28, observed=27, history complete, and incomplete only `__COHORT_COUNT_DRIFT__`.

Successor prewrite: `ace4b03855ca0c5593d7feafeeade0dafe211042`.
Functional successor: `128664d8b6998ff6184eda0f5ad518879d6e0016`.
Compare proved one modified file with one addition and one deletion: only `EXPECTED_GROUP_COUNT = 28` → `27`.

Exact functional-head verification:
- Internal-ID `33364577371`: SUCCESS
- Full-Stack `33364577312`: SUCCESS
- Runtime `33364577338`: SUCCESS
- M2 `33364577305`: SUCCESS
- Real Mutation Matrix: NOT APPLICABLE to the census-only diff.

Final census artifact `9747836287`, digest `sha256:2d904d30cbe4a97e8f186ee1a03ad2d1d5292b0f4ecca5a15f716e895efa3e58`, proved expected=27, observed=27, history_complete=true, history_scope=all locally reachable refs, classification_complete=true, decision=CENSUSED, incomplete_group_ids=[].

Current governed MEMORY_TO_ROOT baseline is 27. Priority 2 remains OPEN; Global Integrity remains HOLD.
