---
name: code-analyzer
description: Professional code analysis with AI-powered insights. Generates comprehensive reports with quality scores, issue detection, and actionable recommendations. Use when: (1) Analyzing code quality and architecture, (2) Identifying technical debt and refactoring opportunities, (3) Preparing code reviews, (4) Onboarding to new codebases, (5) Generating documentation. Supports 20+ languages including Python, JavaScript, Java, Go, Rust, and more.
---

# Code Analyzer Pro

Professional codebase analysis tool that generates comprehensive reports with:
- Quality scores (maintainability, testability, documentation, complexity)
- Issue detection with severity levels
- Actionable recommendations
- Architecture insights

## Quick Start

```bash
# Full analysis with report
python3 scripts/analyze.py --path /path/to/code --output report.md

# Quick summary
python3 scripts/analyze.py --path /path/to/code

# Exclude directories
python3 scripts/analyze.py --path /path/to/code --exclude "node_modules,vendor,.git"
```

## Features

### 📊 Quality Metrics
- **Maintainability Score** - How easy to maintain
- **Testability Score** - How easy to test
- **Documentation Score** - Documentation coverage
- **Complexity Score** - Code complexity assessment
- **Overall Score** - Weighted average

### ⚠️ Issue Detection
- **Critical** - Circular dependencies, architectural issues
- **Major** - High complexity, tight coupling
- **Minor** - Large files, code smells

### 🎯 Recommendations
- **Quick Wins** - Fixable in hours
- **Short Term** - 1-2 weeks
- **Long Term** - 1-3 months

## Output Example

```markdown
# Code Analysis Report

## Executive Summary
- Overall Score: 73/100
- Issues Found: 5

## Quality Metrics
| Metric | Score | Status |
|--------|-------|--------|
| Maintainability | 62/100 | ⚠️ Needs Improvement |
| Testability | 89/100 | ✅ Excellent |

## Issues Found
### CRITICAL
- Circular dependency: module_a → module_b → module_a

### MAJOR  
- High complexity in calculate_score (complexity=25)

## Recommendations
### Quick Wins
- [ ] Add type hints
- [ ] Remove unused imports
```

## Analysis Modes

### Full Analysis (Default)
Complete analysis with all metrics and recommendations.

```bash
python3 scripts/analyze.py --path . --output full-report.md
```

### Quick Summary
Console output with key metrics only.

```bash
python3 scripts/analyze.py --path .
```

### JSON Output
For programmatic processing.

```bash
python3 scripts/analyze.py --path . --json --output report.json
```

## Supported Languages

| Language | Extensions | Analysis Depth |
|----------|-----------|----------------|
| Python | .py | Full (imports, functions, classes, complexity) |
| JavaScript | .js | Full |
| TypeScript | .ts | Full |
| Java | .java | Full |
| Go | .go | Full |
| Rust | .rs | Full |
| C/C++ | .c, .cpp, .h | Basic |
| C# | .cs | Basic |
| Ruby | .rb | Basic |
| PHP | .php | Basic |
| Swift | .swift | Basic |
| Shell | .sh | Basic |
| SQL | .sql | Basic |
| YAML/JSON | .yaml, .yml, .json | Structure only |

## Use Cases

### 1. Code Review Preparation
```bash
# Analyze before PR review
python3 scripts/analyze.py --path ./feature-branch --output pr-analysis.md
```

### 2. Technical Debt Assessment
```bash
# Quarterly debt assessment
python3 scripts/analyze.py --path . --output debt-report-q1.md
```

### 3. New Codebase Onboarding
```bash
# Understand a new project
python3 scripts/analyze.py --path /new/project --output onboarding.md
```

### 4. Architecture Review
```bash
# Focus on architecture
python3 scripts/analyze.py --path . --exclude "tests,docs" --output arch-review.md
```

## Integration

### With AI Assistants

**Claude/Codex:**
```
"Analyze this codebase and identify the top 3 issues"
```

The AI will:
1. Run the analyzer
2. Interpret the report
3. Provide context-specific recommendations

### With CI/CD

```yaml
# GitHub Actions example
- name: Code Analysis
  run: |
    python3 scripts/analyze.py --path . --output report.md
    # Fail if score < 60
```

## Advanced Usage

### Custom Exclude Patterns
```bash
# Exclude test and vendor directories
python3 scripts/analyze.py --path . --exclude "tests,vendor,node_modules,.git"
```

### Analyze Specific Language
```bash
# Only Python files
python3 scripts/analyze.py --path . --include "*.py"
```

### Compare Two Versions
```bash
# Before and after comparison
python3 scripts/analyze.py --path ./before --output before.md
python3 scripts/analyze.py --path ./after --output after.md
```

## Best Practices

See [references/best-practices.md](references/best-practices.md) for:
- How to interpret scores
- Common issue patterns
- Refactoring strategies
- Quality improvement roadmap

## Limitations

- Does not execute code (static analysis only)
- Some languages have limited support
- Architecture detection is heuristic-based
- Does not replace manual code review

## Troubleshooting

### "No files found"
Check exclude patterns - they might be too aggressive.

### "Permission denied"
Run with appropriate permissions or exclude protected directories.

### Slow analysis
Large codebases (>10k files) may take time. Use `--exclude` to focus.

## See Also

- [Best Practices Guide](references/best-practices.md)
- [OpenClaw Documentation](https://docs.openclaw.ai)
- [ClawHub Skills](https://clawhub.com)
