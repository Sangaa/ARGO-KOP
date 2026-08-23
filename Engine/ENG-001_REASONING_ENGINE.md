# ENG-001

---

# REASONING ENGINE SPECIFICATION

---

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: ENG-001  
Version: 3.1.2  
Status: Integrity Hold / Revalidated  
Category: Engine  
Canonical: Yes  
Priority: Critical  
Last Audit Date: 2026-08-23  

---

# Purpose

The Reasoning Engine (`ENG-001`) serves as the primary cognitive reasoning component of ARGO KOP. Its purpose is to transform structured and unstructured inputs into explicit, testable interpretations, hypotheses and conclusions while preserving evidence state and uncertainty.

Reasoning is not assumed to be deterministic merely because the same conceptual pipeline is used. Reproducibility depends on the execution environment, model, inputs, configuration and applicable controls.

---

# Engine Processing Architecture

+-----------------------------------------------------------------------+
|                            INPUT BOUNDARY                             |
|    (Facts / Evidence / Context / Knowledge Objects / Constraints)     |
+-----------------------------------------------------------------------+
│
▼
+-----------------------------------------------------------------------+
|                    STAGE 1: OBSERVATION & PARSING                     |
|  - Ingests raw inputs via Context Engine (ENG-009)                    |
|  - Identifies explicit facts, claims, constraints and missing data   |
+-----------------------------------------------------------------------+
│
▼
+-----------------------------------------------------------------------+
|                   STAGE 2: INTERPRETATION & CORRELATION               |
|  - Maps information against applicable Knowledge Models               |
|  - Cross-references relevant memory where authorized                  |
+-----------------------------------------------------------------------+
│
▼
+-----------------------------------------------------------------------+
|                   STAGE 3: INFERENCE & VALIDATION                     |
|  - Produces explicit hypotheses and supporting evidence               |
|  - Sends validation candidates to Validation Engine (ENG-004)         |
+-----------------------------------------------------------------------+
│
▼
+-----------------------------------------------------------------------+
|                           OUTPUT SYNTHESIS                            |
|       (Structured Understanding / Decision Candidates / Audit Trail)  |
+-----------------------------------------------------------------------+

---

# Execution Matrix & Data Contracts

| Pipeline Phase | Primary Input | Processing Logic | Output Artifact | Upstream/Downstream Binding |
| :--- | :--- | :--- | :--- | :--- |
| **Observe** | Raw Context, User Prompts | Extract explicit facts, claims, constraints and evidence state. | Fact Set | Declared from `ENG-009` |
| **Interpret** | Fact Set | Map facts to applicable canonical definitions. | Interpretation Set | Declared against `Models/` |
| **Correlate** | Interpretation Set | Cross-link relevant constraints and authorized memory. | Relation Set | Declared against `ENG-008` and applicable governance |
| **Infer** | Relation Set | Generate testable hypotheses and candidate explanations. | Hypothesis Set | Declared toward `ENG-003` |
| **Validate** | Hypothesis Set | Submit claims for evidence and constraint validation. | Validation Candidate | `ENG-004` |
| **Conclude** | Validation Result | Synthesize conclusions and decision candidates without overstating certainty. | Reasoning Report | Declared toward `ENG-002` |

Declared bindings are not automatically certified integrations. Each dependency must be independently verified.

---

# Core Operating Rules & Constraints

1. **Fact Supremacy Principle:** Validated facts override assumptions when the two conflict.
2. **Claim-Dependent Evidence Precedence:** Evidence priority is determined by the claim type. For normative claims, applicable higher-authority ARGO governance prevails over lower-authority declarations. For identity, state, execution and provenance claims, direct current evidence of the target claim is preferred, followed by independently corroborating evidence, inspectable derived evidence, canonical declarations, historical evidence, and finally inference/assumption.
3. **No Scalar Authority Shortcut:** Authority, claim fitness, identity confidence, temporal validity, evidence independence and completeness MUST remain distinct dimensions. A newer, more detailed or more numerous low-authority observation cannot become normative authority merely through recency or volume.
4. **Evidence-Layer Separation:** Evidence from different stages of the same event must not be forced into a single PASS/FAIL interpretation. Repository state, run metadata, execution evidence, artifact metadata, artifact payload, derived correlation and governance/promotion decisions may legitimately coexist as different evidence layers.
5. **Contradiction Test:** A material `CONTRADICTION` exists only when the same claim, target, scope and relevant time/version are established and valid evidence asserts mutually exclusive outcomes. Textual difference alone is insufficient.
6. **Contradiction Is Not Resolution:** A contradiction is first recorded as a finding. The engine MUST then apply claim-specific authority/evidence precedence and trace propagation before declaring it resolved.
7. **UNRESOLVED Boundary:** When evidence required to align identity, scope, time, provenance or claim meaning is unavailable, or mutually exclusive same-claim evidence remains without legitimate precedence, the result MUST remain `UNRESOLVED`. The engine MUST NOT guess, promote or convert unresolved evidence into PASS/FAIL/CONNECTED.
8. **Derived Evidence Semantics:** A derived artifact proves what its producing calculation reported, subject to verification of its provenance and inputs. Transport, download, digest correlation or filename identity MUST NOT change the semantic conclusion emitted by the producer.
9. **Search Failure Boundary:** A negative result from one retrieval surface is provisional. When material, use independent retrieval; persistent disagreement or incomplete coverage remains an evidence discrepancy rather than silent absence.
10. **Missing Information Identification:** When logical gaps exist, the engine MUST explicitly output a `MISSING_DATA_WARNING` rather than inventing or silently filling missing facts.
11. **Uncertainty Preservation:** The engine MUST preserve meaningful uncertainty and distinguish fact, inference, assumption and recommendation.
12. **Audit Trace Requirement:** Conclusions must preserve an auditable summary of inputs, evidence references, assumptions, key inference steps and validation results. This does not require disclosure of private internal chain-of-thought.
13. **Authority Boundary:** `ENG-001` may reason over canonical material but does not grant or change canonical authority.
14. **Operational Candidate Rule:** The detailed evidence comparison matrix and conflict-resolution procedure is recorded in `Governance/GOV-018_EVIDENCE_REASONING_AND_CONFLICT_RESOLUTION.md` as an evidence-backed candidate rule. Until formally promoted, it is subordinate to existing Constitution/Governance authority.

---

# Evidence Conflict Decision Procedure

For every material evidence comparison, `ENG-001` SHOULD execute the following bounded sequence:

`Claim → Claim Type → Target Identity → Scope/Time/Version → Evidence Layer → Provenance → Proposition Alignment → Classification → Precedence → Propagation → Resolution`

Classification follows:

- **CONSISTENT / CORROBORATED** — same proposition, compatible scope/time, compatible outcome.
- **DIFFERENT EVIDENCE LAYERS** — observations concern different stages, dimensions or propositions and can coexist.
- **CONTRADICTION** — same proposition/target/scope/time with mutually exclusive outcomes.
- **UNRESOLVED** — required comparison evidence is missing/incomplete, identity or scope cannot be aligned, or a genuine contradiction cannot be safely resolved.

The engine MUST preserve the underlying evidence records and the reason for classification rather than storing only the final label.

---

# Current Certification State

**INTEGRITY HOLD / REVALIDATED**

The reasoning specification has been structurally revalidated, and the evidence-conflict reasoning rules have been incorporated as bounded operating logic. Repository-wide dependency and consumer certification remains open.

---

# Revision History

| Version | Date | Description | Author / Authority |
| :--- | :--- | :--- | :--- |
| 1.0.0 | 2026-07-01 | Initial Draft Architecture | ARGO Engineering |
| 3.0.0 | 2026-07-26 | Canonical Core Logic Release | ARGO Engineering |
| 3.1.0 | 2026-08-06 | Full Architecture Expansion & System Binding | ARGO Engineering / Principal Architect |
| 3.1.1 | 2026-08-09 | Revalidated authority, evidence, uncertainty, contradiction and audit-trace boundaries | ARGO Engineering / Repository Audit |
| 3.1.2 | 2026-08-23 | Incorporated claim-dependent evidence precedence, evidence-layer separation, contradiction qualification and UNRESOLVED boundary from GT-017 / GOV-018 candidate learning | HERMUZ / Repository Evidence Review |

---

End of Document
