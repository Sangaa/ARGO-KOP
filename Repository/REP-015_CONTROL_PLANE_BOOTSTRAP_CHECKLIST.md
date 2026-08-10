# REP-015 — CONTROL PLANE BOOTSTRAP CHECKLIST

Platform: ARGO KOP  
Document ID: REP-015  
Version: 1.0.0  
Status: Active / Phase 1 Open  
Development Baseline: 3.2.1  
Last Audit: 2026-08-10

## Purpose

Provide a deterministic bootstrap sequence for any new build/review session before repository mutation begins.

This checklist prevents a model from relying on conversational memory when the repository already contains stronger state and evidence.

## Required Load Order

```text
1. Current repository HEAD
2. REP-002 — structural/domain map
3. REP-013 — folder/file content inventory
4. REP-012 — allocation/state/checkpoint/recovery registry
5. REP-011 — review/mutation evidence
6. REP-014 — relationship registry
7. Relevant canonical domain authorities
8. Relevant Engineering Journal entries
9. Open / unresolved scope
10. Current work item
```

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

## Mutation Gate

A material mutation requires:

`READ → IDENTITY → AUTHORITY → DEPENDENCIES → CONSUMERS → MUTATE → COMMIT → RE-READ → REGISTRY SYNC`

Registry synchronization means updating the affected records in:

- `REP-011`
- `REP-012`
- `REP-013`
- `REP-014`

where applicable.

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

## Failure Gate

If a new contradiction or methodological failure appears:

`STOP PROMOTION → PRESERVE EVIDENCE → CLASSIFY TEMPORALLY → IDENTIFY AFFECTED ARTIFACTS → REVALIDATE → REPAIR/RETAIN/REVERT/QUARANTINE → RECORD LEARNING`

Never silently overwrite the evidence that revealed the failure.

## Phase 1 Completion Gate

No folder/domain may be closed until:

- content inventory reconciles;
- allocation records reconcile;
- review evidence reconciles;
- material relationships reconcile;
- unresolved items are explicit;
- pre-failure mutations are dispositioned;
- an explicit closure decision is recorded.

## Resume Rule

If a previous session ended without closure, resume from the latest repository evidence and checkpoint—not from the last conversational instruction alone.

## Guiding Rule

**The repository is the operational memory; conversation is context, not the authoritative state.**

---

End of Document
