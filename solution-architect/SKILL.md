---
name: solution-architect
description: Professional technical solution and architecture design skill. Generates comprehensive technical proposals including: requirements analysis, architecture design, technology selection, implementation roadmap, risk assessment, and cost estimation. Use when: (1) Writing technical proposals, (2) System architecture design, (3) Technology evaluation, (4) Project planning, (5) RFP responses, (6) Stakeholder presentations. Supports multiple industries and scales.
---

# Solution Architect

Professional technical solution design and architecture planning skill.

## Quick Start

```bash
# Generate complete technical solution
python3 scripts/generate-solution.py \
  --requirements requirements.md \
  --output solution-proposal.md \
  --type full

# Generate architecture design only
python3 scripts/architecture-design.py \
  --requirements requirements.md \
  --output architecture.md

# Technology evaluation
python3 scripts/tech-evaluation.py \
  --criteria evaluation-criteria.md \
  --output tech-comparison.md
```

## Features

### 📋 Requirements Analysis
- Functional requirements breakdown
- Non-functional requirements (performance, security, scalability)
- Stakeholder analysis
- Success criteria definition

### 🏗️ Architecture Design
- System architecture diagrams (Mermaid)
- Component design
- Data flow design
- Integration points
- API design

### 🔧 Technology Selection
- Technology evaluation framework
- Comparison matrix
- Pros/cons analysis
- Recommendation with justification

### 📊 Implementation Planning
- Phased rollout plan
- Timeline estimation
- Resource requirements
- Milestone definition

### ⚠️ Risk Assessment
- Technical risks
- Operational risks
- Mitigation strategies
- Contingency planning

### 💰 Cost Estimation
- Infrastructure costs
- Development costs
- Operational costs
- ROI analysis

## Output Structure

```markdown
# Technical Solution Proposal

## Executive Summary
- Problem statement
- Proposed solution
- Key benefits
- Investment required

## Requirements Analysis
### Functional Requirements
### Non-Functional Requirements
### Constraints and Assumptions

## Architecture Design
### System Overview
### Component Architecture
### Data Architecture
### Integration Architecture
### Security Architecture

## Technology Stack
### Selected Technologies
### Technology Comparison
### Justification

## Implementation Plan
### Phase 1: Foundation (Weeks 1-4)
### Phase 2: Core Features (Weeks 5-12)
### Phase 3: Enhancement (Weeks 13-16)

## Risk Assessment
### Technical Risks
### Operational Risks
### Mitigation Strategies

## Cost Estimation
### Development Costs
### Infrastructure Costs
### Operational Costs
### ROI Analysis

## Recommendations
### Next Steps
### Success Metrics
```

## Use Cases

### 1. New System Development
```bash
python3 scripts/generate-solution.py \
  --requirements "Build e-commerce platform" \
  --output ecommerce-solution.md \
  --type full
```

### 2. System Migration
```bash
python3 scripts/generate-solution.py \
  --requirements "Migrate monolith to microservices" \
  --output migration-plan.md \
  --type migration
```

### 3. Technology Evaluation
```bash
python3 scripts/tech-evaluation.py \
  --options "PostgreSQL vs MongoDB vs Redis" \
  --criteria "performance,scalability,cost" \
  --output db-evaluation.md
```

### 4. Architecture Review
```bash
python3 scripts/architecture-review.py \
  --architecture current-arch.md \
  --output review-report.md
```

## Templates Included

- Technical Proposal Template
- Architecture Decision Record (ADR)
- Technology Evaluation Matrix
- Risk Assessment Template
- Cost Estimation Template
- Implementation Timeline Template

## Integration

### With AI Assistants

**Claude/Codex:**
```
"Create a technical solution for building a real-time chat application 
with 100k concurrent users, including architecture, technology selection, 
and implementation timeline."
```

AI will:
1. Analyze requirements
2. Generate architecture design
3. Recommend technologies
4. Create implementation plan
5. Assess risks

### With docs-improver

Generate comprehensive documentation:
```bash
# Generate solution
python3 solution-architect/scripts/generate-solution.py --requirements req.md --output solution.md

# Improve documentation quality
python3 docs-improver/scripts/docs-improver.py --path ./solution.md --mode all
```

## Best Practices

See [references/best-practices.md](references/best-practices.md) for:
- Architecture design principles
- Technology selection criteria
- Risk management strategies
- Cost optimization techniques
- Stakeholder communication tips

## See Also

- [Architecture Templates](assets/templates/)
- [Mermaid Diagrams](assets/diagrams/)
- [OpenClaw Documentation](https://docs.openclaw.ai)
