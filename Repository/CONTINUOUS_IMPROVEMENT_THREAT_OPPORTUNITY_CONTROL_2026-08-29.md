# ARGO Continuous Improvement — Threat & Opportunity Control

Date: 2026-08-29
Status: Active operational control / non-authoritative planning surface
Authority: does not override Core, Governance, evidence gates, or Room71 role boundaries

## Purpose

Turn continuous improvement into a closed control loop that attacks weaknesses, contains threats, and captures future opportunities without converting forecasts into authority.

## Control Loop

`OBSERVE → CLASSIFY → PRIORITIZE → EXPERIMENT/REPAIR → VERIFY → LEARN → STANDARDIZE → RE-SCAN`

Every cycle must preserve claim scope and evidence level. A failed control becomes learning evidence, not a hidden exception.

## Weakness / Threat Register

| ID | Weakness / threat | Current control | Residual state | Next safe action |
|---|---|---|---|---|
| T01 | external evidence may be self-asserted or pre-promoted | quarantine intake + resolver + explicit trust-transition guard | controlled to RESOLVED_UNAUTHENTICATED | require real provider-controlled trust anchor before authentication |
| T02 | orchestration may skip epistemic stages | executable explicit-edge transition guard | bounded closed | add future edges only with stage-specific evidence and adversarial tests |
| T03 | repository identity collisions / stale indexes | document-ID audit + migrated Governance IDs + synchronized REP-001/002 | Governance bounded closed | keep semantic identity audit in CI; never infer identity from headings/templates |
| T04 | tests may encode transitional wording instead of invariants | post-migration semantic assertion repair | controlled | prefer stable semantic state assertions; treat brittle-text failures as learning |
| T05 | protected mutation can escape its Mutation Matrix | same-change-set Matrix preflight | controlled | protected mutation must carry visible matrix in same CI diff |
| T06 | canonical-looking artifacts can be bulk-indexed without authority proof | per-domain authority classification | controlled | distinguish canonical+revalidated from reviewed+validation-pending |
| T07 | concurrent sessions can overwrite shared control state | repository-first re-entry + Room71 leases + serialized shared files | controlled but operational | discover live HEAD before every material write; reconcile before mutation |
| T08 | branch population can hide live/diverged work or invite destructive cleanup | classify before deletion; no bulk delete | open non-blocking | classify by ancestry/evidence and preserve diverged branches until reviewed |
| T09 | Governance provenance/identity correctness can be mistaken for substantive correctness | separate content-semantic review point | open | run claim-by-claim semantic review against current executable evidence |
| T10 | global Connected Baseline can be falsely inferred from bounded P4 closure | bounded-claim rule + relationship gates | open | close graph partitions only with bidirectional authority/consumer evidence |
| T11 | cognitive benefit can be asserted from architecture quality | explicit UNPROVEN state | open | controlled B0/L1/L2 novel-case experiment after evidence prerequisites |
| T12 | future plans can become accidental authority | this document is explicitly non-authoritative planning | controlled | promotion requires normal governance/evidence gates |

## Opportunity Register

| ID | Opportunity | Trigger / prerequisite | Capture plan | Proof required |
|---|---|---|---|---|
| O01 | provider-backed authenticity | concrete provider-controlled signature/API/attestation mechanism becomes available | implement isolated authentication stage + replay/key-rotation/wrong-content tests | provider provenance + execution evidence |
| O02 | automated Connected-Baseline partition closure | stable relationship registry and current authority graph | generate bounded partition work queue and close independently | bidirectional edges + consumers + CI |
| O03 | Governance content critic | identity layer stable | create separate semantic-review role/gate that evaluates claims, assumptions, expiry and contradictions | reproducible review rubric + independent evidence |
| O04 | branch evidence lifecycle automation | branch classification rules stabilized | build read-only branch classifier before any deletion capability | ancestry + merge/evidence disposition tests |
| O05 | cognitive-effect proof | evidence lifecycle can preserve independent model-run evidence | run blind B0/L1/L2 novel-case experiments | sealed inputs/outputs + independent scoring |
| O06 | Android/Kotlin product proof | repository baseline sufficiently stable | isolate learning/product project from Core authority; Product Proof → User Proof → Revenue Proof | executable app + tests + user evidence |
| O07 | external-model comparative learning | provenance and quarantine pipeline mature | ingest Copilot/Gemini/other outputs as untrusted evidence and compare boundedly | source binding + no auto-promotion |
| O08 | self-improving quality gates | repeated failure patterns accumulate | convert recurring failures into invariant-based regression gates | demonstrated recurrence prevention |

## Prioritization Rule

Use: `Risk reduction × evidence readiness × reversibility × future leverage`.

Priority order:
1. prevent illegal authority/trust transitions;
2. protect shared control-plane integrity;
3. close independently verifiable Connected-Baseline partitions;
4. review semantic content after identity stability;
5. automate hygiene only after safe classification;
6. run cognitive-benefit experiments only after evidence prerequisites;
7. exploit product/external-model opportunities without contaminating canonical authority.

## Stop Rules

- No simulated provider authenticity.
- No bulk branch deletion.
- No global baseline claim from bounded success.
- No promotion because a document is old, detailed, indexed, or frequently referenced.
- No opportunity roadmap item becomes authority without its normal evidence path.

## Continuous-Improvement Exit Criterion

There is no permanent `DONE` state for the improvement loop. A bounded weakness may close only when its control is executable or independently evidenced, regression-protected where practical, and residual risk is explicitly recorded. New observations reopen only the affected scope.
