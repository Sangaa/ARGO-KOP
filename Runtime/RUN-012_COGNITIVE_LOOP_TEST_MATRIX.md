# RUN-012 — COGNITIVE LOOP TEST MATRIX

Platform: ARGO KOP
Document ID: RUN-012
Version: 1.1.0
Status: Candidate / Integrity Hold
Category: Runtime Test Contract
Priority: High
Date: 2026-08-23

---

# Purpose

Provide a compact acceptance matrix for the first cognitive runtime proof, including evidence comparison and protected uncertainty states introduced by GT-018/GT-020.

| Test | Expected proof | Failure signal |
| :--- | :--- | :--- |
| Context relevance | Only task-relevant state is selected | Irrelevant history dominates |
| Provenance | Material claims retain source references | Unsupported claims |
| Memory recall | Historical state is recovered with evidence | Generic answer without source |
| Fact / hypothesis separation | Uncertainty remains explicit | Hypothesis presented as fact |
| Decision boundary | Decision candidate contains rationale | Direct jump to action |
| Validation gate | Invalid candidate is held/rejected | Candidate proceeds |
| Authorization | Human approval is explicit | Implicit authorization |
| Safe action | Output remains non-destructive | External side effect |
| Failure handling | Missing context produces HOLD/uncertainty | Fabricated completion |
| Traceability | Full stage trace is preserved | Missing stage/provenance |
| Evidence precedence | Claim-dependent authority/fitness is applied | Newest/highest-numbered evidence wins without claim analysis |
| Evidence-layer separation | Different propositions/layers coexist without false conflict | Layer difference classified as contradiction |
| Contradiction qualification | Same claim/target/scope/time + mutually exclusive valid outcomes required | Textual difference alone classified as contradiction |
| Unresolved protection | Incomplete alignment or unresolved producer result remains UNRESOLVED | Engine guesses or promotes unresolved evidence |
| Evidence preservation | Original observations remain traceable after resolution | Resolution overwrites source observations |

# Evidence Comparison Test

For a material comparison, construct or retrieve two evidence observations and verify the reasoning sequence:

`Claim → Claim Type → Target → Scope/Time → Evidence Layer → Provenance → Proposition Alignment → Classification → Precedence → Resolution`

Expected classifications:

1. same proposition + compatible outcome → `CONSISTENT / CORROBORATED`;
2. different proposition or evidence stage → `DIFFERENT EVIDENCE LAYERS`;
3. same proposition + mutually exclusive outcomes → `CONTRADICTION`;
4. insufficient alignment/completeness or unresolved conflict → `UNRESOLVED`.

The evidence observations must remain preserved independently of the final reasoning result.

# Memory Recall Test

Retrieve a historical operational commitment using only bounded context and repository memory, then return:

1. answer;
2. source reference;
3. selected context;
4. confidence / uncertainty.

An answer without provenance does not pass.

# Regression Rule

Any implementation change affecting Context, Cognition, Decision, Validation, Evidence Reasoning or Runtime must rerun the applicable cases.

# Related Contracts

- `Runtime/RUN-011_COGNITIVE_LOOP_PROTOTYPE.md`
- `Engine/ENG-013_COGNITIVE_EXECUTION_LOOP.md`
- `Engine/ENG-014_COGNITIVE_LOOP_INTEGRATION_VALIDATION.md`
- `Cognition/COG-010_REASONING_PIPELINE_BOUNDARY.md`
- `Engine/ENG-001_REASONING_ENGINE.md`
- `Engine/ENG-004_VALIDATION_ENGINE.md`
- `Governance/GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md`
- `EJR/EJR-327_2026-08-23_GT020_MINIMAL_EVIDENCE_OBJECT_CONTRACT.md`

# Current Evidence Boundary

The added evidence-comparison cases are **TEST CONTRACT / STRUCTURAL**, not runtime execution proof.

Runtime verification requires an executable test path that actually constructs/consumes the EvidenceObservation contract and demonstrates the four classifications against controlled inputs.

Until that evidence exists, the runtime state remains `INTEGRITY HOLD`.

---

End of Document
