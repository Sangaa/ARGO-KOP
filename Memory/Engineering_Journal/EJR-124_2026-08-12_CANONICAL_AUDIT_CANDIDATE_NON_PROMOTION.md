# EJR-124 — Canonical Audit Candidate Non-Promotion Guard

**Date:** 2026-08-12
**Status:** CLOSED

## Purpose
Strengthen the boundary between candidate discovery and verified seam certification before assembling the first canonical evidence set.

## Change
Added a regression test proving that candidate artifacts discovered by the canonical scanner remain PARTIAL/candidate provenance and cannot promote a seam to CONNECTED.

## Evidence Rule
Candidate provenance is navigation context only. A seam requires an explicit verified registry record plus materialized contract, test, and trace artifacts before the canonical audit may report CONNECTED.

## Why This Checkpoint Is Conservative
No production seam was promoted. No new runtime layer was introduced. The change only prevents a future regression in the certification boundary.

## Next Step
Inspect the highest-value unresolved seam using the preserved candidate provenance, then assemble one actual-runtime evidence set and validate it through loader, registry, and canonical audit in sequence.
