# ARGO System Logs

## Purpose

The Logs directory maintains the authoritative record of:
- Major decisions made in the system
- Changes to governance and architecture
- System reviews and evaluations
- Historical context and rationale

## Directory Structure

```
Logs/
├── Decisions/           [Major decision records]
├── Changes/             [System changes and updates]
├── Reviews/             [Periodic system reviews]
├── Archive/             [Historical logs]
└── README.md            [This file]
```

## Using the Logs

### Finding Decisions
Look in `Logs/Decisions/` using the decision ID (e.g., DECISION-2026-001)

### Tracking Changes
Refer to `Logs/Changes/` for system updates and their rationale

### Understanding Evolution
Review `Logs/Reviews/` for periodic assessments of how the system is working

## Adding to Logs

When making significant changes:

1. Document the decision or change
2. Include clear rationale
3. Reference any related items
4. Add to appropriate logs directory
5. Update this README if new log types are created

## Log Entry Format

```markdown
# [Type]: [Title]

Date: YYYY-MM-DD
ID: [DECISION-YYYY-###]
Author: [Name]
Status: [Active | Superseded | Archived]

---

[Content]

---

Related Items: [Links to related decisions/changes]
```

## Status
Established: Foundation Build 001
Created: 2026-07-26
