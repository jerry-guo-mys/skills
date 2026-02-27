---
name: docs-improver
description: Comprehensive technical documentation improvement tool. Analyzes documentation quality (completeness, accuracy, clarity, structure, maintainability), generates missing docs (README, API docs), checks consistency between docs and code, and provides actionable improvement recommendations. Use when: (1) Auditing documentation quality, (2) Generating missing documentation, (3) Ensuring docs match code, (4) Improving doc structure, (5) Creating onboarding docs. Supports all programming languages.
---

# Docs Improver

Professional technical documentation analysis, generation, and improvement tool.

## Features

### 📊 Documentation Quality Assessment
- **Completeness** - Coverage of essential topics
- **Accuracy** - Alignment with actual code
- **Clarity** - Readability and understandability
- **Structure** - Organization and navigation
- **Maintainability** - Ease of updates

### 📝 Documentation Generation
- **README.md** - Project overview and quick start
- **API.md** - API endpoint documentation
- **ARCHITECTURE.md** - System architecture
- **INSTALL.md** - Installation guide
- **CONTRIBUTING.md** - Contribution guidelines

### 🔍 Consistency Checking
- API docs vs actual endpoints
- Code examples vs actual code
- Broken link detection
- Outdated information

### 💡 Improvement Recommendations
- Quick wins (hours)
- Short term (days)
- Long term (weeks)

## Quick Start

```bash
# Full analysis + generation + checking
python3 scripts/docs-improver.py --path /path/to/project --mode all --output ./docs

# Quality assessment only
python3 scripts/docs-improver.py --path . --mode analyze --report quality-report.md

# Generate missing docs only
python3 scripts/docs-improver.py --path . --mode generate --output ./docs

# Consistency check only
python3 scripts/docs-improver.py --path . --mode check
```

## Output Examples

### Quality Report

```markdown
# Documentation Quality Report

## Overall Score: 72/100

## Dimension Scores

| Dimension | Score | Status |
|-----------|-------|--------|
| Completeness | 65/100 | ⚠️ Needs Work |
| Accuracy | 80/100 | ✅ Good |
| Clarity | 75/100 | ✅ Good |
| Structure | 60/100 | ⚠️ Needs Work |
| Maintainability | 70/100 | ⚠️ Needs Work |

## Missing Documentation
- API.md
- ARCHITECTURE.md
- CONTRIBUTING.md

## Critical Issues
- Missing project description
- No code examples
- No installation instructions

## Recommendations

### Quick Wins
- [ ] Add project description and badges
- [ ] Add code examples
- [ ] Fix broken links

### Short Term
- [ ] Create API documentation
- [ ] Add architecture diagram
- [ ] Write contributing guide

### Long Term
- [ ] Set up automated doc generation
- [ ] Create video tutorials
- [ ] Establish doc review process
```

### Generated README

```markdown
# Project Name

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

## 📖 Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Development](#development)

## 📝 About

Auto-generated project description based on package.json/setup.py

## 🚀 Installation

```bash
# Install dependencies
npm install
```

## 💡 Usage

```python
# Example usage
from package import main
main()
```

## 🔌 API

See [API.md](API.md) for complete API documentation.

## 🛠️ Development

```bash
# Setup development environment
npm install
npm run dev
```
```

### Consistency Issues

```markdown
## Consistency Issues Found: 5

[MAJOR] api_mismatch
Location: API.md
Issue: API endpoint /api/users exists in code but not documented
Fix: Add documentation for /api/users

[MINOR] code_example_outdated
Location: README.md
Issue: Function process_data in code example may not exist
Fix: Update or remove the code example

[MINOR] broken_link
Location: docs/guide.md
Issue: Link to architecture.md may be broken
Fix: Update or remove the link
```

## Use Cases

### 1. Documentation Audit

```bash
# Assess current documentation quality
python3 scripts/docs-improver.py --path . --mode analyze --report audit.md
```

**Use when:**
- Taking over a project
- Preparing for release
- Quarterly documentation review

### 2. Generate Missing Docs

```bash
# Generate missing documentation
python3 scripts/docs-improver.py --path . --mode generate --output ./docs
```

**Use when:**
- Starting a new project
- Preparing for open source
- Onboarding new team members

### 3. Consistency Check Before Release

```bash
# Check docs match code before release
python3 scripts/docs-improver.py --path . --mode check
```

**Use when:**
- Before major releases
- After large refactoring
- API changes

### 4. Complete Documentation Overhaul

```bash
# Full analysis + generation + checking
python3 scripts/docs-improver.py --path . --mode all --output ./docs --report report.md
```

**Use when:**
- Documentation is severely outdated
- New project documentation setup
- Technical debt sprint

## Integration

### CI/CD Pipeline

```yaml
# GitHub Actions example
- name: Documentation Check
  run: |
    python3 scripts/docs-improver.py --path . --mode check
    # Fail if critical issues found
```

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit
python3 scripts/docs-improver.py --path . --mode check --report /tmp/doc-check.md
```

### With AI Assistants

**Claude/Codex:**
```
"Analyze our documentation quality and suggest improvements"
```

AI will:
1. Run docs-improver
2. Interpret the quality report
3. Generate specific improvement plans
4. Help implement recommendations

## Quality Scoring

### Score Ranges

| Score | Rating | Action |
|-------|--------|--------|
| 90-100 | Excellent | Maintain |
| 80-89 | Good | Minor improvements |
| 70-79 | Fair | Needs work |
| 60-69 | Poor | Major improvements |
| 0-59 | Critical | Complete overhaul |

### Dimension Weights

- Completeness: 30%
- Clarity: 25%
- Structure: 20%
- Maintainability: 15%
- Accuracy: 10%

## Best Practices

### README.md
- Clear project title and description
- Installation instructions
- Usage examples
- Contribution guidelines
- License information

### API Documentation
- All endpoints documented
- Request/response examples
- Error codes
- Authentication requirements

### Architecture Docs
- System overview diagram
- Component descriptions
- Data flow
- Technology stack

## Limitations

- **Static Analysis** - Does not execute code
- **Language Coverage** - Best support for Python, JS/TS
- **Context Understanding** - May miss nuanced requirements
- **External Links** - Basic link checking only

## Troubleshooting

### "No documentation found"
- Check if README exists
- Verify file permissions
- Ensure correct path

### "False positives in consistency check"
- Review manually
- Add to ignore list
- Update detection patterns

### "Generated docs need manual review"
- Always review generated content
- Add project-specific details
- Verify code examples work

## See Also

- [Best Practices Guide](references/best-practices.md)
- [Documentation Templates](assets/templates/)
- [OpenClaw Documentation](https://docs.openclaw.ai)

## Contributing

Contributions welcome! Especially:
- Better detection patterns
- Additional doc templates
- Language support
- Integration examples
