---
name: code-analyzer
description: Fast and accurate code analysis for any codebase. Use when: (1) Analyzing code structure and architecture, (2) Understanding unfamiliar codebases, (3) Reviewing code for issues or patterns, (4) Generating code summaries or documentation, (5) Identifying dependencies and relationships, (6) Analyzing code complexity or metrics. Supports all major programming languages and frameworks.
---

# Code Analyzer

A comprehensive code analysis tool for fast and accurate codebase understanding.

## Quick Start

Analyze a codebase:
```bash
# Basic analysis
scripts/analyze.py --path /path/to/code --output summary.md

# Deep analysis with dependencies
scripts/analyze.py --path /path/to/code --deep --output analysis.md

# Specific file analysis
scripts/analyze.py --file /path/to/file.py --output file-analysis.md
```

## Analysis Types

### 1. Structure Analysis
Map the codebase structure:
```bash
scripts/analyze.py --path . --mode structure
```
- Directory tree
- File organization
- Module relationships

### 2. Dependency Analysis
Find dependencies and imports:
```bash
scripts/analyze.py --path . --mode dependencies
```
- Import chains
- External dependencies
- Circular dependencies

### 3. Complexity Analysis
Calculate code metrics:
```bash
scripts/analyze.py --path . --mode complexity
```
- Cyclomatic complexity
- Lines of code
- Function lengths

### 4. Pattern Analysis
Identify code patterns:
```bash
scripts/analyze.py --path . --mode patterns
```
- Design patterns
- Code smells
- Best practices

## Analysis Workflow

1. **Discover** - Map the codebase structure
2. **Analyze** - Deep dive into key files
3. **Summarize** - Generate human-readable summary
4. **Report** - Output findings with recommendations

## Language Support

- Python, JavaScript/TypeScript, Java, Go, Rust
- C/C++, C#, Ruby, PHP, Swift
- Shell scripts, SQL, YAML/JSON

## Best Practices

- Start with structure analysis for large codebases
- Use file filters to focus on relevant code
- Combine multiple analysis modes for comprehensive review
- See [references/best-practices.md](references/best-practices.md) for detailed guidelines

## Advanced Usage

### Filtering
```bash
# Exclude tests and vendor directories
scripts/analyze.py --path . --exclude "tests/,vendor/,node_modules/"

# Focus on specific extensions
scripts/analyze.py --path . --include "*.py,*.js"
```

### Custom Rules
Add custom analysis rules in `references/custom-rules.md`
