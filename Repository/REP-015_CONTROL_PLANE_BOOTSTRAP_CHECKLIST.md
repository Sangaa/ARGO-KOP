# REP-015 — CONTROL PLANE BOOTSTRAP CHECKLIST

Platform: ARGO KOP  
Document ID: REP-015  
Version: 1.0.2  
Status: Active / Phase 1 Open  
Development Baseline: 3.3.0  
Last Audit: 2026-08-10

## Purpose

Provide a deterministic bootstrap sequence for any new build/review session before repository mutation begins.

This checklist prevents a model from relying on conversational memory when the repository already contains stronger state and evidence.

## Required Load Order

```text
1. Current repository HEAD
2. REP-001 — master navigation/index
3. REP-002 — structural/domain map
4. REP-013 — folder/file content inventory
5. REP-012 — allocation/state/checkpoint/recovery registry
6. REP-011 — review/mutation evidence
7. REP-014 — relationship registry
8. REP-016 — Phase 1 partition work queue
9. Relevant canonical domain authorities
10. Relevant Engineering Journal entries
11. Open / unresolved scope
12. Current work item
```

## Baseline Verification Gate

Before interpreting any registered state, compare the Development Baseline and audit date of the relevant control-plane artifacts.

If control-plane artifacts carry different baselines:

```text
STOP PROMOTION
    ↓
IDENTIFY BASELINE MISMATCH
    ↓
COMPARE CURRENT CONTENT / COMMITS
    ↓
REVALIDATE AFFECTED REGISTRIES
    ↓
SYNCHRONIZE OR EXPLICITLY RETAIN DIFFERENCE
    ↓
RECORD EVIDENCE
```

A baseline number is a coordination marker, not proof that an artifact is correct or that Phase 1 is complete.

## Evidence Priority Rule

When sources disagree, do not resolve the conflict by recency alone.

Use this order of investigation:

```text
Current repository state
        ↓
Artifact identity / content evidence
        ↓
Canonical authority
        ↓
Review / mutation evidence
        ↓
Relationship and consumer evidence
        ↓
Historical journal / checkpoint
        ↓
Conversation narrative
```

A historical record can remain valuable evidence while being insufficient for current correctness.

## Pre-Mutation Gate

Before changing any file, answer:

```text
Current HEAD:
Artifact Path:
Document ID:
Current Content Identity:
Last Reviewed Identity:
Allocation State:
Review State:
Relationship State:
Authority:
Known Dependencies:
Known Consumers:
Open Scope:
Recovery Checkpoint:
Reason for Current Work:
```

If identity or state cannot be resolved, stop promotion and perform repository reconciliation first.

## Intent Interpretation Gate

If the requested change depends on interpreting a human statement or design intention:

```text
Observed wording
      ↓
Literal meaning
      ↓
Model interpretation
      ↓
Assumption / hypothesis
      ↓
Repository + authority validation
      ↓
Explicit decision
```

A model interpretation must not silently become canonical meaning.

## Mutation Gate

A material mutation requires:

`READ → IDENTITY → AUTHORITY → DEPENDENCIES → CONSUMERS → MUTATE → COMMIT → RE-READ → REGISTRY SYNC`

Registry synchronization means updating the affected records in:

- `REP-011`
- `REP-012`
- `REP-013`
- `REP-014`
- `REP-015`
- `REP-016`

where applicable.

## Persistence Boundary Rule

When session termination is possible, treat each material mutation as a final persisted unit:

`ONE MATERIAL CHANGE → COMMIT → RE-READ → RECORD EVIDENCE → NEXT CHANGE`

Do not depend on conversation continuity to preserve uncommitted work.

## Post-Mutation Gate

After a commit:

1. Re-read the mutated artifact from the repository.
2. Confirm the resulting commit and content identity.
3. Verify affected relationships.
4. Verify affected consumers.
5. Update review state.
6. Update allocation/checkpoint state.
7. Record unresolved scope.
8. Decide whether the mutation is provisional or trusted.

If any required post-mutation verification is unavailable, leave the affected item open rather than declaring completion.

## Failure Gate

If a new contradiction or methodological failure appears:

`STOP PROMOTION → PRESERVE EVIDENCE → CLASSIFY TEMPORALLY → IDENTIFY AFFECTED ARTIFACTS → REVALIDATE → REPAIR/RETAIN/REVERT/QUARANTINE → RECORD LEARNING`

Never silently overwrite the evidence that revealed the failure.

## Review Loop Control

If repeated review produces no new evidence:

1. record what has already been verified;
2. identify why the item remains open;
3. record the missing evidence;
4. define the next concrete action;
5. move to that action instead of repeating the same pass.

## Control-Plane Reconciliation Rule

The presence of all control-plane files does not establish that the control plane is reconciled.

Current control-plane scope is:

`REP-011 / REP-012 / REP-013 / REP-014 / REP-015 / REP-016`

The current status remains:

`PARTIALLY RECONCILED / INTEGRITY HOLD`

until the registered states, identities, relationships and work-queue evidence are reconciled across the scope.

## Phase 1 Completion Gate

No folder/domain may be closed until:

- content inventory reconciles;
- allocation records reconcile;
- review evidence reconciles;
- material relationships reconcile;
- consumers/impact are addressed where applicable;
- unresolved items are explicit;
- pre-failure mutations are dispositioned;
- an explicit closure decision is recorded.

## Resume Rule

If a previous session ended without closure, resume from the latest repository evidence and checkpoint—not from the last conversational instruction alone.

A resumed session must compare current repository state against registered state before assuming that prior review remains valid.

## Cross-Model Handoff Minimum

A new model must be able to locate the current execution state through repository artifacts without human explanation.

Minimum control-plane load:

`REP-001 → REP-002 → REP-013 → REP-011/012/014 → REP-015/016 → Journal`

## Guiding Rule

**The repository is the operational memory; conversation is context, not the authoritative state.**

---

End of Document
