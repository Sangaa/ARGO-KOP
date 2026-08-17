# EJR-195 — P4 Reverse-Evidence & Search-Learning Review

Date: 2026-08-17
Status: RECORDED / SESSION-CLOSABLE
Scope: P4 continuation / reverse-evidence verification / evidence-search learning
Repository: Sangaa/ARGO-KOP
Branch: main
Development Baseline: 3.2.1
Integrity State: INTEGRITY WARNING / CONNECTED-BASELINE AUDIT

## Resumption

P4 remains OPEN.
Current unresolved critical edges:
- `REL-009 — RUN-010 → SRV-009`
- `REL-061 — GOV-013A → GOV-013`

`REL-005 — ENG-006 → SRV-009` is already `BIDIRECTIONAL / EXECUTABLE-VERIFIED / GOVERNED / ISOLATED E2E / REGISTRY PROMOTED`.

## REL-009 Reverse-Evidence Review

Three materially different retrieval approaches were applied:
1. direct path / identifier retrieval;
2. repository semantic/file search for `RUN-010` and `SRV-009` coupling;
3. reverse/inferential commit-history retrieval for relationship evidence.

No independent `SRV-009 → RUN-010` reverse evidence was recovered.

The current P4 matrix remains correct:
`ONE-WAY / REVALIDATION REQUIRED`.

No promotion was made.

## REL-061 Reverse-Evidence Review

Current `GOV-013` content was directly re-read. It identifies itself as the canonical HERMUZ operating contract and does not independently cite `GOV-013A` in the reviewed current content.

Repository history independently confirms that `GOV-013A → GOV-013` was deliberately registered as `REFERENCES`, while preserving the stronger semantic description `Canonical Addendum / Supplements GOV-013`.

No authority transfer is implied and no reverse relationship is promoted.

Classification remains:
`ONE-WAY / GOVERNANCE-REVALIDATED / REVERSE EVIDENCE REQUIRED`.

## Search-Learning Finding

An important retrieval defect was confirmed during this session: ordinary repository file search returned no usable result for artifacts that were demonstrably present in commit history.

The recovery path was commit-history search followed by direct commit inspection.

Learning:
`Repository file-search absence is not sufficient negative evidence when the identifier is known and historical commits are available; commit-history retrieval must be treated as a separate evidence channel.`

This learning is operationally consistent with GOV-013's three-search rule and remains session evidence rather than a newly promoted permanent rule.

## Boundary

No speculative relationship was created.
No registry state was promoted by inference.
No runtime behavior was changed.
No CI SUCCESS or new RUNTIME VERIFIED claim was made in this session.

## Session Closure

This entry is the session-closing checkpoint and is sufficient for safe resumption if the session ends now.

Next safe actions:
1. recover independent reverse evidence for `REL-009` only if a materially different evidence source becomes available;
2. disposition `REL-061` as intentional one-way if canonical authority confirms no reverse reference is required;
3. preserve `REL-005` as promoted and do not reopen it without contradictory evidence.

No destructive mutation. P4 remains OPEN.
