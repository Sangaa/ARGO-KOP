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
| C02 | Runtime/Execution/run010_handoff_contract.py | ADD | pure execution and authorization provenance handoff builder | Y | Y |
| C03 | Runtime/Execution/run010_srv009_observation.py | ADD | isolated observable RUN-010 to SRV-009 composition using existing adapter | Y | Y |
| C04 | Quality/Integration/test_eng006_srv009_production_adapter.py | MODIFY | preserve adapter regressions and fail closed without authorization identity | Y | Y |
| C05 | Quality/Integration/test_run010_eng006_handoff_contract.py | MODIFY | update existing candidate consumer for explicit authorization identity | Y | Y |
| C06 | Quality/Integration/test_rel009_run010_srv009_observation.py | ADD | positive attributable dispatch observation plus negative authorization controls | Y | Y |
| C07 | .github/workflows/p3-runtime-github-e2e.yml | MODIFY | keep real connector E2E compatible with authorization identity contract | Y | Y |

## Preservation Controls

KEEP all unrelated main content unchanged.

KEEP `Runtime/Execution/connected_spine_runner.py` unchanged; its normal path remains simulation-only.

KEEP the existing governed `Tools/GOVERNED_WRITE_DISPATCH.py`, connector implementation, relationship registry and canonical authority unchanged.

Do not import the alternate `run010_eng006_srv009_consumer.py` from historical PR #64 because it duplicates lower-level connector dispatch rather than composing the existing governed adapter.

Unexpected Changes: NONE OBSERVED.

## Post-Commit Reconciliation

Functional commit: `5ba50b88d77de4ff15273d16d13da472e25c0f2f`.

Post-commit read-back was completed for all seven target paths. Direct compare against base `09b216e403fe99a6f1a4a35e3c3038831398f6a3` reports:

- status: `ahead`
- ahead by: `1`
- behind by: `0`
- exactly eight changed files: the seven declared targets plus this mutation matrix.

No unexpected path was observed.

## Verification Contract

Exact-head governed CI is still required through a pull-request observation surface. The REL-009 observation test must prove:

1. originating runtime reference is RUN-010;
2. explicit target is SRV-009;
3. callable boundary is observable;
4. downstream dispatch trace is attributable to the same execution context;
5. authorization identity and source provenance are preserved;
6. repository side effects are controlled by an in-memory connector in the integration test;
7. post-write read-back is verified;
8. no canonical promotion is inferred from PASS.

## Promotion Boundary

`SOURCE/APPLICATION != CI VERIFICATION != RELATIONSHIP PROMOTION`.

Read-back verification is complete. CI verification and promotion review remain separate gates.

Until exact-head CI and separate promotion review are complete:

`REL-009 = REVALIDATION REQUIRED`
