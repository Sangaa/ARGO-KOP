# EJR — OpenHands Execution Layer Decision — 2026-08-27

## Context

The current conversational-session limits are becoming a practical bottleneck for repository execution. OpenHands was evaluated conceptually as a candidate external execution layer, not as a replacement for HERMUZ.

## Decision

Proceed to a separate qualification session before installation/use. OpenHands is a candidate only until ARGO evaluates it.

## Architectural insight

The intended separation is:

`ARGO/HERMUZ = reasoning + memory + governance + evidence/judgment`

`OpenHands = candidate execution agent`

`Execution Gateway = controlled boundary between them`

`GitHub/Repository = source of truth`

This is an architectural separation, not a chatbot replacement strategy.

## Why this matters

If qualified, execution can continue through an external/local agent without making a single ChatGPT session the execution bottleneck. This also creates a real-world test of ARGO's ability to evaluate another agent and transfer its governance principles into a different execution environment.

## Trust principle

Installation does not equal trust. Access does not equal authorization. A successful task does not equal general capability.

Trust must be capability-specific and evidence-backed.

## Qualification sequence

`Identity → Read-only understanding → Observation/testing → Sandbox mutation → Branch mutation → Failure injection → Capability certificate`

Default state: `NOT AUTHORIZED`.

## Required review

Before any canonical repository execution, ARGO must review:

- identity/version/source
- workspace boundary
- model/provider
- permissions
- communication channel
- evidence behavior
- failure behavior
- Git discipline
- rollback/reversibility
- policy-boundary recognition

## Strategic learning

The next environment is deliberately treated as a laboratory. We are not rushing to market or competition. The purpose is to let ARGO encounter new engineering problems and test whether its principles generalize.

## Market/operational posture

OpenHands is an execution candidate. Hugging Face remains a potential source of open models/tools and an external observation environment. Neither is being designated a competitor or strategic dependency by this record.

## Session boundary

No installation, connection, repository mutation, or trust certification is authorized by this record. Those belong to the next dedicated qualification session.
