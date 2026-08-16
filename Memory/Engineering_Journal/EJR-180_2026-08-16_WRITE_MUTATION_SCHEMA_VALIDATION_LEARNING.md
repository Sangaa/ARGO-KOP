# EJR-180

---

# WRITE MUTATION SCHEMA VALIDATION LEARNING

Platform: ARGO KOP  
Document ID: EJR-180  
Date: 2026-08-16  
Category: Engineering Learning  
Status: Validated Operational Lesson  
Scope: Repository mutation / governed write tooling

---

## Trigger

During a governed repository mutation, the write payload was prepared correctly but the tool invocation omitted a required `message` field. The mutation was rejected before any repository write occurred.

## Observed Fact

The write tool schema is itself a precondition boundary. A mutation is not considered attempted merely because content has been prepared; the complete tool contract must validate before the repository is touched.

## Root Cause

The mutation workflow validated file existence, content and current SHA, but the invocation payload was not validated against the complete tool schema before dispatch.

## Learning

The governed write sequence must include two distinct preconditions:

1. **Repository-state validation** — existence, current SHA, ownership, necessity and intended Create/Update route.
2. **Mutation-schema validation** — all required tool arguments are present and valid before dispatch.

A failure in either precondition must result in **no repository mutation**.

## Operational Rule

**Never treat a prepared mutation as executable until both repository-state and tool-schema preconditions have passed.**

## Evidence Boundary

This lesson does not grant any tool authority and does not replace the repository write contract. It is a reusable operational rule for future governed mutations.

## Revalidation Requirement

When a new connector or write tool is introduced, its complete schema must be inspected before use. The existence/Create/Update decision remains separate from tool invocation validation.

---

End of Document
