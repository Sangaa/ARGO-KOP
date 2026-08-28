# REL-009 CLEAN OBSERVATION MUTATION MATRIX

Transaction ID: `MUT-2026-08-28-P3-REL009-CLEAN-001`
Protocol: GOV-014
Base: `main@09b216e403fe99a6f1a4a35e3c3038831398f6a3`
Scope: isolated P3 REL-009 observation candidate only

## Boundary

This transaction extracts only the dependency-closed observation seam needed to test the current P374 evidence contract. It does not copy PR #63 or PR #64 wholesale, does not promote REL-009, and does not enable production side effects in the normal connected spine.

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|---|---|
| C01 | Services/ENG006_SRV009_PRODUCTION_ADAPTER.py | MODIFY | require explicit authorization identity before governed dispatch | Y | Y |
| C02 | Runtime/Execution/run010_handoff_contract.py | ADD | pure execution and authorization provenance handoff builder with no SRV-009 literal or dispatch | Y | Y |
| C03 | Quality/Integration/rel009_run010_srv009_observation.py | ADD | isolated integration-only observable RUN-010 to SRV-009 composition using existing governed adapter | Y | Y |
| C04 | Quality/Integration/test_eng006_srv009_production_adapter.py | MODIFY | preserve adapter regressions and fail closed without authorization identity | Y | Y |
| C05 | Quality/Integration/test_run010_eng006_handoff_contract.py | MODIFY | update existing candidate consumer for explicit authorization identity | Y | Y |
| C06 | Quality/Integration/test_rel009_run010_srv009_observation.py | MODIFY | positive attributable dispatch observation plus negative authorization controls against integration helper | Y | Y |
| C07 | .github/workflows/p3-runtime-github-e2e.yml | MODIFY | keep real connector E2E compatible with authorization identity contract | Y | Y |
| C08 | Runtime/Execution/run010_srv009_observation.py | DELETE | remove initial observation helper from protected Runtime/Execution scope after integrity gate rejection | Y | Y |

## Preservation Controls

KEEP all unrelated main content unchanged.

KEEP `Runtime/Execution/connected_spine_runner.py` unchanged; its normal path remains simulation-only.

KEEP `Quality/Integrity/test_rel009_negative_executable_consumer_boundary.py` unchanged. Its existing rule that Runtime/Execution Python must not contain the `SRV-009` literal remains intact.

KEEP the existing governed `Tools/GOVERNED_WRITE_DISPATCH.py`, connector implementation, relationship registry and canonical authority unchanged.

Do not import the alternate `run010_eng006_srv009_consumer.py` from historical PR #64 because it duplicates lower-level connector dispatch rather than composing the existing governed adapter.

Unexpected Changes: NONE OBSERVED.

## Exact-Head CI Finding and Correction

Initial clean-candidate head `c83683e3262412dc7015a62bae94389dfef6b020` produced:

- Full-Stack Repository Audit: PASS.
- Runtime Prototype job: PASS.
- Integration job: PASS.
- Integrity job: FAIL.

The integrity failure was specific and deterministic: `Quality/Integrity/test_rel009_negative_executable_consumer_boundary.py` found the literal `SRV-009` in `Runtime/Execution/run010_srv009_observation.py`.

This is classified as:

`NEW EVIDENCE SEAM PLACED IN PROTECTED RUNTIME SCOPE / EXISTING INTEGRITY RULE CORRECT / DESIGN LOCATION CORRECTED`.

The guard was not weakened or exempted. The evidence helper was relocated to `Quality/Integration`, while Runtime/Execution retains only the pure handoff contract and the normal connected spine remains simulation-only.

## Post-Commit Reconciliation

Original functional commit: `5ba50b88d77de4ff15273d16d13da472e25c0f2f`.
Original read-back closure commit: `c83683e3262412dc7015a62bae94389dfef6b020`.
Integrity-boundary correction commit: `180b4c89ee51ff93f0f2ba1043bdcbccd511865b`.

Correction read-back established:

- `Quality/Integration/rel009_run010_srv009_observation.py` exists with the intended integration-only composition seam;
- `Quality/Integration/test_rel009_run010_srv009_observation.py` imports the relocated helper;
- `Runtime/Execution/run010_srv009_observation.py` is absent at the correction commit;
- compare against base remains `ahead`, with no behind commits and exactly eight final changed files;
- no unexpected path is present in the final diff.

Therefore C03/C06/C08 are read-back verified. This read-back does not substitute for exact-head CI.

## Verification Contract

Exact-head governed CI is required through the existing pull-request observation surface. The REL-009 observation test must prove:

1. originating runtime reference is RUN-010;
2. explicit target is SRV-009;
3. callable boundary is observable;
4. downstream dispatch trace is attributable to the same execution context;
5. authorization identity and source provenance are preserved;
6. repository side effects are controlled by an in-memory connector in the integration test;
7. post-write read-back is verified;
8. Runtime/Execution negative consumer guard remains PASS;
9. no canonical promotion is inferred from PASS.

## Promotion Boundary

`SOURCE/APPLICATION != READ-BACK != CI VERIFICATION != RELATIONSHIP PROMOTION`.

Read-back is complete. Exact-head CI and separate promotion review remain required.

Until those gates are complete:

`REL-009 = REVALIDATION REQUIRED`
