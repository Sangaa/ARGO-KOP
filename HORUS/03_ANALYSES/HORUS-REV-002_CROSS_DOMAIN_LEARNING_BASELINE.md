# HORUS-REV-002 — Cross-Domain Learning Baseline

Date: 2026-08-23
Status: ANALYSIS / CANDIDATE SYNTHESIS
Owner: HORUS
Branch: horus/meta-learning-foundation-v6

## Purpose
Test whether the candidate principle from HORUS-REV-001 is broader than GitHub Connector behavior by comparing independent learning evidence already present in ARGO's corpus.

Candidate under test:

> The meaning of an observation is bounded by the surface, identity, scope and contract through which it was obtained.

## Evidence reviewed

### A. GitHub Connector training
GT-010 and GT-011C repeatedly distinguish bounded search results, exact retrieval, schema contracts, evidence classes, identity validation, and downstream ID-dependent observation. These establish strong evidence for the candidate inside the GitHub Connector domain.

### B. Programming / Python learning boundary
The programming knowledge domain explicitly requires `Source → Extraction → Concepts → Evidence → Validation → Practice/Test → Experience → Promotion Candidate → Governed Knowledge`. It also states that merely reading or uploading a programming source does not establish learning. This is an observation-boundary rule: the source surface is not equivalent to validated learned knowledge.

### C. Synthetic programming experiment
The executable-function experiment distinguishes source concepts from observed execution and explicitly limits the conclusion: validating a small function does not prove that every function should be small, pure, or single-purpose. This is direct evidence that observation scope constrains generalization.

### D. Multi-channel training
M1-M5 preserve task/channel identity, workspace isolation, provenance, conflict quarantine and explicit reconciliation. The record explicitly says that parallel work does not imply shared authority and that provenance must precede cross-source reconciliation. This provides a second non-GitHub engineering domain where identity, scope and provenance bound interpretation.

### E. False-positive audit hardening
The audit record demonstrates that the first 79 findings were not treated as truth: evidence extraction rules were narrowed, syntactic context was distinguished from prose/string content, and the initial candidate set was explicitly forbidden from becoming a final gap list without independent verification.

## Cross-domain comparison

| Domain | Observation boundary | Identity/scope control | Generalization restraint |
|---|---|---|---|
| GitHub | connector operation / result surface | exact repo, ref, path, run ID | bounded result ≠ global absence |
| Programming learning | source → practice/test | evidence/source location | experiment validates concepts, not universal design law |
| Multi-channel | task/channel/source provenance | isolated workspace and source identity | parallel work ≠ shared authority |
| Audit | parser/syntax evidence | actual Markdown/AST context | candidate finding ≠ confirmed defect |

## HORUS interpretation

The evidence is no longer confined to GitHub. A recurring mechanism appears across at least four domains:

**An observation acquires meaning only within its evidence boundary; crossing that boundary requires additional evidence rather than assumption.**

This is stronger and more general than the original GitHub wording because the same mechanism governs learning validation, execution experiments, multi-source reconciliation, and repository auditing.

## Important distinction

The evidence supports a meta-learning principle about interpretation and evidence, not a claim that ARGO has developed this principle autonomously. The current corpus shows that ARGO/HERMUZ records and applies related rules. Whether ARGO can independently transfer the principle to a novel domain remains unproven.

## Candidate refinement

Previous candidate:
`Observation is bounded by surface, identity, scope and contract.`

HORUS refined candidate:
`Evidence meaning is bounded by the observation boundary; transfer beyond that boundary requires independent supporting evidence.`

## Validation status

State: `CANDIDATE / CROSS-DOMAIN SUPPORTED`

Not yet `PROMOTED`.

Remaining test:
- observe whether ARGO independently invokes this principle in a genuinely new, non-GitHub/non-audit task;
- distinguish explicit rule recall from spontaneous transfer;
- test whether contradictory evidence causes ARGO to revise the interpretation.

## Knowledge value

If independently transferred, this candidate could become a high-level ARGO reasoning principle because it governs how ARGO should interpret search, experiments, memory retrieval, tests, external evidence and cross-domain learning.

## Routing

Source: `HORUS-ANALYSIS`
Potential consumers: `ARGO`, `HERMUZ`
Current handoff eligibility: `NO — validation of autonomous transfer remains outstanding.`
