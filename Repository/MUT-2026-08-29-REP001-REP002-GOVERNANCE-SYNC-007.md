# REP-001 / REP-002 GOVERNANCE SYNC MUTATION MATRIX

Transaction ID: `MUT-2026-08-29-REP001-REP002-GOVERNANCE-SYNC-007`
Protocol: GOV-014 v1.0.1
Parent lease: `R71-20260829-GOV-IDENTITY-CLASSIFY-006`
Entry verified migration head: `030ff323212c430877f63e46cd10677517bbe9e4`
Initial protected-change head: `34764880b27c9a4d689dc3d179be44ce8e42c248`
Status: `PACKAGING REPAIR APPLIED / CI VERIFICATION PENDING`

## Boundary

Synchronize Governance identity migration into repository inventory without promoting Proposed/Candidate documents and without modifying unrelated control-plane content.

| Change ID | Target | Action | Expected Content | Applied | Verified |
|---|---|---|---|:---:|:---:|
| GOVSYNC-001 | `Repository/REP-001_MASTER_INDEX.md` | UPDATE | active Governance inventory reflects verified unique identities; candidates remain non-active | Y | Y |
| GOVSYNC-002 | `Repository/REP-002_REPOSITORY_MAP.md` | UPDATE | physical Governance map mirrors REP-001 authority boundary | Y | Y |
| GOVSYNC-003 | `Repository/REP-015_CONTROL_PLANE_BOOTSTRAP_CHECKLIST.md` | UPDATE | record same-change-set Mutation Matrix visibility rule learned from failed Full-Stack gate | Y | N |
| GOVSYNC-004 | `Repository/MUT-2026-08-29-REP001-REP002-GOVERNANCE-SYNC-007.md` | UPDATE | canonical matrix shape plus failure/repair evidence visible in same protected change set | Y | N |

## KEEP Requirement

All content outside the explicitly listed changes is `KEEP`. No unrelated repository, runtime, governance-content, release/version, provider-authentication, or cognitive-effect mutation is authorized.

## Applied Inventory Decision

Active/governed paths added to REP-001/REP-002:

- `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER.md`
- `Governance/GOV-019_HERMUZ_OBSERVATION_SIDE_EFFECT_GATE.md`
- `Governance/GOV-020_HERMUZ_SESSION_WORKGROUP_CONTINUATION_AMENDMENT.md`
- `Governance/GOV-021_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md`
- `Governance/GOV-022_ARGO_SELF_ASSURANCE_AND_CAPABILITY_EVALUATION_PROTOCOL.md`
- `Governance/GOV-027_PROVENANCE_PRESERVATION_AND_SESSION_RECONSTRUCTION_AMENDMENT.md`

Existing active owners remain GOV-001/004/005/006/009/010/013/013A/014/016.

Candidate/non-active physical paths remain outside active canonical authority:

- GOV-011, GOV-012, GOV-018, GOV-023, GOV-024, GOV-025, GOV-026.

Compatibility/superseded old identity paths remain historical reconstruction evidence only.

## Execution Evidence

### Identity migration prerequisite

Exact Governance migration head `030ff323212c430877f63e46cd10677517bbe9e4` passed Runtime/Integration, Full-Stack and M2.

### Initial index synchronization

Atomic commit `34764880b27c9a4d689dc3d179be44ce8e42c248` changed exactly:

- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`

Post-write read-back verified both Governance sections and the commit diff confirmed no unrelated file mutation.

Exact-head results:

- Runtime/Integration — SUCCESS;
- M2 — SUCCESS;
- Internal Document-ID Audit — SUCCESS;
- GOV-014 Controlled Document Mutation workflow — SUCCESS;
- Full-Stack Repository Audit `33238163854` — FAILURE at `Enforce Mutation Matrix on current change set`.

### Root cause

The failure was not a REP-001/REP-002 semantic failure. The preflight gate evaluates `git diff BASE...HEAD` and requires a Matrix file in the **same changed-file set** whenever protected paths change.

The pre-write matrix existed in parent commit `bb8fde56d4ee13f56fba35498269bff1cdaee880`; therefore the protected-change diff reported:

`changed_files=2 / protected_changes=2 / mutation_matrices=0`.

Classification: `TRANSACTION_PACKAGING_FAILURE`.

The repair changes `REP-015` to encode this exact operational constraint and updates this Matrix in the same protected change set. The gate is not weakened.

## Learned Control Rule

`PRE-WRITE MATRIX EXISTS` is necessary but not sufficient for protected-change CI.

For a protected atomic mutation, the governing Matrix must also be **visible in the same CI diff range** that contains the protected change, either because the protected mutation and finalized matrix are committed together or because the workflow's declared transaction range explicitly contains both.

Current workflow uses the immediate push before/head range, so the safe repository rule is:

`PROTECTED CHANGE + GOVERNING MATRIX VISIBILITY = SAME CHANGE SET`

## Post-Commit Reconciliation

After the repair commit:

1. re-read REP-015 and this Matrix;
2. verify changed-file set contains the protected REP-015 path and this Matrix;
3. require Mutation Matrix preflight PASS;
4. require Matrix semantic validation PASS;
5. require Runtime/Integration + Full-Stack + M2 PASS on exact repair head;
6. only then close the Governance REP-001/REP-002 synchronization point.

Post-write read-back: `PENDING` until commit exists.
Unexpected Changes = 0 required.

## Non-Claims

- Index membership is inventory/discoverability, not semantic correctness proof.
- Candidate presence is not promotion.
- This synchronization does not close repository-wide Connected Baseline.
- It does not resolve provider authentication or cognitive-benefit holds.
