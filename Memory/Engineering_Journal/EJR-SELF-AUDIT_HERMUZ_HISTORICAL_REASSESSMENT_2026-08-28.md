# HERMUZ Historical Self-Audit & Assumption Reassessment

Date: 2026-08-28
Protocol: GOV-013
Scope: historical reconstruction of HERMUZ decisions, assumptions, evidence discipline, and current architectural debt
Status: `ANALYSIS COMPLETE / DOCUMENTED / NO FUNCTIONAL MUTATION / NO PROMOTION`

## 1. Why this exists

This is a dedicated self-audit record for HERMUZ. The purpose is not to defend prior decisions. It is to identify which decisions remain valid, which were locally correct but are now obsolete, and where HERMUZ introduced or preserved assumptions that should no longer be trusted.

The audit deliberately treats prior HERMUZ output as fallible evidence. Repository reality outranks conversation memory and prior reports.

## 2. Existing self-audit surface

A repository search found several audit and self-assessment records, including `EJR-001_SELF_ASSESSMENT_AND_MARKET_FEEDBACK.md`, `EJR-005_POST_SESSION_AUDIT_REPAIR.md`, `EJR-015_PRE_FAILURE_MUTATION_AUDIT.md`, `EJR-220_MUTATION_INTEGRITY_AUDIT_AND_PREVENTION.md`, and `EJR-230_FULL_STACK_AUDIT_CHECKPOINT.md`.

These prove that self-audit activity already existed. However, no single canonical HERMUZ record was found that performs the broader historical reassessment requested here: decisions across the build, their current validity, assumption failures, and the architectural consequences of the accumulated history.

Therefore this document establishes that missing synthesis layer. It does not replace the earlier records.

## 3. Historical judgment

### 3.1 Decisions that remain valid

1. **Repository reality outranks conversational memory.**
   This remains foundational. The P430 archaeology confirmed that historical summaries can become stale while the repository continues evolving.

2. **Do not treat PASS, NO RUN, or source inspection as interchangeable.**
   This distinction materially improved evidence quality and remains valid.

3. **Exact-HEAD attribution is required for strong execution claims.**
   This remains valid and was necessary to establish the real provider-backed E2E result.

4. **Do not promote relationships merely because a candidate seam exists.**
   Contract, consumer, runtime, and governance evidence remain separate concerns.

5. **Minimal mutation before proof is preferable to broad speculative implementation.**
   The B07/B08 work demonstrated that focused seams and isolated execution produced better evidence than importing a divergent historical PR wholesale.

6. **Production side effects must not be inferred from simulated traces.**
   The distinction between simulated execution and real provider-backed execution remains architecturally important.

7. **Provenance must survive correction.**
   The REP-identifier correction demonstrated that fixing provenance should preserve history rather than erase it.

### 3.2 Decisions that were locally reasonable but became liabilities

1. **Continuing to use PR #64 as the long-lived diagnostic/promotion surface.**
   It was reasonable when the PR was a narrow probe. It became a liability once implementation, tests, workflow changes, evidence, and dozens of checkpoint records accumulated on the same branch.

2. **Treating every successful checkpoint as a natural next construction step.**
   This created a tendency toward checkpoint momentum. A successful proof should trigger a priority reassessment, not automatically another mutation.

3. **Using repeated session deltas as the primary navigation mechanism.**
   Strong raw provenance is valuable, but chronology alone is a poor architectural index once the history becomes large.

4. **Allowing evidence machinery to grow alongside the experimental branch without a periodic compression boundary.**
   The machinery improved trust but increased review complexity and made the promotion unit harder to see.

5. **Delaying repository-wide architectural reassessment until after many local proofs.**
   The P430 archaeology shows that this should happen earlier whenever a narrow seam consumes many checkpoints.

## 4. Assumptions that HERMUZ should no longer trust

### A-001 — “The next unresolved gate is automatically the highest-value next task.”

Status: `REJECTED`

Why: a gate can remain technically unresolved while the repository's higher-level priorities have changed. P430 exposed this through the growing focus on RUN-010/SRV-009.

### A-002 — “More evidence is progress.”

Status: `REJECTED`

Why: evidence is valuable only when it reduces an actual uncertainty or authorizes a decision. Repeating already-proven execution without changing the decision boundary becomes evidence accumulation.

### A-003 — “A mergeable PR is a promotion-ready PR.”

Status: `REJECTED`

Why: GitHub mergeability is a platform state, not governance authorization.

### A-004 — “A clean isolated experiment can remain the same promotion unit indefinitely.”

Status: `REJECTED`

Why: isolation is temporal and purpose-bound. A diagnostic branch can become a debt container if its lifecycle is not explicitly bounded.

### A-005 — “A large provenance record is self-explanatory.”

Status: `REJECTED`

Why: raw chronology preserves evidence but does not automatically preserve architectural meaning. Synthesis/index layers are necessary.

### A-006 — “Historical decisions remain valid because they passed their contemporary tests.”

Status: `REJECTED`

Why: a decision can be correct under an earlier architecture and obsolete under a later one. Validity must be reassessed against current-main contracts and goals.

## 5. Where HERMUZ was wrong or insufficient

This section intentionally records failures without defensive reinterpretation.

1. HERMUZ repeatedly followed the immediate checkpoint path too literally after the work had already demonstrated that the remaining blocker was governance/consolidation rather than missing runtime behavior.

2. HERMUZ allowed the distinction between “new learning” and “failure to apply existing learning” to become blurred in reporting. The user's correction was valid: an existing lesson not applied is a process failure, not automatically a new lesson.

3. HERMUZ sometimes treated the absence of a workflow run as a reason to create another trigger/mutation before fully proving whether the execution surface itself was the actual bottleneck. The later P420 result proved the E2E path, but the earlier sequence was not optimally economical.

4. HERMUZ over-relied on checkpoint numbering as an organizing structure. The result was strong chronology but weaker architectural compression.

5. HERMUZ did not perform the repository-wide pause early enough. P430 became necessary precisely because local correctness had begun to obscure global direction.

6. HERMUZ should have recognized sooner that the promotion question had changed from “does the seam work?” to “what exactly should be promoted, and in what unit?”

## 6. Decisions requiring change now

### C-001 — Replace checkpoint momentum with priority gates

Future checkpoint continuation must require a demonstrated current Gap. A prior checkpoint's “next step” is a candidate, not an instruction.

### C-002 — Introduce promotion-unit thinking

Functional code, tests, workflow support, evidence, and historical records must be classified separately before a long-lived experimental branch is promoted.

### C-003 — Preserve raw history but add synthesis

Do not delete session records to reduce noise. Add architectural summaries, debt maps, decision ledgers, and assumption audits above them.

### C-004 — Reassess architecture after major proof milestones

A real provider-backed E2E proof is a milestone that should trigger a repository-wide priority review before another local seam is expanded.

### C-005 — Separate authority from evidence explicitly

Evidence can prove a technical fact. It cannot manufacture the governance authority required to promote that fact.

## 7. What remains uncertain

This audit is not a claim that every historical commit and every decision has been individually re-read line-by-line. It is a cross-layer historical reassessment grounded in the repository's audit records, HERMUZ records, the P430 archaeology, current promotion state, and representative historical control-plane artifacts.

Therefore the following remain `OPEN / NEED DEEPER LEDGER REVIEW`:

- complete per-commit classification of every PR #64 file;
- complete reconciliation of all historical assumptions against current-main;
- whether any older canonical rule is now redundant but still referenced;
- whether the accumulated evidence archive should live partly outside the promotion branch.

These uncertainties are explicitly retained rather than silently converted to conclusions.

## 8. Architectural conclusion

HERMUZ's most durable achievement is not the individual B07/B08 seam. It is the evolution of a disciplined evidence model:

`memory → repository evidence → contract → test → exact HEAD → governed execution → runtime proof → promotion authority`

The principal failure mode is now the inverse:

`proof → more proof → more checkpoints → branch accumulation`

The correction is therefore not “build faster.” It is to make **reassessment and compression first-class engineering operations**.

## 9. Future rule for HERMUZ

Before any future functional mutation, HERMUZ should answer four questions:

1. What current repository Gap exists now?
2. Which prior decision or assumption is this action relying on?
3. Has that decision been revalidated against the current architecture?
4. What is the smallest action that can change the decision state?

If any answer is unknown, analysis continues before mutation.

## 10. Relationship to the new repository question

A separate repository is **not justified merely to escape accumulated history**. The current repository still contains the authoritative provenance and the technical evidence.

A new repository becomes justified only if the future promotion architecture requires a clean product/canonical surface that cannot be safely derived through a governed consolidation of the existing branch. That decision should follow the complete PR classification and promotion-unit design, not precede it.

## 11. Close

`HERMUZ SELF-AUDIT = ESTABLISHED`
`HISTORICAL REASSESSMENT = COMPLETE AT CROSS-LAYER LEVEL`
`KNOWN WRONG ASSUMPTIONS = RECORDED`
`CURRENT VALID PRINCIPLES = RETAINED`
`OBSOLETE/LIABLE DECISIONS = IDENTIFIED`
`FUNCTIONAL MUTATION = NONE`
`PROMOTION = NONE`

Next safe action: classify the full promotion surface before deciding whether to consolidate in ARGO-KOP or establish a clean successor repository.
