# Governance Identity Migration Matrix — 2026-08-29

Transaction: `R71-20260829-GOV-IDENTITY-CLASSIFY-006`
Baseline: `main@d4b4c7854c3c9859bf712bcf727cba4788b2516f`
Status: `CLASSIFICATION DECISION / MIGRATION TARGETS RESERVED / NO PROMOTION BY RENUMBERING`

## Governing Rule

`GOV-006` requires:

- one ID → one active canonical path;
- filename identity = internal Document ID for canonical artifacts;
- historical conflicts are classified through explicit migration decisions;
- no silent normalization or deletion.

The current identity audit independently reports `governance_identity_hold_required = true` and exposes current collision families.

## Classification Method

Identity ownership is not chosen by filename similarity or latest date alone. The decision considers:

1. explicit `Document ID` metadata;
2. Canonical/Active status;
3. chronology/provenance;
4. existing operational references;
5. whether the artifact is Proposed/Candidate versus already governed;
6. whether two files are actually distinct contracts or duplicate generations of the same contract.

Renumbering does not promote a Proposed document. Its authority/status must remain unchanged unless a separate promotion gate succeeds.

## Family Decisions

| Current family | Path | Current state | Classification | Migration target |
|---|---|---|---|---|
| `GOV-013A` | `Governance/GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md` | Approved / Canonical Addendum; explicit Document ID `GOV-013A`; v1.0.1 | **OWNER — retain GOV-013A** | `GOV-013A` |
| `GOV-013A` | `Governance/GOV-013A_HERMUZ_OBSERVATION_SIDE_EFFECT_GATE.md` | Canonical Governance Addendum | distinct contract; identity collision | reserve `GOV-019` |
| `GOV-013A` | `Governance/GOV-013A_HERMUZ_SESSION_WORKGROUP_CONTINUATION_AMENDMENT.md` | Approved / Canonical Addendum | distinct contract; identity collision | reserve `GOV-020` |
| `GOV-013A` | `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md` | Canonical Amendment / Effective; expanded 2026-08-29 form | distinct current contract; identity collision | reserve `GOV-021` |
| `GOV-013A` | `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION_AMENDMENT.md` | Canonical Amendment; earlier/lighter same subject | **SUPERSEDED DUPLICATE CANDIDATE** by expanded effective form; preserve provenance, no new active identity unless later evidence disproves supersession | compatibility/archive disposition, not new canonical ID |
| `GOV-014` | `Governance/GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md` | Canonical; explicit Document ID; v1.0.1; active operating dependency | **OWNER — retain GOV-014** | `GOV-014` |
| `GOV-014` | `Governance/GOV-014_ARGO_SELF_ASSURANCE_AND_CAPABILITY_EVALUATION_PROTOCOL.md` | Canonical / Initial Baseline, 2026-08-27 | distinct contract created after occupied identity | reserve `GOV-022` |
| `GOV-015` | `Governance/GOV-015_EXECUTION_DOCUMENTATION_AND_KNOWLEDGE_TRANSFER.md` | ACTIVE / GOVERNED, 2026-08-17 | **OWNER — retain GOV-015** | `GOV-015` |
| `GOV-015` | `Governance/GOV-015_HERMUZ_CONTROLLED_DIAGNOSTIC_EXPERIMENT_PROTOCOL.md` | Proposed Canonical / pending review | distinct **candidate**, not owner | reserve `GOV-023`; status remains Proposed |
| `GOV-016` | `Governance/GOV-016_FAILURE_TO_LEARNING_PROTOCOL.md` | ACTIVE / MANDATORY | **OWNER — retain GOV-016** | `GOV-016` |
| `GOV-016` | `Governance/GOV-016_HERMUZ_SOLUTION_SIMULATION_AND_EFFECT_ANALYSIS_PROTOCOL.md` | PROPOSED / governance review required | distinct **candidate**, not owner | reserve `GOV-024`; status remains Proposed |
| `GOV-017` | `Governance/GOV-017_HERMUZ_CONNECTOR_SELF_LEARNING_PROTOCOL.md` | PROPOSED / governance review required | no evidence sufficient to make it canonical family owner | reserve `GOV-025`; status remains Proposed |
| `GOV-017` | `Governance/GOV-017_HERMUZ_SOLUTION_EVOLUTION_AND_STABILITY_PROTOCOL.md` | PROPOSED / governance review required | no evidence sufficient to make it canonical family owner | reserve `GOV-026`; status remains Proposed |
| `GOV-018` | `Governance/GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md` | Candidate / Canonical No / promotion pending | unique candidate identity; no current Governance-file collision | retain `GOV-018`; no promotion |

## Reserved-Target Rule

`GOV-019` through `GOV-026` above are reserved migration targets for this classified set. Reservation means only:

`UNIQUE TARGET ID SELECTED TO REMOVE COLLISION`

It does **not** mean:

- Canonical promotion;
- higher authority;
- validation of the document's substantive content;
- insertion into `REP-001`;
- activation of Proposed protocols.

## Migration Order

The safe implementation order is:

1. preserve source content/provenance and exact source SHA;
2. create correctly named target artifact with identical substantive content except identity/path metadata needed by migration;
3. update material canonical references to the target path;
4. convert old colliding path to explicit non-authoritative compatibility/supersession record or archive it;
5. run identity audit and affected integration tests;
6. only after the Governance family has one unambiguous active identity per contract, reconcile `REP-001`/`REP-002`;
7. run final current-head Full-Stack + Runtime/Integration + M2;
8. do not promote Proposed/Candidate status during identity repair.

## Why GOV-017 Is Not Retained as an Owner

Both current `GOV-017` artifacts explicitly state `PROPOSED — GOVERNANCE REVIEW REQUIRED`. Choosing either as the canonical owner merely to preserve a number would silently promote a proposal. Therefore the number is treated as historically collided/unassigned for active authority until a later explicit governance decision.

## Why the Earlier Repository-First Amendment Is Not Given Another Active ID

The two repository-first files express the same core contract. The expanded `Governance/GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md` is newer, explicitly `CANONICAL AMENDMENT / EFFECTIVE`, records 2026-08-29 promotion evidence, and contains the current HERMUZ/HORUS/MAAT/Room71 lease model. The lighter `_AMENDMENT` form is therefore classified as a superseded duplicate candidate, not as a separate governing concept.

This classification is bounded to current repository evidence and can be overturned only by contrary provenance/authority evidence.

## Non-Claims

- This matrix does not yet claim the identity HOLD is removed.
- `REP-001` and `REP-002` remain frozen for Governance inventory mutation until migration verification.
- Reserved IDs do not promote candidate documents.
- Content correctness of the protocols is not established merely by resolving their identity.
