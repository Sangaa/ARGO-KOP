# EJR-176 — Current-main Candidate Setup

Current main at candidate creation: `f3135921f4dea2599905b741a705744df632ab18`.

This is the required revalidation base after PR #5 was superseded.

Mutation scope for the candidate:
- Runtime Prototype authorization semantics only.
- No Integration test changes.
- No CORE-000 format changes.
- No REP-013 changes.
- No baseline authority changes.

Expected semantics:
- missing human authorization → `HOLD`;
- explicit approved authorization → `AUTHORIZED` then `PROPOSED`;
- `REJECTED` is not a reachable authorization result and should not be selected by the state mapping.

CI is the next verification gate.
