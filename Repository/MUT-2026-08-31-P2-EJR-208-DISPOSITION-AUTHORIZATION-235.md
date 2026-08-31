# MUT-2026-08-31-P2-EJR-208-DISPOSITION-AUTHORIZATION-235

Status: OPEN / PREWRITE
Scope: Priority-2 disposition authorization for EJR-208 only.
Baseline: main@69f8c2649143c3c25589f3e20b68f026b3f2ca7b

## Evidence
Current deterministic MEMORY_TO_ROOT census (exact verified functional-head artifact from Lease233) classifies EJR-208 as a two-member MEMORY_EJR→ROOT_EJR ambiguity group with distinct content, zero external exact-ID references, and zero exact-member-path references.

Current members:
- RETAIN candidate: `Memory/Engineering_Journal/EJR-208_2026-08-14_P26_SESSION_CLOSURE.md`.
- DISPLACE candidate: `EJR/EJR-208_P2_REL003_CONTROLLED_MUTATION_PREPARATION_2026-08-17.md`.

Git path history proves Memory creation at `34b05a37c627956daea5ac5962363b8a17e12fc5` on 2026-08-14 and root creation at `98947c873eed9bfe0f294b47b143d05c83612cf8` on 2026-08-17. Full-source reads show both records are legitimate, semantically distinct engineering evidence. No reviewed evidence invalidates the earlier Memory allocation.

## Decision boundary
Applying the same bounded first-valid-allocation rule used by Plan204, this lease authorizes disposition for EJR-208 only:
- retain the earlier valid Memory EJR-208 allocation;
- classify the later root EJR-208 record as displaced and eligible for a new identity;
- preserve its semantic content and chronology;
- do not allocate a replacement until a separate complete-history vacancy proof returns VACANT;
- do not change census baseline 30 in this lease.

This is not repository-wide migration authority and does not authorize any other unresolved group.
