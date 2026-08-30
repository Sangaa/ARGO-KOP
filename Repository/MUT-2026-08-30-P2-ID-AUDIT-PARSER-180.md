# MUT-2026-08-30-P2-ID-AUDIT-PARSER-180

**Status:** CLOSED / EXECUTION-VERIFIED / PARSER GRAMMAR REPAIRED
**Baseline:** `main@9ab30264e937885833c814b850a58d21c77dd82a`
**Parent evidence:** `Repository/MUT-2026-08-30-P2-ID-AUDIT-COVERAGE-179.md`

## Gap proved before mutation

Priority-2 audit expansion 179 executed and GitHub Actions run `33290249900`, job `99200522544`, failed at `Run internal Document-ID audit`; M2 succeeded on the same HEAD.

Direct source inspection proved the expanded heading fallback was over-broad: `PROJECT_STATUS.md` declares `Document ID: PROJECT_STATUS`, while its human title begins `# ARGO KOP — Current Project Status`. The generic heading regex accepted the token `ARGO` as a document identity, producing a parser false positive rather than a repository identity collision.

## Repair applied

Namespace independence was preserved while requiring a structural document-ID shape for H1 fallback. A heading identity candidate must contain a namespace token followed by a numeric document sequence (for example `REL-001`, `GOV-013A`, `BOOTSTRAP-001`) instead of accepting any uppercase title word. Explicit `Document ID:` remained primary.

Regression coverage proves:

- a human H1 such as `ARGO KOP` does not become an identity token;
- a previously unseen structural namespace can still be discovered without an allowlist.

Lease 180 then exposed a different downstream failure family rather than the original parser-overreach problem. That new evidence was correctly handed to 181/182 instead of weakening the grammar.

## Boundaries preserved

No Core, Governance, Runtime, Engine, Services, Interfaces, Knowledge, Release, REP-001/002/014, or Room71 authority surface was mutated by the parser repair. No branch deletion or force ref mutation occurred.

## Verification chain

The final identity-source implementation on `e04b073f268aa1291bbb747429d92ac69d83e9ec` preserves the 180 regressions and passed:

- Internal Document-ID Audit `33298557071`
- Full-Stack Repository Audit `33298557075`
- ARGO Runtime Prototype and Integration Tests `33298557080`
- M2 Multi-Channel Proposal Training `33298557081`

All four concluded `SUCCESS` on the same head.

## Learning

`GENERIC PARSING != UNCONSTRAINED PARSING`

A generic detector should generalize the grammar of identity, not accept arbitrary surface text as identity.

`A REPAIR THAT REVEALS A DIFFERENT FAILURE IS PROGRESS IF THE ORIGINAL FAILURE CLASS IS REGRESSION-LOCKED AND THE NEW FAILURE IS PRESERVED AS NEW EVIDENCE.`

Final lease state:
`P2_ID_AUDIT_PARSER_180 = CLOSED / EXECUTION-VERIFIED`.
