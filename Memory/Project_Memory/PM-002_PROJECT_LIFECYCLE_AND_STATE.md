# PM-002 — PROJECT LIFECYCLE AND STATE

Version: 1.0.0
Status: Build-01 / Integrity Hold

## Lifecycle

```text
Candidate
  ↓
Defined
  ↓
Active
  ↓
Executed / Observed
  ↓
Validated
  ↓
Completed
  ├── Maintained
  ├── Superseded
  └── Archived
```

A project may also enter `Blocked` from an active state when execution cannot proceed. `Blocked` is a state, not a terminal lifecycle stage.

## State Discipline

Project state must be supported by evidence. File existence, planned milestones or previous conversation statements are insufficient by themselves to declare a project completed or validated.

## Validation Separation

The following are separate claims:

1. the project work was performed;
2. the expected output was produced;
3. the output was validated;
4. the output remains useful under current conditions.

## Supersession

When project scope or implementation is replaced, preserve the prior project context and record the successor relationship rather than silently rewriting history.

## Boundary

Project lifecycle governs Project Memory state representation. It does not override the platform lifecycle or impose project workflow on users.

---

End of PM-002
