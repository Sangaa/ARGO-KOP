# ENG-009

---

# CONTEXT ENGINE SPECIFICATION

---

Platform: ARGO KOP (Knowledge Operating Platform)  
Document ID: ENG-009  
Version: 3.1.0  
Status: Approved  
Category: Engine  
Canonical: Yes  
Priority: Critical  
Last Audit Date: 2026-08-06  

---

# Purpose

The Context Engine (`ENG-009`) controls context window hydration, boundary enforcement, and prompt payload construction for ARGO KOP.

It enforces the **Absolute Repository Scope Isolation Fence**, stripping irrelevant external data while enriching inputs with required governance standards.

---

# Context Hydration Protocol

1. **Isolation Fence Enforcement:** Automatically filters out files outside `ARGO-KOP/`.
2. **Metadata Injection:** Hydrates incoming user prompts with relevant canonical definitions from `Standards/` and `Models/`.
3. **Token Optimization:** Summarizes historical execution traces while preserving critical decision vectors for `ENG-001`.

---

# Revision History

| Version | Date | Description | Author / Authority |
| :--- | :--- | :--- | :--- |
| 3.1.0 | 2026-08-06 | Context Hydration & Scope Isolation Upgrade | ARGO Engineering / Principal Architect |
9.