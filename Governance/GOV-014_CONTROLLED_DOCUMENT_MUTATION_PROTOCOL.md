# GOV-014

---

# CONTROLLED DOCUMENT MUTATION PROTOCOL

Platform: ARGO KOP (Knowledge Operating Platform)
Document ID: GOV-014
Version: 1.0.1
Status: Canonical / Session-Approved Operating Pattern
Category: Governance / Repository Mutation
Canonical: Yes
Priority: Critical
Date: 2026-08-17

---

## 1. Purpose

Define a repository-safe mutation method for large or high-risk documents where direct full-file replacement can create content-loss, ordering, truncation, or unintended-change risk.

The protocol is designed for documents such as `REP-001`, and is reusable for any artifact whose mutation requires strict preservation of untouched content.

---

## 2. Governing Principle

A mutation is not the act of writing a new file.

A controlled mutation is a transaction:

**Read → Segment → Identify → Specify → Build Candidate → Validate → Commit → Re-read → Reconcile**

No step may be skipped merely because the requested change appears small.

---

## 3. Document Segmentation

Before mutation, the complete source document MUST be converted into an ordered Section Matrix.

Each section MUST have at minimum:

- stable Section ID;
- sequence/order;
- heading or semantic label;
- original content;
- original content hash;
- mutation flag;
- verification state.

Line numbers may be used as supporting evidence but MUST NOT be the sole section identity because line numbers change after mutation.

---

## 4. Mutation Matrix

The Mutation Matrix is the authoritative specification for the candidate document.

Minimum fields:

| Field | Meaning |
|---|---|
| Change ID | Unique mutation identifier |
| Section ID | Target section |
| Original Hash | Source content fingerprint |
| Action | KEEP / UPDATE / ADD / REMOVE |
| Expected Content | Required candidate state |
| Applied | Y/N |
| Verified | Y/N |
| Notes | Evidence or constraint |

A section marked `KEEP` is an explicit preservation requirement, not an absence of instructions.

---

## 5. Zero-Touch Rule

Any section marked `KEEP` MUST remain byte-for-byte/content-equivalent unless the mutation specification explicitly changes it.

For every untouched section:

`Original Hash == Candidate Hash`

Any unexpected difference MUST abort the mutation before commit.

---

## 6. Candidate Construction

The candidate document MUST be built from the complete Section Matrix and Mutation Matrix.

The candidate MUST contain:

- every required retained section;
- every approved update;
- every approved addition;
- every approved removal;
- original ordering unless reordering is explicitly specified.

The candidate is a temporary verification artifact and is not repository truth until committed and re-read.

---

## 7. Pre-Commit Validation

Before repository mutation, validate:

1. section count and ordering;
2. all required changes present;
3. all `KEEP` sections unchanged;
4. no unexpected additions;
5. no unexpected deletions;
6. identity/path consistency;
7. metadata consistency;
8. relationship/reference impact;
9. candidate-to-specification reconciliation.

Required condition:

**Unexpected Changes = 0**

---

## 8. Transaction Identity

Every controlled mutation MUST have a unique Transaction ID, for example:

`MUT-2026-08-17-REP001-001`

The transaction record MUST retain:

- target path;
- source commit/blob SHA;
- Section Matrix reference;
- Mutation Matrix reference;
- candidate specification;
- expected changes;
- pre-commit validation result;
- resulting commit SHA;
- post-commit validation result;
- final reconciliation status.

A controlled mutation MUST NOT be considered Matrix-compliant unless its Mutation Matrix artifact exists **before the repository write** and is linked to the transaction record.

A retroactive Matrix record may repair traceability after a historical gap, but MUST be explicitly labeled `RETROACTIVE RECONCILIATION` and MUST NOT be represented as proof that the original pre-write gate was satisfied.

---

## 9. Commit Boundary

Only a validated candidate may be committed.

A commit proves repository persistence only. It does not by itself prove semantic correctness.

---

## 10. Post-Commit Read-back

After commit, the actual repository file MUST be read again from the new HEAD.

The post-commit artifact MUST be compared against the Mutation Matrix.

Every required change MUST reach:

`Applied = Y`

and then:

`Verified = Y`

---

## 11. Final Reconciliation

Mutation closure requires:

- all required changes applied;
- all required changes verified;
- all untouched sections preserved;
- no unexpected changes;
- identity/path consistency maintained;
- downstream registry/index impact recorded;
- transaction status explicitly closed or blocked;
- Mutation Matrix transaction record preserved and linked.

A session MUST NOT claim the mutation is complete while any required row remains unresolved.

---

## 12. Abort Conditions

Abort before commit when any of the following occurs:

- incomplete source read;
- uncertain section boundary;
- candidate truncation risk;
- unexpected content difference;
- missing required field in mutation specification;
- source SHA mismatch;
- inability to perform post-commit read-back;
- unresolved identity/authority conflict that would be silently changed by the mutation.

An aborted transaction is evidence and MUST remain traceable.

---

## 13. Reuse Rule

This protocol applies to all high-risk document mutations, not only `REP-001`.

`REP-001` is the first intended application case because its size, authority and mutation sensitivity make it an appropriate validation target.

---

## 14. Relationship to Existing Governance

GOV-014 supplements, and does not replace:

- `GOV-013_HERMUZ_SESSION_BUILD_PROTOCOL.md`
- `GOV-013A_HERMUZ_BOOTSTRAP_INTEGRITY_GATE.md`
- applicable repository mutation and metadata governance.

The protocol preserves the existing authority hierarchy and does not grant semantic authority to a mutation tool or candidate file.

---

## 15. Learning Rule

A safe mutation method must be learned from repository failures and converted into a reusable control rather than retained only as session memory.

**Repository mutation safety is a system capability, not an operator memory task.**

---

End of GOV-014
