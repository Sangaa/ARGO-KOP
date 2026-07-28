# ARGO Knowledge Organization Specification

## Version: 3.0.0
Status: Foundation Build

---

## Knowledge Classification

### Tier 1: Foundational Knowledge
**Characteristics:**
- Core principles and values
- Fundamental facts about ARGO
- Non-negotiable rules
- Essential frameworks

**Storage:** Governance/ and Architecture/ directories
**Update Frequency:** Rarely (requires governance approval)
**Validation:** High (multiple reviews)

### Tier 2: Operational Knowledge
**Characteristics:**
- Documented processes
- Proven practices
- Guidelines and standards
- Reusable patterns

**Storage:** Blueprints/ and Specifications/ directories
**Update Frequency:** Periodically (quarterly or as needed)
**Validation:** Medium (peer review)

### Tier 3: Domain Knowledge
**Characteristics:**
- Facts within specific domains
- Analysis and insights
- Research findings
- Subject-matter expertise

**Storage:** Knowledge/ directory (organized by domain)
**Update Frequency:** Regularly (as new knowledge emerges)
**Validation:** Medium-High (based on domain standards)

### Tier 4: Exploratory Knowledge
**Characteristics:**
- Preliminary research
- Hypotheses and theories
- Emerging patterns
- Speculative content

**Storage:** Projects/ directory or dedicated exploratory folders
**Update Frequency:** Frequently (ongoing investigation)
**Validation:** Low-Medium (marked as provisional)

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

### Review Process

1. **Initial Creation** - Author documents knowledge
2. **Peer Review** - Subject matter expert reviews
3. **Validation** - Sources verified, facts checked
4. **Approval** - Appropriate authority approves
5. **Publication** - Knowledge published
6. **Maintenance** - Scheduled reviews and updates

---

## Cross-Linking

### Internal References
Use relative paths for internal links:
```markdown
[Related Topic](../Domain-2/Overview.md)
[Specific Fact](./Core-Facts.md#verified-facts)
```

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

---

## Domain Examples

### Example Domain: Decision-Making
```
Knowledge/Decision-Making/
├── Overview.md
├── Core-Facts.md (Decision frameworks, models)
├── Analysis.md (Effectiveness studies, patterns)
├── References.md (Research sources)
└── SubDomains/
    ├── Strategic-Decisions/
    ├── Tactical-Decisions/
    └── Operational-Decisions/
```

---

## Status
Established: Foundation Build 001
Last Review: 2026-07-26
Next Review: 2026-10-26
