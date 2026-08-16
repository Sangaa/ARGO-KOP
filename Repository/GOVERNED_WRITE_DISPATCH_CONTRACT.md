# GOVERNED WRITE DISPATCH CONTRACT

Document ID: WRITE-DISPATCH-001
Status: Active / Integrity Hold
Development Baseline: 3.2.1

## Purpose

Define the single decision point used before repository writes so a file is never sent to the wrong GitHub mutation operation.

## Required Sequence

```text
WRITE INTENT
  ↓
CURRENT EXISTENCE PROBE
  ↓
┌───────────────────────────────┐
│ exists + current SHA → UPDATE │
│ confirmed 404 → CREATE        │
└───────────────────────────────┘
  ↓
COMMIT
  ↓
CURRENT READ-BACK
  ↓
CONTENT / IDENTITY VERIFICATION
  ↓
RECORD EVIDENCE
```

## Create Gate

A new file may be created only when all of the following are explicit:

- the existence probe returned a confirmed not-found state;
- file purpose is stated;
- file importance is classified;
- necessity evidence explains why a new artifact is required instead of updating/reusing an existing artifact;
- canonical/authority implications are identified;
- the intended content is complete enough to stand as the target file;
- post-create read-back is planned and mandatory.

A filename alone is never sufficient evidence for creation.

## Update Gate

An existing file may be updated only when:

- current existence has been directly verified;
- current content/blob SHA is captured from that verification;
- the intended change is scoped;
- authority and consumer impact have been checked where material;
- the update uses the exact current SHA;
- post-update read-back succeeds.

## Race Rule

If the existence probe says `NOT_FOUND` but Create returns a conflict because another write appeared, the operation must stop and re-read the current file. It must not silently fall back to Update or overwrite the newly appeared file.

## Read-Back Rule

A commit is not considered safely persisted until the target is re-read from current repository state and the resulting content matches the intended target.

## Error-Learning Rules

The following failures observed during the HERMUZ build sessions are permanent regression knowledge:

1. **Wrong mutation verb:** attempting `update_file` for a path that did not exist caused an argument/operation mismatch. Existence must be checked first.
2. **Wrong ref assumption:** a write was followed by a read using an incorrect or stale reference. Read-back must use the current authoritative branch/state.
3. **Stale SHA:** sequential mutations occasionally attempted to use an older SHA. Every update must obtain the current SHA immediately before the write.
4. **Create vs update ambiguity:** a new Evidence artifact was sometimes treated like an update target. Creation requires explicit necessity evidence; updating requires an existing target SHA.
5. **CI/collector mismatch:** tests can execute a different copy of a guard than the intended integrity suite. Test ownership and collection boundaries must be checked before interpreting failures.
6. **Evidence vs implementation confusion:** documentation/contract presence must never be promoted to executable proof merely because a write succeeded.

## Authority Boundary

This contract governs write dispatch mechanics only. It does not grant repository mutation authority, canonical authority, or execution authority. Those remain subject to GOV-013, Repository control-plane rules, applicable domain authorities and human approval boundaries.
