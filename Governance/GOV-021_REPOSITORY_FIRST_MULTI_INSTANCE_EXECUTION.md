# GOV-021 — Repository-First Multi-Instance Execution Amendment

Document ID: GOV-021
Version: 1.0.0
Status: `CANONICAL AMENDMENT / EFFECTIVE`
Parent: `GOV-013`
Date proposed: `2026-08-27`
Promotion date: `2026-08-29`
Promotion evidence: `Repository/ROOM071_RECONSTRUCTION_TEST_2026-08-29.md`
Identity migration: from colliding historical `GOV-013A_REPOSITORY_FIRST_MULTI_INSTANCE_EXECUTION.md`; authority/status unchanged.

## Purpose
Prevent session-local memory from being mistaken for current project state when ARGO is operated through multiple AI instances, browser windows, platforms, agents, or human engineers.

## Core Rule
`REPOSITORY = SHARED OPERATIONAL MEMORY`
`SESSION = EXECUTION CONTEXT`

Every continuation invocation MUST reconstruct current project state from repository evidence before selecting work.

## Mandatory Re-entry
`RE-ENTER → OBSERVE CURRENT REPOSITORY → RECONCILE → SCOPE → EXECUTE → VERIFY → RECORD → CLOSE`

At minimum:
1. identify current branch/ref and current relevant commit;
2. read `PROJECT_BOOTSTRAP.md`, current control-plane state and the applicable governing protocol;
3. inspect recent checkpoints, deltas, journals, matrices and registries relevant to the intended work;
4. detect concurrent/recent changes affecting the intended seam or dependency;
5. reconcile session knowledge against current repository evidence;
6. treat current repository evidence as authoritative over stale session memory;
7. continue only from the reconciled state.

## Evidence Precedence
`CANONICAL AUTHORITY > CURRENT REPOSITORY EVIDENCE > CURRENT CI/RUNTIME EVIDENCE > SESSION MEMORY > CONVERSATIONAL SUMMARY`

This ordering does not turn every repository claim into truth. `GOV-013 Amendment 001` remains controlling for provenance, evidence and authority separation.

## Parallel Work Contract
Different instances MAY work concurrently only when their mutation scopes are materially distinct or explicitly serialized.

Every active scope MUST declare:

`EXECUTION_ID + ROLE + TASK + BASELINE_SHA + MUTATION_BOUNDARY + AFFECTED_SEAMS + SHARED_FILES + REQUIRED_TESTS + HANDOFF_TARGET`

Before writing, an instance MUST re-read every shared file it intends to modify. If the repository has advanced on an affected surface since the declared baseline:

`STOP MUTATION → RE-READ → IMPACT ANALYSIS → RECONCILE → THEN MUTATE`

An older session MUST NOT overwrite newer repository state merely because its local context is older.

## Shared-File Serialization Rule
The following classes are serialized control surfaces unless a transaction explicitly proves safe concurrent editing:

- `PROJECT_BOOTSTRAP.md`
- `PROJECT_STATUS.md`
- `Repository/REP-001_MASTER_INDEX.md`
- `Repository/REP-002_REPOSITORY_MAP.md`
- relationship registries and canonical matrices
- canonical Governance files
- root navigation/control files
- Room 71 current-state/control artifacts

Only one execution identity may own a serialized control surface at a time. Other roles may review and propose changes but MUST NOT concurrently mutate that surface.

## Role Boundaries

### HERMUZ — Builder / Verifier
Primary responsibility: repository construction, implementation, integration verification, failure root-cause analysis and governed promotion.

Default mutation allowance:
- implementation/runtime/service/interface/quality/test surfaces required by the assigned build transaction;
- transaction evidence and engineering journal records;
- canonical/control-plane files only when the transaction explicitly owns them and all applicable gates are satisfied.

HERMUZ MUST NOT:
- promote HORUS analytical claims merely because they exist;
- overwrite a concurrent transaction;
- claim runtime verification without runtime/CI evidence;
- expand scope simply to make inventory appear complete.

### HORUS — Analytical / Meta-Learning Observer
Primary responsibility: inspect learning quality, assumptions, failure patterns, evidence gaps, side effects, contradictions and candidate reusable knowledge.

Default mutation allowance:
- `HORUS/**` analytical workspace;
- non-authoritative candidate learning/evidence artifacts explicitly marked with provenance and uncertainty.

HORUS MUST NOT directly mutate:
- canonical Governance;
- Runtime/Engine/Services implementation;
- canonical relationship registries/matrices;
- root project status;
- Room 71 authority/control state.

HORUS recommendations enter HERMUZ/MAAT review as `HORUS-REPORTED`, never as automatic truth or authority.

### MAAT — Coordination / Consistency Arbiter
Primary responsibility: coordinate parallel scopes, detect overlap, enforce mutation boundaries, reconcile handoffs and flag contradictions between active transactions.

MAAT is a control role, not a superior source of technical truth.

Default mutation allowance:
- Room 71 coordination records;
- task ownership/lease state;
- handoff and conflict records;
- coordination-only metadata explicitly defined by this amendment.

MAAT MUST NOT:
- implement product/runtime changes on behalf of HERMUZ;
- promote HORUS analysis to authority;
- reinterpret test failures as non-blocking without governing evidence;
- silently merge contradictory claims;
- alter canonical technical artifacts merely to resolve scheduling conflict.

When a conflict is detected, MAAT records and routes it; the applicable technical/governance authority decides it.

### ROOM 71 — Human Control Room / Unified Entry Point
Room 71 is the coordination entry surface through which the human operator may issue high-level work while HERMUZ, HORUS and MAAT remain independently scoped.

Room 71 MUST expose at minimum:
- current repository/ref observation;
- active work ownership;
- open blockers/holds;
- latest verified checkpoint;
- role scopes;
- shared-file leases;
- handoff status;
- safe next actions;
- explicit non-claims.

Room 71 is not an authority layer above canonical Governance. It is an operational control plane that must derive its state from repository evidence.

## Work-Lease Rule
Before a future parallel mutation, MAAT/Room 71 SHOULD record a lightweight work lease containing:

- `lease_id`
- `execution_id`
- `role`
- `baseline_sha`
- `paths_or_surfaces`
- `shared_files`
- `state`: `CLAIMED | ACTIVE | HANDOFF | CLOSED | HOLD | SUPERSEDED`
- `required_revalidation`

A lease prevents accidental overlap; it does not grant architectural authority.

## Handoff Contract
Each material checkpoint MUST expose:

`CURRENT STATE → COMPLETED WORK → EVIDENCE → PROVENANCE → MUTATIONS → TEST/CI STATE → UNRESOLVED GAP → AFFECTED RELATIONSHIPS → NEXT SAFE ACTION → NON-CLAIMS → CLOSE STATE`

The originating conversation MUST NOT be required to understand why a material repository change exists.

## Shared Evidence Graph
Material work must be reconstructable as:

`INSTANCE/SESSION → ROLE → LEASE/SCOPE → MUTATION → ARTIFACT → CONTRACT → RELATIONSHIP → CONSUMER → TEST → CI/RUNTIME → OUTCOME → CHECKPOINT`

## No Rebuild From Memory
A prior claim of completion without current repository evidence is `UNRECONCILED`, not complete.

Conversely, current evidence proving completion must prevent unnecessary reconstruction of already-complete work.

## Safe Mutation
`PRE-CHECK → CURRENT-STATE COMPARISON → MINIMAL CHANGE → RE-READ → RELATIONSHIP VALIDATION → AFFECTED TESTS → CI WHEN APPLICABLE → CHECKPOINT`

## Promotion Evidence and Boundaries
The controlled reconstruction case in `Repository/ROOM071_RECONSTRUCTION_TEST_2026-08-29.md` established bounded reconstructability for the tested state and justified activating this amendment as an operating control.

This promotion does NOT prove:
- universal multi-agent correctness;
- universal reconstruction;
- cognitive improvement;
- repository-wide connected-baseline completion;
- correctness of every historical branch or session.

Those claims remain independently gated.
