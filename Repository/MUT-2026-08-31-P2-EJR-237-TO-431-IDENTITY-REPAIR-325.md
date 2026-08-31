# Repair 325 — Root EJR-237 → EJR-431 Identity Repair

Status: CLOSED / EXECUTION-VERIFIED / DRIFT-PRESERVED / RESUME-SAFE
Date: 2026-08-31

## Authorization
Lease323 explicitly retained the earlier Memory EJR-237 allocation and classified the later root EJR-237 as displaced. Lease324 complete-history run `33426371329` proved EJR-431 VACANT.

## First attempt and governance hold
Initial functional attempt `423170ca485bb8693b23fd1044d573b989e49c9f` had the intended bounded semantic diff, but Full-Stack run `33426813721` failed only at current-change Mutation Matrix enforcement because protected REP-020 changed while the pre-write Matrix existed only in the parent commit.

Classification: `SAME-CHANGE-SET GOVERNANCE BINDING DEFECT / NOT SEMANTIC REPAIR FAILURE`.

A controlled atomic rollback `0f7273e0b0fdbf155bdf693afa9f746ac186b5d3` restored the pre-attempt functional state while changing the Matrix in the rollback commit. Rollback verification passed:
- Full-Stack `33427024520`: SUCCESS, including current-change Matrix enforcement;
- Internal-ID `33427024464`: SUCCESS;
- Real Mutation Matrix `33427024471`: SUCCESS;
- Runtime/Integration `33427024517`: SUCCESS.

## Compliant functional mutation
Reexecution head `49680f1eddd29a4a18336261ae5aec594087d3a0` performed the same bounded repair with the Mutation Matrix included in the same atomic commit:
1. root `EJR-237` → `EJR-431`, changing first-H1 identity only;
2. EJR-418 live semantic references updated from EJR-237 to EJR-431;
3. REP-020 P322 negative-runtime evidence heading/reference updated from EJR-237 to EJR-431;
4. Memory EJR-237 preserved byte-for-byte.

Exact compare from rollback head proves only four changed paths: the root rename/H1, EJR-418, REP-020 P322, and the Repair325 Mutation Matrix.

## Verification
Full-Stack run `33427225861`: SUCCESS, including `Enforce Mutation Matrix on current change set`.
Runtime/Integration run `33427225759`: SUCCESS.
Memory EJR-237 retained blob `ff85f1270ebb4d30985f9bc9183bcc179ad43021`.

Internal-ID run `33427225894` passed every audit/chronology/lineage stage and failed only at MEMORY_TO_ROOT census emission.
Census artifact `9771215241`, digest `sha256:abf5b10e02459cad33d05944542549e6d3cf33760ea7fb48ab68155487c13df9`, proves:
- expected_group_count: 6
- observed_group_count: 5
- history_complete: true
- classification_complete: false
- decision: PARTIAL
- incomplete_group_ids: [`__COHORT_COUNT_DRIFT__`] only
- target_ids: EJR-165, EJR-293, EJR-294, EJR-295, EJR-296

The drift failure is preserved as required. No baseline change occurred inside Repair325.

## Learning
Reusable candidate learning from the rejected first attempt:

`PRE-WRITE MATRIX EXISTENCE ≠ SAME-CHANGE-SET MATRIX BINDING FOR PROTECTED CI ENFORCEMENT.`

When the CI gate evaluates only the current changed-file set, a protected mutation must carry a changed Mutation Matrix in that same functional commit even though the Matrix also existed as pre-write authority before execution. This learning is recorded here without changing GOV-014A authority.

## Outcome
EJR-237→EJR-431 is bounded and execution-verified. Priority 2 remains OPEN. Current deterministic baseline remains 6 until a separate rebaseline lease normalizes the proven 6→5 drift.
