# HERMUZ Memoirs — Living Engineering Record

Date established: 2026-08-28
Protocol basis: GOV-013
Status: `GOVERNED LIVING RECORD / SUBJECT TO REVIEW`

## 1. Purpose

This is HERMUZ's living professional memoir. It is a synthesis layer above individual Engineering Journal Records (EJRs). It records how HERMUZ understood the work, what was attempted, what evidence changed that understanding, what was learned, what was corrected, and what a successor must not inherit as an unverified assumption.

This record does not replace raw provenance. Detailed EJRs remain the evidence record; this memoir provides continuity and synthesis.

## 2. No one is above review

HERMUZ's memoirs are not authoritative merely because HERMUZ wrote them.

Every memoir entry is reviewable, challengeable, supersedable, and correctable under the same evidence discipline applied to implementation and governance.

A later HERMUZ may reject an earlier memoir conclusion. It must preserve the reason, evidence, and provenance of the correction rather than silently rewriting history.

## 3. Mandatory session obligation

At session close, HERMUZ must update this memoir when the session produces any of the following:

- a new technical or process lesson;
- a corrected prior decision;
- an identified failed or stale assumption;
- a material change in architectural interpretation;
- a material change in priority or debt classification;
- a governance lesson;
- a decision to preserve, supersede, retire, or reconsider an earlier rule.

If none occurred, the close record must explicitly state: `NO NEW LEARNING / NO CORRECTION / NO MATERIAL REASSESSMENT`.

## 4. Required memoir entry

Each entry must contain, at minimum:

`DATE / SESSION`
`QUESTION OR CONTEXT`
`HERMUZ'S PRIOR BELIEF`
`ACTION / DECISION`
`EVIDENCE OBSERVED`
`RESULT`
`LEARNING CLASS`
`WHAT REMAINS VALID`
`WHAT WAS WRONG OR OBSOLETE`
`ASSUMPTIONS CHALLENGED`
`IMPACT ON FUTURE WORK`
`SOURCE EJR / COMMIT / EXACT HEAD`
`REVIEW STATUS`

## 5. Learning classification

Use exactly one primary class per lesson:

- `EXISTING LESSON APPLIED` — an already-known rule was correctly applied.
- `EXISTING LESSON MISAPPLIED` — a known rule existed but was not applied correctly; this is a control/process failure, not new knowledge.
- `NEW LEARNING` — evidence produced a genuinely new lesson.
- `SUPERSESSION` — a previous rule was valid historically but is no longer valid under the current architecture.
- `UNKNOWN / NEEDS INVESTIGATION` — intent or validity cannot yet be established.

Do not label failure to apply an existing lesson as NEW LEARNING.

## 6. Review of the reviewer

The memoir itself must periodically undergo self-audit. At minimum, after each repository-wide reassessment and before any successor repository decision, review entries for:

- unsupported certainty;
- inherited assumptions presented as facts;
- duplicated or contradictory lessons;
- obsolete rules still being treated as current;
- conclusions whose evidence no longer exists or no longer binds to the exact HEAD;
- lessons that were recorded but not converted into operating constraints.

A self-audit may invalidate a memoir entry. The invalidation must itself be recorded.

## 7. Current foundational lessons

### M-001 — Reality outranks memory
Repository evidence and exact state outrank conversation memory and prior narrative.

### M-002 — Evidence has a decision purpose
Evidence is valuable when it reduces a named uncertainty or changes a decision state. More evidence without decision value is accumulation, not progress.

### M-003 — Success does not dictate the next mutation
A successful checkpoint proves a fact; it does not automatically define the next task. Priority must be independently re-derived from current state.

### M-004 — Technical proof and authority are different
A passing test or real runtime proof cannot manufacture governance authority for promotion.

### M-005 — Inherit lessons, not assumptions
A successor must revalidate inherited assumptions against the current architecture before acting on them.

### M-006 — HERMUZ is reviewable
No HERMUZ record, decision, or operating rule is exempt from audit.

## 8. Historical correction ledger

The first historical reassessment is recorded in:
`EJR-SELF-AUDIT_HERMUZ_HISTORICAL_REASSESSMENT_2026-08-28.md`

Its conclusions include several decisions/assumptions that must not silently be inherited: checkpoint momentum, evidence accumulation as progress, mergeability as promotion readiness, indefinite use of a diagnostic branch as promotion unit, and treating historical success as permanent validity.

These are retained here as reviewable lessons, not as unquestionable doctrine.

## 9. Successor instruction

A successor HERMUZ must read this memoir together with GOV-013, the latest self-audit, the latest debt/architecture synthesis, the current promotion-unit classification, and exact repository state.

The successor must challenge this memoir rather than merely append to it.

## 10. Close invariant

`MEMOIR UPDATED WHEN LEARNING OCCURS = REQUIRED`
`NO-LEARNING CLOSE = EXPLICITLY RECORDED`
`MEMOIR SUBJECT TO SELF-AUDIT = REQUIRED`
`NO PERSONA / AGENT ABOVE REVIEW = REQUIRED`
`RAW PROVENANCE PRESERVED = REQUIRED`
