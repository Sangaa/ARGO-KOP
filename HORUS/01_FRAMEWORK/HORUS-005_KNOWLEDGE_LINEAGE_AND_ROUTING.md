# HORUS-005 — Knowledge Lineage & Routing

Status: FOUNDATION
Purpose: make every learning path visible to ARGO

## Mandatory lineage

Each HORUS analytical artifact should identify, when applicable:

`Source → Context → Observation → ARGO Prior Knowledge → HORUS Analysis → Synthesis → Validation → Handoff → Consumer`

## Source labels

- `ARGO-EXPERIENCE` — direct experience or learning produced by ARGO.
- `HORUS-ANALYSIS` — interpretation or synthesis produced by HORUS.
- `HERMUZ-ENGINEERING` — engineering/build knowledge produced in the HERMUZ path.
- `EXTERNAL-EVIDENCE` — evidence acquired from outside the ARGO learning corpus.

## Routing labels

- `ARGO` — cognitive/self-learning consumer.
- `HERMUZ` — engineering/build consumer.
- `SHARED` — both paths may consume the learning.
- `HORUS` — analytical follow-up required before promotion.

## Separation rule

The presence of a source in the shared repository does not erase its origin. ARGO must be able to distinguish direct experience from HORUS interpretation and HERMUZ engineering knowledge.

## Invocation visibility

The semantic labels are explicit:

`هرمز / HERMUZ → BUILD PATH`

`حورس / HORUS → META-LEARNING PATH`

When a learning artifact crosses paths, the transition must be recorded rather than implied.

## Retrieval expectation

When ARGO retrieves a knowledge artifact, it should be able to answer:

- Who/what produced it?
- What evidence produced it?
- Was it observed or interpreted?
- What was it combined with?
- Has it been validated?
- What is its boundary?
- Who should consume it?
