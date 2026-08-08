# ARGO Knowledge Organization Specification

## Version: 3.0.1
Status: Foundation Specification / Integrity Hold
Category: Operational Specification
Last Audit: 2026-08-08

---

## Scope

This specification defines operational guidance for organizing knowledge artifacts inside ARGO KOP.

It is an **operational specification**, not the canonical authority for the platform's knowledge-object schema. `Models/MOD-001_KNOWLEDGE_MODEL.md` defines the canonical conceptual knowledge model, while applicable Governance documents define approval and authority rules.

Where this specification conflicts with a newer canonical model, governance rule, repository map, or explicit authority decision, the applicable higher authority prevails and the conflict must be recorded and resolved.

---

## Knowledge Classification

### Tier 1: Foundational Knowledge
**Characteristics:**
- Core principles and values
- Fundamental facts about ARGO
- Non-negotiable rules
- Essential frameworks

**Typical Storage:** Governance/ and Architecture/ directories
**Update Frequency:** Rarely (requires governance approval)
**Validation:** High (multiple reviews)

### Tier 2: Operational Knowledge
**Characteristics:**
- Documented processes
- Proven practices
- Guidelines and standards
- Reusable patterns

**Typical Storage:** Specifications/, Engine/, Services/, Models/, Runtime/ and other explicitly governed operational paths
**Update Frequency:** Periodically (quarterly or as needed)
**Validation:** Medium (peer/technical review appropriate to the artifact)

### Tier 3: Domain Knowledge
**Characteristics:**
- Facts within specific domains
- Analysis and insights
- Research findings
- Subject-matter expertise

**Typical Storage:** Knowledge/ directory, organized according to the active repository structure
**Update Frequency:** Regularly (as new knowledge emerges)
**Validation:** Medium-High (based on domain standards)

### Tier 4: Exploratory Knowledge
**Characteristics:**
- Preliminary research
- Hypotheses and theories
- Emerging patterns
- Speculative content

**Typical Storage:** Projects/ directory or dedicated exploratory folders where explicitly governed
**Update Frequency:** Frequently (ongoing investigation)
**Validation:** Low-Medium (marked as provisional)

Classification tier and physical storage path must not be treated as interchangeable authority claims.

---

## Knowledge Organization Structure

### Knowledge/ Directory Organization

```
Knowledge/
├── Domain-1/
│   ├── Overview.md
│   ├── Core-Facts.md
│   ├── Analysis.md
│   ├── References.md
│   └── SubDomains/
│       ├── SubDomain-A/
│       └── SubDomain-B/
├── Domain-2/
└── Domain-3/
```

This is an organizational example, not evidence that every example artifact exists in the current repository.

### Domain Structure Requirements

**1. Overview.md**
- Domain name and purpose
- Scope and boundaries
- Key concepts
- Related domains

**2. Core-Facts.md**
- Verified facts about the domain
- Data and evidence
- Established truths
- Sources and citations

**3. Analysis.md**
- Interpretation of facts
- Patterns and insights
- Conclusions and recommendations
- Limitations and uncertainties

**4. References.md**
- Source citations
- Related documents
- External resources
- Methodology documentation

---

## Content Standards

### Metadata Requirements

Every knowledge document must include:

```markdown
# Document Title

## Domain: [Domain Name]
Category: [Category]
Status: [Verified | Provisional | Exploratory]
Author: [Name]
Date Created: [YYYY-MM-DD]
Last Updated: [YYYY-MM-DD]
Next Review: [YYYY-MM-DD]

---

[Content]

---

## Sources & References
- [Citation 1]
- [Citation 2]

## Related Documents
- [Related Doc 1]
- [Related Doc 2]
```

Metadata requirements remain subject to `Governance/GOV-004_DOCUMENT_METADATA.md` and applicable document authority.

### Content Organization

**Facts Section:**
```markdown
## Verified Facts
- Fact 1 (Source: ...)
- Fact 2 (Source: ...)
- Fact 3 (Source: ...)
```

**Analysis Section:**
```markdown
## Analysis & Interpretation
- Pattern 1: [Description]
- Pattern 2: [Description]
- Insight 1: [Description]
```

**Uncertainty Section:**
```markdown
## Limitations & Uncertainties
- Unknown aspect 1
- Unverified assumption 1
- Area needing further research
```

---

## Quality Assurance

### Validation Checklist

- [ ] All facts have supporting evidence
- [ ] Sources are cited and accessible
- [ ] Assumptions clearly marked
- [ ] Analysis distinguishable from fact
- [ ] Status accurately reflects content
- [ ] Related documents identified
- [ ] No conflicts with core principles
- [ ] Metadata complete and current
- [ ] Canonical relationships verified where applicable

### Review Process

1. **Initial Creation** - Author documents knowledge
2. **Peer Review** - Subject matter expert reviews
3. **Validation** - Sources verified, facts checked
4. **Approval** - Appropriate authority approves
5. **Publication** - Knowledge published
6. **Maintenance** - Scheduled reviews and updates

Approval and publication do not override repository, governance or canonical-model authority.

---

## Cross-Linking

### Internal References
Use relative paths for internal links:
```markdown
[Related Topic](../Domain-2/Overview.md)
[Specific Fact](./Core-Facts.md#verified-facts)
```

Before treating an internal link as a dependency, verify that its target exists, is the intended artifact, and is within the applicable authority boundary.

### External References
Include full URLs with access dates:
```markdown
[External Source](https://example.com/resource)
Accessed: 2026-07-26
```

---

## Archival Process

### When to Archive
- Knowledge superseded by newer information
- Domain no longer relevant
- Content deprecated by policy changes
- Projects completed

### Archival Steps

1. Update status to "Archived"
2. Record archival reason
3. Move to Archive/ directory
4. Update cross-references
5. Create archive entry in logs
6. Preserve sufficient migration traceability

---

## Authority and Relationship Boundary

This specification may guide how knowledge is organized, but it does not by itself establish:

- canonical document identity;
- governance authority;
- repository-wide integrity;
- platform lifecycle state;
- knowledge-object schema ownership.

Those claims require the applicable canonical authority and current repository evidence.

---

## Status

Established: Foundation Build 001
Last Review: 2026-08-08
Next Review: To be determined by the applicable governance/review authority after the connected-baseline audit.

---

End of Document
