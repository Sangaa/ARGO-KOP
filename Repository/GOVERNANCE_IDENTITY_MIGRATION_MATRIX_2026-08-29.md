# Governance Identity Migration Matrix — 2026-08-29

Transaction: `R71-20260829-GOV-IDENTITY-CLASSIFY-006`
Baseline: `main@d4b4c7854c3c9859bf712bcf727cba4788b2516f`
Status: `CLASSIFICATION DECISION / MIGRATION TARGETS RESERVED / NO PROMOTION BY RENUMBERING`

## Governing Rule

`GOV-006` requires one ID → one active canonical path, filename/internal-ID alignment for canonical artifacts, explicit migration of historical conflicts, and no silent normalization/deletion.

The current identity audit independently reported `governance_identity_hold_required = true` before this migration.

## Classification Method

Identity ownership is determined from explicit metadata, authority/status, chronology/provenance, operational references, candidate-vs-governed state, and whether artifacts are distinct contracts or duplicate generations. Renumbering never promotes authority.

## Family Decisions

| Current family | Path | Current state | Classification | Migration target |
|---|---|---|---|---|
| `GOV-013` | `Governance/GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md` | Approved / Canonical / explicit Document ID / v1.1.3 | **OWNER — retain GOV-013** | `GOV-013` |
| `GOV-013` | `Governance/GOV-013_AMENDMENT_001_PROVENANCE_RECONSTRUCTION_2026-08-27.md` | CANONICAL AMENDMENT / EFFECTIVE | distinct active contract; heading collision with parent | reserve `GOV-027`; authority/status unchanged |
| `GOV-013` | `Governance/GOV-013_BASELINE_AUTHORITY_RECONCILIATION_2026-08-14.md` | Decision Evidence / Integrity Hold | evidence record, not a second governance authority identity | retain content as evidence but remove document-identity heading claim; no new GOV ID |
| `GOV-013A` | `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` | Approved / Canonical Addendum; explicit Document ID `GOV-013A`; v1.0.1 | **OWNER — retain GOV-013A** | `GOV-013A` |
| `GOV-013A` | `Governance/GOV-013A_HERMUZ_OBSERVATION_SIDE_EFFECT_GATE.md` | Canonical Governance Addendum | distinct contract; identity collision | `GOV-019` |
| `GOV-013A` | `Governance/GOV-013A_HERMUZ_SESSION_WORKGROUP_CONTINUATION_AMENDMENT.md` | Approved / Canonical Addendum | distinct contract; identity collision | `GOV-020` |
| `GOV-013A` | `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md` | Canonical Amendment / Effective | distinct current contract; identity collision | `GOV-021` |
| `GOV-013A` | `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION_AMENDMENT.md` | earlier/lighter same subject | **SUPERSEDED DUPLICATE** by expanded effective form | compatibility/historical disposition; no second active ID |
| `GOV-014` | `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md` | Canonical; explicit Document ID; v1.0.1 | **OWNER — retain GOV-014** | `GOV-014` |
| `GOV-014` | `Governance/GOV-014_ARGO_SELF_ASSURANCE_AND_CAPABILITY_EVALUATION_PROTOCOL.md` | Canonical / Initial Baseline | distinct contract created after occupied identity | `GOV-022` |
| `GOV-015` | `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER.md` | ACTIVE / GOVERNED | **OWNER — retain GOV-015** | `GOV-015` |
| `GOV-015` | `Governance/GOV-015_HERMUZ_CONTROLLED_DIAGNOSTIC_EXPERIMENT_PROTOCOL.md` | Proposed / pending review | distinct candidate | `GOV-023`; remains Proposed |
| `GOV-016` | `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md` | ACTIVE / MANDATORY | **OWNER — retain GOV-016** | `GOV-016` |
| `GOV-016` | `Governance/GOV-016_HERMUZ_SOLUTION_SIMULATION_AND_EFFECT_ANALYSIS_PROTOCOL.md` | PROPOSED | distinct candidate | `GOV-024`; remains Proposed |
| `GOV-017` | `Governance/GOV-017_HERMUZ_CONNECTOR_SELF_LEARNING_PROTOCOL.md` | PROPOSED | no evidence sufficient to make canonical family owner | `GOV-025`; remains Proposed |
| `GOV-017` | `Governance/GOV-017_HERMUZ_SOLUTION_EVOLUTION_AND_STABILITY_PROTOCOL.md` | PROPOSED | no evidence sufficient to make canonical family owner | `GOV-026`; remains Proposed |
| `GOV-018` | `Governance/GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md` | Candidate / Canonical No | unique candidate identity | retain `GOV-018`; no promotion |

## Reserved-Target Rule

`GOV-019` through `GOV-027` are migration targets only. A unique number does not establish canonicality, content correctness, index membership or promotion.

## Migration Order

1. preserve source provenance/SHA;
2. create correctly named target artifact while preserving substantive status and requirements;
3. update material current canonical references;
4. convert old colliding path to explicit compatibility/supersession/evidence record;
5. run identity audit and affected integration tests;
6. only after one unambiguous active identity per governing contract, reconcile `REP-001/REP-002`;
7. exact-head Runtime/Integration + Full-Stack + M2;
8. never promote Proposed/Candidate status during identity repair.

## Family Reasoning

### GOV-013

The session-build protocol owns `GOV-013` because it carries the explicit Document ID, Approved/Canonical status and current operating-contract identity. Amendment 001 is itself authoritative but must receive a unique active identity (`GOV-027`) rather than masquerade as a second `GOV-013` document. The baseline-authority reconciliation is decision evidence and therefore does not require a second GOV identity.

### GOV-017

Both former `GOV-017` artifacts are explicitly Proposed. Choosing either as canonical owner merely to preserve a number would be an authority promotion by bookkeeping, so neither is promoted.

### Repository-First Duplicate

The expanded repository-first document is current/effective and contains current HERMUZ/HORUS/MAAT/Room71 lease controls. The lighter earlier form is preserved as superseded provenance, not assigned another active governing identity.

## Non-Claims

- This matrix alone does not close the identity HOLD.
- `REP-001/REP-002` remain frozen until migration/reference/audit verification.
- Reserved IDs do not promote candidates.
- Identity correctness is not proof of protocol-content correctness.
