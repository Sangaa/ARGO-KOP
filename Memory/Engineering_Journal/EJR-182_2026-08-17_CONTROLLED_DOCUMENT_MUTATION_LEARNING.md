# EJR-182

---

# CONTROLLED DOCUMENT MUTATION LEARNING

Platform: ARGO KOP  
Document ID: EJR-182  
Date: 2026-08-17  
Category: Engineering Learning / Repository Integrity
Status: Validated Operational Lesson
Scope: Large-document mutation / REP-001 / governed write safety

---

## 1. Trigger

During continued repository construction, `REP-001` became the clearest example of a mutation-risk boundary: the available write channel replaces the full file, while the requested changes are usually small and localized.

## 2. Observed Problem

Direct full-file replacement creates unnecessary risk of:

- dropped content;
- reordered sections;
- unintended edits to untouched material;
- truncation;
- inability to prove that every requested change reached the final file.

## 3. User-Proposed Solution

Create an ordered reading matrix for the entire file, then create a mutation matrix containing both:

- sections that MUST change;
- sections that MUST remain unchanged.

Each mutation row carries a flag and is rechecked after the candidate document is built and after the final repository write.

## 4. Engineering Assessment

The proposal is accepted and generalized into `GOV-014_CONTROLLED_DOCUMENT_MUTATION_PROTOCOL.md`.

The key improvement is to treat the matrix as an **Executable Mutation Specification**, not merely a checklist.

The candidate file is built from the matrix, verified against the original, committed only after pre-commit validation, and then read back from the repository for final reconciliation.

## 5. New Learning

For a high-risk document mutation:

**KEEP is an explicit preservation requirement.**

Untouched sections require hash/content equality between source and candidate.

The mutation is closed only when every required change is `Applied=Y` and `Verified=Y`, while every untouched section remains unchanged.

## 6. Root-Cause Prevention

This converts mutation safety from model/operator memory into a repository-level procedure that can be reused across sessions and by future models.

The procedure is intended to prevent recurrence of the earlier REP-001 mutation boundary and any equivalent issue in other large authoritative documents.

## 7. First Application

`REP-001` is the first planned full application of GOV-014.

The protocol itself is documented now; the REP-001 mutation has **not** yet been performed under the new protocol.

## 8. Session Handoff Requirement

The next session MUST NOT modify `REP-001` using the old direct full-file replacement method.

It must begin by constructing:

1. Section Matrix;
2. Mutation Matrix;
3. Candidate build;
4. Pre-commit comparison;
5. Controlled commit;
6. Post-commit read-back;
7. Final reconciliation.

---

End of EJR-182
