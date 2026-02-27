---
name: code-analyzer
description: Deep codebase analysis with DDD pattern recognition. Generates comprehensive reports with: architecture analysis, execution paths, data models, business rules, external dependencies, data flows, AND domain-driven design patterns (aggregates, entities, value objects, domain services, repositories, domain events, bounded contexts). Use when: (1) Onboarding to new codebases, (2) Architecture documentation, (3) DDD pattern detection, (4) Domain model understanding, (5) Technical debt assessment, (6) Code review preparation. Supports Python, JavaScript, TypeScript, Rust, Java, Go, and more.
---

# Code Analyzer Pro - Deep Codebase Understanding

Professional tool for **deep codebase analysis** that goes beyond surface metrics to understand:

- 🏗️ **Architecture** - Style, layers, module organization
- 🚀 **Execution Flow** - Entry points, call graphs, execution paths
- 📊 **Data Models** - Entities, DTOs, value objects, relationships
- 📜 **Business Rules** - Validation, constraints, workflows encoded in code
- 🔗 **External Dependencies** - APIs, databases, services, libraries
- 💧 **Data Flows** - How data moves through the system

## Quick Start

```bash
# Full deep analysis
python3 scripts/analyze.py --path /path/to/code --output report.md

# Exclude directories
python3 scripts/analyze.py --path /path/to/code --exclude "node_modules,vendor,target" --output report.md
```

## What You Get

### 📋 Executive Summary
- Total files and lines
- Architecture style detection
- Entry points count
- Data models discovered
- Business rules identified
- External dependencies

### 🏗️ Architecture Analysis
- Detected architecture style (MVC, Clean, Layered, Microservices, etc.)
- Module/layer structure
- Directory organization

### 🚀 Entry Points & Execution Flow
- All entry points (main, run, handle, process functions)
- Function parameters and return types
- Call relationships
- Execution path tracing

### 📊 Data Models
- **Core Entities** - Business domain objects
- **DTOs** - Data transfer objects
- **Value Objects** - Immutable value types
- **Relationships** - Inheritance, composition, usage

### 📜 Business Rules
Extracted from code:
- **Validation Rules** - Input validation logic
- **Constraints** - Business constraints and invariants
- **Workflows** - State transitions and process flows
- **Calculations** - Business logic formulas

### 🔗 External Dependencies
- **Libraries** - Third-party packages
- **APIs** - External service integrations
- **Databases** - Data persistence layers
- **Critical Dependencies** - Core functionality dependencies

### 💧 Data Flows
- Source and destination
- Data types being transferred
- Transformations applied
- Triggers for data movement

### 🛤️ Execution Paths
Key execution paths through the system:
- Step-by-step function calls
- Critical path identification
- Flow visualization

## Output Example

```markdown
# Deep Code Analysis Report

## Executive Summary
- Total Files: 105
- Total Lines: 24,780
- Architecture: Layered
- Entry Points: 5
- Data Models: 45
- Business Rules: 23

## Architecture
Style: Layered

Layers:
- api/
- service/
- repository/
- domain/

## Entry Points

### process_message
- Location: agent.rs
- Parameters: components, context, user_input
- Business Logic: ✅ Yes
- Calls: validate, transform, execute, respond

## Data Models

### Core Entities

**User** (domain/user.rs)
Fields:
- id
- name
- email
- role

**Message** (domain/message.rs)
Fields:
- id
- content
- timestamp
- user_id

## Business Rules

### Validation Rules (15)

**rule_1:** Validation on user input
- Location: agent.rs:match
- Priority: high
- Condition: if input.is_empty() { return Err(...) }

### Constraints (8)

**rule_16:** Business constraint
- Location: service/payment.rs
- Priority: critical
- Condition: amount must be positive

## External Dependencies

### Critical
- serde - serialization
- tokio - async runtime
- sqlx - database

### Other
- reqwest, chrono, uuid, ...

## Data Flows

- external → process_message
  Data: user_input
  Trigger: API call

- process_message → validate
  Data: validated_input
  Trigger: function_call

## Key Execution Paths

### process_message
1. process_message
2. validate
3. transform
4. execute
5. respond
```

## Supported Languages

| Language | Extensions | Analysis Depth |
|----------|-----------|----------------|
| Python | .py | Deep (AST-based) |
| JavaScript | .js | Deep (regex + patterns) |
| TypeScript | .ts | Deep |
| Rust | .rs | Deep (structs, enums, functions, rules) |
| Java | .java | Medium |
| Go | .go | Medium |
| C/C++ | .c, .cpp, .h | Basic |

## Use Cases

### 1. New Codebase Onboarding
```bash
# Understand a new project in minutes
python3 scripts/analyze.py --path /new/project --output onboarding.md
```

**Benefits:**
- Identify entry points quickly
- Understand data models
- Learn business rules
- Map dependencies

### 2. Architecture Documentation
```bash
# Generate architecture docs
python3 scripts/analyze.py --path . --output architecture.md
```

**Outputs:**
- Architecture style
- Module structure
- Data flows
- Execution paths

### 3. Technical Debt Assessment
```bash
# Quarterly debt review
python3 scripts/analyze.py --path . --exclude "tests" --output debt-review.md
```

**Identifies:**
- Complex code areas
- Tight coupling
- Missing documentation
- Critical dependencies

### 4. Code Review Preparation
```bash
# Pre-PR analysis
python3 scripts/analyze.py --path ./feature --output pr-analysis.md
```

**Provides:**
- Changed business rules
- New dependencies
- Modified data flows
- Impact analysis

### 5. Knowledge Transfer
```bash
# Document for team handoff
python3 scripts/analyze.py --path . --output knowledge-base.md
```

**Captures:**
- Core business logic
- Key execution paths
- Critical dependencies
- Architecture decisions

## Advanced Usage

### Analyze Specific Directories
```bash
# Focus on core business logic
python3 scripts/analyze.py --path ./src --output core-analysis.md
```

### Exclude Test Code
```bash
python3 scripts/analyze.py --path . --exclude "tests,specs,__tests__" --output prod-analysis.md
```

### Compare Versions
```bash
# Before and after comparison
python3 scripts/analyze.py --path ./before --output before.md
python3 scripts/analyze.py --path ./after --output after.md
diff before.md after.md
```

## Integration with AI Assistants

### Claude/Codex Usage
```
"Analyze this codebase and explain:
1. What are the main entry points?
2. What are the core data models?
3. What business rules are encoded?
4. How does data flow through the system?"
```

AI will:
1. Run the analyzer
2. Interpret the deep report
3. Provide context-specific explanations
4. Answer questions about architecture

### Automated Documentation
```bash
# Generate docs for each module
for dir in src/*/; do
  python3 scripts/analyze.py --path $dir --output docs/$(basename $dir).md
done
```

## Interpreting Results

### Architecture Styles

**MVC** - Model-View-Controller
- Look for: controllers/, models/, views/
- Good for: Web applications

**Clean Architecture**
- Look for: domain/, application/, infrastructure/
- Good for: Enterprise applications

**Layered**
- Look for: api/, service/, repository/, data/
- Good for: Traditional enterprise apps

**Microservices**
- Look for: service/, gateway/, client/
- Good for: Distributed systems

### Business Rule Types

**Validation** - Input/data validation
**Constraint** - Business invariants
**Workflow** - Process flows
**Calculation** - Business formulas

### Dependency Criticality

**Critical** - Core functionality depends on it
**Important** - Used in key features
**Optional** - Nice to have, not critical

## Limitations

- **Static Analysis Only** - Does not execute code
- **Language Coverage** - Deep support for Python, JS/TS, Rust; basic for others
- **Heuristic Detection** - Architecture and rules detected via patterns
- **No Runtime Info** - Does not capture runtime behavior
- **Complementary** - Does not replace manual code review

## Best Practices

See [references/best-practices.md](references/best-practices.md) for:
- How to interpret analysis results
- Common architecture patterns
- Business rule extraction techniques
- Dependency management strategies
- Documentation guidelines

## Troubleshooting

### "No entry points found"
- Check if your language is supported
- Entry points named differently (try custom patterns)
- Code might be library/framework, not application

### "No business rules detected"
- Rules may be in configuration files
- Business logic might be implicit
- Try analyzing specific business logic files

### Slow analysis
- Large codebases (>10k files) take time
- Use `--exclude` to focus on relevant code
- Analyze specific directories instead

## See Also

- [Best Practices Guide](references/best-practices.md)
- [OpenClaw Documentation](https://docs.openclaw.ai)
- [ClawHub Skills](https://clawhub.com)

## Contributing

Contributions welcome! Especially:
- Additional language support
- Better business rule detection
- Architecture pattern recognition
- Data flow visualization
