# EJR-181 — HERMUZ Bootstrap Non-Compliance Correction

**Platform:** ARGO KOP  
**Document ID:** EJR-181  
**Version:** 1.0.0  
**Status:** Session Evidence / Corrective Learning  
**Date:** 2026-08-16  
**Category:** Engineering Journal / Failure Learning / Session Integrity  
**Canonical:** No — promotion requires governance review

## 1. Event

During the 2026-08-16 HERMUZ continuation session, the collaborator began repository construction from conversational checkpoint/context instead of first proving a complete ARGO KOP bootstrap from current repository reality.

The later explicit `Boot ARGO KOP` correctly loaded the repository bootstrap, Constitution, HERMUZ protocol, control-plane artifacts and current state, and exposed synchronization gaps that the earlier continuation had not established.

## 2. Root Cause

The failure was **bootstrap execution non-compliance**, not absence of a bootstrap method.

The collaborator treated:

`conversation context + prior checkpoint + recent session summary`

as sufficient continuation state, although the repository itself requires:

`current repository identity/state → bootstrap → authority/control-plane verification → checkpoint reconciliation → safe continuation`.

The previous handoff was therefore overweighted relative to repository authority.

## 3. Why the Error Was Dangerous

A continuation checkpoint can be internally coherent while being stale, partially synchronized, historical, or incomplete relative to current `main`.

Starting mutation from that checkpoint can cause:

- work to be based on stale control-plane state;
- historical checkpoints to be mistaken for current state;
- local reconciliation to be performed before repository-wide orientation;
- evidence boundaries to be inherited without revalidation;
- false confidence in completed work.

The incident therefore affected **process integrity**, even where individual later mutations were technically valid.

## 4. Corrective Rule

For every HERMUZ invocation that can lead to mutation, **bootstrap is a precondition, not an optional contextual step**.

The collaborator must establish, from current repository evidence:

1. repository identity and active ref;
2. current HEAD;
3. `PROJECT_BOOTSTRAP.md`;
4. Constitution and applicable authority;
5. `GOV-013`;
6. current control-plane indexes/maps;
7. latest checkpoint/session delta;
8. open work and integrity state;
9. applicable integration-test/CI state;
10. reconciliation between checkpoint claims and current repository reality.

Only after these checks may the collaborator select the next mutation.

## 5. Continuation Is Not Bootstrap

A previous HERMUZ handoff, EJR entry, checkpoint, or conversational summary is **historical/session evidence**.

It is never a substitute for current repository bootstrap.

The deterministic distinction is:

`Handoff = orientation evidence`

`Bootstrap = current-state verification`

`Checkpoint = historical/current work evidence subject to verification`

`Authority = governed repository source`

## 6. Detection Requirement

If the collaborator cannot prove that bootstrap prerequisites were executed, it must not perform structural mutation.

It may perform only the minimum repository reads required to complete bootstrap and establish the safe continuation point.

This is a **BOOTSTRAP GATE**, not a user reminder requirement.

## 7. Search-Learning Connection

The same session also demonstrated that negative search results can be tool/index artifacts rather than repository absence. Therefore bootstrap must use direct-path verification and materially different retrieval methods before treating an artifact as absent.

A false negative caused by retrieval method is an **Evidence Search Defect**.

## 8. Required Future Behavior

When the user invokes:

> «أكمل البناء طبقًا لبروتوكول البناء الخاص بهرمز.»

HERMUZ must silently execute the repository-first bootstrap gate before mutation and must not infer successful bootstrap merely because a previous session appears complete.

If bootstrap reveals drift, the first task is reconciliation of that drift. Construction resumes only after the safe continuation point is established.

## 9. Scope of This Learning

This is not a GPT-specific claim. The failure mode is model-independent: any collaborator can overweight handoff context, stale checkpoints, local references, or successful prior commits.

The reusable engineering principle is therefore:

> **Repository reality outranks continuation context; bootstrap proof precedes mutation.**

## 10. Validation Requirement

This learning should be considered effective only when the HERMUZ invocation path itself contains an enforceable bootstrap precondition and subsequent sessions demonstrate compliance without requiring the user to remind the collaborator to boot.

Until then, this remains corrective session evidence rather than permanent canonical knowledge.

---

# End of EJR-181
