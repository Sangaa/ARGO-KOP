# EXT-001 — EXTERNAL REVIEW PROTOCOL

Version: 1.0.0
Status: Candidate / Integrity Hold

## Purpose

Define how external AI reviews of ARGO KOP are evaluated without allowing an external model, incomplete repository loading, or search/index limitations to silently become repository truth.

## Required Reviewer Declaration

Every external review should state:

1. Repository URL and branch/ref inspected.
2. Whether the current repository was actually loaded or only selected files were inspected.
3. Scope of files/domains reviewed.
4. Evidence coverage limitations.
5. Whether conclusions are verified, partially verified, inferred, or assumed.
6. Tools or access limitations affecting completeness.

## Minimum Review Request

The reviewer should be instructed to:

- follow `START_HERE.md`;
- read `README.md` and `PROJECT_BOOTSTRAP.md`;
- inspect the current repository rather than rely on prior conversation context;
- distinguish direct repository evidence from inference;
- report the actual loading/inspection scope before making global claims;
- avoid redesigning ARGO merely to match generic architecture preferences.

## External Finding Classes

External findings should be classified as:

- Strength
- Weakness
- Opportunity
- Threat
- Contradiction
- Missing Evidence
- Recommendation
- Optional Future Idea

## Decision Rule

External review is evidence, not authority.

A finding becomes an ARGO engineering action only after internal review confirms its relevance, evidence, scope, impact and timing.

## Loading Integrity

A reviewer that cannot load the repository completely must not claim a complete repository review. Partial review remains useful when its scope is explicit.

A disagreement between direct repository evidence and an external review is resolved by inspecting the current repository artifact and tracing the evidence.

## Review Comparison

When multiple external reviewers are used, compare:

```text
Gemini / Reviewer A
        +
Copilot / Reviewer B
        +
Other Reviewer Evidence
        ↓
ARGO Internal Review
        ↓
Confirm / Modify / Reject / Defer
        ↓
Construction Plan
```

## Boundary

This protocol does not grant external AI systems write authority. Repository mutations remain governed by ARGO repository rules and the applicable engineering workflow.

---

End of EXT-001
