# ARGO Repository Management Guidelines

## Version: 3.0.0
Status: Foundation Build

---

## Repository Structure Governance

### Core Directories (Non-Negotiable)

```
Repository/
├── Governance/         [Core policies and decision frameworks]
├── Architecture/       [System design and technical frameworks]
├── Blueprints/         [Reusable patterns and templates]
├── Specifications/     [Detailed technical definitions]
├── Templates/          [Knowledge organization templates]
├── Knowledge/          [Actual knowledge base content]
├── Projects/           [Active initiatives and work]
├── Archive/            [Historical and obsolete content]
└── Logs/               [Decision and change logs]
```

### Directory Responsibilities

**Governance/**
- Core principles (non-negotiable)
- Decision-making frameworks
- Policy documents
- Governance structure

**Architecture/**
- System design philosophy
- Framework definitions
- Integration patterns
- Technology standards

**Blueprints/**
- Reusable solution patterns
- Domain-specific templates
- Implementation guides
- Best practices

**Specifications/**
- Detailed technical specs
- Interface definitions
- Data models
- Process specifications

**Templates/**
- Document templates
- Content structure templates
- Contribution templates
- Submission forms

**Knowledge/**
- Organized by domain
- Facts and findings
- Analysis and insights
- Research outputs

**Projects/**
- Active work items
- Project plans
- Progress tracking
- Deliverables

**Archive/**
- Superseded decisions
- Completed projects
- Deprecated content
- Historical reference

**Logs/**
- Decision logs
- Change logs
- Audit trails
- System history

---

## Branch Management

### Branch Naming Convention

```
main/                 → Production (stable, protected)
development/          → Integration branch
feature/DESCRIPTION   → New features
fix/DESCRIPTION       → Bug fixes
docs/DESCRIPTION      → Documentation updates
refactor/DESCRIPTION  → Code/structure improvements
```

### Branch Protection Rules (main)

- ✅ Require pull request reviews
- ✅ Require commit history
- ✅ Allow force pushes: NO
- ✅ Dismiss stale reviews on new push
- ✅ Require branches up to date before merge

---

## Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `perf`: Performance improvement
- `test`: Tests
- `chore`: Build, dependencies

### Examples
```
feat(governance): add decision-making framework
docs(architecture): update system design overview
fix(templates): correct markdown formatting
refactor(knowledge): reorganize content structure
```

---

## Pull Request Process

### PR Requirements

1. **Description**: Clear explanation of changes
2. **Related Issues**: Link to relevant issues/decisions
3. **Changes**: What is being added/modified/removed
4. **Testing**: How changes were validated
5. **Documentation**: Updated docs where relevant

### Review Checklist

- [ ] Aligns with ARGO principles
- [ ] Follows repository guidelines
- [ ] Properly documented
- [ ] No conflicts with main principles
- [ ] Content is accurate and validated
- [ ] Appropriate file structure
- [ ] Commit messages are clear

### Merge Criteria

✅ At least 1 approval
✅ All conversations resolved
✅ Branch is up to date with main
✅ No conflicts
✅ Aligns with governance framework

---

## File Naming Conventions

### Documents
- Use descriptive names
- Use hyphens for spaces: `Core-Principles.md`
- Include version info when appropriate
- Prefix with sequence number: `01-First.md`, `02-Second.md`

### Examples
```
01-Core-Principles.md
02-Decision-Making-Framework.md
ARGO-Architecture-v3.0.0.md
Knowledge-Organization-Template.md
```

---

## Content Standards

### Markdown Requirements
- Use standard Markdown format
- Include headers with proper hierarchy
- Tables for structured data
- Code blocks for examples
- Clear section organization

### Metadata Requirements

Each document should include:
```markdown
# Document Title

## Version: X.X.X
Status: [Foundation Build | Active | Deprecated]

---

[Content here]

---

## Status
Established: [Date]
Last Review: [Date]
Next Review: [Date]
```

---

## Access & Permissions

### Repository Access Tiers

1. **Admin** - Full access, all operations
2. **Maintainer** - Push, merge, manage branches
3. **Contributor** - Create branches, submit PRs
4. **Viewer** - Read-only access

### Default Settings
- Require status checks before merge: Yes
- Require code reviews: Yes (for Tier 1 decisions)
- Require branches up to date: Yes

---

## Status
Established: Foundation Build 001
Last Review: 2026-07-26
Next Review: 2026-10-26
