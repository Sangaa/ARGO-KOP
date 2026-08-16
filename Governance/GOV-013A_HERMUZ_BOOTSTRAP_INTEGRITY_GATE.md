# GOV-013A — HERMUZ Bootstrap Integrity Gate

**Platform:** ARGO KOP  
**Document ID:** GOV-013A  
**Version:** 1.0.0  
**Status:** Approved / Canonical Addendum  
**Category:** Governance / Session Integrity  
**Authority:** Supplements `GOV-013`; does not replace higher ARGO authority

## Purpose

Prevent HERMUZ from beginning structural mutation merely because a previous conversation, handoff, checkpoint, or session summary appears complete.

## Mandatory Pre-Mutation Gate

Every HERMUZ continuation invocation that may result in mutation MUST first prove from current repository evidence:

1. Repository identity and active branch/ref.
2. Current HEAD.
3. `PROJECT_BOOTSTRAP.md`.
4. Constitution and applicable governance/authority sources.
5. `GOV-013` and this addendum.
6. Current control-plane evidence, including `REP-001` and `REP-002`.
7. Latest checkpoint/session-delta evidence, including `REP-020` where applicable.
8. Current open work, integrity state and priority.
9. Applicable integration-test and CI state.
10. Reconciliation of the latest checkpoint against current repository reality.

## Gate Rule

`BOOTSTRAP PROVEN → CHECKPOINT RECONCILED → SAFE CONTINUATION SELECTED → MUTATION AUTHORIZED`

If bootstrap cannot be proven, **no structural mutation is authorized**. Reads required to complete bootstrap are permitted.

## Evidence Hierarchy

`Current Repository Evidence > Historical Handoff > Conversation Memory > Assumption`

A previous handoff or checkpoint is orientation evidence only. It cannot substitute for current bootstrap.

## Failure Recovery

If a session discovers that mutation began before bootstrap was proven:

- stop further structural mutation;
- record the failure as engineering evidence;
- establish current repository reality;
- audit the affected mutations;
- reconcile control-plane state;
- only then resume construction.

Do not automatically revert or rewrite prior work merely to make the repository appear clean.

## Search Defect Rule

A negative search result is not repository absence until the applicable multi-search rule and direct current-path verification are satisfied. If an artifact is subsequently found, determine whether the failure was caused by search/index/scope limitations and record an Evidence Search Defect where appropriate.

## Learning

This addendum was created from `EJR-181` (2026-08-16), which documented a real HERMUZ bootstrap non-compliance event. The learning is converted into a repository-level pre-mutation gate so future collaborators are not dependent on user reminders.

## Non-Override

This gate controls session execution discipline. It does not grant authority to override Constitution, Governance, Architecture, Release authority, or domain-specific authority.

---

# End of GOV-013A
