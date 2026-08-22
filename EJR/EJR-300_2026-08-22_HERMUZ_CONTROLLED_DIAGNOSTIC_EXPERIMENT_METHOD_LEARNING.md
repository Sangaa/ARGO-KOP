# EJR-300 — HERMUZ Controlled Diagnostic Experiment Method Learning

Date: 2026-08-22
Status: CLOSED — Diagnostic Method Captured / Governance Review Pending

## 1. Observation

Recent GitHub channel experiments showed that historical evidence can become a source of interpretive contamination, and that different observation surfaces can expose different parts of the same repository state.

## 2. Learning

A fresh, layered, controlled experiment is the preferred diagnostic method when prior learning does not resolve a material problem or when historical evidence may distort interpretation.

The experiment must not only test the intended result. It must inspect the repository broadly for traces of the operation, identify the first layer where observation diverges from prediction, and investigate unexpected changes causally.

## 3. Method

`Prior Learning → Bounded Simulation → Verified Gap → Fresh Baseline → Layered Test → Blind Repository Sweep → Causal Effect Review → Cleanup → Post-State Verification → Learning Assessment`

## 4. Why This Matters

An unexpected repository change is not automatically a harmless side effect. It is evidence that the actual operation may contain a mechanism omitted from the current model. The correct response is to trace the change back to the operation and update the model before classifying it.

## 5. Reusable Tool / Protocol

Captured as `Governance/GOV-015_HERMUZ_CONTROLLED_DIAGNOSTIC_EXPERIMENT_PROTOCOL.md`.

GOV-015 is currently proposed canonical and requires governance review before being treated as higher-authority methodology.

## 6. Test-Effectiveness Gate

A diagnostic test is not promoted merely because it succeeds. Reuse requires evidence of isolation, predefined hypothesis, layered observation, blind search where applicable, causal review, cleanup, reproducibility or material diagnostic value, and documented limitations.

## 7. Production Impact

NONE. No ARGO production semantics, P6 authority, relationship authority, or runtime evidence state was promoted by this learning capture.

## 8. Closure

The method is captured for future diagnostic use. The next applicable material problem should enter this method only after the GOV-013 prior-learning gate and bounded simulation fail to resolve it.
