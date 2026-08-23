# HORUS-REV-003 — World-Facing Truth Criteria

Date: 2026-08-23
Status: FOUNDATION / ANALYTICAL STANDARD
Owner: HORUS

## Purpose
Define how HORUS evaluates whether an ARGO learning claim corresponds to the world rather than merely to an internal record, tool response, or successful procedure.

## Core distinction

A repository record is evidence about what was recorded.
A tool response is evidence about what that tool exposed.
An experiment result is evidence about what that experiment observed.
None of these alone automatically proves a broader claim about the world.

## Truth-facing ladder

1. **Recorded** — a claim exists in the corpus.
2. **Observed** — a direct observation supports the claim within a defined context.
3. **Reproduced** — the observation can be repeated under stated conditions.
4. **Cross-validated** — independent evidence supports the same mechanism.
5. **Transferred** — the principle works in a new context without being specially fitted to the original case.
6. **Boundary-known** — counterexamples and applicability limits are identified.
7. **World-facing knowledge** — the claim has enough independent evidence and known boundaries to be treated as a reliable model for further reasoning.

## Anti-confusion rules

- Successful execution does not by itself prove the intended explanation.
- A tool's exposed capability is not identical to the provider's full capability.
- A search result is not the complete population unless exhaustiveness is established.
- An empty result is evidence about the observed surface, not global absence.
- Repeated records are not independent validation when they derive from the same underlying evidence.
- A rule demonstrated in one domain must not be promoted as universal without transfer evidence.
- A HORUS interpretation remains an interpretation until its evidence state is promoted through the validation path.

## Current application to HORUS candidate H-REV-002

The candidate principle is cross-domain supported, but autonomous ARGO transfer is not yet demonstrated. Therefore it must remain `CANDIDATE`, not `WORLD-FACING KNOWLEDGE`.

## Required future test

Present ARGO with a genuinely new problem where no explicit invocation of the candidate principle is supplied. Observe whether ARGO:

1. recognizes the observation boundary;
2. distinguishes local evidence from global claims;
3. seeks additional evidence before generalizing;
4. carries the principle into the new domain;
5. revises its conclusion when contradictory evidence appears.

Only this kind of behavioral evidence can distinguish stored rule recall from genuine transferable learning.

## Routing

Source: `HORUS-ANALYSIS`
Consumer: `ARGO`
Engineering relevance: `HERMUZ` may consume validated principles when they affect build reasoning, but HORUS does not execute engineering changes.
