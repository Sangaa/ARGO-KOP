# P10 Runtime — Gate 15 Execution Authority Hardening — Transaction L

Transaction ID: `MUT-2026-09-03-P10-GATE15-EXECUTION-AUTHORITY-L`
Priority: `10 — Runtime`
Gate: `15 — Runtime ↔ Engine executable boundary`
State: `CLOSED / VERIFIED / RESUME-SAFE`
Entry HEAD: `16d2efca91d1f7507cc23474c23a284002684dd5`
Pre-write HEAD: `78fb6a597b6492316ffeb449d749319ecfdc869b`
Initial Material HEAD: `5d94dfc26bf886b36d04ea75b92f60937707add0`
First Status Repair HEAD: `a5c2ea19ff85de2decd94b0eb6b6e19728179d99`
Authority-Baseline Repair HEAD: `d6ef08f5879606642db761e653e9101d67853235`
Final Status Compatibility HEAD: `0c9797bb36e71ca76bd055ff3768e25f6fff006a`
Final Exact-Head Validation HEAD: `c32b8de1a55798f82612f6b0a17a69ed0868005f`
Material Stale-Consumer Repair HEAD: `bd2daf831fbff70c82d4c5f76a831aa8143cea2c`
Protocol: `PROJECT_BOOTSTRAP / CORE-003 / GOV-013 / GOV-014 / GOV-014A / GOV-016 / ENG-006 / RUN-013 / RUN-015 / Runtime Execution contracts / REP-011 / REP-016`

## Independently verified tracked defects

1. `Runtime/Execution/execution_entrypoint.py` accepted authorization through Python truthiness despite declaring `authorized: bool`; truthy non-booleans could cross as implicit authorization.
2. Current execution contracts require a valid `authorization_id`, but `Runtime/Execution/mock_executor.py` did not reject a ready/not-started plan with missing authorization identity.

Classification: `REAL TRACKED GATE-15 AUTHORIZATION BOUNDARY DEFECTS / MATERIAL REPAIR APPLIED`.

## Required semantic boundary

`INVALID AUTHORIZATION TYPE OR IDENTITY OR PLAN/EXECUTION STATE` → `FAIL CLOSED / BLOCKED / NO EXECUTION HANDOFF`.

Preserved:
- RUN-013 controlled handoff remains `READY_FOR_CONTROLLED_HANDOFF`/`HOLD` only and never returns `EXECUTED`;
- mock execution remains `SIMULATED / SIMULATED_ONLY / side_effect=false`;
- no external API/email/production mutation or irreversible side effect is authorized;
- provider authenticity and availability remain independent Gate-13/external-trust holds;
- no candidate Runtime contract is promoted merely by passing local tests.

## Authorized bounded surface

| Change ID | Target | Action | Purpose | Pre-write | Post-write |
|---|---|---|---|:---:|:---:|
| P10-L-01 | `Runtime/Execution/execution_entrypoint.py` | UPDATE | exact boolean authorization + stable identities | PASS | PASS |
| P10-L-02 | `Runtime/Execution/test_execution_entrypoint.py` | UPDATE | negative authorization/identity coverage | PASS | PASS |
| P10-L-03 | `Runtime/Execution/mock_executor.py` | UPDATE | enforce authorization identity | PASS | PASS |
| P10-L-04 | `Runtime/Execution/test_mock_executor_authorization_boundary.py` | UPDATE | missing/blank auth rejection | PASS | PASS |
| P10-L-05 | `Runtime/_FOLDER_STATUS.md` | UPDATE | additive L evidence while preserving all protected authority wording | PASS | PASS |
| P10-L-06 | `Quality/Integrity/test_runtime_p10_gate15_execution_authority.py` | CREATE | bind semantics and independent holds | PASS | PASS |
| P10-L-07 | `Repository/REP-011_PRIORITY10_RUNTIME_GATE15_EXECUTION_AUTHORITY_ADDENDUM_2026-09-03_L.md` | CREATE | bounded evidence/non-claims | PASS | PASS |
| P10-L-08 | this Matrix | UPDATE | material/CI/closure evidence | PASS | PASS |

## Preserved exact-head failures

Initial material HEAD `5d94dfc26bf886b36d04ea75b92f60937707add0` produced Runtime integrity `178 passed / 6 failed`; prototype tests passed. All six failures were status-consumer regressions caused by replacing protected prior authority wording. No new execution semantic test failed.

First status-repair HEAD `a5c2ea19ff85de2decd94b0eb6b6e19728179d99` improved the result to `179 passed / 5 failed` but still omitted five protected K-era phrases. Again no execution semantic test failed.

Authority-baseline repair HEAD `d6ef08f5879606642db761e653e9101d67853235` restored the last exact known-green pre-L status and reduced the result to `182 passed / 2 failed`. The remaining two failures were compatibility-only: the K-era Gate-15 next pointer and the exact L material marker. No execution semantic test failed.

Final status compatibility HEAD `0c9797bb36e71ca76bd055ff3768e25f6fff006a` adds those two phrases without removing or weakening any prior invariant. Because that status-only commit triggers only a subset of workflow path filters, this Matrix update intentionally creates one final exact head on which all four required workflow families can run.

Tests were never weakened. No Services/provider adapter, credentials, Interfaces implementation, or unrelated Runtime files changed.

## Final exact-head failure classification and repair authorization

Runtime workflow run `33755053512`, failing job `100647374091`, is preserved as the final exact-head failure evidence for `c32b8de1a55798f82612f6b0a17a69ed0868005f`: `3 failed / 582 passed / 11 subtests passed`. The three failures are limited to two tracked integration consumers that still require the superseded pre-L rejection strings `EXECUTION_NOT_AUTHORIZED` and `SOURCE_TRACE_REQUIRED`.

Direct source, unit-test, ENG-006, RUN-013 and Transaction-L review confirms that the current safety invariant is the stricter L boundary: authorization must be exact boolean `True`, and every execution identity must be a stable nonblank string. The source is semantically correct; the failing consumers preserve fail-closed behavior but pin obsolete diagnostic wording.

Primary classification: `STALE_CONSUMER`.

Authorized bounded repair:

| Change ID | Target | Action | Expected change | KEEP requirements | Pre-write | Post-write |
|---|---|---|---|---|:---:|:---:|
| P10-L-09 | `Quality/Integration/test_authorization_to_execution_canonical_seam_certification.py` | UPDATE | require the current explicit-authorization rejection code | unauthorized execution remains blocked; exception type unchanged; no source/status mutation | PASS | PASS |
| P10-L-10 | `Quality/Integration/test_run010_eng006_handoff_contract.py` | UPDATE | require current explicit-authorization and stable-identity rejection codes | missing trace and unauthorized execution remain fail-closed; successful handoff assertions unchanged | PASS | PASS |
| P10-L-11 | this Matrix | UPDATE | bind repair/read-back/test/exact-head evidence | retain all prior failure evidence and non-claims | PASS | PASS |

This authorization does not permit another `Runtime/_FOLDER_STATUS.md` mutation, Runtime source relaxation, exception swallowing, provider claim or executable promotion. The repair must change diagnostic expectations only and then rerun the targeted tests plus all four exact-head workflow families.

Immutable local read-back confirmed that only the three obsolete exact-string expectations changed. Targeted Gate-15 tests passed `32/32`; the integration suite under the tracked workflow `PYTHONPATH` passed `585/585` with `11` subtests and one existing audit warning. At that pre-verification point exact-head workflow evidence remained pending and Gate 15 remained open; the final evidence below supersedes only that disposition, not the preserved checkpoint.

Final material exact-head evidence: Full-Stack `33776295695` — SUCCESS; Runtime `33776295841` — SUCCESS; M2 `33776295756` — SUCCESS; Real Matrix `33776295741` — SUCCESS. Exact compare contains only P10-L-09..11. `GATE 15 = BOUNDED CLOSED FOR THE TRACKED SIDE-EFFECT-FREE AUTHORIZATION / IDENTITY EXECUTION SEAM`; provider/production execution and candidate/canonical executable promotion remain unclaimed.

Validation:
`pre-write → bounded hardening → immutable read-back → preserved CI failures → authority-baseline restoration → additive compatibility repair → exact-head four workflow families → classify Gate15 close/hold Resume-Safe`.
