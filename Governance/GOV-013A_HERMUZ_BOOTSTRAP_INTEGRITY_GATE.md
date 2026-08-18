# GOV-013A — HERMUZ Bootstrap Integrity Gate

**Platform:** ARGO KOP  
**Document ID:** GOV-013A  
**Version:** 1.0.1  
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

## Handoff Non-Authority / Boot-Proof Rule

A session handoff, Engineering Journal entry, previous model summary, chat memory, user-provided continuation report, or prior session status claim MUST be treated as **historical orientation evidence**, even when it is accurate and repository-backed.

It may identify likely checkpoints and reduce search effort, but it MUST NOT by itself establish any of the following:

- that the current repository HEAD equals the checkpoint HEAD;
- that the checkpoint's reviewed content is still current;
- that the reported work remains complete;
- that a relationship remains in the reported state;
- that integration/CI evidence still applies to the current HEAD;
- that a session is BOOTED, VERIFIED, or SAFE FOR MUTATION.

A model MUST NOT declare a session `BOOTED`, `INTEGRITY PASS`, `SAFE TO MUTATE`, `CONTINUATION VERIFIED`, or equivalent based only on a handoff/summary.

### Required Boot-Proof Record

Before the first structural mutation of every continuation session, the engineer MUST establish a current-repository proof record containing at minimum:

`Current HEAD → Branch/Ref → Bootstrap Artifacts Loaded → Current Checkpoint Identity → Checkpoint Reconciled → Open Work → Applicable Authority → Integration/CI State → Mutation Scope`

Each item must be supported by current repository evidence or explicitly marked `UNKNOWN / BLOCKED`.

If any mandatory item cannot be established, the session remains in:

`BOOTSTRAP INCOMPLETE / MUTATION BLOCKED`

until the missing evidence is resolved or the scope is explicitly narrowed to read-only inspection.

### Handoff Conflict Rule

If a handoff/summary conflicts with current repository evidence:

`CURRENT REPOSITORY EVIDENCE WINS → PRESERVE HANDOFF AS HISTORICAL EVIDENCE → CLASSIFY THE DRIFT → REVALIDATE AFFECTED SCOPE → DO NOT PROMOTE FROM THE HANDOFF`

The conflict must never be resolved by silently trusting the newer-sounding or more detailed narrative.

### Model-Independence Rule

This gate is intentionally model-independent. It applies equally to HERMUZ, another AI model, a human engineer, an automated agent, or a future ARGO runtime worker.

Compliance is determined by repository evidence, not by model confidence, memory quality, conversational fluency, or a convincing handoff.

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

The strengthened handoff rule also addresses the later observed recurrence pattern in which a model correctly understood a previous checkpoint but did not independently re-prove current repository state before treating that checkpoint as sufficient continuation authority.

## Non-Override

This gate controls session execution discipline. It does not grant authority to override Constitution, Governance, Architecture, Release authority, or domain-specific authority.

---

# End of GOV-013A
