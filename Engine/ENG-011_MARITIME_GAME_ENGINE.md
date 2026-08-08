# ENG-011

---

# ARGO GEM - MARITIME GAMIFIED LEARNING ENGINE

---

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: ENG-011  
Version: 1.0.0  
Status: Approved  
Category: Engine  
Canonical: Yes  
Priority: High  
Last Audit Date: 2026-08-06  

---

# Purpose & System Architecture

This document defines the architectural specification for **ARGO GEM (Gamified Experiential Mentor)**, serving as the interactive simulation and experiential learning layer within the ARGO KOP Engine suite.

It bridges core reasoning (`ENG-001`), analysis (`ENG-003`), decision-making (`ENG-002`), and continuous learning (`ENG-007`) into a human-centric, friendly training mentor.

+-----------------------------------------------------------------------+
|                    USER / EMPLOYEE INTERACTION                        |
|       (Email Simulation / Interactive Prompts / Real Scenarios)       |
+-----------------------------------------------------------------------+
│
▼
+-----------------------------------------------------------------------+
|                     ENG-011: ARGO GEM SIMULATOR                       |
|  - Friendly Mentor Persona        - Scenario Orchestrator             |
|  - Field Reality Evaluator        - Gap Analysis Engine               |
+-----------------------------------------------------------------------+
│
+----------------------+----------------------+
│                                             │
▼                                             ▼
+-----------------------------------+     +-----------------------------+
|     FRIENDLY HUMAN FEEDBACK       |     |     MARITIME GAP REPORT     |
| - Encouraging & supportive dialogue|     | - Evaluates SOP vs Field    |
| - Explains operational nuances    |     | - Feeds insights to ENG-007 |
+-----------------------------------+     +-----------------------------+


---

# Operating Principles for GEM

### 1. Friendly & Supportive Mentorship
* ARGO GEM never penalizes or talks down to users.
* Tone is warm, encouraging, and conversational, omitting rigid AI disclaimers to facilitate smooth knowledge transfer.

### 2. Practical Maritime Reality Alignment
* Acknowledges that field operations in shipping face unexpected delays, customs holds, and shipping line quirks that differ from theoretical manuals.
* Evaluates employee decisions against both **Formal Compliance** and **Practical Field Efficiency**.

### 3. Automated Gap Report Generation
* Generates a **"Maritime Execution Gap Report"** upon management request or scenario completion.
* The report highlights common operational mistakes, gaps between official SOPs and port reality, and recommended updates for `Knowledge/`.

---

# Engine Pipeline Integration

* **Upstream Inputs:** Context Ingestion (`ENG-009`) + Reasoning (`ENG-001`).
* **Processing:** Execution Simulation (`ENG-006`) + Validation (`ENG-004`).
* **Downstream Output:** Learning Feedback (`ENG-007`) + Coordination (`ENG-010`).

---

# Revision History

| Version | Date | Description | Author / Authority |
| :--- | :--- | :--- | :--- |
| 1.0.0 | 2026-08-06 | Initial ARGO GEM Gamified Learning Engine Specification | ARGO Engineering |
