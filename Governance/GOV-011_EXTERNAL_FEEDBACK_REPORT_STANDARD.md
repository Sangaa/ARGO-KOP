# GOV-011

---

# EXTERNAL FEEDBACK REPORT STANDARD

Platform: ARGO KOP
Knowledge Operating Platform

Document ID: GOV-011
Version: 1.0.1
Status: Proposed / Integrity Hold
Category: Governance
Canonical: No
Development Baseline: 3.2.1
Latest Official Release: 1.0.0
Last Audit: 2026-08-10

---

# Purpose

Defines the mandatory format for external model, reviewer, evaluator, partner or tool feedback submitted to ARGO KOP.

The purpose is to make external feedback comparable, traceable, machine-readable where possible, and safe to use as evidence without allowing the reporting model to silently become an ARGO authority.

# Mandatory Submission Rule

Any external review intended to influence ARGO engineering MUST be submitted using the canonical sections below.

A report may use Markdown, JSON, YAML, CSV or plain text only when the same required fields are preserved.

Free-form commentary may be included, but it does not replace the required fields.

# Required Report Envelope

Every report MUST contain:

1. `Report ID`
2. `Reporter / Model`
3. `Report Type`
4. `Report Date`
5. `Repository Commit / Baseline`
6. `Scope Reviewed`
7. `Files / Artifacts Reviewed`
8. `Evidence Coverage`
9. `Findings`
10. `Contradictions`
11. `Missing Evidence`
12. `Risk / Severity`
13. `Recommended Actions`
14. `Confidence`
15. `Limitations`
16. `Validation Performed`
17. `Unresolved Questions`
18. `Final Assessment`

# Report Types

The reporter MUST identify one or more:

- `STRUCTURAL_AUDIT`
- `ARCHITECTURE_REVIEW`
- `GOVERNANCE_REVIEW`
- `RUNTIME_REVIEW`
- `SECURITY_REVIEW`
- `INTERFACE_REVIEW`
- `MEMORY_LEARNING_REVIEW`
- `DOCUMENTATION_REVIEW`
- `INTEGRITY_AUDIT`
- `GENERAL_EXTERNAL_REVIEW`

# Finding Format

Each finding MUST distinguish:

- `Finding ID`
- `Category`
- `Severity`: `CRITICAL | HIGH | MEDIUM | LOW | INFO`
- `Status`: `CONFIRMED | PROBABLE | POSSIBLE | UNKNOWN`
- `Evidence`
- `Affected Artifact`
- `Affected Layer`
- `Why It Matters`
- `Recommended Action`
- `Confidence`

A recommendation without evidence MUST be marked as a recommendation, not a confirmed defect.

# Contradiction Format

Each contradiction MUST identify:

- Source A
- Source B
- Exact conflict
- Authority relationship if known
- Impact
- Required resolution
- Current status

The reporter MUST NOT resolve authority conflicts by personal preference.

# Evidence Rules

External feedback is an evidence input.

It is NOT, by itself:

- Canonical ARGO authority;
- a Governance decision;
- an Architecture decision;
- proof that a file is correct;
- proof that a file is wrong;
- proof of successful execution.

`UNKNOWN` MUST remain `UNKNOWN` when evidence is insufficient.

Model-generated claims MUST be distinguishable from repository-observed facts.

# Required Evidence Coverage

The reporter MUST state what was actually inspected and what could not be inspected.

Minimum coverage statement:

- Repository access: `FULL | PARTIAL | NONE`
- File content access: `FULL | PARTIAL | NONE`
- Runtime execution access: `FULL | PARTIAL | NONE`
- External system access: `FULL | PARTIAL | NONE`
- Historical/commit access: `FULL | PARTIAL | NONE`

# Final Assessment

The final assessment MUST use one of:

- `PASS`
- `PASS_WITH_WARNINGS`
- `INTEGRITY_HOLD`
- `FAIL`
- `INSUFFICIENT_EVIDENCE`

The reporter MUST NOT use `PASS` when required evidence was unavailable.

# Recommended Structured JSON Shape

```json
{
  "report_id": "EXT-YYYYMMDD-###",
  "reporter": "model-or-reviewer-name",
  "report_type": ["ARCHITECTURE_REVIEW"],
  "report_date": "YYYY-MM-DD",
  "repository": {
    "commit": "<commit-sha>",
    "baseline": "<baseline>"
  },
  "scope_reviewed": [],
  "files_reviewed": [],
  "evidence_coverage": {
    "repository": "FULL|PARTIAL|NONE",
    "files": "FULL|PARTIAL|NONE",
    "runtime": "FULL|PARTIAL|NONE",
    "external_systems": "FULL|PARTIAL|NONE",
    "history": "FULL|PARTIAL|NONE"
  },
  "findings": [],
  "contradictions": [],
  "missing_evidence": [],
  "risks": [],
  "recommended_actions": [],
  "confidence": "HIGH|MEDIUM|LOW",
  "limitations": [],
  "validation_performed": [],
  "unresolved_questions": [],
  "final_assessment": "PASS|PASS_WITH_WARNINGS|INTEGRITY_HOLD|FAIL|INSUFFICIENT_EVIDENCE"
}
```

# Compact Markdown Submission Shape

```text
REPORT ID:
REPORTER / MODEL:
REPORT TYPE:
DATE:
REPOSITORY COMMIT / BASELINE:

SCOPE REVIEWED:
FILES / ARTIFACTS REVIEWED:

EVIDENCE COVERAGE:
- Repository:
- Files:
- Runtime:
- External Systems:
- History:

FINDINGS:
- [ID] [SEVERITY] [STATUS] Evidence → Impact → Recommendation

CONTRADICTIONS:
- Source A ↔ Source B → Conflict → Impact → Resolution needed

MISSING EVIDENCE:

RISKS:

RECOMMENDED ACTIONS:

CONFIDENCE:
LIMITATIONS:
VALIDATION PERFORMED:
UNRESOLVED QUESTIONS:

FINAL ASSESSMENT:
```

# Intake Rule

ARGO MUST parse the report into structured findings before acting on recommendations.

The report itself is not an instruction to modify the Repository.

ARGO MUST independently verify material claims against current repository evidence before implementing changes.

# Multi-Model Comparison Rule

When several external models review the same baseline, ARGO should preserve each report independently and produce a comparison containing:

- Agreement
- Disagreement
- Unique findings
- Shared evidence
- Conflicting evidence
- Confidence differences
- Evidence gaps
- Proposed verification order

Consensus is not proof. A finding remains evidence-weighted until verified.

# Feedback Learning Boundary

External feedback may improve ARGO's understanding of recurring failure modes, review patterns and useful heuristics.

Such learning belongs to the applicable learning / memory domain unless explicitly promoted through canonical Governance authority.

Repeated external model feedback MUST NOT silently rewrite ARGO rules.

# Security / Privacy

External reports MUST NOT require disclosure of secrets, credentials, personal data or unnecessary confidential material.

Redacted evidence is acceptable when the redaction is declared as an evidence limitation.

# Authority Boundary

This standard governs the format and intake of external feedback. It does not grant external models authority over ARGO KOP.

# Related Documents

- `Core/CORE-003_CONSTITUTION.md`
- `Governance/GOV-005_REVIEW_STANDARD.md`
- `Governance/GOV-009_REPOSITORY_POLICY.md`
- `Governance/GOV-010_GOVERNANCE_MODEL.md`
- `Architecture/ARC-009_ARCHITECTURE_DECISIONS.md`
- `Architecture/ARC-010_EVOLUTION_MODEL.md`
- `Architecture/ARC-011_CANONICAL_ARCHITECTURE_MODEL.md`
- `Repository/REP-001_MASTER_INDEX.md`

---

# Guiding Statement

External feedback becomes useful when ARGO can distinguish exactly what was observed, what was inferred, what remains unknown and what must still be verified.

---

End of Document
