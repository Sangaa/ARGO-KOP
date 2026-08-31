# MUT-2026-08-31-P2-EJR-MEMORY-TO-ROOT-COHORT-BASELINE-228

Status: CLOSED / EXECUTION-VERIFIED / RESUME-SAFE
Baseline repair head: `a7434269d28c2f4bf5510497091291a2579feb74`
Prewrite: `2413ec8a164a1551e82043398bef3953f3f9cef2`
Functional baseline head: `1972ebe9fd5b32e3eaf5703866e671d697e27975`
Triggering repair: Lease227, final displaced root EJR-302 → EJR-405

## Evidence that authorized this successor
Repair-head Internal-ID `33359946109` failed only on the memory-to-root census after all preceding tests/analyzers passed. Artifact `9746355744`, digest `sha256:5cf5e30dc15fbd91dadddf810bb102e352ece47e99d4a9b2572435ef6ef05c51`, proved complete deterministic cohort drift expected=32→observed=31 after EJR-302 ceased to have a root ambiguity.

## Executed mutation
Only `Quality/Integration/ejr_memory_to_root_provenance_census.py` changed:
`EXPECTED_GROUP_COUNT = 32` → `EXPECTED_GROUP_COUNT = 31`.
Compare prewrite→functional head proved exactly one modified file, one addition and one deletion. No classifier logic, tests, workflows, EJR, GOV, REP, Memory, or repair-history mutation occurred.

## Exact-head verification
At `1972ebe…`:
- Internal Document-ID Audit `33360190075`: SUCCESS.
- Full-Stack Repository Audit `33360190109`: SUCCESS.
- Runtime Prototype and Integration Tests `33360190080`: SUCCESS.
- M2 Multi-Channel Proposal Training `33360190147`: SUCCESS.
- Real Mutation Matrix: NOT APPLICABLE; the census-only functional diff did not trigger its path filter, and no artificial change was introduced.

Deterministic census artifact `9746432334`, digest `sha256:de6ff87769bbc7b17dc5d7e8dcba032c5e69582bd09273ee68b73990d27caef8`, proved expected=31, observed=31, history_complete=true, classification_complete=true, decision=CENSUSED, incomplete=[].

## Learning
A repair that removes the final root member behind a Memory→Root ambiguity removes that ID from the classifier cohort; a prior repair of one of multiple roots may leave cohort cardinality unchanged. Baseline movement therefore follows observed classifier state, never a mechanical per-repair decrement rule.
